# Third-party imports
from datasets import load_from_disk

# Project imports
from ._config import CACHE_DIR
from dataset_apps_decode import APPSDecode


class APPSDecodeRun:
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
        apps_decode = APPSDecode(logger=self.logger).dataset()

        return apps_decode
