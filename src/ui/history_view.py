from tkinter import *


class HistoryView:

    def __init__(self):
        """Alustetaan ikkuna historianäkymälle
        """
        self.root = Tk()
        self.root.title("History")
        self.root.geometry("425x700")
        self.root.resizable(0, 0)

    def show_historyview(self, list):
        """Näytetään historianäkymä

        Args:
            list (str): Argumenttina lista, jossa laskutoimituksia muodossa "1+2=3"
        """
        if len(list) != 0:
            for value in list:
                calculation = Label(self.root, text=value,
                                    font=("Arial", 12, "bold"))
                calculation.grid(pady=4)
        else:
            message = Label(
                self.root, text="No calculations!")
            message.pack()

    def refresh_history_button(self):
        """Toiminnon tarkoituksena päivittää laskinhistoria suoraan historianäkymästä
        """
        pass  # TODO

    def run(self):
        """Käynnistää laskinnäkymän
        """
        self.root.mainloop()
