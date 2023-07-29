import sys
import logging
import numpy as np
from datasets import Dataset


from .dataset import APPSDecodeGenInputRun


def main():
    """Entry point for the application script"""
    print("Call your main application code here")

    logging.basicConfig(
        level=logging.INFO,
    )

    logger = logging.getLogger(__name__)

    apps = APPSDecodeGenInputRun(
        logger=logger,
    )

    return apps.dataset()
