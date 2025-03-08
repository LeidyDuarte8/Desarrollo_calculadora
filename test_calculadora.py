import unittest
from calculadora import suma, resta, multiplicacion, division

class TestCalculadora(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(5, 3), 8)
        self.assertEqual(suma(-2, 7), 5)
        self.assertEqual(suma(0, 0), 0)

    def test_resta(self):
        self.assertEqual(resta(10, 4), 6)
        self.assertEqual(resta(5, 8), -3)
        self.assertEqual(resta(0, 0), 0)

    def test_multiplicacion(self):
        self.assertEqual(multiplicacion(3, 3), 9)
        self.assertEqual(multiplicacion(-4, 2), -8)
        self.assertEqual(multiplicacion(0, 10), 0)

    def test_division(self):
        self.assertEqual(division(10, 2), 5)
        self.assertEqual(division(9, 3), 3)
        self.assertEqual(division(7, 2), 3)  # División entera
        
