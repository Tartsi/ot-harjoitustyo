import unittest
from ui.calculator_view import CalculatorView


class TestCalculatorView(unittest.TestCase):

    def setUp(self):
        self.calculatorview = CalculatorView()
        self.calculatorview.screen.update_idletasks()

    def test_calculator_size(self):
        self.assertEqual(str(self.calculatorview.screen.winfo_height()), "600")
        self.assertEqual(str(self.calculatorview.screen.winfo_width()), "400")

    def test_calculator_title(self):
        self.assertEqual(self.calculatorview.screen.title(), "Calculator")

    def test_areas_mapped(self):
        self.assertEqual(self.calculatorview.display_area.winfo_exists(), 1)
        self.assertEqual(self.calculatorview.button_area.winfo_exists(), 1)

    def test_labels_exist(self):
        self.assertEqual(self.calculatorview.equation_label.winfo_exists(), 1)
        self.assertEqual(self.calculatorview.answer_label.winfo_exists(), 1)

    def test_labels_update_correctly_numbers(self):
        self.calculatorview.press_numeric_button(".")
        self.calculatorview.press_numeric_button(1)
        self.calculatorview.press_numeric_button(2)
        self.calculatorview.press_numeric_button(3)
        self.calculatorview.press_numeric_button(4)
        self.calculatorview.press_numeric_button(5)
        self.calculatorview.press_numeric_button(6)
        self.calculatorview.press_numeric_button(7)
        self.calculatorview.press_numeric_button(8)
        self.calculatorview.press_numeric_button(9)
        self.assertEqual(self.calculatorview.answer_to_equation, ".123456789")

    def test_labels_update_correctly_operators(self):
        self.calculatorview.press_numeric_button(1)
        self.calculatorview.press_operator_button("+")
        self.assertEqual(self.calculatorview.equation, "1+")
        self.calculatorview.clear_calculator()
        self.calculatorview.press_numeric_button(2)
        self.calculatorview.press_operator_button("-")
        self.assertEqual(self.calculatorview.equation, "2-")
        self.calculatorview.clear_calculator()
        self.calculatorview.press_numeric_button(3)
        self.calculatorview.press_operator_button("*")
        self.assertEqual(self.calculatorview.equation, "3*")
        self.calculatorview.clear_calculator()
        self.calculatorview.press_numeric_button(4)
        self.calculatorview.press_operator_button("/")
        self.assertEqual(self.calculatorview.equation, "4/")

    def test_calculator_clearing(self):
        self.calculatorview.press_numeric_button(5)
        self.calculatorview.clear_calculator()
        self.assertEqual(self.calculatorview.answer_to_equation, "")

    def test_calculator_equals_button(self):
        self.calculatorview.press_numeric_button(1)
        self.calculatorview.use_operator_buttons("+")
        self.calculatorview.press_numeric_button(2)
        self.calculatorview.evaluate_equation()
        self.assertEqual(self.calculatorview.answer_to_equation, "3")

    def test_negative_answer_to_equation(self):
        self.calculatorview.press_numeric_button(1)
        self.calculatorview.use_operator_buttons("-")
        self.calculatorview.press_numeric_button(2)
        self.calculatorview.evaluate_equation()
        self.assertEqual(self.calculatorview.answer_to_equation, "-1")

    def test_first_number_negative(self):
        self.calculatorview.press_numeric_button(-1)
        self.calculatorview.use_operator_buttons("+")
        self.calculatorview.press_numeric_button(2)
        self.calculatorview.evaluate_equation()
        self.assertEqual(self.calculatorview.answer_to_equation, "1")

    def test_zero_div_error(self):
        self.calculatorview.press_numeric_button(1)
        self.calculatorview.use_operator_buttons("/")
        self.calculatorview.press_numeric_button(0)
        self.calculatorview.evaluate_equation()
        self.assertEqual(self.calculatorview.answer_to_equation, "/0 Error")

    def test_incorrect_operator(self):
        self.calculatorview.press_numeric_button(3)
        self.calculatorview.use_operator_buttons("*")
        self.calculatorview.use_operator_buttons("*")
        self.calculatorview.use_operator_buttons("*")
        self.calculatorview.press_numeric_button(2)
        self.calculatorview.evaluate_equation()
        self.assertEqual(self.calculatorview.answer_to_equation, "Error")
