from ui.calculator import Calculator

class UI:
    
    def __init__(self):
        self.calculator = Calculator()
        self.current_view = None
        
    def start(self):
        self.calculator.run()