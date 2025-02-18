from PyQt5 import QtWidgets

from model.Form1 import Form1
from model.Form2 import Form2
from model.Form3 import Form3
from model.Form4 import Form4
from model.Form5 import Form5
from model.Form6 import Form6
from model.Form7 import Form7
from model.Form8 import Form8
from model.GeoMap import GeoMap
from views.MainWindowForm import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.new_window = None

        self.ui.lanseazaFormButton.clicked.connect(self.run_form)

    def run_form(self):
        if self.ui.form1.isChecked():
            self.new_window = Form1()
            self.new_window.show()
        elif self.ui.form2.isChecked():
            self.new_window = Form2()
            self.new_window.show()
        elif self.ui.form3.isChecked():
            self.new_window = Form3()
            self.new_window.show()
        elif self.ui.form4.isChecked():
            self.new_window = Form4()
            self.new_window.show()
        elif self.ui.form5.isChecked():
            self.new_window = Form5()
            self.new_window.show()
        elif self.ui.form6.isChecked():
            self.new_window = Form6()
            self.new_window.show()
        elif self.ui.form7.isChecked():
            self.new_window = Form7()
            self.new_window.show()
        elif self.ui.form8.isChecked():
            self.new_window = Form8()
            self.new_window.show()
        elif self.ui.geo_map.isChecked():
            self.new_window = GeoMap()
            self.new_window.show()