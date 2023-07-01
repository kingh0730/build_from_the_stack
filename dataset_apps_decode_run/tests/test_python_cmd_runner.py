from dataset_apps_decode_run.python_cmd_runner import python_cmd


def test():
    cmd = "print(input() + 'Hello World')"
    input_text = "I am a string\n"
    python_cmd(cmd, input_text)
