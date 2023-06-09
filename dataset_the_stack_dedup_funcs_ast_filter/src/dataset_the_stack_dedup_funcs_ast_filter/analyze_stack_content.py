import ast
import astpretty


FUNCTION_MAX_LINES = 50
FUNCTION_MIN_LINES = 2


FUNCTION_REMOVAL_PREDICATES = [
    lambda node: isinstance(getattr(node, "parent", None), ast.ClassDef),
    lambda node: len(node.decorator_list) > 0,
    lambda node: len(ast.unparse(node).split("\n")) > FUNCTION_MAX_LINES,
    lambda node: len(ast.unparse(node).split("\n")) < FUNCTION_MIN_LINES,
    lambda node: len(node.body) == 0,
    lambda node: len(node.body) == 1 and isinstance(node.body[0], ast.Pass),
    lambda node: function_only_raises_not_implemented_error(node),
]


def function_only_raises_not_implemented_error(func_def: ast.FunctionDef) -> bool:
    """
    Check if a function only raises NotImplementedError
    """
    if len(func_def.body) != 1:
        return False
    if not isinstance(func_def.body[0], ast.Raise):
        return False
    if not isinstance(func_def.body[0].exc, ast.Name):
        return False
    if func_def.body[0].exc.id != "NotImplementedError":
        return False
    return True


class AnalyzeContent:
    """
    Filter based on syntactic analysis
    """

    @staticmethod
    def _extract_functions(tree: ast.AST) -> list[ast.FunctionDef]:
        func_defs = []
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                func_defs.append(node)
        return func_defs

    @staticmethod
    def filter_functions(func_defs: list[ast.FunctionDef]) -> list[ast.FunctionDef]:
        """
        Remove functions that are members of some class
        Remove functions having decorators
        Remove very long and very short functions
        """
        final_func_defs = []
        for func_def in func_defs:
            if any(predicate(func_def) for predicate in FUNCTION_REMOVAL_PREDICATES):
                continue
            final_func_defs.append(func_def)

        return final_func_defs

    @staticmethod
    def _analyze(tree: ast.AST) -> list[str]:
        func_defs = AnalyzeContent._extract_functions(tree)
        filtered = AnalyzeContent.filter_functions(func_defs)
        unparsed = [ast.unparse(func_def) for func_def in filtered]
        unparsed = list(set(unparsed))
        return unparsed

    @staticmethod
    def build_ast(content: str) -> ast.AST:
        tree = ast.parse(content)
        # add parent attribute to each node
        for node in ast.walk(tree):
            for child in ast.iter_child_nodes(node):
                child.parent = node
        # astpretty.pprint(tree)
        return tree

    @staticmethod
    def analyze(content: str) -> list[str]:
        try:
            tree = AnalyzeContent.build_ast(content)
            return AnalyzeContent._analyze(tree)
        except Exception:
            return []


if __name__ == "__main__":
    content = """
from multiprocessing import Pool
def func(i : int):
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
    print(AnalyzeContent.analyze(content))
