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


def content_to_functions_that_do_not_use_names(
    content: str, names: list[str]
) -> list[str]:
    """
    This function is used to find functions that do not use names.
    """

    try:
        tree = ast.parse(content)
    except Exception:
        return []

    functions = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            if not function_uses_names(node, names):
                functions.append(node.name)

    return functions


def get_names_not_stdlib_and_not_top_pypi(
    namespace: list[str], namespace_origin: list[str]
) -> list[str]:
    return [
        name
        for name, name_origin in zip(namespace, namespace_origin)
        if name_origin not in stdlib_module_names
        and name_origin not in top_pypi_packages
    ]
