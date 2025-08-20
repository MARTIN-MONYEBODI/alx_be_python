import unittest
from simple_calculator import SimpleCalculator

class TestSimplecalculator(unittest.TestCase):
    
    def setUp(self):
        self.calc = SimpleCalculator()
    
    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(2, 3), -1)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(-1, -1), 1)
        

    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 1), 6)
        self.assertEqual(self.calc.divide(6, 2), 3)
        self.assertEqual(self.calc.divide(6, -2), -3)

    def test_divide_by_zero(self):
        self.assertIsNone(self.calc.divide(6, 0))
        
if __name__ == "__main__":
  unittest.main()
