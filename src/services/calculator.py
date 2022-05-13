
# Tämä luokka vielä vaiheessa, tarkoitus vastata laskimen sovelluslogiikasta


import math


class Calculator:

    def __init__(self):
        self.equation = ""
        self.answer = ""

    def use_numeric_buttons(self, number):
        """Yksinkertainen funktio joka palauttaa saadun numeron

        Args:
            number (int): Laskinnäkymästä saatu numero

        Returns:
            str: Muokattu tekstikenttä, joka palautetaan laskinnäkymään
        """
        self.answer = str(number)
        return self.answer

    def use_operator_buttons(self, operator):
        """Yksinkertainen funktio joka palauttaa saadun operaattori

        Args:
            operator (str): Laskinnäkymästä saatu operaattori

        Returns:
            str: Operaattori, joka palautetaan laskinnäkymään
        """
        self.answer = operator
        return self.answer

    def squaring_function(self, current_number):

        if len(current_number) != 0:
            try:
                calculation = math.pow(float(current_number), 2)
                return calculation
            except OverflowError:
                return "Overflow, please reset"
        else:
            return "Enter number first!"

    def square_root_button_function(self):  # Lasku
        self.equation = "\u221a"+self.answer_to_equation+"="
        self.update_equation_label()
        self.answer_to_equation = str(eval(f"{self.answer_to_equation}**0.5"))
        self.update_answer_label()
        self.equation = ""

    def clear_calculator(self):  # Lasku
        self.equation = ""
        self.answer_to_equation = ""
        self.update_equation_label()
        self.update_answer_label()

    def evaluate_equation(self):  # Lasku
        self.equation += self.answer_to_equation
        self.update_equation_label()

        try:
            self.answer_to_equation = str(eval(self.equation))
        except ZeroDivisionError as e:
            self.answer_to_equation = "/0 Error"
        except Exception as e:
            self.answer_to_equation = "Error"

        self.update_answer_label()
        self.equation += "="
        self.update_equation_label()
        self.equation = ""
