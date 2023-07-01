# Stdlib imports
import json

# Third-party imports
from datasets import load_from_disk

# Project imports
from ._config import CACHE_DIR, NUM_PROC
from .python_cmd_runner import python_cmd
from dataset_apps_decode import APPSDecode


class APPSDecodeRun:
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
        apps_decode = APPSDecode(logger=self.logger).dataset()

        only_codeforces = apps_decode.filter(
            lambda x: x["platform"] == "codeforces" and x["problem_id"] < 10,
            num_proc=NUM_PROC,
        )

        only_codeforces = only_codeforces.map(
            lambda x: {
                "inputs_str": [
                    json.loads(input) for input in x["input_output"]["inputs"]
                ],
                "outputs_str": [
                    json.loads(output) for output in x["input_output"]["outputs"]
                ],
            },
            num_proc=NUM_PROC,
        )

        only_codeforces = only_codeforces.map(
            lambda x: {
                "answers": [
                    [
                        python_cmd(
                            solution,
                            input,
                        )
                        for solution in x["solutions"]
                    ]
                    for input in x["inputs_str"]
                ],
            },
            num_proc=NUM_PROC,
        )

        only_codeforces = only_codeforces.map(
            lambda x: {
                "answers_eq_outputs": [
                    [answer == output for answer in x["answers"][i]]
                    for i, output in enumerate(x["outputs_str"])
                ],
            },
            num_proc=NUM_PROC,
        )

        only_codeforces = only_codeforces.map(
            lambda x: {
                "answers_agree": [
                    len(
                        set(answers),
                    )
                    == 1
                    for answers in x["answers"]
                ],
            },
            num_proc=NUM_PROC,
        )

        return only_codeforces
