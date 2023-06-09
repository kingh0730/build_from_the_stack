# Third-party imports
from datasets import load_dataset

# Project imports
from ._config import CACHE_DIR


class TheStackDedup:
    def __init__(self):
        self._ds = None

    def loads(self):
        self._ds = load_dataset(
            "bigcode/the-stack-dedup",
            data_dir="data/python",  # Only use Python
            split="train",  # This dataset has no split
            cache_dir=CACHE_DIR,
        )

    def dataset(self):
        if self._ds is None:
            self.loads()

        return self._ds
