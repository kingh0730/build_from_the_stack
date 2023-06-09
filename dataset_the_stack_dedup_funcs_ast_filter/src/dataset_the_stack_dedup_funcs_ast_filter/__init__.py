# Stdlib imports
import logging

# Project imports
from .dataset import TheStackDedupFuncsAstFilter


def main():
    """Entry point for the application script"""
    print("Call your main application code here")

    logging.basicConfig(
        level=logging.INFO,
    )

    logger = logging.getLogger(__name__)

    global ds

    the_stack_dedup = TheStackDedupFuncsAstFilter(
        logger=logger,
    )
    ds = the_stack_dedup.dataset()
