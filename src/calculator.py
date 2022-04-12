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

    # Luodaan funktio, joka luo ja palauttaa "vastausalueen" ja nappialueen

    def create_areas(self):
        display_frame = Frame(self.screen, height=200, bg=self.color_light_gray)
        display_frame.pack(expand=False, fill="both")
        button_frame = Frame(self.screen)
        button_frame.pack(expand=False, fill="both")
        return display_frame, button_frame

    # Funktio laskimen käynnistykselle

    def run(self):
        self.screen.mainloop()