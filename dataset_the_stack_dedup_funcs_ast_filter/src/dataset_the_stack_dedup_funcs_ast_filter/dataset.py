# Third-party imports
from dataset_the_stack_dedup import TheStackDedup

# Project imports
from ._config import CACHE_DIR


class TheStackDedupFuncsAstFilter:
    def __init__(self):
        self._the_stack_dedup = TheStackDedup()
        self._ds = None

    def loads(self, streaming=True):
        self._ds = self._the_stack_dedup.dataset()

    def dataset(self):
        if self._ds is None:
            self.loads()
        return self._ds
