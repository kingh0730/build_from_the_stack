from .dataset import TheStackDedupFuncsAstFilter


def main():
    """Entry point for the application script"""
    print("Call your main application code here")

    the_stack_dedup = TheStackDedupFuncsAstFilter()
    ds = the_stack_dedup.dataset()
