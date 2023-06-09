# Stdlib imports
import ast
from sys import stdlib_module_names
from typing import Tuple

# Project imports
from .top_pypi import top_pypi_packages


def take_before_dot(s: str) -> str:
    return s.split(".")[0]


def find_imports_stats(
    content: str,
) -> Tuple[list[str], list[str], list[str], list[str]]:
    try:
        tree = ast.parse(content)
    except Exception:
        tree = ast.parse("")

    matches_abs = []
    matches_rel = []
    namespace = []
    namespace_origin = []

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                module_name = take_before_dot(alias.name)
                matches_abs.append(module_name)

                # namespace
                name = module_name if alias.asname is None else alias.asname
                namespace.append(name)
                namespace_origin.append(module_name)

        elif isinstance(node, ast.ImportFrom):
            module_name = take_before_dot(node.module) if node.module else ""
            matches_rel.append(module_name)

            # namespace
            for alias in node.names:
                name = (
                    take_before_dot(alias.name)
                    if alias.asname is None
                    else alias.asname
                )
                namespace.append(name)
                namespace_origin.append(module_name)

    return {
        "ast.Import": matches_abs,
        "ast.ImportFrom": matches_rel,
        "namespace": namespace,
        "namespace_origin": namespace_origin,
    }


def has_stdlib_imports(matches_abs, matches_rel) -> bool:
    for m in matches_abs:
        if m in stdlib_module_names:
            return True

    for m in matches_rel:
        if m in stdlib_module_names:
            return True

    return False


def has_top_pypi_imports(matches_abs, matches_rel) -> bool:
    for m in matches_abs:
        if m in top_pypi_packages:
            return True

    for m in matches_rel:
        if m in top_pypi_packages:
            return True

    return False


def has_other_imports(matches_abs, matches_rel) -> bool:
    for m in matches_abs:
        if m not in stdlib_module_names and m not in top_pypi_packages:
            return True

    for m in matches_rel:
        if m not in stdlib_module_names and m not in top_pypi_packages:
            return True

    return False


# -----------------------------------------------------------------------------


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


# -----------------------------------------------------------------------------
