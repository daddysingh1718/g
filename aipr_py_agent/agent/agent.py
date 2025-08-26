import os
import json
import google.generativeai as genai
from rich.markdown import Markdown

# Import the tools
from tools.file_system import list_files, read_file, write_file
from tools.shell import execute_shell_command
from tools.web import search_web

# Import the prompt
from prompts.system_prompts import REACT_PROMPT

class ReActAgent:
    """
    The core agent that uses the ReAct framework to reason and act.
    """
    def __init__(self):
        """
        Initializes the agent, including the LLM and the tool registry.
        """
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables.")

        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash-latest')

        # Define the tool registry
        self.tools = {
            "search_web": search_web,
            "list_files": list_files,
            "read_file": read_file,
            "write_file": write_file,
            "execute_shell_command": execute_shell_command,
        }
        self.dangerous_tools = ["write_file", "execute_shell_command"]
        print("ReActAgent initialized with Gemini model and tools.")

    def run(self, user_prompt: str, tui) -> str:
        """
        Runs the ReAct loop to process a user prompt.

        Args:
            user_prompt: The initial prompt from the user.
            tui: The Terminal User Interface instance for interaction (e.g., confirmations).

        Returns:
            The final answer from the agent.
        """
        tui.console.print(f"\n[bold blue]Goal:[/bold blue] {user_prompt}")

        # Use a chat session for multi-turn conversation
        # The history is automatically managed by the chat session object
        chat_session = self.model.start_chat(history=[
            {"role": "user", "parts": [REACT_PROMPT]},
            {"role": "model", "parts": [json.dumps({"thought": "OK, I understand the instructions. I am a helpful AI coding assistant and I am ready to help the user with their request.", "action": {"tool": "list_files", "args": {}}})]},
        ])

        # Start the loop with the user's actual prompt
        next_prompt = user_prompt
        max_iterations = 10

        for i in range(max_iterations):
            tui.console.print(f"\n[bold magenta]--- Iteration {i+1} ---[/bold magenta]")

            with tui.console.status("[bold yellow]Agent is thinking...[/bold yellow]", spinner="dots"):
                response = chat_session.send_message(next_prompt)

            try:
                # A simple way to extract JSON from markdown code blocks
                json_text = response.text.strip().replace("```json", "").replace("```", "").strip()
                parsed_response = json.loads(json_text)
            except (json.JSONDecodeError, AttributeError) as e:
                tui.console.print(f"[bold red]Error parsing model response:[/bold red]\n{response.text}\nError: {e}")
                next_prompt = "Invalid JSON format. Please check your response and provide it in the correct JSON format as specified in the instructions."
                continue

            thought = parsed_response.get("thought")
            if thought:
                tui.console.print(f"[bold green]Thought:[/bold green] {thought}")

            if "final_answer" in parsed_response:
                return parsed_response["final_answer"]

            if "action" in parsed_response:
                action = parsed_response.get("action", {})
                tool_name = action.get("tool")
                tool_args = action.get("args", {})

                if tool_name not in self.tools:
                    observation = f"Error: Tool '{tool_name}' not found."
                else:
                    if tool_name in self.dangerous_tools:
                        if not tui.get_user_confirmation(tool_name, tool_args):
                            observation = f"User denied permission for tool '{tool_name}'."
                        else:
                            tool_function = self.tools[tool_name]
                            observation = tool_function(**tool_args)
                    else:
                        tool_function = self.tools[tool_name]
                        observation = tool_function(**tool_args)

                tui.console.print(f"\n[bold yellow]Observation:[/bold yellow]")
                tui.console.print(Markdown(f"```\n{observation}\n```"))
                next_prompt = f"Observation: {observation}"
            else:
                tui.console.print("[bold red]Error: Response did not contain 'final_answer' or 'action'. Retrying.[/bold red]")
                next_prompt = "Your response was invalid. It must contain either a 'final_answer' or an 'action' in the specified JSON format."

        return "Agent could not complete the task within the maximum number of iterations."
