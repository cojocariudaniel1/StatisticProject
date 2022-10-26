import random

import matplotlib
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, \
    NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from PyQt5 import QtCore, QtWidgets

from model.statistic_functions.form4_functions import get_products
from model.statistic_functions.form4_functions import evolutia_dis_vanz
from views.form4_view import Ui_MainWindow
from matplotlib import rcParams

rcParams.update({'figure.autolayout': True})
matplotlib.use('Qt5Agg')


class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=300):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        super(MplCanvas, self).__init__(self.fig)
        self.fig.tight_layout()


class Form4(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.sc = MplCanvas(self, width=5, height=4, dpi=100)
        self.toolbar = NavigationToolbar(self.sc, self)
        self.ui.chart_layout.addWidget(self.sc)
        self.ui.chart_layout.addWidget(self.toolbar)
        self.ui.genereazaGraph_Button.clicked.connect(self.genereaza_graph)
        self.populate_combobox()


    def populate_combobox(self):

        prducts = get_products()
        for j in prducts:
            self.ui.productComboBox.addItem(str(j))

    def genereaza_graph(self):
        obj = evolutia_dis_vanz(self.ui.productComboBox.currentText())
        self.sc.axes.clear()
        discount = obj[0]
        sales = obj[1]
        profit = obj[2]

        self.sc.axes.plot(discount,sales)
        self.sc.axes.plot(discount,profit)
        self.sc.axes.plot(discount,discount)
        self.sc.axes.set_ylabel("Sales")
        self.sc.axes.set_xlabel("Discount")
        self.sc.axes.legend(["Sales","Profit", "Discount"])
        self.sc.draw()
        self.sc.show()


