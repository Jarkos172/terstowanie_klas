import unittest
from silnia import Silnia


class TestSilnia(unittest.TestCase):
    def test_silnia(self):
        liczba = Silnia()
        
        self.assertAlmostEqual(liczba.silnia_rek(2),2) 