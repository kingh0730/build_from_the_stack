from .dataset import TheStackDedup


def main():
    """Entry point for the application script"""
    print("Call your main application code here")

    the_stack_dedup = TheStackDedup()
    ds = the_stack_dedup.dataset()
