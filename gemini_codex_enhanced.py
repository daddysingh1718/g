#!/usr/bin/env python3
"""
Enhanced Gemini Codex CLI with all advanced features integrated
Complete replacement for OpenAI Codex CLI with Google Gemini 8
"""

import os
import sys
import json
import asyncio
import subprocess
import tempfile
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
from rich.layout import Layout
from rich.columns import Columns
import click

# Initialize Rich console
console = Console()

class EnhancedGeminiCodexCLI:
    """Enhanced CLI with all advanced features using Gemini 8"""
    
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
            self.model = genai.GenerativeModel('gemini-1.5-pro')
            console.print("[green]✓ Gemini API initialized successfully[/green]")
        except Exception as e:
            console.print(f"[red]Error initializing Gemini: {e}[/red]")
            sys.exit(1)
    
    def generate_code(self, prompt: str, context: str = "", language: str = "python") -> str:
        """Generate code using Gemini with language specification"""
        try:
            full_prompt = f"""
            You are an expert {language} developer. Generate high-quality, production-ready code.
            
            Context: {context}
            
            User Request: {prompt}
            
            Requirements:
            1. Generate complete, working {language} code
            2. Include proper error handling
            3. Add comprehensive comments
            4. Follow {language} best practices
            5. Ensure code is production-ready
            6. Use modern {language} features and patterns
            
            Generate the code:
            """
            
            response = self.model.generate_content(full_prompt)
            return response.text
        except Exception as e:
            return f"Error generating code: {e}"
    
    def explain_code(self, code: str, detail_level: str = "comprehensive") -> str:
        """Explain code with configurable detail level"""
        try:
            detail_instructions = {
                "basic": "Provide a brief overview of what the code does",
                "detailed": "Explain the code structure, functions, and key concepts",
                "comprehensive": "Provide complete analysis including algorithms, patterns, and improvements"
            }
            
            prompt = f"""
            Explain this code with {detail_level} detail:
            
            {code}
            
            Instructions: {detail_instructions.get(detail_level, detail_instructions["comprehensive"])}
            
            Provide:
            1. What the code does
            2. How it works
            3. Key concepts and patterns
            4. Potential improvements
            5. Best practices used
            """
            
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error explaining code: {e}"
    
    def debug_code(self, code: str, error: str, context: str = "") -> str:
        """Debug code with enhanced error analysis"""
        try:
            prompt = f"""
            Debug this code. The error is: {error}
            
            Code:
            {code}
            
            Additional Context: {context}
            
            Provide:
            1. Root cause analysis
            2. Step-by-step debugging process
            3. Corrected code with explanations
            4. Prevention strategies
            5. Testing recommendations
            6. Alternative solutions if applicable
            """
            
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error debugging code: {e}"
    
    def refactor_code(self, code: str, improvements: str, target_pattern: str = "modern") -> str:
        """Refactor code with specific target patterns"""
        try:
            prompt = f"""
            Refactor this code with the following improvements: {improvements}
            
            Target Pattern: {target_pattern}
            
            Original code:
            {code}
            
            Requirements:
            1. Refactored code following {target_pattern} patterns
            2. Detailed explanation of changes
            3. Benefits and trade-offs
            4. Performance implications
            5. Maintainability improvements
            6. Before/after comparison
            """
            
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error refactoring code: {e}"
    
    def generate_tests(self, code: str, test_type: str = "comprehensive", framework: str = "pytest") -> str:
        """Generate tests with configurable type and framework"""
        try:
            prompt = f"""
            Generate {test_type} tests for this code using {framework}:
            
            {code}
            
            Test Requirements:
            1. Unit tests for all functions/classes
            2. Edge cases and boundary conditions
            3. Error scenarios and exception handling
            4. Integration tests if applicable
            5. Test documentation and examples
            6. Mock objects and test fixtures
            7. Performance tests if relevant
            
            Framework: {framework}
            Test Type: {test_type}
            """
            
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error generating tests: {e}"
    
    def code_review(self, code: str, review_focus: str = "comprehensive") -> str:
        """Perform code review with specific focus areas"""
        try:
            focus_areas = {
                "security": "Focus on security vulnerabilities and best practices",
                "performance": "Focus on performance optimization and efficiency",
                "maintainability": "Focus on code structure and maintainability",
                "comprehensive": "Cover all aspects including security, performance, and maintainability"
            }
            
            prompt = f"""
            Perform a {review_focus} code review:
            
            {code}
            
            Focus Areas: {focus_areas.get(review_focus, focus_areas["comprehensive"])}
            
            Evaluate:
            1. Code quality and structure
            2. Performance considerations
            3. Security vulnerabilities
            4. Best practices adherence
            5. Error handling and edge cases
            6. Documentation and comments
            7. Testing coverage
            8. Specific recommendations for improvement
            """
            
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error performing code review: {e}"
    
    def generate_docs(self, code: str, doc_type: str = "comprehensive", format: str = "markdown") -> str:
        """Generate documentation with configurable type and format"""
        try:
            prompt = f"""
            Generate {doc_type} documentation for this code in {format} format:
            
            {code}
            
            Documentation Requirements:
            1. Function/class descriptions
            2. Parameters and return values
            3. Usage examples and code snippets
            4. API documentation
            5. Installation and setup instructions
            6. Configuration options
            7. Troubleshooting guide
            8. Performance considerations
            
            Format: {format}
            Type: {doc_type}
            """
            
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error generating documentation: {e}"
    
    def generate_project_structure(self, project_type: str, requirements: str, framework: str = "") -> str:
        """Generate complete project structure"""
        try:
            framework_info = f" using {framework}" if framework else ""
            prompt = f"""
            Generate a complete project structure for a {project_type} project{framework_info}:
            
            Requirements: {requirements}
            
            Provide:
            1. Complete directory structure
            2. File names and purposes
            3. Basic file contents and templates
            4. Dependencies and requirements
            5. Setup and installation instructions
            6. Configuration files
            7. Build and deployment scripts
            8. Testing setup
            9. Documentation structure
            10. Git ignore and other project files
            """
            
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error generating project structure: {e}"
    
    def optimize_code(self, code: str, optimization_type: str, target_metric: str = "performance") -> str:
        """Optimize code for specific metrics"""
        try:
            prompt = f"""
            Optimize this code for {optimization_type} with focus on {target_metric}:
            
            {code}
            
            Optimization Requirements:
            1. Optimized code implementation
            2. Detailed explanation of optimizations
            3. Performance improvements and metrics
            4. Memory usage optimization
            5. Algorithm improvements
            6. Before/after comparison
            7. Trade-offs and considerations
            8. Testing recommendations
            """
            
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error optimizing code: {e}"
    
    def convert_language(self, code: str, source_lang: str, target_lang: str, maintain_style: bool = True) -> str:
        """Convert code between programming languages"""
        try:
            style_instruction = "Maintain the original coding style and patterns" if maintain_style else "Use target language best practices"
            prompt = f"""
            Convert this {source_lang} code to {target_lang}:
            
            {code}
            
            Requirements:
            1. Maintain exact functionality
            2. {style_instruction}
            3. Use {target_lang} best practices and idioms
            4. Handle language-specific features appropriately
            5. Include comprehensive comments
            6. Error handling and edge cases
            7. Performance considerations
            8. Testing recommendations
            """
            
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error converting code: {e}"
    
    def analyze_security(self, code: str, security_level: str = "comprehensive") -> str:
        """Analyze code for security vulnerabilities"""
        try:
            prompt = f"""
            Perform a {security_level} security analysis of this code:
            
            {code}
            
            Security Analysis Areas:
            1. SQL injection vulnerabilities
            2. XSS and injection attacks
            3. Authentication and authorization issues
            4. Data exposure and privacy concerns
            5. Input validation and sanitization
            6. Secure coding practices
            7. OWASP Top 10 compliance
            8. Risk assessment and severity levels
            9. Fix recommendations and examples
            10. Security testing strategies
            """
            
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error analyzing security: {e}"
    
    def create_docker_setup(self, project_type: str, requirements: str, multi_stage: bool = True) -> str:
        """Generate Docker configuration with advanced options"""
        try:
            multi_stage_info = "with multi-stage builds" if multi_stage else "with single-stage build"
            prompt = f"""
            Create a complete Docker setup for {project_type} project {multi_stage_info}:
            
            Requirements: {requirements}
            
            Include:
            1. Optimized Dockerfile
            2. docker-compose.yml with services
            3. .dockerignore file
            4. Build and runtime instructions
            5. Environment configuration
            6. Health checks and monitoring
            7. Security best practices
            8. Performance optimization
            9. Development vs production configs
            10. Troubleshooting guide
            """
            
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error creating Docker setup: {e}"
    
    def generate_ci_cd(self, project_type: str, platform: str, deployment_target: str = "cloud") -> str:
        """Generate CI/CD pipeline configuration"""
        try:
            prompt = f"""
            Generate a {platform} CI/CD pipeline for {project_type} project:
            
            Deployment Target: {deployment_target}
            
            Include:
            1. Build and test stages
            2. Security scanning and code quality checks
            3. Automated testing (unit, integration, e2e)
            4. Deployment strategies and environments
            5. Rollback procedures
            6. Monitoring and alerting
            7. Performance testing
            8. Security compliance checks
            9. Documentation generation
            10. Notification and reporting
            """
            
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error generating CI/CD: {e}"
    
    def interactive_session(self):
        """Enhanced interactive coding session"""
        console.print(Panel.fit(
            "[bold blue]Enhanced Gemini Codex CLI - Interactive Mode[/bold blue]\n"
            "Type 'help' for commands, 'exit' to quit\n"
            "Advanced features available: project, optimize, convert, security, docker, cicd",
            title="🚀 Welcome to Enhanced Mode"
        ))
        
        while True:
            try:
                user_input = Prompt.ask("\n[bold cyan]Enhanced-Codex[/bold cyan]")
                
                if user_input.lower() in ['exit', 'quit', 'q']:
                    break
                elif user_input.lower() == 'help':
                    self.show_enhanced_help()
                elif user_input.lower().startswith('generate'):
                    self.handle_generate_command(user_input)
                elif user_input.lower().startswith('project'):
                    self.handle_project_command(user_input)
                elif user_input.lower().startswith('optimize'):
                    self.handle_optimize_command(user_input)
                elif user_input.lower().startswith('convert'):
                    self.handle_convert_command(user_input)
                elif user_input.lower().startswith('security'):
                    self.handle_security_command(user_input)
                elif user_input.lower().startswith('docker'):
                    self.handle_docker_command(user_input)
                elif user_input.lower().startswith('cicd'):
                    self.handle_cicd_command(user_input)
                else:
                    # Treat as code generation prompt
                    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), console=console):
                        code = self.generate_code(user_input)
                    console.print(Syntax(code, "python", theme="monokai"))
                    
            except KeyboardInterrupt:
                break
            except Exception as e:
                console.print(f"[red]Error: {e}[/red]")
    
    def show_enhanced_help(self):
        """Show enhanced help with all available commands"""
        help_table = Table(title="Enhanced Commands Available")
        help_table.add_column("Command", style="cyan")
        help_table.add_column("Description", style="white")
        help_table.add_column("Usage", style="yellow")
        
        commands = [
            ("generate", "Generate code from description", "generate <prompt> [--lang <language>]"),
            ("explain", "Explain code in file", "explain <file> [--detail <level>]"),
            ("debug", "Debug code with error", "debug <file> <error> [--context <context>]"),
            ("refactor", "Refactor code", "refactor <file> <improvements> [--pattern <pattern>]"),
            ("test", "Generate tests", "test <file> [--type <type>] [--framework <framework>]"),
            ("review", "Code review", "review <file> [--focus <focus>]"),
            ("docs", "Generate documentation", "docs <file> [--type <type>] [--format <format>]"),
            ("project", "Generate project structure", "project <type> <requirements> [--framework <framework>]"),
            ("optimize", "Optimize code", "optimize <file> <type> [--metric <metric>]"),
            ("convert", "Convert language", "convert <file> <source> <target> [--maintain-style]"),
            ("security", "Security analysis", "security <file> [--level <level>]"),
            ("docker", "Docker setup", "docker <type> <requirements> [--multi-stage]"),
            ("cicd", "CI/CD pipeline", "cicd <type> <platform> [--target <target>]"),
            ("help", "Show this help", "help"),
            ("exit", "Exit interactive mode", "exit")
        ]
        
        for cmd, desc, usage in commands:
            help_table.add_row(cmd, desc, usage)
        
        console.print(help_table)
    
    def handle_generate_command(self, user_input: str):
        """Handle generate command in interactive mode"""
        parts = user_input.split()
        if len(parts) < 2:
            console.print("[yellow]Usage: generate <prompt> [--lang <language>][/yellow]")
            return
        
        prompt = " ".join(parts[1:])
        language = "python"  # Default
        
        # Parse language option
        if "--lang" in parts:
            try:
                lang_index = parts.index("--lang")
                if lang_index + 1 < len(parts):
                    language = parts[lang_index + 1]
            except ValueError:
                pass
        
        with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), console=console):
            code = self.generate_code(prompt, language=language)
        console.print(Syntax(code, language, theme="monokai"))
    
    def handle_project_command(self, user_input: str):
        """Handle project command in interactive mode"""
        parts = user_input.split()
        if len(parts) < 3:
            console.print("[yellow]Usage: project <type> <requirements> [--framework <framework>][/yellow]")
            return
        
        project_type = parts[1]
        requirements = " ".join(parts[2:])
        framework = ""
        
        # Parse framework option
        if "--framework" in parts:
            try:
                framework_index = parts.index("--framework")
                if framework_index + 1 < len(parts):
                    framework = parts[framework_index + 1]
            except ValueError:
                pass
        
        with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), console=console):
            result = self.generate_project_structure(project_type, requirements, framework)
        console.print(Panel(result, title="Project Structure"))
    
    def handle_optimize_command(self, user_input: str):
        """Handle optimize command in interactive mode"""
        parts = user_input.split()
        if len(parts) < 3:
            console.print("[yellow]Usage: optimize <file> <type> [--metric <metric>][/yellow]")
            return
        
        file_path = parts[1]
        opt_type = parts[2]
        metric = "performance"
        
        # Parse metric option
        if "--metric" in parts:
            try:
                metric_index = parts.index("--metric")
                if metric_index + 1 < len(parts):
                    metric = parts[metric_index + 1]
            except ValueError:
                pass
        
        try:
            with open(file_path, 'r') as f:
                code = f.read()
            
            with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), console=console):
                result = self.optimize_code(code, opt_type, metric)
            console.print(Panel(result, title="Code Optimization"))
        except FileNotFoundError:
            console.print(f"[red]File {file_path} not found[/red]")
        except Exception as e:
            console.print(f"[red]Error: {e}[/red]")
    
    def handle_convert_command(self, user_input: str):
        """Handle convert command in interactive mode"""
        parts = user_input.split()
        if len(parts) < 4:
            console.print("[yellow]Usage: convert <file> <source> <target> [--maintain-style][/yellow]")
            return
        
        file_path = parts[1]
        source_lang = parts[2]
        target_lang = parts[3]
        maintain_style = "--maintain-style" in parts
        
        try:
            with open(file_path, 'r') as f:
                code = f.read()
            
            with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), console=console):
                result = self.convert_language(code, source_lang, target_lang, maintain_style)
            console.print(Panel(result, title="Language Conversion"))
        except FileNotFoundError:
            console.print(f"[red]File {file_path} not found[/red]")
        except Exception as e:
            console.print(f"[red]Error: {e}[/red]")
    
    def handle_security_command(self, user_input: str):
        """Handle security command in interactive mode"""
        parts = user_input.split()
        if len(parts) < 2:
            console.print("[yellow]Usage: security <file> [--level <level>][/yellow]")
            return
        
        file_path = parts[1]
        level = "comprehensive"
        
        # Parse level option
        if "--level" in parts:
            try:
                level_index = parts.index("--level")
                if level_index + 1 < len(parts):
                    level = parts[level_index + 1]
            except ValueError:
                pass
        
        try:
            with open(file_path, 'r') as f:
                code = f.read()
            
            with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), console=console):
                result = self.analyze_security(code, level)
            console.print(Panel(result, title="Security Analysis"))
        except FileNotFoundError:
            console.print(f"[red]File {file_path} not found[/red]")
        except Exception as e:
            console.print(f"[red]Error: {e}[/red]")
    
    def handle_docker_command(self, user_input: str):
        """Handle docker command in interactive mode"""
        parts = user_input.split()
        if len(parts) < 3:
            console.print("[yellow]Usage: docker <type> <requirements> [--multi-stage][/yellow]")
            return
        
        project_type = parts[1]
        requirements = " ".join(parts[2:])
        multi_stage = "--multi-stage" in parts
        
        with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), console=console):
            result = self.create_docker_setup(project_type, requirements, multi_stage)
        console.print(Panel(result, title="Docker Setup"))
    
    def handle_cicd_command(self, user_input: str):
        """Handle CI/CD command in interactive mode"""
        parts = user_input.split()
        if len(parts) < 3:
            console.print("[yellow]Usage: cicd <type> <platform> [--target <target>][/yellow]")
            return
        
        project_type = parts[1]
        platform = parts[2]
        target = "cloud"
        
        # Parse target option
        if "--target" in parts:
            try:
                target_index = parts.index("--target")
                if target_index + 1 < len(parts):
                    target = parts[target_index + 1]
            except ValueError:
                pass
        
        with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), console=console):
            result = self.generate_ci_cd(project_type, platform, target)
        console.print(Panel(result, title="CI/CD Pipeline"))
    
    def process_file(self, file_path: str, operation: str, **kwargs):
        """Process a file with specified operation"""
        try:
            with open(file_path, 'r') as f:
                code = f.read()
            
            if operation == 'explain':
                detail_level = kwargs.get('detail_level', 'comprehensive')
                result = self.explain_code(code, detail_level)
            elif operation == 'debug':
                error = kwargs.get('error', '')
                context = kwargs.get('context', '')
                result = self.debug_code(code, error, context)
            elif operation == 'refactor':
                improvements = kwargs.get('improvements', '')
                pattern = kwargs.get('pattern', 'modern')
                result = self.refactor_code(code, improvements, pattern)
            elif operation == 'test':
                test_type = kwargs.get('test_type', 'comprehensive')
                framework = kwargs.get('framework', 'pytest')
                result = self.generate_tests(code, test_type, framework)
            elif operation == 'review':
                focus = kwargs.get('focus', 'comprehensive')
                result = self.code_review(code, focus)
            elif operation == 'docs':
                doc_type = kwargs.get('doc_type', 'comprehensive')
                format = kwargs.get('format', 'markdown')
                result = self.generate_docs(code, doc_type, format)
            elif operation == 'optimize':
                opt_type = kwargs.get('optimization_type', 'performance')
                metric = kwargs.get('target_metric', 'performance')
                result = self.optimize_code(code, opt_type, metric)
            elif operation == 'security':
                level = kwargs.get('security_level', 'comprehensive')
                result = self.analyze_security(code, level)
            else:
                result = "Unknown operation"
            
            return result
        except FileNotFoundError:
            return f"File {file_path} not found"
        except Exception as e:
            return f"Error processing file: {e}"

