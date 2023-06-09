# Stdlib imports
from multiprocessing import Pool
from itertools import chain

# Third-party imports
import pandas as pd
from tqdm import tqdm
from datasets import load_from_disk, Dataset
from dataset_the_stack_dedup import TheStackDedup

# Project imports
from ._config import CACHE_DIR
from .analyze_stack_content import AnalyzeContent


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

        with Pool() as p:
            funcs = list(
                chain.from_iterable(
                    tqdm(
                        p.imap(self._file_to_funcs, the_stack_dedup_ds),
                        total=len(the_stack_dedup_ds),
                    )
                )
            )

        return Dataset.from_pandas(pd.DataFrame(funcs))

    @staticmethod
    def _file_to_funcs(file_entry):
        file_content = file_entry["content"]
        return [
            {"func": func}
            | {k: v for k, v in file_entry.items() if k not in EXCLUDE_KEYS}
            for func in AnalyzeContent.analyze(file_content)
        ]
