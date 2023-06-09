from .dataset import TheStackDedupDataset


def main():
    """Entry point for the application script"""
    print("Call your main application code here")

    the_stack_dedup = TheStackDedupDataset()
    ds = the_stack_dedup.dataset()
