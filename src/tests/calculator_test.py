import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()
        self.calculator.screen.update_idletasks()

    def test_calculator_size(self):
        self.assertEqual(str(self.calculator.screen.winfo_height()), "600")
        self.assertEqual(str(self.calculator.screen.winfo_width()), "400")

    def test_calculator_title(self):
        self.assertEqual(self.calculator.screen.title(), "Calculator")
        
    def test_areas_mapped(self):
        self.assertEqual(self.calculator.display_area.winfo_exists(), 1)
        self.assertEqual(self.calculator.button_area.winfo_exists(), 1)