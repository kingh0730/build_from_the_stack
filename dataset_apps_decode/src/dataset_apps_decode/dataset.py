# Stdlib imports
import sys
import json

# Third-party imports
import numpy as np
from datasets import load_from_disk, Dataset

# Project imports
from dataset_apps import APPSDataset
from ._config import CACHE_DIR


class APPSDecode:
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
        original_max_digits = sys.get_int_max_str_digits()

        sys.set_int_max_str_digits(0)
        result = self._build()
        sys.set_int_max_str_digits(original_max_digits)

        return result

    def _build(self):
        ds = APPSDataset().dataset()

        df = ds.to_pandas()

        df["solutions"] = df["solutions"].apply(
            lambda x: json.loads(x) if x else [],
        )
        df["num_answers"] = df["solutions"].apply(
            len,
        )

        df["input_output"] = df["input_output"].apply(
            lambda x: self._decode_input_output(x),
        )
        df["num_tests"] = df["input_output"].apply(
            lambda x: len(x["inputs"]),
        )

        df["mean_answer_lines"] = df["solutions"].apply(
            lambda x: np.mean([len(soln.split("\n")) for soln in x]),
        )
        df["std_answer_lines"] = df["solutions"].apply(
            lambda x: np.std([len(soln.split("\n")) for soln in x]),
        )

        platforms = df["url"].str.split(".")
        platforms0 = platforms.str[0].str.split("/").str[-1]
        platforms0[platforms0.isin(["open", "www"])] = platforms[
            platforms0.isin(["open", "www"])
        ].str[1]
        df["platform"] = platforms0

        return Dataset.from_pandas(df)

    def _decode_input_output(self, input_output):
        default_input_output = {
            "inputs": [],
            "outputs": [],
        }

        json_loads = (
            json.loads(
                input_output,
            )
            if input_output
            else default_input_output
        )

        return json_loads | {
            "inputs": [json.dumps(input) for input in json_loads["inputs"]],
            "outputs": [json.dumps(output) for output in json_loads["outputs"]],
        }
