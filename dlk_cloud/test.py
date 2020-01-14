import unittest


class TestImportFromModule(unittest.TestCase):

    # __init__.py import
    def test_booger(self):
        assert Booger().add(1, 2, 3, 4) == 10

    def test_boogeyman(self, ):
        assert Boogeyman().echo(1) == 1
