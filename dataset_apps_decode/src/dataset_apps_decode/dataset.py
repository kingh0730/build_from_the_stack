# Stdlib imports
import json

# Third-party imports
import numpy as np
from datasets import load_from_disk

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
        ds = APPSDataset().dataset()

        df = ds.to_pandas()

        df["solutions"] = df["solutions"].apply(
            lambda x: json.loads(x) if x else [],
        )
        df["num_answers"] = df["solutions"].apply(
            len,
        )
        df["input_output"] = df["input_output"].apply(
            lambda x: json.loads(x) if x else {"inputs": [], "outputs": []},
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

        return ds
