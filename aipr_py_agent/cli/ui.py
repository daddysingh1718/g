from rich.console import Console
from rich.markdown import Markdown
from rich.prompt import Prompt
from rich.panel import Panel

class TUI:
    """
    Terminal User Interface for the agent.
    Handles all user interaction.
    """
    def __init__(self, agent):
        self.agent = agent
        self.console = Console()

    def get_user_confirmation(self, tool_name: str, args: dict) -> bool:
        """
        Prints the details of a dangerous action and asks the user for confirmation.
        """
        self.console.print(Panel(
            f"[bold]Tool:[/bold] {tool_name}\n[bold]Arguments:[/bold] {str(args)}",
            title="[bold yellow]Confirmation Required[/bold yellow]",
            border_style="yellow",
            expand=False
        ))
        confirm = Prompt.ask("Do you want to execute this action?", choices=["y", "n"], default="n")
        return confirm.lower() == "y"

    def start(self):
        """
        Starts the main loop of the terminal UI.
        """
        self.console.print("[bold green]Welcome to the AI Pair Programmer![/bold green]")
        self.console.print("Type your request, or 'exit'/'quit' to exit.")

        while True:
            prompt = Prompt.ask("\n[bold cyan]You[/bold cyan]")

            if prompt.lower() in ["exit", "quit"]:
                self.console.print("[bold red]Exiting...[/bold red]")
                break

            # The agent's run method will now handle the spinner and printing
            response = self.agent.run(prompt, self)

            self.console.print("\n[bold green]Final Answer:[/bold green]")
            self.console.print(Markdown(response))
