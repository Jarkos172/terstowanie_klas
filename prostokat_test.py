import unittest
from prostokat import Prostokat

class TestProstokat(unittest. TestCase):
    def test_prostokat(self):
        
        Pros1 = Prostokat(2,2)
        #Pros1.szerokosc = 2
        #Pros1.wysokosc = 2
        self.assertAlmostEqual(Pros1.pobierz_obwod(),8)
        self.assertAlmostEqual(Pros1.pobierz_pole(),4)
  
     
