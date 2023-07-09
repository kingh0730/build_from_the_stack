# Stdlib imports
import sys
import json
from .langchain_dsl.template import dsl_chain

# Third-party imports
import numpy as np
from datasets import load_from_disk, Dataset

# Project imports
from dataset_apps_decode import APPSDecode
from ._config import CACHE_DIR


class APPSDecodeGenInput:
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
        ds = APPSDecode().dataset()

        ds.map(
            lambda x: {
                "solution: gpt-4": dsl_chain(
                    x["question"],
                    model="gpt-4",
                ),
                "solution: gpt-3.5-turbo": dsl_chain(
                    x["question"],
                    model="gpt-3.5-turbo",
                ),
            }
        )

        return ds
