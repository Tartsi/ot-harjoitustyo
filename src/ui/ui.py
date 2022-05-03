from ui.calculator_view import CalculatorView


class UI:

    """Moduulista tarkoitus hallinnoida laskimen näkymiä, laskinta ja laskinhistoriaa
    """

    def __init__(self):
        self.calculator = CalculatorView()
        self.current_view = None

    def show_calculator(self):
        """Metodi käynnistää laskinnäkymän
        """
        self.calculator.run()

    def show_history(self):
        """Metodin tarkoituksena näyttää laskinhistoria. Vielä toteuttamatta
        """
        pass
