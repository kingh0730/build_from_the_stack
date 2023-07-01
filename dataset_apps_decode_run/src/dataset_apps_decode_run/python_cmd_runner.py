import subprocess


def python_cmd(cmd, input_text):
    # Define the command to run your Python file
    command = ["python", "-c", cmd]

    # Create a subprocess and redirect input/output
    process = subprocess.Popen(
        command,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    # Provide input to the subprocess
    process.stdin.write(input_text)
    process.stdin.flush()

    # Get the output from the subprocess
    output, error = process.communicate()

    # Print the output
    print(output)

    # Check for any errors
    if process.returncode != 0:
        print(f"Error: {error}")
