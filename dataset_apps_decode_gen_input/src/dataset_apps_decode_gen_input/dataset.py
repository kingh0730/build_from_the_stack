# Stdlib imports
import sys
import json

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
        original_max_digits = sys.get_int_max_str_digits()

        sys.set_int_max_str_digits(0)
        result = self._build()
        sys.set_int_max_str_digits(original_max_digits)

        return result

    def _build(self):
        ds = APPSDecode().dataset()

        return ds
