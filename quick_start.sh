#!/bin/bash
# Quick start script for Gemini Codex CLI

echo "🚀 Quick Start: Gemini Codex CLI"
echo "=================================="

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8+ first."
    exit 1
fi

# Check Python version
python_version=$(python3 --version 2>&1 | grep -oE '[0-9]+\.[0-9]+' | head -1)
echo "✅ Python version: $python_version"

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "�� Installing dependencies..."
pip install -r requirements.txt

# Check API key
if [ -z "$GOOGLE_API_KEY" ]; then
    echo ""
    echo "⚠️  GOOGLE_API_KEY not set!"
    echo "📝 Please set your Google API key:"
    echo "   export GOOGLE_API_KEY='your_api_key_here'"
    echo ""
    echo "🔑 Get your API key from: https://makersuite.google.com/app/apikey"
    echo ""
else
    echo "✅ GOOGLE_API_KEY is set"
fi

echo ""
echo "🎉 Setup complete!"
echo ""
echo "📖 Usage examples:"
echo "   # Basic code generation"
echo "   python gemini_codex_enhanced.py generate --prompt 'Create a hello world function'"
echo ""
echo "   # Interactive mode"
echo "   python gemini_codex_enhanced.py interactive"
echo ""
echo "   # Show all commands"
echo "   python gemini_codex_enhanced.py --help"
echo ""
echo "📚 See README.md for complete documentation"
echo "�� Run ./deploy.sh for full deployment"
