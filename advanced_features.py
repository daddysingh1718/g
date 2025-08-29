#!/usr/bin/env python3
"""
Advanced Features for Gemini Codex CLI
Additional capabilities beyond basic code generation
"""

import os
import sys
import json
import subprocess
import tempfile
from pathlib import Path
from typing import List, Dict, Any, Optional
import google.generativeai as genai
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.syntax import Syntax

console = Console()

class AdvancedCodexFeatures:
    """Advanced features for enhanced code generation and analysis"""
    
    def __init__(self, model):
        self.model = model
    
    def generate_project_structure(self, project_type: str, requirements: str) -> str:
        """Generate complete project structure"""
        try:
            prompt = f"""
            Generate a complete project structure for a {project_type} project.
            
            Requirements: {requirements}
            
            Provide:
            1. Directory structure
            2. File names and purposes
            3. Basic file contents
            4. Dependencies
            5. Setup instructions
            """
            
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error generating project structure: {e}"
    
    def optimize_code(self, code: str, optimization_type: str) -> str:
        """Optimize code for performance, memory, or readability"""
        try:
            prompt = f"""
            Optimize this code for {optimization_type}:
            
            {code}
            
            Provide:
            1. Optimized code
            2. Explanation of optimizations
            3. Performance improvements
            4. Before/after comparison
            """
            
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error optimizing code: {e}"
    
    def convert_language(self, code: str, source_lang: str, target_lang: str) -> str:
        """Convert code between programming languages"""
        try:
            prompt = f"""
            Convert this {source_lang} code to {target_lang}:
            
            {code}
            
            Requirements:
            1. Maintain functionality
            2. Use {target_lang} best practices
            3. Include comments
            4. Handle language-specific features
            """
            
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error converting code: {e}"
    
    def generate_api_client(self, api_spec: str, language: str) -> str:
        """Generate API client from specification"""
        try:
            prompt = f"""
            Generate a {language} API client from this specification:
            
            {api_spec}
            
            Include:
            1. Client class
            2. Method implementations
            3. Error handling
            4. Authentication
            5. Example usage
            """
            
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error generating API client: {e}"
    
    def analyze_security(self, code: str) -> str:
        """Analyze code for security vulnerabilities"""
        try:
            prompt = f"""
            Analyze this code for security vulnerabilities:
            
            {code}
            
            Check for:
            1. SQL injection
            2. XSS vulnerabilities
            3. Authentication issues
            4. Data exposure
            5. Input validation
            6. Secure coding practices
            
            Provide:
            1. Vulnerability assessment
            2. Risk levels
            3. Fix recommendations
            4. Secure code examples
            """
            
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error analyzing security: {e}"
    
    def generate_migrations(self, old_schema: str, new_schema: str, db_type: str) -> str:
        """Generate database migration scripts"""
        try:
            prompt = f"""
            Generate {db_type} migration scripts:
            
            Old Schema:
            {old_schema}
            
            New Schema:
            {new_schema}
            
            Provide:
            1. Migration scripts
            2. Rollback scripts
            3. Data transformation
            4. Testing instructions
            """
            
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error generating migrations: {e}"
    
    def create_docker_setup(self, project_type: str, requirements: str) -> str:
        """Generate Docker configuration"""
        try:
            prompt = f"""
            Create Docker setup for {project_type} project:
            
            Requirements: {requirements}
            
            Include:
            1. Dockerfile
            2. docker-compose.yml
            3. .dockerignore
            4. Build instructions
            5. Runtime configuration
            """
            
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error creating Docker setup: {e}"
    
    def generate_ci_cd(self, project_type: str, platform: str) -> str:
        """Generate CI/CD pipeline configuration"""
        try:
            prompt = f"""
            Generate {platform} CI/CD pipeline for {project_type}:
            
            Include:
            1. Build steps
            2. Testing
            3. Deployment
            4. Security scanning
            5. Notifications
            """
            
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error generating CI/CD: {e}"
    
    def code_metrics(self, code: str) -> Dict[str, Any]:
        """Analyze code metrics and quality"""
        try:
            prompt = f"""
            Analyze code metrics for this code:
            
            {code}
            
            Provide metrics for:
            1. Cyclomatic complexity
            2. Lines of code
            3. Code duplication
            4. Maintainability index
            5. Code quality score
            6. Recommendations
            """
            
            response = self.model.generate_content(prompt)
            return {"metrics": response.text, "raw_code": code}
        except Exception as e:
            return {"error": f"Error analyzing metrics: {e}"}
    
    def generate_mock_data(self, schema: str, count: int) -> str:
        """Generate mock data from schema"""
        try:
            prompt = f"""
            Generate {count} mock data records from this schema:
            
            {schema}
            
            Requirements:
            1. Realistic data
            2. Proper data types
            3. Relationships maintained
            4. Export formats (JSON, CSV, SQL)
            """
            
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error generating mock data: {e}"
