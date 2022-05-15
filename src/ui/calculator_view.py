from tkinter import Tk, Frame, Label, Button, NSEW, E
from services.calculator import Calculator


class CalculatorView:

    """Laskinnäkymästä vastaava luokka"""

    color_light_gray = "#D3D3D3"
    numeric_button_font = ("Helvetica", 24, "bold")
    operator_button_font = ("Arial", 20)

    def __init__(self):
        """Konstruktori, alustaa laskinnäkymän

        Konstruktori ei ota argumentteja vaan toimii "itsenäisesti"

        Konstruktori kutsuu metodeita, jotka muodostavat laskinnäkymän
        """
        self.screen = Tk()
        self.screen.geometry("400x600")
        self.screen.title("Calculator")

        self.equation = ""
        self.answer_to_equation = ""

        self.display_area, self.button_area = self.create_areas()
        self.equation_label, self.answer_label = self.create_labels()

        self.create_and_place_numeric_buttons()
        self.create_and_place_operator_buttons()
        self.create_and_place_misc_buttons()
        self.fill_button_area()

        self.calculator = Calculator()

        # "Resetöidään" laskinhistoria jokaiselle uudelle laskinnäkymälle

        open("calculationhistory.txt", "w").close()

    def create_areas(self):
        """Funktio luo laskimen "vastausalueen" ja nappialueen

        Returns:
            Frame: Palauttaa "vastausalueen" ja nappialueen
        """
        display_frame = Frame(self.screen, height=200,
                              bg=self.color_light_gray)
        display_frame.pack(expand=True, fill="both")
        button_frame = Frame(self.screen)
        button_frame.pack(expand=True, fill="both")
        return display_frame, button_frame

    def create_labels(self):
        """Funktio sijoittaa laskimen vastausalueelle yhtälön ja vastauksen

        Returns:
            Label: Palauttaa laskimen vastausalueelle yhtälön ja vastauksen kentät
        """
        equation_label = Label(self.display_area, text=self.equation,
                               bg=self.color_light_gray, anchor=E,
                               font=("Arial", 16), padx=20)
        answer_label = Label(self.display_area, text=self.answer_to_equation,
                             bg=self.color_light_gray, anchor=E,
                             font=("Arial", 40, "bold"), padx=20)
        equation_label.pack(expand=True, fill="both")
        answer_label.pack(expand=True, fill="both")
        return equation_label, answer_label

    def fill_button_area(self):
        """Funktio muotoilee nappialuetta niin, että laskimen napit täyttävät sen kokonaan
        """
        self.button_area.rowconfigure(0, weight=1)

        for i in range(1, 5):
            self.button_area.rowconfigure(i, weight=1)
            self.button_area.columnconfigure(i, weight=1)

    def press_numeric_button(self, number):
        """Funktio saa numeron parametriksi ja hyödyntäen calculator-luokan
        palvelua lisää sen näkymään, jonka jälkeen päivittää näkymää

        Args:
            number (int): Käyttöliittymästä valittu numero joka lisätään näkymään
        """
        self.answer_to_equation += self.calculator.use_numeric_buttons(number)
        self.update_answer_label()

    def create_and_place_numeric_buttons(self):
        """Funktio luo ja sijoittaa laskimen numeronapit nappialueelle antaen niille
        myös toiminnallisuuden
        """
        buttons_dictionary = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            ".": (4, 1), 0: (4, 2)
        }

        for button, area in buttons_dictionary.items():
            button_in_dictionary = Button(self.button_area, text=str(button),
                                          font=self.numeric_button_font,
                                          borderwidth=0,
                                          command=lambda
                                          temp_button=button:
                                              self.press_numeric_button(temp_button))
            button_in_dictionary.grid(row=area[0], column=area[1], sticky=NSEW)

    def press_operator_button(self, operator):
        """Toiminto käyttämään laskimen operaattorinappeja, suurin osa funktiosta on
        laskinnäkymän kenttien päivittämistä varten

        Args:
            operator (str): Operaattori joka välitetään sovelluslogiikasta vastaavaan moduuliin
        """
        self.answer_to_equation += self.calculator.use_operator_buttons(
            operator)
        self.equation += self.answer_to_equation
        self.answer_to_equation = ""
        self.update_equation_label()
        self.update_answer_label()

    def create_and_place_operator_buttons(self):
        """Funktio luo ja sijoittaa operaattorinapit laskimen nappialueelle
        """
        operators = ["+", "-", "*", "/"]

        i = 0

        for operator in operators:
            button_in_list = Button(self.button_area, text=operator,
                                    font=self.operator_button_font, borderwidth=0,
                                    command=lambda temp_button=operator:
                                    self.press_operator_button(temp_button))
            button_in_list.grid(row=i, column=4, sticky=NSEW)
            i += 1

    def press_squaring_button(self):
        """Neliöinti toiminto laskimelle, näkymien päivitys tapahtuu tässä,
        itse laskemisesta vastaa sovelluslogiikan calculator-luokka
        """
        squared = self.calculator.squaring_function(self.answer_to_equation)

        if isinstance(squared, float):
            self.equation = self.answer_to_equation+"\u00b2"+"="
            self.update_equation_label()
            self.answer_to_equation = str(squared)
            self.update_answer_label()
            self.calculator.add_to_history(
                self.equation, self.answer_to_equation)
            self.equation = ""
        else:
            self.equation = squared
            self.update_equation_label()

    def press_square_root_button(self):
        """Neliöjuuri toiminto laskimelle, näkymien päivitys tapahtuu tässä,
        itse laskemisesta vastaa sovelluslogiikan calculator-luokka
        """
        square_root = self.calculator.square_root_function(
            self.answer_to_equation)

        if isinstance(square_root, float):
            self.equation = "\u221a"+self.answer_to_equation+"="
            self.update_equation_label()
            self.answer_to_equation = str(square_root)
            self.update_answer_label()
            self.calculator.add_to_history(
                self.equation.replace("\u221a", f"sqrt("), self.answer_to_equation)
            self.equation = ""
        else:
            self.equation = square_root
            self.update_equation_label()

    def press_clear_button(self):
        """Calculator-luokka tyhjentää laskimen yhtälö- ja vastauskentän,
        jonka jälkeen metodi päivittää näkymät
        """
        self.equation = self.calculator.clear()
        self.answer_to_equation = self.calculator.clear()
        self.update_equation_label()
        self.update_answer_label()

    def press_evaluate_button(self):
        """Calculator-luokka laskee yhteen laskimen yhtälö- ja vastauskentän,
        jonka jälkeen palauttaa sen vastauskenttään ja päivittää kentät
        """

        result = self.calculator.evaluate(
            self.equation, self.answer_to_equation)

        self.equation += self.answer_to_equation
        self.update_equation_label()

        self.answer_to_equation = result

        self.update_answer_label()
        self.equation += "="
        self.update_equation_label()
        self.calculator.add_to_history(
            self.equation, self.answer_to_equation)
        self.equation = ""

    def press_history_button(self):
        """Avaa laskuhistoria näkymän calculator-luokkaa hyödyntäen
        """
        self.calculator.show_history()

    def create_and_place_misc_buttons(self):
        """Luo ja sijoittaa laskimen "erityisnapit" laskimen nappialueelle
           neliöintinappi, neliöjuurinappi, tyhjennysnappi ja yhtäsuuruusnappi
        """
        clear_button = Button(self.button_area, text="C", font=(
            "Arial", 24, "bold"), borderwidth=0, command=self.press_clear_button)
        clear_button.grid(row=0, column=1, sticky=NSEW)

        equals_to_button = Button(self.button_area, text="=", font=(
            "Arial", 24, "bold"), borderwidth=0, command=self.press_evaluate_button)
        equals_to_button.grid(row=4, column=4, sticky=NSEW)

        history_button = Button(self.button_area, text="H", font=(
            "Arial", 24, "bold"), borderwidth=0, command=self.press_history_button)
        history_button.grid(row=4, column=3, sticky=NSEW)

        square_button = Button(
            self.button_area, text="x\u00b2", font=self.operator_button_font,
            borderwidth=0, command=self.press_squaring_button)
        square_button.grid(row=0, column=2, sticky=NSEW)

        square_root_button = Button(self.button_area, text="\u221ax",
                                    font=self.operator_button_font,
                                    borderwidth=0, command=self.press_square_root_button)
        square_root_button.grid(row=0, column=3, sticky=NSEW)

    def update_equation_label(self):
        """Päivittää laskimen yhtälökenttää
        """
        self.equation_label.config(text=self.equation)

    def update_answer_label(self):
        """Päivittää laskimen vastauskenttää
        """
        if len(self.answer_to_equation) > 9:
            self.answer_label.config(
                text=self.answer_to_equation, font=("Arial", 20, "bold"))
        else:
            self.answer_label.config(
                text=self.answer_to_equation, font=("Arial", 40, "bold"))

    def run(self):
        """Käynnistää laskimen
        """
        self.screen.mainloop()
