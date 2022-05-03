import unittest
from ui.calculator_view import CalculatorView


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = CalculatorView()
        self.calculator.screen.update_idletasks()

    def test_calculator_size(self):
        self.assertEqual(str(self.calculator.screen.winfo_height()), "600")
        self.assertEqual(str(self.calculator.screen.winfo_width()), "400")

    def test_calculator_title(self):
        self.assertEqual(self.calculator.screen.title(), "Calculator")

    def test_areas_mapped(self):
        self.assertEqual(self.calculator.display_area.winfo_exists(), 1)
        self.assertEqual(self.calculator.button_area.winfo_exists(), 1)

    def test_labels_exist(self):
        self.assertEqual(self.calculator.equation_label.winfo_exists(), 1)
        self.assertEqual(self.calculator.answer_label.winfo_exists(), 1)

    def test_labels_update_correctly_numbers(self):
        self.calculator.use_numeric_buttons(".")
        self.calculator.use_numeric_buttons(1)
        self.calculator.use_numeric_buttons(2)
        self.calculator.use_numeric_buttons(3)
        self.calculator.use_numeric_buttons(4)
        self.calculator.use_numeric_buttons(5)
        self.calculator.use_numeric_buttons(6)
        self.calculator.use_numeric_buttons(7)
        self.calculator.use_numeric_buttons(8)
        self.calculator.use_numeric_buttons(9)
        self.assertEqual(self.calculator.answer_to_equation, ".123456789")

    def test_labels_update_correctly_operators(self):
        self.calculator.use_numeric_buttons(1)
        self.calculator.use_operator_buttons("+")
        self.assertEqual(self.calculator.equation, "1+")
        self.calculator.clear_calculator()
        self.calculator.use_numeric_buttons(2)
        self.calculator.use_operator_buttons("-")
        self.assertEqual(self.calculator.equation, "2-")
        self.calculator.clear_calculator()
        self.calculator.use_numeric_buttons(3)
        self.calculator.use_operator_buttons("*")
        self.assertEqual(self.calculator.equation, "3*")
        self.calculator.clear_calculator()
        self.calculator.use_numeric_buttons(4)
        self.calculator.use_operator_buttons("/")
        self.assertEqual(self.calculator.equation, "4/")

    def test_calculator_clearing(self):
        self.calculator.use_numeric_buttons(5)
        self.calculator.clear_calculator()
        self.assertEqual(self.calculator.answer_to_equation, "")

    def test_calculator_equals_button(self):
        self.calculator.use_numeric_buttons(1)
        self.calculator.use_operator_buttons("+")
        self.calculator.use_numeric_buttons(2)
        self.calculator.evaluate_equation()
        self.assertEqual(self.calculator.answer_to_equation, "3")

    def test_negative_answer_to_equation(self):
        self.calculator.use_numeric_buttons(1)
        self.calculator.use_operator_buttons("-")
        self.calculator.use_numeric_buttons(2)
        self.calculator.evaluate_equation()
        self.assertEqual(self.calculator.answer_to_equation, "-1")

    def test_first_number_negative(self):
        self.calculator.use_numeric_buttons(-1)
        self.calculator.use_operator_buttons("+")
        self.calculator.use_numeric_buttons(2)
        self.calculator.evaluate_equation()
        self.assertEqual(self.calculator.answer_to_equation, "1")

    def test_zero_div_error(self):
        self.calculator.use_numeric_buttons(1)
        self.calculator.use_operator_buttons("/")
        self.calculator.use_numeric_buttons(0)
        self.calculator.evaluate_equation()
        self.assertEqual(self.calculator.answer_to_equation, "/0 Error")

    def test_incorrect_operator(self):
        self.calculator.use_numeric_buttons(3)
        self.calculator.use_operator_buttons("*")
        self.calculator.use_operator_buttons("*")
        self.calculator.use_operator_buttons("*")
        self.calculator.use_numeric_buttons(2)
        self.calculator.evaluate_equation()
        self.assertEqual(self.calculator.answer_to_equation, "Error")
