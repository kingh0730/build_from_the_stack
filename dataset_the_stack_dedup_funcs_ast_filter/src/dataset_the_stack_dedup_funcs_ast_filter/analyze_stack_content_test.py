from .analyze_stack_content import AnalyzeContent


def test1():
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
    result = AnalyzeContent.analyze(content)
    print(result)

    assert result == []


def test2():
    content = """
from multiprocessing import Pool
def func1(i : int):
    pass

def func2(i : int):
    \"\"\"
    This is a docstring.
    \"\"\"
    pass

def func3(i : int):
    raise NotImplementedError

def func4(i : int):
    raise Exception

class A:
    def __init__(self):
        pass

    @staticmethod
    def compute():
        return 2

    def run(self):
        return 1

def hello_world():
    print("Hello world")

"""
    result = AnalyzeContent.analyze(content)
    print(result)

    assert len(result) == 3


if __name__ == "__main__":
    test1()
    test2()
