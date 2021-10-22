import logging
from unittest import TestCase
from gendiscalpy.GenDisCalTree import GenDisCalTree

logging.basicConfig(level=logging.INFO)


class TestGenDisCalTree(TestCase):
    def test_from_csv(self):
        tree = GenDisCalTree.from_csv(csv='../test-data/distancematrix.csv')
        print(tree)

    def test_from_files(self):
        tree = GenDisCalTree.from_files('../test-data/*.fna')
        print(tree)
