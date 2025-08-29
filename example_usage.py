#!/usr/bin/env python3
"""
Example usage of Gemini Codex CLI
Demonstrates various features and capabilities
"""

from gemini_codex_cli import GeminiCodexCLI
from advanced_features import AdvancedCodexFeatures

def main():
    """Example usage of the CLI features"""
    
    # Initialize the CLI
    codex = GeminiCodexCLI()
    
    # Example 1: Generate a simple function
    print("=== Example 1: Generate a function ===")
    prompt = "Create a Python function that calculates fibonacci numbers with memoization"
    code = codex.generate_code(prompt)
    print(f"Generated code:\n{code}\n")
    
    # Example 2: Explain existing code
    print("=== Example 2: Explain code ===")
    sample_code = """
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)
    """
    explanation = codex.explain_code(sample_code)
    print(f"Code explanation:\n{explanation}\n")
    
    # Example 3: Generate tests
    print("=== Example 3: Generate tests ===")
    tests = codex.generate_tests(sample_code)
    print(f"Generated tests:\n{tests}\n")
    
    # Example 4: Code review
    print("=== Example 4: Code review ===")
    review = codex.code_review(sample_code)
    print(f"Code review:\n{review}\n")
    
    # Example 5: Generate documentation
    print("=== Example 5: Generate documentation ===")
    docs = codex.generate_docs(sample_code)
    print(f"Generated documentation:\n{docs}\n")

if __name__ == "__main__":
    main()