# CLI Commands using Click
@click.group()
@click.version_option(version="2.0.0")
def cli():
    """Enhanced Gemini Codex CLI - AI-powered code generation and analysis"""
    pass

@cli.command()
@click.option('--prompt', '-p', required=True, help='Code generation prompt')
@click.option('--output', '-o', help='Output file path')
@click.option('--context', '-c', help='Additional context for generation')
@click.option('--language', '-l', default='python', help='Target programming language')
def generate(prompt, output, context, language):
    """Generate code from description"""
    codex = EnhancedGeminiCodexCLI()
    
    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), console=console):
        code = codex.generate_code(prompt, context or "", language)
    
    if output:
        with open(output, 'w') as f:
            f.write(code)
        console.print(f"[green]Code generated and saved to {output}[/green]")
    else:
        console.print(Syntax(code, language, theme="monokai"))

@cli.command()
@click.argument('file_path')
@click.option('--detail', '-d', default='comprehensive', help='Detail level (basic, detailed, comprehensive)')
def explain(file_path, detail):
    """Explain code in file"""
    codex = EnhancedGeminiCodexCLI()
    result = codex.process_file(file_path, 'explain', detail_level=detail)
    console.print(Panel(result, title="Code Explanation"))

@cli.command()
@click.argument('file_path')
@click.argument('error')
@click.option('--context', '-c', help='Additional context for debugging')
def debug(file_path, error, context):
    """Debug code with error"""
    codex = EnhancedGeminiCodexCLI()
    result = codex.process_file(file_path, 'debug', error=error, context=context or "")
    console.print(Panel(result, title="Debug Results"))

