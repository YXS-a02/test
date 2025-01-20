import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from ui.calculator import Ui_Calculator  # 假设你有一个生成的 Python 文件
from controllers.calculator_controller import CalculatorController

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Calculator()
        self.ui.setupUi(self)
        self.controller = CalculatorController(self.ui)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())