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
        """Funktio joka neliöi saamansa luvun

        Args:
            current_number (str): Laskinnäkymän vastauskentästä saatu luku

        Returns:
            float/str: Neliöidyn luvun float-muodossa/virheviestin stringinä
        """
        if len(current_number) != 0:
            try:
                calculation = math.pow(float(current_number), 2)
                return calculation
            except OverflowError:
                return "Overflow, please reset"
        else:
            return "Enter number first!"

    def square_root_function(self, current_number):
        """Funktio joka laskee neliöjuureen saamastaan luvusta

        Args:
            current_number (str): Laskinnäkymän vastauskentästä saatu luku

        Returns:
            float/str: Neliöjuuren floatina tai virheviestin stringinä
        """
        if len(current_number) != 0:
            try:
                return math.sqrt(float(current_number))
            except Exception:
                return "Error occurred, please reset"
        else:
            return "Enter number first!"

    def clear(self):
        """Tyhjentää tekstikentän

        Returns:
            str: Palauttaa tyhjän merkkijono joka sijoitetaan laskinnäkymän tekstikenttiin
        """
        return ""

    def evaluate(self, equation, answer):

        self.equation = equation
        self.answer = answer

        self.equation += self.answer

        try:
            self.answer = str(eval(self.equation))
            return self.answer
        except ZeroDivisionError:
            return "/0 Error, please reset"
        except Exception:
            return "Error, please reset"

    def show_history(self):
        pass
