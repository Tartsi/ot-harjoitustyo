from tkinter import *

class Calculator:
    
    # Alustetaan laskimelle pääikkuna ja määritetään sen koko vakioksi, annetaan ikkunalle myös nimi
    
    def __init__(self):
        self.screen = Tk()
        self.screen.resizable(0,0)
        self.screen.geometry("400x600")
        self.screen.title("Calculator")
    
    # Funktio laskimen käynnistykselle
    
    def run(self):
        self.screen.mainloop()