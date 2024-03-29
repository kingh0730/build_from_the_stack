# Stdlib imports
from importlib.metadata import version


BASE_CACHE_DIR = "E:/build_from_the_stack/cache/"
_dir = __package__ + version(__package__)
CACHE_DIR = BASE_CACHE_DIR + _dir


# If included, the dataset will be too large
EXCLUDE_KEYS = [
    "content",
]
