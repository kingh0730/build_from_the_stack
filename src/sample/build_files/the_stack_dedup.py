# Third-party imports
from datasets import load_dataset

# Project imports
from ._config import THE_STACK_DEDUP_CACHE_DIR


def the_stack():
    ds = load_dataset(
        "bigcode/the-stack-dedup",
        data_dir="data/python",
        cache_dir=THE_STACK_DEDUP_CACHE_DIR,
    )

    return ds
