import json


TOP_PYPI_PACKAGES_JSON = "../data/top_pypi_packages/top-pypi-packages-30-days.json"

# Read JSON
with open(TOP_PYPI_PACKAGES_JSON, "r") as f:
    top_pypi_packages_json = json.load(f)

top_pypi_packages = set(
    [row["project"] for row in top_pypi_packages_json["rows"]],
)
