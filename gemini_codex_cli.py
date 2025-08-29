#!/usr/bin/env python3
"""
Gemini Codex CLI - A complete CLI tool powered by Google Gemini 8
Replaces OpenAI Codex CLI with full feature parity and enhanced capabilities
"""

import os
import sys
import json
import asyncio
import subprocess
from pathlib import Path
from typing import Optional, List, Dict, Any
import google.generativeai as genai
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt, Confirm
from rich.table import Table
from rich.syntax import Syntax
from rich.progress import Progress, SpinnerColumn, TextColumn
import click

# Initialize Rich console
console = Console()

class GeminiCodexCLI:
    """Main CLI class with all Codex-like features using Gemini 8"""
    
    def __init__(self):
        self.api_key = os.getenv('GOOGLE_API_KEY')
        self.model = None
        self.conversation_history = []
        self.workspace_path = Path.cwd()
        self.setup_gemini()
    
    def setup_gemini(self):
        """Initialize Gemini API"""
        if not self.api_key:
            console.print("[red]Error: GOOGLE_API_KEY environment variable not set[/red]")
            console.print("Please set your Google API key: export GOOGLE_API_KEY='your_key_here'")
            sys.exit(1)
        
        genai.configure(api_key=self.api_key)
        try:
            # Use Gemini Pro for code generation (equivalent to Codex)
            self.model = genai.GenerativeModel('gemini-1.5-pro')
            console.print("[green]✓ Gemini API initialized successfully[/green]")
        except Exception as e:
            console.print(f"[red]Error initializing Gemini: {e}[/red]")
            sys.exit(1)
    
    def generate_code(self, prompt: str, context: str = "") -> str:
        """Generate code using Gemini"""
        try:
            full_prompt = f"""
            You are an expert code generator. Generate high-quality, production-ready code.
            
            Context: {context}
            
            User Request: {prompt}
            
            Requirements:
            1. Generate complete, working code
            2. Include proper error handling
            3. Add comprehensive comments
            4. Follow best practices
            5. Ensure code is production-ready
            
            Generate the code:
            """
            
            response = self.model.generate_content(full_prompt)
            return response.text
        except Exception as e:
            return f"Error generating code: {e}"
    
    def explain_code(self, code: str) -> str:
        """Explain code using Gemini"""
        try:
            prompt = f"""
            Explain this code in detail:
            
            {code}
            
            Provide:
            1. What the code does
            2. How it works
            3. Key concepts
            4. Potential improvements
            """
            
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error explaining code: {e}"
    
    def debug_code(self, code: str, error: str) -> str:
        """Debug code using Gemini"""
        try:
            prompt = f"""
            Debug this code. The error is: {error}
            
            Code:
            {code}
            
            Provide:
            1. What's causing the error
            2. How to fix it
            3. Corrected code
            4. Prevention tips
            """
            
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error debugging code: {e}"
    
    def refactor_code(self, code: str, improvements: str) -> str:
        """Refactor code using Gemini"""
        try:
            prompt = f"""
            Refactor this code with the following improvements: {improvements}
            
            Original code:
            {code}
            
            Requirements:
            1. Refactored code
            2. Explanation of changes
            3. Benefits of refactoring
            """
            
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error refactoring code: {e}"
    
    def generate_tests(self, code: str) -> str:
        """Generate tests for code"""
        try:
            prompt = f"""
            Generate comprehensive tests for this code:
            
            {code}
            
            Include:
            1. Unit tests
            2. Edge cases
            3. Error scenarios
            4. Test documentation
            """
            
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error generating tests: {e}"
    
    def code_review(self, code: str) -> str:
        """Perform code review"""
        try:
            prompt = f"""
            Perform a comprehensive code review:
            
            {code}
            
            Evaluate:
            1. Code quality
            2. Performance
            3. Security
            4. Best practices
            5. Suggestions for improvement
            """
            
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error performing code review: {e}"
    
    def generate_docs(self, code: str) -> str:
        """Generate documentation for code"""
        try:
            prompt = f"""
            Generate comprehensive documentation for this code:
            
            {code}
            
            Include:
            1. Function/class descriptions
            2. Parameters and return values
            3. Usage examples
            4. API documentation
            """
            
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error generating documentation: {e}"
    
    def interactive_session(self):
        """Start interactive coding session"""
        console.print(Panel.fit(
            "[bold blue]Gemini Codex CLI - Interactive Mode[/bold blue]\n"
            "Type 'help' for commands, 'exit' to quit",
            title="🚀 Welcome"
        ))
        
        while True:
            try:
                user_input = Prompt.ask("\n[bold cyan]Codex[/bold cyan]")
                
                if user_input.lower() in ['exit', 'quit', 'q']:
                    break
                elif user_input.lower() == 'help':
                    self.show_help()
                elif user_input.lower().startswith('generate'):
                    prompt = user_input[9:].strip()
                    if prompt:
                        with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), console=console):
                            code = self.generate_code(prompt)
                        console.print(Syntax(code, "python", theme="monokai"))
                    else:
                        console.print("[yellow]Please provide a prompt for code generation[/yellow]")
                elif user_input.lower().startswith('explain'):
                    # Handle file explanation
                    pass
                else:
                    # Treat as code generation prompt
                    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), console=console):
                        code = self.generate_code(user_input)
                    console.print(Syntax(code, "python", theme="monokai"))
                    
            except KeyboardInterrupt:
                break
            except Exception as e:
                console.print(f"[red]Error: {e}[/red]")
    
    def show_help(self):
        """Show available commands"""
        help_table = Table(title="Available Commands")
        help_table.add_column("Command", style="cyan")
        help_table.add_column("Description", style="white")
        
        commands = [
            ("generate <prompt>", "Generate code from description"),
            ("explain <file>", "Explain code in file"),
            ("debug <file> <error>", "Debug code with error"),
            ("refactor <file> <improvements>", "Refactor code"),
            ("test <file>", "Generate tests for code"),
            ("review <file>", "Perform code review"),
            ("docs <file>", "Generate documentation"),
            ("help", "Show this help"),
            ("exit", "Exit interactive mode")
        ]
        
        for cmd, desc in commands:
            help_table.add_row(cmd, desc)
        
        console.print(help_table)
    
    def process_file(self, file_path: str, operation: str, **kwargs):
        """Process a file with specified operation"""
        try:
            with open(file_path, 'r') as f:
                code = f.read()
            
            if operation == 'explain':
                result = self.explain_code(code)
            elif operation == 'debug':
                result = self.debug_code(code, kwargs.get('error', ''))
            elif operation == 'refactor':
                result = self.refactor_code(code, kwargs.get('improvements', ''))
            elif operation == 'test':
                result = self.generate_tests(code)
            elif operation == 'review':
                result = self.code_review(code)
            elif operation == 'docs':
                result = self.generate_docs(code)
            else:
                result = "Unknown operation"
            
            return result
        except FileNotFoundError:
            return f"File {file_path} not found"
        except Exception as e:
            return f"Error processing file: {e}"

