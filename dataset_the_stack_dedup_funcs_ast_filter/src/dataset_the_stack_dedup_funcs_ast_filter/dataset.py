# Third-party imports
from datasets import load_dataset
from dataset_the_stack_dedup import TheStackDedup

# Project imports
from ._config import CACHE_DIR


class TheStackDedupFuncsAstFilter:
    def __init__(self):
        self._ds = None

    def loads(self):
        try:
            ds = load_dataset(CACHE_DIR)
        except FileNotFoundError:
            ds = self.build()
            ds.save_to_disk(CACHE_DIR)
        self._ds = ds

    def dataset(self):
        if self._ds is None:
            self.loads()
        return self._ds

    def build(self):
        # the_stack_dedup = TheStackDedup().dataset()
        ds = load_dataset("squad", split="train")
        return ds