@cli.command()
@click.argument('file_path')
@click.argument('improvements')
@click.option('--pattern', '-p', default='modern', help='Target refactoring pattern')
def refactor(file_path, improvements, pattern):
    """Refactor code with improvements"""
    codex = EnhancedGeminiCodexCLI()
    result = codex.process_file(file_path, 'refactor', improvements=improvements, pattern=pattern)
    console.print(Panel(result, title="Refactored Code"))

@cli.command()
@click.argument('file_path')
@click.option('--type', '-t', default='comprehensive', help='Test type (basic, comprehensive, performance)')
@click.option('--framework', '-f', default='pytest', help='Testing framework')
def test(file_path, type, framework):
    """Generate tests for code"""
    codex = EnhancedGeminiCodexCLI()
    result = codex.process_file(file_path, 'test', test_type=type, framework=framework)
    console.print(Panel(result, title="Generated Tests"))

@cli.command()
@click.argument('file_path')
@click.option('--focus', '-f', default='comprehensive', help='Review focus (security, performance, maintainability, comprehensive)')
def review(file_path, focus):
    """Perform code review"""
    codex = EnhancedGeminiCodexCLI()
    result = codex.process_file(file_path, 'review', focus=focus)
    console.print(Panel(result, title="Code Review"))

@cli.command()
@click.argument('file_path')
@click.option('--type', '-t', default='comprehensive', help='Documentation type (basic, comprehensive, api)')
@click.option('--format', '-f', default='markdown', help='Output format (markdown, html, rst)')
def docs(file_path, type, format):
    """Generate documentation for code"""
    codex = EnhancedGeminiCodexCLI()
    result = codex.process_file(file_path, 'docs', doc_type=type, format=format)
    console.print(Panel(result, title="Generated Documentation"))

