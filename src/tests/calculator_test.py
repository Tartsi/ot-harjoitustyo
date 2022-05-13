import unittest
from services.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_use_numeric_buttons(self):
        self.assertEqual(self.calculator.use_numeric_buttons(0), "0")
        self.assertEqual(self.calculator.use_numeric_buttons(1), "1")
        self.assertEqual(self.calculator.use_numeric_buttons(2), "2")
        self.assertEqual(self.calculator.use_numeric_buttons(3), "3")
        self.assertEqual(self.calculator.use_numeric_buttons(4), "4")
        self.assertEqual(self.calculator.use_numeric_buttons(5), "5")
        self.assertEqual(self.calculator.use_numeric_buttons(6), "6")
        self.assertEqual(self.calculator.use_numeric_buttons(7), "7")
        self.assertEqual(self.calculator.use_numeric_buttons(8), "8")
        self.assertEqual(self.calculator.use_numeric_buttons(9), "9")
        self.assertEqual(self.calculator.use_numeric_buttons("."), ".")

    def test_use_operator_buttons(self):
        self.assertEqual(self.calculator.use_operator_buttons("+"), "+")
        self.assertEqual(self.calculator.use_operator_buttons("-"), "-")
        self.assertEqual(self.calculator.use_operator_buttons("*"), "*")
        self.assertEqual(self.calculator.use_operator_buttons("/"), "/")
