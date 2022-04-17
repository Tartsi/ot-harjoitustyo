from tkinter import *

class Calculator:

    # Luodaan uusi luokkamuuttuja laskimen muotoiluun liittyen

    color_light_gray = "#D3D3D3"

    # Alustetaan laskimelle pääikkuna ja määritetään sen koko vakioksi, annetaan ikkunalle myös nimi

    def __init__(self):
        self.screen = Tk()
        self.screen.resizable(0, 0)
        self.screen.geometry("400x600")
        self.screen.title("Calculator")
        
        # Luodaan muuttujat jotka näyttävät laskimen tämänhetkisen yhtälön ja sen vastauksen
        
        self.equation = ""
        self.answer_to_equation = ""
        
        # Luodaan muuttujat, joihin sijoitetaan laskimen "vastausalue" ja nappialue
        
        self.display_area, self.button_area = self.create_areas()
        
        # Kutsutaan funktioita, jotka luovat ja sijoittavat laskimeen napit

        self.create_and_place_numeric_buttons()
        self.create_and_place_operator_buttons()
        self.create_and_place_misc_buttons()
        self.fill_button_area()

    # Luodaan funktio, joka luo ja palauttaa "vastausalueen" ja nappialueen

    def create_areas(self):
        display_frame = Frame(self.screen, height=200, bg=self.color_light_gray)
        display_frame.pack(expand=True, fill="both")
        button_frame = Frame(self.screen)
        button_frame.pack(expand=True, fill="both")
        return display_frame, button_frame
    
    # Muotoillaan nappialuetta niin, että laskimen napit täyttävät sen kokonaan

    def fill_button_area(self):

        self.button_area.rowconfigure(0, weight=1)

        for i in range(1, 5):
            self.button_area.rowconfigure(i, weight=1)
            self.button_area.columnconfigure(i, weight=1)
    
    # Luodaan ja sijoitetaan laskimeen numeronapit. Asetetaan nille myös toiminta
    
    def use_numeric_buttons(self):
        return
    
    def create_and_place_numeric_buttons(self):
    
        buttons_dictionary = {
            7: (1,1), 8: (1,2), 9: (1,3),
            4: (2,1), 5: (2,2), 6: (2,3),
            1: (3,1), 2: (3,2), 3: (3,3),
            ".": (4,1), 0: (4,2)
        }
        
        for button, area in buttons_dictionary.items():
            b = Button(self.button_area, text=str(button),font=("Helvetica", 24, "bold"), borderwidth=0, command=lambda temp_button=button: self.use_numeric_buttons(temp_button))
            b.grid(row=area[0], column=area[1], sticky=NSEW)
    
    # Luodaan ja sijoitetaan laskimeen operaattorinapit. Asetetaan nille myös toiminta
    
    def use_operator_buttons(self):
        return
    
    def create_and_place_operator_buttons(self):
        
        operators = ["+","-","*","/"]

        i = 0

        for operator in operators:
            b = Button(self.button_area, text=operator, font=("Arial", 20), borderwidth=0, command=lambda temp_button=operator: self.use_operator_buttons(temp_button))
            b.grid(row=i, column=4,sticky=NSEW)
            i += 1
    
    # Luodaan ja sijoitetaan laskimeen loput napit. Asetetaan nille myös toiminnat
    
    def clear(self):
        return
    
    def evaluate(self):
        return
    
    def create_and_place_misc_buttons(self):
        
        clear_button = Button(self.button_area, text="C", font=("Arial", 24, "bold"), borderwidth=0, command=self.clear)
        clear_button.grid(row=0, column=1,sticky=NSEW,columnspan=3)

        equals_to_button = Button(self.button_area, text="=", font=("Arial", 24, "bold"), borderwidth=0, command=self.evaluate)
        equals_to_button.grid(row=4,column=3,columnspan=2,sticky=NSEW)
           
    # Funktio laskimen käynnistykselle

    def run(self):
        self.screen.mainloop()

def main():
    calculator = Calculator()
    calculator.run()

if __name__ == '__main__':
    main()