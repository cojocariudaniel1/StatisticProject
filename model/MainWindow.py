from PyQt5 import QtCore, QtWidgets

from model.Form2 import Form2
from model.Form3 import Form3
from model.Form4 import Form4
from model.Form5 import Form5
from views.MainWindowForm import Ui_MainWindow
from model.Form1 import Form1


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.new_window = None

        self.ui.lanseazaFormButton.clicked.connect(self.run_form)

    def run_form(self):
        if self.ui.form1.isChecked():
            MainWindow.hide(self)
            self.new_window = Form1()
            self.new_window.show()
        elif self.ui.form2.isChecked():
            MainWindow.hide(self)
            self.new_window = Form2()
            self.new_window.show()
        elif self.ui.form3.isChecked():
            MainWindow.hide(self)
            self.new_window = Form3()
            self.new_window.show()
        elif self.ui.form4.isChecked():
            MainWindow.hide(self)
            self.new_window = Form4()
            self.new_window.show()
        elif self.ui.form5.isChecked():
            MainWindow.hide(self)
            self.new_window = Form5()
            self.new_window.show()