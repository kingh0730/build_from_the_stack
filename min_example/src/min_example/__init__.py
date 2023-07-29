import sys
import json
import numpy as np
from datasets import Dataset


from .dataset import MinExample


def main():
    """Entry point for the application script"""
    print("Call your main application code here")

    apps = MinExample()
    return apps.dataset()
