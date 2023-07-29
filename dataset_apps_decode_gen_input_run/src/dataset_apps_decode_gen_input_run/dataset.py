import json

# Third-party imports
from datasets import load_from_disk

# Project imports
from ._config import CACHE_DIR, NUM_PROC
from dataset_apps_decode_gen_input import APPSDecodeGenInput
from dataset_apps_decode_run.python_cmd_runner import python_cmd

# TODO Perhaps not wildcard
from dataset_apps_decode_gen_input_run.dsl_impl_copy_to_run import *


DSL_GEN_BASE_DIR = "./data/inputs_gen/dsl/gen/"


GENERATE_INPUTS_COUNT = 10
GENERATE_ONE_INPUT_TRY_HARD_LIMIT = 1000

# ! Should not override this name
GENERATE_INPUT_FUNC_NAME = "generate_input"


class APPSDecodeGenInputRun:
    def __init__(self, *, logger):
        self._ds = None
        self.logger = logger

    def loads(self):
        try:
            ds = load_from_disk(CACHE_DIR)
            self.logger.info("Loaded dataset from cache")

        except FileNotFoundError:
            ds = self.build()
            ds.save_to_disk(CACHE_DIR)
            self.logger.info("Saved dataset to cache")

        self._ds = ds

    def dataset(self):
        if self._ds is None:
            self.loads()
        return self._ds

    def build(self):
        ds = APPSDecodeGenInput(
            logger=self.logger,
        ).dataset()

        self.save_dsl_py(ds)

        # Execute python files
        new_inputs_all_gpt_4 = {}
        new_inputs_all_gpt_3 = {}
        for row in ds:
            file_name = f"dsl_{row['problem_id']}.py"

            generate_input_gpt_4 = self.process_dsl_py(row["solution: gpt-4"])
            generate_input_gpt_3 = self.process_dsl_py(row["solution: gpt-3.5-turbo"])

            new_inputs = [
                self.generate_one_input_try_hard(generate_input_gpt_4, file_name)
                for _ in range(GENERATE_INPUTS_COUNT)
            ]
            new_inputs_all_gpt_4[row["problem_id"]] = new_inputs

            new_inputs = [
                self.generate_one_input_try_hard(generate_input_gpt_3, file_name)
                for _ in range(GENERATE_INPUTS_COUNT)
            ]
            new_inputs_all_gpt_3[row["problem_id"]] = new_inputs

        ds = ds.map(
            lambda row: {
                "new_inputs: gpt-4": json.dumps(
                    new_inputs_all_gpt_4[row["problem_id"]],
                ),
                "new_inputs: gpt-3.5-turbo": json.dumps(
                    new_inputs_all_gpt_3[row["problem_id"]],
                ),
                "new_inputs_codeforces: gpt-4": [
                    self.input_to_codeforces_format(input)
                    for input in new_inputs_all_gpt_4[row["problem_id"]]
                ],
                "new_inputs_codeforces: gpt-3.5-turbo": [
                    self.input_to_codeforces_format(input)
                    for input in new_inputs_all_gpt_3[row["problem_id"]]
                ],
            },
        )

        ds = ds.map(
            lambda x: {
                "new_answers: gpt-4": [
                    [
                        python_cmd(
                            solution,
                            input,
                        )
                        if input is not None
                        else None
                        for solution in x["solutions"]
                    ]
                    for input in x["new_inputs_codeforces: gpt-4"]
                ],
            },
            num_proc=NUM_PROC,
        )

        ds = ds.map(
            lambda x: {
                "new_answers: gpt-3.5-turbo": [
                    [
                        python_cmd(
                            solution,
                            input,
                        )
                        if input is not None
                        else None
                        for solution in x["solutions"]
                    ]
                    for input in x["new_inputs_codeforces: gpt-3.5-turbo"]
                ],
            },
            num_proc=NUM_PROC,
        )

        ds = ds.map(
            lambda x: {
                "new_answers_agree: gpt-4": [
                    len(set(answers)) == 1 and None not in answers
                    for answers in x["new_answers: gpt-4"]
                ],
            },
            num_proc=NUM_PROC,
        )

        ds = ds.map(
            lambda x: {
                "new_answers_agree: gpt-3.5-turbo": [
                    len(set(answers)) == 1 and None not in answers
                    for answers in x["new_answers: gpt-3.5-turbo"]
                ],
            },
            num_proc=NUM_PROC,
        )

        return ds

    def input_to_codeforces_format(self, input: list | None) -> str | None:
        if input is None:
            return None

        result = []

        for x in input:
            if isinstance(x, list):
                line = " ".join(map(str, x))
                result.append(line)

            else:
                result.append(str(x))

        return "\n".join(result)

    def generate_one_input_try_hard(
        self, generate_input: str, file_name: str
    ) -> list | None:
        for _ in range(GENERATE_ONE_INPUT_TRY_HARD_LIMIT):
            once_or_none = self.generate_input_once_or_none(
                generate_input,
                file_name,
            )

            if once_or_none is not None:
                return once_or_none

    def generate_input_once_or_none(
        self, generate_input: str, file_name: str
    ) -> list | None:
        try:
            loc = {}
            # TODO import statements do not work inside exec
            exec(generate_input, None, loc)

            return loc[GENERATE_INPUT_FUNC_NAME]()
        except Exception as e:
            print(f"Failed to execute {file_name} due to {e}")

    def save_dsl_py(self, apps_decode_gen_input):
        for row in apps_decode_gen_input:
            generate_input_gpt_4 = self.process_dsl_py(row["solution: gpt-4"])
            generate_input_gpt_3 = self.process_dsl_py(row["solution: gpt-3.5-turbo"])

            file_name = f"dsl_{row['problem_id']}.py"

            with open(f"{DSL_GEN_BASE_DIR}/gpt-4/{file_name}", "w") as f:
                f.write(generate_input_gpt_4)

            with open(f"{DSL_GEN_BASE_DIR}/gpt-3.5-turbo/{file_name}", "w") as f:
                f.write(generate_input_gpt_3)

    def process_dsl_py(self, dsl_py: str):
        if dsl_py.startswith("```python"):
            stripped = dsl_py[10:-3]
        elif dsl_py.startswith("```"):
            stripped = dsl_py[4:-3]
        else:
            stripped = dsl_py

        append = """\
from dataset_apps_decode_gen_input_run.dsl_impl_copy_to_run import *


"""

        return append + stripped
