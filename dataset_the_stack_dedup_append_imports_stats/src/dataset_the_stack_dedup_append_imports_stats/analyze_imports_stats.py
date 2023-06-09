# Stdlib imports
import ast
from typing import Tuple


def take_before_dot(s: str) -> str:
    return s.split(".")[0]


def match_abs_and_rel(
    content: str,
) -> Tuple[list[str], list[str], list[str], list[str]]:
    try:
        tree = ast.parse(content)
    except Exception:
        return [], [], [], []

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

    return matches_abs, matches_rel, namespace, namespace_origin
