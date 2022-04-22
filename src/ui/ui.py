from ui.calculator import Calculator

# Moduulista hallinnoidaan näkymiä - laskinta ja myöhemmin tarkoitus mahdollistaa myös historia


class UI:

    def __init__(self):
        self.calculator = Calculator()
        self.current_view = None

    def start(self):
        self.calculator.run()
