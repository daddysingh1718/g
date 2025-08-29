#!/bin/bash
# Deployment script for Gemini Codex CLI

set -e

echo "�� Deploying Gemini Codex CLI..."

# Check if Python 3.8+ is installed
python_version=$(python3 --version 2>&1 | grep -oE '[0-9]+\.[0-9]+' | head -1)
required_version="3.8"

if [ "$(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1)" != "$required_version" ]; then
    echo "❌ Python 3.8+ is required. Current version: $python_version"
    exit 1
fi

echo "✅ Python version check passed: $python_version"

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Upgrade pip
echo "⬆️ Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "📚 Installing dependencies..."
pip install -r requirements.txt

# Make CLI executable
echo "🔧 Making CLI executable..."
chmod +x gemini_codex_cli.py

# Create symlink for global access
echo "🔗 Creating global symlink..."
if [ -w /usr/local/bin ]; then
    sudo ln -sf "$(pwd)/gemini_codex_cli.py" /usr/local/bin/gemini-codex
    echo "✅ Global symlink created: gemini-codex"
elif [ -w ~/.local/bin ]; then
    mkdir -p ~/.local/bin
    ln -sf "$(pwd)/gemini_codex_cli.py" ~/.local/bin/gemini-codex
    echo "✅ Local symlink created: ~/.local/bin/gemini-codex"
    echo "📝 Add ~/.local/bin to your PATH if not already added"
else
    echo "⚠️ Could not create symlink. You can run with: python3 gemini_codex_cli.py"
fi

# Create configuration directory
echo "⚙️ Setting up configuration..."
mkdir -p ~/.gemini_codex

# Check for API key
if [ -z "$GOOGLE_API_KEY" ]; then
    echo "⚠️ GOOGLE_API_KEY environment variable not set"
    echo "📝 Please set it with: export GOOGLE_API_KEY='your_key_here'"
    echo "📝 Or add it to your shell profile (.bashrc, .zshrc, etc.)"
else
    echo "✅ GOOGLE_API_KEY is set"
fi

# Run tests
echo "🧪 Running tests..."
python3 test_cli.py

echo ""
echo "🎉 Deployment completed successfully!"
echo ""
echo "📖 Usage:"
echo "  gemini-codex --help                    # Show help"
echo "  gemini-codex interactive               # Start interactive mode"
echo "  gemini-codex generate --prompt '...'   # Generate code"
echo ""
echo "🔑 Don't forget to set your GOOGLE_API_KEY!"
echo "📚 See README.md for complete documentation"
