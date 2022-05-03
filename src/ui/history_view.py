from tkinter import *


class HistoryView:

    def __init__(self):
        """Alustetaan ikkuna historianäkymälle
        """
        self.root = Tk()
        self.root.title("History")
        self.root.geometry("425x700")
        self.root.resizable(0, 0)
        self.button_frame = self.create_button_frame()
        self.history_frame = self.create_history_frame()
        self.clear_history_button()

    def create_button_frame(self):
        """Luo lohkon johon napit sijoitetaan

        Returns:
            Frame: Lohko johon näkymän napit sijoitetaan
        """
        temporary_button_frame = Frame(self.root)
        temporary_button_frame.pack()
        return temporary_button_frame

    def create_history_frame(self):
        """Luo lohkon johon laskuhistoria sijoittuu allekkain

        Returns:
            Frame: Lohko johon laskuhistoria sijoitetaan
        """
        temporary_history_frame = Frame(self.root)
        temporary_history_frame.pack()
        return temporary_history_frame

    def refresh_history_button(self):
        """Toiminnon tarkoituksena päivittää laskinhistoria suoraan historianäkymästä
        """
        pass  # TODO

    def clear_action(self):
        """Toiminto tyhjentää laskinhistorian
        """
        open("calculationhistory.txt", "w").close()

    def clear_history_button(self):
        """Luo napin laskinhistorian tyhjennykselle
        """
        clear = Button(self.button_frame, text="CLEAR HISTORY",
                       borderwidth=5, command=self.clear_action)
        clear.grid()

    def show_historyview(self, list):
        """Näytetään historianäkymä

        Args:
            list (str): Argumenttina lista, jossa laskutoimituksia muodossa "1+2=3"
        """
        if len(list) != 0:
            for value in list:
                calculation = Label(self.history_frame, text=value,
                                    font=("Arial", 12, "bold"))
                calculation.grid(pady=4)
        else:
            message = Label(
                self.history_frame, text="No calculations!")
            message.grid()

    def run(self):
        """Käynnistää laskinnäkymän
        """
        self.root.mainloop()


# if __name__ == "__main__":
#     h = HistoryView()
#     h.run()
