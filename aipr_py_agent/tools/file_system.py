import os

def list_files(directory: str = ".") -> str:
    """
    Lists all files and directories under the given path.

    Args:
        directory: The path to the directory to list. Defaults to the current directory.

    Returns:
        A string containing the list of files and directories, separated by newlines.
    """
    print(f"Tool: list_files, Directory: {directory}")
    try:
        if not os.path.isdir(directory):
            return f"Error: Directory '{directory}' not found."

        files = os.listdir(directory)

        if not files:
            return "The directory is empty."

        # Add a trailing slash to directories for clarity
        output = []
        for f in sorted(files): # Sorting for consistent output
            if os.path.isdir(os.path.join(directory, f)):
                output.append(f + "/")
            else:
                output.append(f)

        return "\n".join(output)
    except Exception as e:
        return f"An error occurred while listing files: {e}"

def read_file(filepath: str) -> str:
    """
    Reads the content of the specified file.

    Args:
        filepath: The path to the file to read.

    Returns:
        The content of the file as a string.
    """
    print(f"Tool: read_file, Filepath: {filepath}")
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return f"Error: File '{filepath}' not found."
    except Exception as e:
        return f"An error occurred while reading the file: {e}"

def write_file(filepath: str, content: str) -> str:
    """
    Writes the given content to the specified file.
    This will create the directory if it doesn't exist and overwrite the file if it exists.

    Args:
        filepath: The path to the file to write.
        content: The content to write to the file.

    Returns:
        A confirmation message.
    """
    print(f"Tool: write_file, Filepath: {filepath}")
    try:
        # Ensure the directory exists
        directory = os.path.dirname(filepath)
        if directory:
            os.makedirs(directory, exist_ok=True)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return f"File '{filepath}' written successfully."
    except Exception as e:
        return f"An error occurred while writing the file: {e}"
