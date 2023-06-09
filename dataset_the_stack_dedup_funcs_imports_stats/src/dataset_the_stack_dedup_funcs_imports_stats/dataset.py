# Stdlib imports
from multiprocessing import Pool
from itertools import chain

# Third-party imports
import pandas as pd
from tqdm import tqdm
from datasets import load_from_disk, Dataset
from dataset_the_stack_dedup_funcs_ast_filter import TheStackDedupFuncsAstFilter

# Project imports
from ._config import CACHE_DIR

# from .analyze_stack_content import AnalyzeContent


class TheStackDedupFuncsImportsStats:
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
        funcs = TheStackDedupFuncsAstFilter(
            logger=self.logger,
        ).dataset()
