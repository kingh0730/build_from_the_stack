# Stdlib imports
import ast
from sys import stdlib_module_names
from typing import Tuple

# Project imports
from .top_pypi import top_pypi_packages


def function_uses_names(func_def: ast.FunctionDef, names: list[str]) -> bool:
    """
    Function uses names?
    """

    for node in ast.walk(func_def):
        # if node is a name
        if isinstance(node, ast.Name):
            # if name matches a module name
            if node.id in names:
                return True

    return False


def parse_function_uses_names(func_def: str, names: list[str]) -> bool:
    """
    This function is used to find functions that do not use names.
    """

    tree = ast.parse(func_def)

    if not isinstance(node, ast.FunctionDef):
        raise ValueError("Expected ast.FunctionDef")

    return function_uses_names(node, names)


def get_names_not_stdlib_and_not_top_pypi(
    namespace: list[str], namespace_origin: list[str]
) -> list[str]:
    return [
        name
        for name, name_origin in zip(namespace, namespace_origin)
        if name_origin not in stdlib_module_names
        and name_origin not in top_pypi_packages
    ]