@cli.command()
@click.argument('project_type')
@click.argument('requirements')
@click.option('--framework', '-f', help='Specific framework to use')
@click.option('--output', '-o', help='Output directory for project structure')
def project(project_type, requirements, framework, output):
    """Generate complete project structure"""
    codex = EnhancedGeminiCodexCLI()
    
    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), console=console):
        result = codex.generate_project_structure(project_type, requirements, framework or "")
    
    if output:
        # Save project structure to file
        with open(output, 'w') as f:
            f.write(result)
        console.print(f"[green]Project structure saved to {output}[/green]")
    else:
        console.print(Panel(result, title="Project Structure"))

@cli.command()
@click.argument('file_path')
@click.argument('optimization_type')
@click.option('--metric', '-m', default='performance', help='Target optimization metric')
def optimize(file_path, optimization_type, metric):
    """Optimize code for specific metrics"""
    codex = EnhancedGeminiCodexCLI()
    result = codex.process_file(file_path, 'optimize', optimization_type=optimization_type, target_metric=metric)
    console.print(Panel(result, title="Code Optimization"))

@cli.command()
@click.argument('file_path')
@click.argument('source_language')
@click.argument('target_language')
@click.option('--maintain-style', is_flag=True, help='Maintain original coding style')
@click.option('--output', '-o', help='Output file for converted code')
def convert(file_path, source_language, target_language, maintain_style, output):
    """Convert code between programming languages"""
    codex = EnhancedGeminiCodexCLI()
    
    try:
        with open(file_path, 'r') as f:
            code = f.read()
        
        with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), console=console):
            result = codex.convert_language(code, source_language, target_language, maintain_style)
        
        if output:
            with open(output, 'w') as f:
                f.write(result)
            console.print(f"[green]Converted code saved to {output}[/green]")
        else:
            console.print(Panel(result, title="Language Conversion"))
    except FileNotFoundError:
        console.print(f"[red]File {file_path} not found[/red]")
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")

