import subprocess

def execute_shell_command(command: str) -> str:
    """
    Executes a shell command and returns its output.

    !!! WARNING !!!
    This tool is highly dangerous as it can execute any command on the system.
    The agent's design MUST include a user confirmation step before this tool is ever called.
    This function assumes that confirmation has already been granted.

    Args:
        command: The command string to execute.

    Returns:
        A string containing the STDOUT, STDERR, and return code of the command.
    """
    print(f"Tool: execute_shell_command, Command: {command}")

    try:
        # Using a timeout is crucial to prevent the agent from hanging on long-running commands.
        result = subprocess.run(
            command,
            shell=True,      # Using shell=True for flexibility, but it carries security risks.
                             # The primary safeguard is the user confirmation in the agent loop.
            capture_output=True,
            text=True,
            timeout=60,      # 60-second timeout
            check=False      # We handle non-zero exit codes manually.
        )

        output = ""
        if result.stdout:
            output += f"STDOUT:\n---\n{result.stdout.strip()}\n---\n"
        if result.stderr:
            output += f"STDERR:\n---\n{result.stderr.strip()}\n---\n"

        output += f"Return Code: {result.returncode}"

        # If there was no output to stdout or stderr, provide a confirmation.
        if not result.stdout and not result.stderr:
            return f"Command executed successfully with no output.\nReturn Code: {result.returncode}"
        else:
            return output.strip()

    except subprocess.TimeoutExpired:
        return "Error: Command timed out after 60 seconds."
    except Exception as e:
        return f"An error occurred while executing the shell command: {e}"
