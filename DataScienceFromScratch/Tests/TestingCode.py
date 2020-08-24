import unittest
from DataScienceFromScratch.Tests import Soma

class TestSoma(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(Soma.soma(10,10),20)