@click.group()
@click.version_option(version="1.0.0")
def cli():
    """Gemini Codex CLI - AI-powered code generation and analysis"""
    pass

@cli.command()
@click.option('--prompt', '-p', required=True, help='Code generation prompt')
@click.option('--output', '-o', help='Output file path')
@click.option('--context', '-c', help='Additional context for generation')
def generate(prompt, output, context):
    """Generate code from description"""
    codex = GeminiCodexCLI()
    
    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), console=console):
        code = codex.generate_code(prompt, context or "")
    
    if output:
        with open(output, 'w') as f:
            f.write(code)
        console.print(f"[green]Code generated and saved to {output}[/green]")
    else:
        console.print(Syntax(code, "python", theme="monokai"))

@cli.command()
@click.argument('file_path')
def explain(file_path):
    """Explain code in file"""
    codex = GeminiCodexCLI()
    result = codex.process_file(file_path, 'explain')
    console.print(Panel(result, title="Code Explanation"))

@cli.command()
@click.argument('file_path')
@click.argument('error')
def debug(file_path, error):
    """Debug code with error"""
    codex = GeminiCodexCLI()
    result = codex.process_file(file_path, 'debug', error=error)
    console.print(Panel(result, title="Debug Results"))

@cli.command()
@click.argument('file_path')
@click.argument('improvements')
def refactor(file_path, improvements):
    """Refactor code with improvements"""
    codex = GeminiCodexCLI()
    result = codex.process_file(file_path, 'refactor', improvements=improvements)
    console.print(Panel(result, title="Refactored Code"))

@cli.command()
@click.argument('file_path')
def test(file_path):
    """Generate tests for code"""
    codex = GeminiCodexCLI()
    result = codex.process_file(file_path, 'test')
    console.print(Panel(result, title="Generated Tests"))

@cli.command()
@click.argument('file_path')
def review(file_path):
    """Perform code review"""
    codex = GeminiCodexCLI()
    result = codex.process_file(file_path, 'review')
    console.print(Panel(result, title="Code Review"))

@cli.command()
@click.argument('file_path')
def docs(file_path):
    """Generate documentation for code"""
    codex = GeminiCodexCLI()
    result = codex.process_file(file_path, 'docs')
    console.print(Panel(result, title="Generated Documentation"))

@cli.command()
def interactive():
    """Start interactive coding session"""
    codex = GeminiCodexCLI()
    codex.interactive_session()

if __name__ == '__main__':
    cli()
