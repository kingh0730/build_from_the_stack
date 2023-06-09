# Stdlib imports
from importlib.metadata import version


BASE_CACHE_DIR = "E:/build_from_the_stack/cache/"
_dir = __package__ + version(__package__)
CACHE_DIR = BASE_CACHE_DIR + _dir


TOP_PYPI_PACKAGES_JSON = "../data/top_pypi_packages/top-pypi-packages-30-days.json"
