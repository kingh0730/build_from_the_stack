# Third-party imports
from datasets import load_dataset

# Project imports
from ._config import THE_STACK_DEDUP_CACHE_DIR


class TheStackDedupDataset:
    def __init__(self):
        self._ds = None

    def loads(self, streaming=True):
        self._ds = load_dataset(
            "bigcode/the-stack-dedup",
            data_dir="data/python",
            streaming=streaming,
            cache_dir=THE_STACK_DEDUP_CACHE_DIR,
        )
        return self._ds

    def dataset(self):
        return self._ds
