class CalculatorController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.set_controller(self)

    def perform_calculation(self, input_expression):
        try:
            result = self.model.calculate(input_expression)
            self.update_display(result)
        except Exception as e:
            self.update_display("Error")

    def update_display(self, value):
        self.view.display.setText(str(value))