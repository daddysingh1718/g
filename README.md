# 🚀 Gemini Codex CLI

A complete, feature-rich CLI tool powered by Google Gemini 8, designed to replace OpenAI Codex CLI with full feature parity and enhanced capabilities.

## ✨ Features

### 🎯 Core Code Generation
- **AI-Powered Code Generation**: Generate production-ready code from natural language descriptions
- **Context-Aware Generation**: Provide additional context for better code generation
- **Multi-Language Support**: Generate code in Python, JavaScript, Java, C++, Go, Rust, and more
- **Interactive Mode**: Real-time coding assistance with conversation history

### 🔍 Code Analysis & Understanding
- **Code Explanation**: Get detailed explanations of any codebase
- **Code Review**: Comprehensive code quality analysis and improvement suggestions
- **Security Analysis**: Vulnerability detection and security best practices
- **Performance Optimization**: Code optimization for speed, memory, and readability

### 🛠️ Advanced Development Tools
- **Project Structure Generation**: Complete project scaffolding
- **API Client Generation**: Generate API clients from specifications
- **Database Migrations**: Create migration scripts for schema changes
- **Test Generation**: Comprehensive test suites for your code
- **Documentation Generation**: Auto-generate API docs and code documentation

### 🚀 DevOps & Infrastructure
- **Docker Configuration**: Generate Dockerfiles and docker-compose files
- **CI/CD Pipelines**: Create GitHub Actions, GitLab CI, and other pipeline configs
- **Kubernetes Manifests**: Generate K8s deployment configurations
- **Infrastructure as Code**: Terraform and CloudFormation templates

### 🔧 Code Transformation
- **Language Conversion**: Convert code between programming languages
- **Code Refactoring**: Improve code structure and maintainability
- **Legacy Code Modernization**: Update old code to modern standards
- **Format Conversion**: Convert between different code formats

## 🚀 Installation

### Prerequisites
- Python 3.8+
- Google API key for Gemini

### Quick Install
```bash
# Clone the repository
git clone <repository-url>
cd gemini-codex-cli

# Install dependencies
pip install -r requirements.txt

# Set your Google API key
export GOOGLE_API_KEY="your_api_key_here"

# Make executable
chmod +x gemini_codex_cli.py
```

### Environment Setup
```bash
# Add to your shell profile (.bashrc, .zshrc, etc.)
export GOOGLE_API_KEY="your_google_api_key"
export PATH="$PATH:/path/to/gemini-codex-cli"
```

## 📖 Usage

### Basic Commands

#### Generate Code
```bash
# Generate code from description
python gemini_codex_cli.py generate --prompt "Create a REST API endpoint for user authentication"

# Save to file
python gemini_codex_cli.py generate --prompt "Create a web scraper" --output scraper.py

# With context
python gemini_codex_cli.py generate --prompt "Add error handling" --context "existing_code.py"
```

#### Code Analysis
```bash
# Explain code
python gemini_codex_cli.py explain myfile.py

# Code review
python gemini_codex_cli.py review myfile.py

# Security analysis
python gemini_codex_cli.py security myfile.py

# Generate tests
python gemini_codex_cli.py test myfile.py
```

#### Code Transformation
```bash
# Refactor code
python gemini_codex_cli.py refactor myfile.py "improve performance and readability"

# Convert language
python gemini_codex_cli.py convert myfile.py python javascript

# Optimize code
python gemini_codex_cli.py optimize myfile.py performance
```

### Interactive Mode
```bash
# Start interactive session
python gemini_codex_cli.py interactive

# Available commands in interactive mode:
# - generate <prompt> - Generate code
# - explain <file> - Explain code
# - debug <file> <error> - Debug code
# - refactor <file> <improvements> - Refactor code
# - test <file> - Generate tests
# - review <file> - Code review
# - docs <file> - Generate documentation
# - help - Show help
# - exit - Exit session
```

### Advanced Features

#### Project Generation
```bash
# Generate complete project structure
python gemini_codex_cli.py project --type "web-app" --requirements "React frontend, Node.js backend, MongoDB"

# Generate with specific framework
python gemini_codex_cli.py project --type "api" --framework "FastAPI" --database "PostgreSQL"
```

#### Infrastructure Generation
```bash
# Generate Docker setup
python gemini_codex_cli.py docker --type "python-web" --requirements "Flask, Redis"

# Generate CI/CD pipeline
python gemini_codex_cli.py cicd --platform "github" --type "python-package"

# Generate Kubernetes manifests
python gemini_codex_cli.py k8s --type "web-application" --ingress "nginx"
```

## ⚙️ Configuration

### Configuration File
The CLI creates a configuration file at `~/.gemini_codex/config.json`:

```json
{
  "model": "gemini-1.5-pro",
  "temperature": 0.7,
  "max_tokens": 4000,
  "theme": "monokai",
  "auto_save": true,
  "backup_count": 5,
  "log_level": "INFO",
  "timeout": 30,
  "retry_attempts": 3
}
```

### Environment Variables
- `GOOGLE_API_KEY`: Your Google API key for Gemini
- `GEMINI_MODEL`: Override default model
- `GEMINI_TEMPERATURE`: Control creativity (0.0-1.0)
- `GEMINI_TIMEOUT`: API timeout in seconds

## 🔧 Architecture

### Core Components
- **GeminiCodexCLI**: Main CLI interface and orchestration
- **AdvancedCodexFeatures**: Extended capabilities and utilities
- **Config**: Configuration management
- **Rich Integration**: Beautiful terminal UI with syntax highlighting

### Design Principles
- **Modular Architecture**: Easy to extend and maintain
- **Error Handling**: Robust error handling and user feedback
- **Performance**: Optimized for fast response times
- **User Experience**: Intuitive interface with rich formatting

## 🚀 Use Cases

### For Developers
- **Rapid Prototyping**: Quickly generate working prototypes
- **Code Learning**: Understand complex codebases
- **Bug Fixing**: Get AI-powered debugging assistance
- **Code Review**: Automated code quality analysis

### For Teams
- **Onboarding**: Help new developers understand codebases
- **Code Standards**: Enforce consistent coding practices
- **Documentation**: Auto-generate and maintain docs
- **Testing**: Ensure comprehensive test coverage

### For Projects
- **Project Setup**: Quick project scaffolding
- **API Development**: Generate API clients and servers
- **Database Design**: Create schemas and migrations
- **DevOps Automation**: Infrastructure and deployment configs

## 🔒 Security

- **API Key Management**: Secure handling of API credentials
- **Input Validation**: Safe processing of user inputs
- **Error Handling**: No sensitive information in error messages
- **Audit Logging**: Track usage for security monitoring

## 🤝 Contributing

We welcome contributions! Please see our contributing guidelines for:
- Bug reports
- Feature requests
- Code contributions
- Documentation improvements

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Google Gemini team for the powerful AI model
- OpenAI Codex for inspiration
- Rich library for beautiful terminal UI
- Click for excellent CLI framework

## 📞 Support

- **Issues**: GitHub Issues
- **Discussions**: GitHub Discussions
- **Documentation**: Comprehensive docs included
- **Examples**: See examples/ directory

---

**Made with ❤️ using Google Gemini 8**