@cli.command()
@click.argument('file_path')
@click.option('--level', '-l', default='comprehensive', help='Security analysis level')
def security(file_path, level):
    """Analyze code for security vulnerabilities"""
    codex = EnhancedGeminiCodexCLI()
    result = codex.process_file(file_path, 'security', security_level=level)
    console.print(Panel(result, title="Security Analysis"))

@cli.command()
@click.argument('project_type')
@click.argument('requirements')
@click.option('--multi-stage', is_flag=True, help='Use multi-stage Docker build')
@click.option('--output', '-o', help='Output directory for Docker files')
def docker(project_type, requirements, multi_stage, output):
    """Generate Docker configuration"""
    codex = EnhancedGeminiCodexCLI()
    
    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), console=console):
        result = codex.create_docker_setup(project_type, requirements, multi_stage)
    
    if output:
        # Save Docker configuration to files
        dockerfile_path = os.path.join(output, "Dockerfile")
        compose_path = os.path.join(output, "docker-compose.yml")
        
        os.makedirs(output, exist_ok=True)
        
        # Extract Dockerfile and docker-compose.yml from result
        # This is a simplified approach - in practice, you'd parse the result more carefully
        with open(dockerfile_path, 'w') as f:
            f.write(result)
        
        console.print(f"[green]Docker configuration saved to {output}[/green]")
    else:
        console.print(Panel(result, title="Docker Setup"))

@cli.command()
@click.argument('project_type')
@click.argument('platform')
@click.option('--target', '-t', default='cloud', help='Deployment target')
@click.option('--output', '-o', help='Output file for CI/CD configuration')
def cicd(project_type, platform, target, output):
    """Generate CI/CD pipeline configuration"""
    codex = EnhancedGeminiCodexCLI()
    
    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), console=console):
        result = codex.generate_ci_cd(project_type, platform, target)
    
    if output:
        with open(output, 'w') as f:
            f.write(result)
        console.print(f"[green]CI/CD configuration saved to {output}[/green]")
    else:
        console.print(Panel(result, title="CI/CD Pipeline"))

@cli.command()
def interactive():
    """Start enhanced interactive coding session"""
    codex = EnhancedGeminiCodexCLI()
    codex.interactive_session()

if __name__ == '__main__':
    cli()
