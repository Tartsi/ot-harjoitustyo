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
        try:
            with open(self.historyfile, "a") as file:
                file.write(f"{equation}{answer}\n")
        except FileNotFoundError:
            print('File not found!')
        except PermissionError:
            print("Permission denied!")
        except Exception as e:
            print("Error occured:", e)

    def read_calculation_historyfile(self):
        """Luetaan laskinhistoria listaan ja lähetetään eteenpäin
           historianäkymää käsittelevälle luokalle
        """
        historylist = []
        hist = HistoryView()

        try:
            with open(self.historyfile) as file:

                for line in file:

                    line.replace("\n", "")
                    strippedline = line.strip()
                    historylist.append(strippedline)

            hist.show_historyview(historylist)
        except FileNotFoundError:
            print('File not found!')
        except PermissionError:
            print("Permission denied!")
        except Exception as e:
            print("Error occured:", e)
