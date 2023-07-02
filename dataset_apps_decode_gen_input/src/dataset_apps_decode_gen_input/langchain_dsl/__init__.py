import openai
from dotenv import dotenv_values

env = dotenv_values()
openai.api_key = env["OPENAI_API_KEY"]
