import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator

    def test_add(self):
        self.assertEqual(self.calc.add(self, 10, 15), 25)
        self.assertEqual(self.calc.add(self, 10, -5), 5)
        self.assertEqual(self.calc.add(self, -1, -1), -2)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(self, 10, 5), 5)
        self.assertEqual(self.calc.subtract(self, 10, -5), 15)
        self.assertEqual(self.calc.subtract(self, -1, -5), 4)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(self, 15,2), 30)

    def test_divide(self):
        self.assertEqual(self.calc.divide(self, 10, 5), 2)

# if __name__ == "__main__":
#     unittest.main()
