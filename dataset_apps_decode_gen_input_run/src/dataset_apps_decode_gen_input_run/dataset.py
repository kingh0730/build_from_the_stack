# Third-party imports
from datasets import load_from_disk

# Project imports
from ._config import CACHE_DIR
from dataset_apps_decode_gen_input import APPSDecodeGenInput

# TODO Perhaps not wildcard
from dataset_apps_decode_gen_input_run.dsl_impl_copy_to_run import *


DSL_GEN_BASE_DIR = "./data/inputs_gen/dsl/gen/"


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
                for _ in range(10)
            ]
            new_inputs_all_gpt_4[row["problem_id"]] = new_inputs

            new_inputs = [
                self.generate_one_input_try_hard(generate_input_gpt_3, file_name)
                for _ in range(10)
            ]
            new_inputs_all_gpt_3[row["problem_id"]] = new_inputs

        ds = ds.map(
            lambda row: {
                "new_inputs: gpt-4": new_inputs_all_gpt_4[row["problem_id"]],
                "new_inputs: gpt-3.5-turbo": new_inputs_all_gpt_3[row["problem_id"]],
            },
        )

        return ds

    def generate_one_input_try_hard(self, generate_input: str, file_name: str):
        for _ in range(100):
            once_or_none = self.generate_input_once_or_none(
                generate_input,
                file_name,
            )

            if once_or_none is not None:
                return once_or_none

    def generate_input_once_or_none(self, generate_input: str, file_name: str):
        try:
            loc = {}
            exec(generate_input, None, loc)

            new_input = loc[GENERATE_INPUT_FUNC_NAME]()
            return new_input

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
