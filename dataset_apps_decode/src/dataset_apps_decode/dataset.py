# Third-party imports
from datasets import load_dataset

# Project imports
from ._config import CACHE_DIR, SPLIT


class APPSDataset:
    def __init__(self):
        self._ds = None

    def loads(self):
        self._ds = load_dataset(
            "codeparrot/apps",
            cache_dir=CACHE_DIR,
            split=SPLIT,
        )

    def dataset(self):
        if self._ds is None:
            self.loads()
        return self._ds
