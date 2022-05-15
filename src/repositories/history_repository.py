from ui.history_view import HistoryView


class HistoryRepository:

    """Laskimen historiaa käsittelevä luokka
    """

    def __init__(self):
        """Alustetaan käsiteltävä historiatiedosto
        """
        self.historyfile = "calculationhistory.txt"

    def add_calculation_to_history(self, equation, answer):
        """Liitetään laskutoimitus historiaan
        """

        errors = ["Error, please reset",
                  "Overflow, please reset", "Enter number first!",
                  "/0 Error, please reset", "Too many numbers!"]

        if equation in errors or answer in errors:
            pass
        else:
            with open(self.historyfile, "a") as file:
                file.write(f"{equation}{answer}\n")

    def read_calculation_historyfile(self):
        """Luetaan laskinhistoria listaan ja lähetetään eteenpäin
           historianäkymää käsittelevälle luokalle
        """
        historylist = []
        history_view = HistoryView()

        with open(self.historyfile) as file:

            for line in file:

                line.replace("\n", "")
                strippedline = line.strip()
                historylist.append(strippedline)

        history_view.show_historyview(historylist)
        return historylist  # testausta varten
