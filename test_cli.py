#!/usr/bin/env python3
"""
Test suite for Gemini Codex CLI
Tests all major functionality and features
"""

import unittest
import tempfile
import os
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock

# Mock the Gemini API for testing
class MockGeminiModel:
    def generate_content(self, prompt):
        mock_response = Mock()
        mock_response.text = f"Mock response for: {prompt[:50]}..."
        return mock_response

class MockGeminiAPI:
    def GenerativeModel(self, model_name):
        return MockGeminiModel()

# Test the CLI functionality
class TestGeminiCodexCLI(unittest.TestCase):
    
    def setUp(self):
        """Set up test environment"""
        self.temp_dir = tempfile.mkdtemp()
        self.test_file = Path(self.temp_dir) / "test.py"
        
        # Create a test file
        with open(self.test_file, 'w') as f:
            f.write("def hello():\n    return 'Hello, World!'")
    
    def tearDown(self):
        """Clean up test environment"""
        import shutil
        shutil.rmtree(self.temp_dir)
    
    @patch('google.generativeai.GenerativeModel')
    @patch('google.generativeai.configure')
    def test_setup_gemini(self, mock_configure, mock_model):
        """Test Gemini API setup"""
        from gemini_codex_cli import GeminiCodexCLI
        
        # Mock environment variable
        with patch.dict(os.environ, {'GOOGLE_API_KEY': 'test_key'}):
            mock_model.return_value = MockGeminiModel()
            cli = GeminiCodexCLI()
            
            self.assertIsNotNone(cli.model)
            mock_configure.assert_called_once_with(api_key='test_key')
    
    def test_generate_code(self):
        """Test code generation"""
        from gemini_codex_cli import GeminiCodexCLI
        
        with patch.dict(os.environ, {'GOOGLE_API_KEY': 'test_key'}):
            with patch('google.generativeai.GenerativeModel') as mock_model:
                mock_model.return_value = MockGeminiModel()
                cli = GeminiCodexCLI()
                
                result = cli.generate_code("Create a hello function")
                self.assertIn("Mock response", result)
    
    def test_explain_code(self):
        """Test code explanation"""
        from gemini_codex_cli import GeminiCodexCLI
        
        with patch.dict(os.environ, {'GOOGLE_API_KEY': 'test_key'}):
            with patch('google.generativeai.GenerativeModel') as mock_model:
                mock_model.return_value = MockGeminiModel()
                cli = GeminiCodexCLI()
                
                result = cli.explain_code("def test(): pass")
                self.assertIn("Mock response", result)
    
    def test_process_file(self):
        """Test file processing"""
        from gemini_codex_cli import GeminiCodexCLI
        
        with patch.dict(os.environ, {'GOOGLE_API_KEY': 'test_key'}):
            with patch('google.generativeai.GenerativeModel') as mock_model:
                mock_model.return_value = MockGeminiModel()
                cli = GeminiCodexCLI()
                
                result = cli.process_file(str(self.test_file), 'explain')
                self.assertIn("Mock response", result)
    
    def test_file_not_found(self):
        """Test handling of non-existent files"""
        from gemini_codex_cli import GeminiCodexCLI
        
        with patch.dict(os.environ, {'GOOGLE_API_KEY': 'test_key'}):
            with patch('google.generativeai.GenerativeModel') as mock_model:
                mock_model.return_value = MockGeminiModel()
                cli = GeminiCodexCLI()
                
                result = cli.process_file("nonexistent.py", 'explain')
                self.assertIn("not found", result)

class TestAdvancedFeatures(unittest.TestCase):
    
    def setUp(self):
        """Set up test environment"""
        self.mock_model = MockGeminiModel()
        from advanced_features import AdvancedCodexFeatures
        self.advanced = AdvancedCodexFeatures(self.mock_model)
    
    def test_generate_project_structure(self):
        """Test project structure generation"""
        result = self.advanced.generate_project_structure("web-app", "React frontend")
        self.assertIn("Mock response", result)
    
    def test_optimize_code(self):
        """Test code optimization"""
        result = self.advanced.optimize_code("def test(): pass", "performance")
        self.assertIn("Mock response", result)
    
    def test_analyze_security(self):
        """Test security analysis"""
        result = self.advanced.analyze_security("def test(): pass")
        self.assertIn("Mock response", result)

if __name__ == '__main__':
    # Run tests
    unittest.main(verbosity=2)
