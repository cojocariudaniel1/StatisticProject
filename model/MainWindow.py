from PyQt5 import QtCore, QtWidgets
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
        if self.ui.form1.isChecked() == True:
            try:
                MainWindow.hide(self)
                self.new_window = Form1()
                self.new_window.show()
            except Exception as e:
                print(e)
        else:
            pass
