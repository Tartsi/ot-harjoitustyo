from tkinter import *

# Luokka luo laskimen


class Calculator:

    # Luodaan luokkamuuttujat laskimen muotoiluun liittyen

    color_light_gray = "#D3D3D3"
    numeric_button_font = ("Helvetica", 24, "bold")
    operator_button_font = ("Arial", 20)

    # Alustetaan laskin

    def __init__(self):
        self.screen = Tk()
        self.screen.geometry("400x600")
        self.screen.title("Calculator")

        # Luodaan muuttujat jotka näyttävät laskimen tämänhetkisen yhtälön ja sen vastauksen

        self.equation = ""
        self.answer_to_equation = ""

        # Luodaan muuttujat, joihin sijoitetaan laskimen "vastausalue" ja nappialue

        self.display_area, self.button_area = self.create_areas()

        # Luodaan laskimen vastaukselle ja yhtälölle kentät joihin ne voidaan asettaa

        self.equation_label, self.answer_label = self.create_labels()

        # Kutsutaan funktioita, jotka luovat ja sijoittavat laskimeen napit

        self.create_and_place_numeric_buttons()
        self.create_and_place_operator_buttons()
        self.create_and_place_misc_buttons()
        self.fill_button_area()

    # Funktio luo laskimen "vastausalueen" ja nappialueen

    def create_areas(self):
        display_frame = Frame(self.screen, height=200,
                              bg=self.color_light_gray)
        display_frame.pack(expand=True, fill="both")
        button_frame = Frame(self.screen)
        button_frame.pack(expand=True, fill="both")
        return display_frame, button_frame

    # Funktio sijoittaa laskimen vastausalueelle yhtälön ja vastauksen

    def create_labels(self):
        equation_label = Label(self.display_area, text=self.equation,
                               bg=self.color_light_gray, anchor=E, font=("Arial", 16), padx=20)
        answer_label = Label(self.display_area, text=self.answer_to_equation,
                             bg=self.color_light_gray, anchor=E, font=("Arial", 40, "bold"), padx=20)
        equation_label.pack(expand=True, fill="both")
        answer_label.pack(expand=True, fill="both")
        return equation_label, answer_label

    # Funktio muotoilee nappialuetta niin, että laskimen napit täyttävät sen kokonaan

    def fill_button_area(self):

        self.button_area.rowconfigure(0, weight=1)

        for i in range(1, 5):
            self.button_area.rowconfigure(i, weight=1)
            self.button_area.columnconfigure(i, weight=1)

    # Funktiot luovat ja sijoittavat laskimeen numeronapit ja antavat niille toiminnon

    def use_numeric_buttons(self, number):
        self.answer_to_equation += str(number)
        self.update_answer_label()

    def create_and_place_numeric_buttons(self):

        buttons_dictionary = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            ".": (4, 1), 0: (4, 2)
        }

        for button, area in buttons_dictionary.items():
            b = Button(self.button_area, text=str(button), font=self.numeric_button_font,
                       borderwidth=0, command=lambda temp_button=button: self.use_numeric_buttons(temp_button))
            b.grid(row=area[0], column=area[1], sticky=NSEW)

    # Funktiot luovat ja sijoittavat laskimeen operaattorinapit ja antavat niille toiminnon

    def use_operator_buttons(self, operator):
        self.answer_to_equation += operator
        self.equation += self.answer_to_equation
        self.answer_to_equation = ""
        self.update_equation_label()
        self.update_answer_label()

    def create_and_place_operator_buttons(self):

        operators = ["+", "-", "*", "/"]

        i = 0

        for operator in operators:
            b = Button(self.button_area, text=operator, font=self.operator_button_font, borderwidth=0,
                       command=lambda temp_button=operator: self.use_operator_buttons(temp_button))
            b.grid(row=i, column=4, sticky=NSEW)
            i += 1

    # Funktiot luovat ja sijoittavat laskimeen "muut" napit ja antavat niille toiminnot

    def squaring_function(self):
        self.equation = self.answer_to_equation+"\u00b2"+"="
        self.update_equation_label()
        try:
            self.answer_to_equation = str(
                eval(f"{self.answer_to_equation}**2"))
        except OverflowError as e:
            self.answer_to_equation = "Overflow"

        self.update_answer_label()
        self.equation = ""

    def square_root_button_function(self):
        self.equation = "\u221a"+self.answer_to_equation+"="
        self.update_equation_label()
        self.answer_to_equation = str(eval(f"{self.answer_to_equation}**0.5"))
        self.update_answer_label()
        self.equation = ""

    def clear_calculator(self):
        self.equation = ""
        self.answer_to_equation = ""
        self.update_equation_label()
        self.update_answer_label()

    def evaluate_equation(self):
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

    def create_and_place_misc_buttons(self):

        clear_button = Button(self.button_area, text="C", font=(
            "Arial", 24, "bold"), borderwidth=0, command=self.clear_calculator)
        clear_button.grid(row=0, column=1, sticky=NSEW)

        equals_to_button = Button(self.button_area, text="=", font=(
            "Arial", 24, "bold"), borderwidth=0, command=self.evaluate_equation)
        equals_to_button.grid(row=4, column=3, columnspan=2, sticky=NSEW)

        square_button = Button(
            self.button_area, text="x\u00b2", font=self.operator_button_font, borderwidth=0, command=self.squaring_function)
        square_button.grid(row=0, column=2, sticky=NSEW)

        square_root_button = Button(self.button_area, text="\u221ax", font=self.operator_button_font,
                                    borderwidth=0, command=self.square_root_button_function)
        square_root_button.grid(row=0, column=3, sticky=NSEW)

    # Funktiot päivittävät (väliaikaista) yhtälöä ja vastausta

    def update_equation_label(self):
        self.equation_label.config(text=self.equation)

    def update_answer_label(self):
        if len(self.answer_to_equation) > 9:
            self.answer_label.config(text=self.answer_to_equation[:11]+"...")
        else:
            self.answer_label.config(text=self.answer_to_equation)

    # Funktio laskimen käynnistykselle

    def run(self):
        self.screen.mainloop()
