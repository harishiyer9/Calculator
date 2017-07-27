from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from py_expression_eval import Parser


class CalcGridLayout(GridLayout):
    # Function called when equals is pressed
    def calculate(self, calculation):
        if calculation:
            try:
                # Solve formula and display it in entry
                # which is pointed at by display
                parser = Parser()
                self.display.text = str(parser.parse(calculation).evaluate({}))
            except Exception:
                self.display.text = "Error"

class CalculatorApp(App):
    def build(self):
        return CalcGridLayout()

if __name__ == '__main__':
    CalculatorApp().run()