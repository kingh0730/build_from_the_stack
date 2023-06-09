from .top_pypi import top_pypi_packages


def test():
    assert len(top_pypi_packages) == 5000


if __name__ == "__main__":
    test()
