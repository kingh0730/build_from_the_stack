from dotenv import dotenv_values

env = dotenv_values()
OPENAI_API_KEY = env["OPENAI_API_KEY"]
