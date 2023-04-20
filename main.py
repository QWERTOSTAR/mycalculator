import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from ui import Ui_MainWindow


class Rof(QtWidgets.QMainWindow):
    def __init__(self):
        super(Rof, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()
    ''''''
    def init_UI(self):
        self.ui.push_1.clicked.connect(self.method_1)
        self.ui.push_2.clicked.connect(self.method_2)
        self.ui.push_3.clicked.connect(self.method_3)
        self.ui.push_4.clicked.connect(self.method_4)
        self.ui.push_5.clicked.connect(self.method_5)
        self.ui.push_6.clicked.connect(self.method_6)
        self.ui.push_7.clicked.connect(self.method_7)
        self.ui.push_8.clicked.connect(self.method_8)
        self.ui.push_9.clicked.connect(self.method_9)
        self.ui.push_zero.clicked.connect(self.method_zero)
        self.ui.push_point.clicked.connect(self.method_point)
        self.ui.push_plus.clicked.connect(self.method_plus)
        self.ui.push_min.clicked.connect(self.method_min)
        self.ui.push_mult.clicked.connect(self.method_mult)
        self.ui.push_div.clicked.connect(self.method_div)
        self.ui.push_equal.clicked.connect(self.method_equal)
        self.ui.push_clear.clicked.connect(self.method_clear)
        self.ui.push_del.clicked.connect(self.method_del)

    '''метод добовление '''
    def method_1(self):
        text = self.ui.label.text()
        self.ui.label.setText(text + "1")

    def method_2(self):
        text = self.ui.label.text()
        self.ui.label.setText(text + "2")

    def method_3(self):
        text = self.ui.label.text()
        self.ui.label.setText(text + "3")

    def method_4(self):
        text = self.ui.label.text()
        self.ui.label.setText(text + "4")

    def method_5(self):
        text = self.ui.label.text()
        self.ui.label.setText(text + "5")

    def method_6(self):
        text = self.ui.label.text()
        self.ui.label.setText(text + "6")

    def method_7(self):
        text = self.ui.label.text()
        self.ui.label.setText(text + "7")

    def method_8(self):
        text = self.ui.label.text()
        self.ui.label.setText(text + "8")

    def method_9(self):
        text = self.ui.label.text()
        self.ui.label.setText(text + "9")

    def method_zero(self):
        text = self.ui.label.text()
        self.ui.label.setText(text + "0")

    def method_point(self):
        text = self.ui.label.text()
        self.ui.label.setText(text + ".")

    def method_plus(self):
        text = self.ui.label.text()
        self.ui.label.setText(text + "+")

    def method_min(self):
        text = self.ui.label.text()
        self.ui.label.setText(text + "-")

    def method_mult(self):
        text = self.ui.label.text()
        self.ui.label.setText(text + "*")

    def method_div(self):
        text = self.ui.label.text()
        self.ui.label.setText(text + "/")

    def method_clear(self):
        self.ui.label.setText("")

    def method_del(self):
        text = self.ui.label.text()
        self.ui.label.setText(text[:len(text) - 1])

    def method_equal(self):
        text = self.ui.label.text()

        try:
            ans = eval(text)
            self.ui.label.setText(str(ans))
        except:
            self.ui.label.setText("Wrong Input")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = Rof()
    main_window.show()
    sys.exit(app.exec())
