from os import path
from dotenv import dotenv_values

_env = dotenv_values()

OPENAI_API_KEY = _env["OPENAI_API_KEY"]


_top_dir = path.dirname(
    path.dirname(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
)

DSL_PROMPT_1_INTRO_MD = _top_dir + "/data/inputs_gen/dsl/dsl_prompt_1_intro.md"
DSL_PY = _top_dir + "/data/inputs_gen/dsl/dsl.py"

with open(DSL_PROMPT_1_INTRO_MD, "r") as f:
    DSL_PROMPT_1_INTRO = f.read()

with open(DSL_PY, "r") as f:
    DSL = f.read()
