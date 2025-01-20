class CalculatorModel:
    def __init__(self):
        self.current_input = ""
        self.result = 0

    def clear(self):
        self.current_input = ""
        self.result = 0

    def calculate(self, expression):
        try:
            self.result = eval(expression)
            self.current_input = str(self.result)
        except Exception as e:
            self.current_input = "Error"