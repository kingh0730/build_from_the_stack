from os import path
from dotenv import dotenv_values

env = dotenv_values()
OPENAI_API_KEY = env["OPENAI_API_KEY"]


DSL_PROMPT_1_INTRO_MD = (
    path.dirname(
        path.dirname(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
    )
    + "/data/inputs_gen/dsl/dsl_prompt_1_intro.md"
)

with open(DSL_PROMPT_1_INTRO_MD, "r") as f:
    DSL_PROMPT_1_INTRO = f.read()
