
# Tämä luokka vielä vaiheessa, tarkoitus vastata laskimen sovelluslogiikasta

# from ui.calculator_view import CalculatorView


class Calculator:

    def __init__(self):
        self.x = 0

    def use_numeric_buttons(self, number):
        """Yksinkertainen funktio joka palauttaa saadun numeron

        Args:
            number (int): Laskinnäkymästä saatu numero

        Returns:
            int: Numero joka palautetaan ilman muutoksia
        """
        return number

    def use_operator_buttons(self, operator):
        """Yksinkertainen funktio joka palauttaa saadun operaattori

        Args:
            operator (str): Laskinnäkymästä saatu operaattori

        Returns:
            str: Operaattori joka palautetaan muuttumattomana
        """
        return operator

#     def squaring_function(self):  # Lasku
#         self.equation = self.answer_to_equation+"\u00b2"+"="
#         self.update_equation_label()
#         try:
#             self.answer_to_equation = str(
#                 eval(f"{self.answer_to_equation}**2"))
#         except OverflowError as e:
#             self.answer_to_equation = "Overflow"

#         self.update_answer_label()
#         self.equation = ""

#     def square_root_button_function(self):  # Lasku
#         self.equation = "\u221a"+self.answer_to_equation+"="
#         self.update_equation_label()
#         self.answer_to_equation = str(eval(f"{self.answer_to_equation}**0.5"))
#         self.update_answer_label()
#         self.equation = ""

#     def clear_calculator(self):  # Lasku
#         self.equation = ""
#         self.answer_to_equation = ""
#         self.update_equation_label()
#         self.update_answer_label()

#     def evaluate_equation(self):  # Lasku
#         self.equation += self.answer_to_equation
#         self.update_equation_label()

#         try:
#             self.answer_to_equation = str(eval(self.equation))
#         except ZeroDivisionError as e:
#             self.answer_to_equation = "/0 Error"
#         except Exception as e:
#             self.answer_to_equation = "Error"

#         self.update_answer_label()
#         self.equation += "="
#         self.update_equation_label()
#         self.equation = ""

#     def update_equation_label(self):  # Lasku
#         self.equation_label.config(text=self.equation)

#     def update_answer_label(self):  # Lasku
#         if len(self.answer_to_equation) > 9:
#             self.answer_label.config(text=self.answer_to_equation[:11]+"...")
#         else:
#             self.answer_label.config(text=self.answer_to_equation)
