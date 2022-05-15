from tkinter import Tk, Frame, Label, Button


class HistoryView:

    """Luokka vastaa laskimen historianäkymästä
    """

    def __init__(self):
        """Alustetaan ikkuna historianäkymälle
        """
        self._root = Tk()
        self._root.title("Calculation History")
        self._root.geometry("425x700")
        self._root.resizable(0, 0)
        self._button_frame = self._create_button_frame()
        self._history_frame = self._create_history_frame()
        self._clear_history_button()

    def _create_button_frame(self):
        """Luo lohkon johon napit sijoitetaan

        Returns:
            Frame: Lohko johon näkymän napit sijoitetaan
        """
        temporary_button_frame = Frame(self._root)
        temporary_button_frame.pack()
        return temporary_button_frame

    def _create_history_frame(self):
        """Luo lohkon johon laskuhistoria sijoittuu allekkain

        Returns:
            Frame: Lohko johon laskuhistoria sijoitetaan
        """
        temporary_history_frame = Frame(self._root)
        temporary_history_frame.pack()
        return temporary_history_frame

    def _clear_action(self):
        """Toiminto tyhjentää laskinhistorian ja avaa ikkunan uudestaan
        """
        open("calculationhistory.txt", "w").close()
        self._root.update()
        self._root.update_idletasks()

    def _clear_history_button(self):
        """Luo napin laskinhistorian tyhjennykselle
        """
        clear = Button(self._button_frame, text="CLEAR HISTORY",
                       borderwidth=5, command=self._clear_action)
        clear.grid()

    def show_historyview(self, list):
        """Näytetään historianäkymä

        Args:
            list (str): Argumenttina lista, jossa laskutoimituksia muodossa "1+2=3"
        """
        if len(list) != 0:
            for value in list:
                calculation = Label(self._history_frame, text=value,
                                    font=("Arial", 12, "bold"))
                calculation.grid(pady=4)
        else:
            message = Label(
                self._history_frame, text="No calculations!")
            message.grid()

    def run(self):
        """Käynnistää historianäkymän
        """
        self._root.mainloop()
