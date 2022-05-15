from tkinter import Tk, Frame, Label, Button, NSEW, E
from services.calculator import Calculator


class CalculatorView:

    """Laskinnäkymästä vastaava luokka"""

    _color_light_gray = "#D3D3D3"
    _numeric_button_font = ("Helvetica", 24, "bold")
    _operator_button_font = ("Arial", 20)

    def __init__(self):
        """Konstruktori, alustaa laskinnäkymän

        Konstruktori ei ota argumentteja vaan toimii "itsenäisesti"

        Konstruktori kutsuu metodeita, jotka muodostavat laskinnäkymän
        """
        self._screen = Tk()
        self._screen.geometry("400x600")
        self._screen.title("Calculator")

        self._equation = ""
        self._answer_to_equation = ""

        self._display_area, self._button_area = self._create_areas()
        self._equation_label, self._answer_label = self._create_labels()

        self._create_and_place_numeric_buttons()
        self._create_and_place_operator_buttons()
        self._create_and_place_misc_buttons()
        self._fill_button_area()

        self._calculator = Calculator()

        # "Resetöidään" laskinhistoria jokaiselle uudelle laskinnäkymälle

        open("calculationhistory.txt", "w").close()

    def _create_areas(self):
        """Funktio luo laskimen "vastausalueen" ja nappialueen

        Returns:
            Frame: Palauttaa "vastausalueen" ja nappialueen
        """
        display_frame = Frame(self._screen, height=200,
                              bg=self._color_light_gray)
        display_frame.pack(expand=True, fill="both")
        button_frame = Frame(self._screen)
        button_frame.pack(expand=True, fill="both")
        return display_frame, button_frame

    def _create_labels(self):
        """Funktio sijoittaa laskimen vastausalueelle yhtälön ja vastauksen

        Returns:
            Label: Palauttaa laskimen vastausalueelle yhtälön ja vastauksen kentät
        """
        equation_label = Label(self._display_area, text=self._equation,
                               bg=self._color_light_gray, anchor=E,
                               font=("Arial", 16), padx=20)
        answer_label = Label(self._display_area, text=self._answer_to_equation,
                             bg=self._color_light_gray, anchor=E,
                             font=("Arial", 40, "bold"), padx=20)
        equation_label.pack(expand=True, fill="both")
        answer_label.pack(expand=True, fill="both")
        return equation_label, answer_label

    def _fill_button_area(self):
        """Funktio muotoilee nappialuetta niin, että laskimen napit täyttävät sen kokonaan
        """
        self._button_area.rowconfigure(0, weight=1)

        for i in range(1, 5):
            self._button_area.rowconfigure(i, weight=1)
            self._button_area.columnconfigure(i, weight=1)

    def _press_numeric_button(self, number):
        """Funktio saa numeron parametriksi ja hyödyntäen calculator-luokan
        palvelua lisää sen näkymään, jonka jälkeen päivittää näkymää

        Args:
            number (int): Käyttöliittymästä valittu numero joka lisätään näkymään
        """
        self._answer_to_equation += self._calculator.use_numeric_buttons(
            number)
        self._update_answer_label()

    def _create_and_place_numeric_buttons(self):
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
            button_in_dictionary = Button(self._button_area, text=str(button),
                                          font=self._numeric_button_font,
                                          borderwidth=0,
                                          command=lambda
                                          temp_button=button:
                                              self._press_numeric_button(temp_button))
            button_in_dictionary.grid(row=area[0], column=area[1], sticky=NSEW)

    def _press_operator_button(self, operator):
        """Toiminto käyttämään laskimen operaattorinappeja, suurin osa funktiosta on
        laskinnäkymän kenttien päivittämistä varten

        Args:
            operator (str): Operaattori joka välitetään sovelluslogiikasta vastaavaan moduuliin
        """
        self._answer_to_equation += self._calculator.use_operator_buttons(
            operator)
        self._equation += self._answer_to_equation
        self._answer_to_equation = ""
        self._update_equation_label()
        self._update_answer_label()

    def _create_and_place_operator_buttons(self):
        """Funktio luo ja sijoittaa operaattorinapit laskimen nappialueelle
        """
        operators = ["+", "-", "*", "/"]

        i = 0

        for operator in operators:
            button_in_list = Button(self._button_area, text=operator,
                                    font=self._operator_button_font, borderwidth=0,
                                    command=lambda temp_button=operator:
                                    self._press_operator_button(temp_button))
            button_in_list.grid(row=i, column=4, sticky=NSEW)
            i += 1

    def _press_squaring_button(self):
        """Neliöinti toiminto laskimelle, näkymien päivitys tapahtuu tässä,
        itse laskemisesta vastaa sovelluslogiikan calculator-luokka
        """
        squared = self._calculator.squaring_function(self._answer_to_equation)

        if isinstance(squared, float):
            self._equation = self._answer_to_equation+"\u00b2"+"="
            self._update_equation_label()
            self._answer_to_equation = str(squared)
            self._update_answer_label()
            self._calculator.add_to_history(
                self._equation, self._answer_to_equation)
            self._equation = ""
        else:
            self._equation = squared
            self._update_equation_label()

    def _press_square_root_button(self):
        """Neliöjuuri toiminto laskimelle, näkymien päivitys tapahtuu tässä,
        itse laskemisesta vastaa sovelluslogiikan calculator-luokka
        """
        square_root = self._calculator.square_root_function(
            self._answer_to_equation)

        if isinstance(square_root, float):
            self._equation = "\u221a"+self._answer_to_equation+"="
            self._update_equation_label()
            self._answer_to_equation = str(square_root)
            self._update_answer_label()
            self._calculator.add_to_history(
                self._equation.replace("\u221a", f"sqrt("), self._answer_to_equation)
            self._equation = ""
        else:
            self._equation = square_root
            self._update_equation_label()

    def _press_clear_button(self):
        """Calculator-luokka tyhjentää laskimen yhtälö- ja vastauskentän,
        jonka jälkeen metodi päivittää näkymät
        """
        self._equation = self._calculator.clear()
        self._answer_to_equation = self._calculator.clear()
        self._update_equation_label()
        self._update_answer_label()

    def _press_evaluate_button(self):
        """Calculator-luokka laskee yhteen laskimen yhtälö- ja vastauskentän,
        jonka jälkeen palauttaa sen vastauskenttään ja päivittää kentät
        """

        result = self._calculator.evaluate(
            self._equation, self._answer_to_equation)

        self._equation += self._answer_to_equation
        self._update_equation_label()

        self._answer_to_equation = result

        self._update_answer_label()
        self._equation += "="
        self._update_equation_label()
        self._calculator.add_to_history(
            self._equation, self._answer_to_equation)
        self._equation = ""

    def _press_history_button(self):
        """Avaa laskuhistoria näkymän calculator-luokkaa hyödyntäen
        """
        self._calculator.show_history()

    def _create_and_place_misc_buttons(self):
        """Luo ja sijoittaa laskimen "erityisnapit" laskimen nappialueelle
           neliöintinappi, neliöjuurinappi, tyhjennysnappi ja yhtäsuuruusnappi
        """
        clear_button = Button(self._button_area, text="C", font=(
            "Arial", 24, "bold"), borderwidth=0, command=self._press_clear_button)
        clear_button.grid(row=0, column=1, sticky=NSEW)

        equals_to_button = Button(self._button_area, text="=", font=(
            "Arial", 24, "bold"), borderwidth=0, command=self._press_evaluate_button)
        equals_to_button.grid(row=4, column=4, sticky=NSEW)

        history_button = Button(self._button_area, text="H", font=(
            "Arial", 24, "bold"), borderwidth=0, command=self._press_history_button)
        history_button.grid(row=4, column=3, sticky=NSEW)

        square_button = Button(
            self._button_area, text="x\u00b2", font=self._operator_button_font,
            borderwidth=0, command=self._press_squaring_button)
        square_button.grid(row=0, column=2, sticky=NSEW)

        square_root_button = Button(self._button_area, text="\u221ax",
                                    font=self._operator_button_font,
                                    borderwidth=0, command=self._press_square_root_button)
        square_root_button.grid(row=0, column=3, sticky=NSEW)

    def _update_equation_label(self):
        """Päivittää laskimen yhtälökenttää
        """
        self._equation_label.config(text=self._equation)

    def _update_answer_label(self):
        """Päivittää laskimen vastauskenttää
        """
        if len(self._answer_to_equation) > 9:
            self._answer_label.config(
                text=self._answer_to_equation, font=("Arial", 20, "bold"))
        else:
            self._answer_label.config(
                text=self._answer_to_equation, font=("Arial", 40, "bold"))

    def run(self):
        """Käynnistää laskimen
        """
        self._screen.mainloop()
