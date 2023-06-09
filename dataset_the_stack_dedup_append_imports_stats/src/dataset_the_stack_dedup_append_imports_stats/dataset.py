# Stdlib imports
from multiprocessing import Pool
from itertools import chain

# Third-party imports
import pandas as pd
from tqdm import tqdm
from datasets import load_from_disk, Dataset
from dataset_the_stack_dedup import TheStackDedup

# Project imports
from ._config import CACHE_DIR, NUM_PROC
from .analyze_imports_stats import match_abs_and_rel


class TheStackDedupAppendImportsStats:
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
        the_stack_dedup_ds = TheStackDedup().dataset()

        matches = the_stack_dedup_ds.map(
            lambda d: {
                "__matches_abs_and_rel__": match_abs_and_rel(d["content"]),
            },
            num_proc=NUM_PROC,
        )

        return matches
