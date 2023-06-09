# Stdlib imports
import logging
import shutil

# Project imports
from ._config import CACHE_DIR
from .dataset import TheStackDedupFuncsImportsStats


def main():
    """Entry point for the application script"""
    print("Call your main application code here")

    logging.basicConfig(
        level=logging.INFO,
    )

    logger = logging.getLogger(__name__)

    the_stack_dedup_funcs = TheStackDedupFuncsImportsStats(
        logger=logger,
    )

    global ds
    ds = the_stack_dedup_funcs.dataset()


def clear_cache():
    shutil.rmtree(CACHE_DIR)
