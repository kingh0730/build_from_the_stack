# Stdlib imports
from os import path, cpu_count
from importlib.metadata import version


BASE_CACHE_DIR = "E:/build_from_the_stack/cache/"
_dir = __package__ + version(__package__)
CACHE_DIR = BASE_CACHE_DIR + _dir


NUM_PROC = cpu_count()
