import unittest
from services.calculator_service import CalculatorService


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator_service = CalculatorService()

    def test_use_numeric_buttons(self):
        self.assertEqual(self.calculator_service.use_numeric_buttons(0), "0")
        self.assertEqual(self.calculator_service.use_numeric_buttons(1), "1")
        self.assertEqual(self.calculator_service.use_numeric_buttons(2), "2")
        self.assertEqual(self.calculator_service.use_numeric_buttons(3), "3")
        self.assertEqual(self.calculator_service.use_numeric_buttons(4), "4")
        self.assertEqual(self.calculator_service.use_numeric_buttons(5), "5")
        self.assertEqual(self.calculator_service.use_numeric_buttons(6), "6")
        self.assertEqual(self.calculator_service.use_numeric_buttons(7), "7")
        self.assertEqual(self.calculator_service.use_numeric_buttons(8), "8")
        self.assertEqual(self.calculator_service.use_numeric_buttons(9), "9")
        self.assertEqual(self.calculator_service.use_numeric_buttons("."), ".")

    def test_use_operator_buttons(self):
        self.assertEqual(
            self.calculator_service.use_operator_buttons("+"), "+")
        self.assertEqual(
            self.calculator_service.use_operator_buttons("-"), "-")
        self.assertEqual(
            self.calculator_service.use_operator_buttons("*"), "*")
        self.assertEqual(
            self.calculator_service.use_operator_buttons("/"), "/")

    def test_squaring_function(self):
        self.assertEqual(self.calculator_service.squaring_function(
            ""), "Enter number first!")
        self.assertEqual(self.calculator_service.squaring_function("8"), 64.0)
        self.assertEqual(self.calculator_service.squaring_function(
            str(99**99)), "Overflow, please reset")

    def test_square_root_function(self):
        self.assertEqual(
            self.calculator_service.square_root_function("9"), 3.0)
        self.assertEqual(self.calculator_service.square_root_function(
            ""), "Enter number first!")
        self.assertEqual(self.calculator_service.square_root_function(
            "Error"), "Error, please reset")

    def test_clear(self):
        self.assertEqual(self.calculator_service.clear(), "")

    def test_evaluate(self):
        self.assertEqual(self.calculator_service.evaluate("1+", "2"), "3")
        self.assertEqual(self.calculator_service.evaluate(
            "9/", "0"), "/0 Error, please reset")
        self.assertEqual(self.calculator_service.evaluate(
            "/93++-", "3"), "Error, please reset")
        self.assertEqual(self.calculator_service.evaluate(
            "99**", "99"), "Too many numbers!")
