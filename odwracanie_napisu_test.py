import unittest
from odwracanie_napisu import Odwracamy


class TestOdwracanieNapisu(unittest.TestCase):
    def test_odwracanie_napisu(self):
        tekst = Odwracamy()
        tekst.txt = "slowo"
        self.assertAlmostEqual(tekst.odwroc(), "owols")

    def test(self):
        self.assertAlmostEqual('ok','ok')