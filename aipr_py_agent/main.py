import os
from dotenv import load_dotenv
from cli.ui import TUI
from agent.agent import ReActAgent

def main():
    """
    The main entry point for the AI Pair Programmer application.
    """
    # Load environment variables from a .env file
    load_dotenv()

    # Check if the Gemini API key is set
    if not os.getenv("GEMINI_API_KEY"):
        TUI(None).console.print("[bold red]Error: GEMINI_API_KEY environment variable not set.[/bold red]")
        TUI(None).console.print("Please create a .env file in the 'aipr_py_agent' directory and add your key:")
        TUI(None).console.print("Example: GEMINI_API_KEY=your_api_key_here")
        return

    # Initialize the agent and the UI
    try:
        react_agent = ReActAgent()
        tui = TUI(react_agent)
        # Start the application
        tui.start()
    except Exception as e:
        TUI(None).console.print(f"[bold red]An error occurred during agent initialization: {e}[/bold red]")


if __name__ == "__main__":
    main()
