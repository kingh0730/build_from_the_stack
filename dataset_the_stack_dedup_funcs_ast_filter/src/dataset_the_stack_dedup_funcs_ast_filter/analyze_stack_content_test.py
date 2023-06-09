from .analyze_stack_content import AnalyzeContent


def test():
    content = """
from multiprocessing import Pool
def func(i : int):
    pass

class A:
    def __init__(self):
        pass

    @staticmethod
    def compute():
        return 2

    def run(self):
        return 1
"""
    print(AnalyzeContent.analyze(content))


if __name__ == "__main__":
    test()
