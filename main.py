import sys

from PyQt5 import QtWidgets

from model.MainWindow import MainWindow

app = QtWidgets.QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
sys.exit(app.exec())

