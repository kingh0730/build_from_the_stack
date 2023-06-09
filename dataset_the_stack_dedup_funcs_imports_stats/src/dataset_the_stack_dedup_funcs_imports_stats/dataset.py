# Stdlib imports
from multiprocessing import Pool
from itertools import chain

# Third-party imports
import pandas as pd
from tqdm import tqdm
from datasets import load_from_disk, Dataset
from dataset_the_stack_dedup_funcs_ast_filter import TheStackDedupFuncsAstFilter

# Project imports
from ._config import CACHE_DIR, NUM_PROC
from .analyze_imports_stats import (
    get_names_not_stdlib_and_not_top_pypi,
    parse_function_uses_names,
)


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
        ds = TheStackDedupFuncsAstFilter(
            logger=self.logger,
        ).dataset()

        ds = ds.map(
            lambda d: {
                "__names_not_stdlib_and_not_top_pypi__": get_names_not_stdlib_and_not_top_pypi(
                    d["__imports_stats__"]["namespace"],
                    d["__imports_stats__"]["namespace_origin"],
                )
            },
            num_proc=NUM_PROC,
            desc="Finding names that are not stdlib and not top PyPI...",
        )

        ds = ds.map(
            lambda d: {
                "__uses_other_imports__": parse_function_uses_names(
                    d["func"], d["__names_not_stdlib_and_not_top_pypi__"]
                )
            },
            num_proc=NUM_PROC,
            desc="Finding functions that do not use names...",
        )

        return ds
