# Stdlib imports
from os import path, cpu_count
from importlib.metadata import version


_dir = __package__ + version(__package__)
BASE_CACHE_DIR = "E:/build_from_the_stack/cache/"
CACHE_DIR = BASE_CACHE_DIR + _dir


TOP_PYPI_PACKAGES_JSON = f"{path.dirname(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))}/data/top_pypi_packages/top-pypi-packages-30-days.json"


NUM_PROC = cpu_count()
