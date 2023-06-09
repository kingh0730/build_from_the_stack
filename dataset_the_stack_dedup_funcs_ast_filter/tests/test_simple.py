# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

from dataset_the_stack_dedup_funcs_ast_filter import main


class TestSimple(unittest.TestCase):
    def test_main_is_a_func(self):
        self.assertTrue(callable(main))


if __name__ == "__main__":
    unittest.main()
