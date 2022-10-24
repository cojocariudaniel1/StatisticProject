import random

import matplotlib
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5 import QtCore, QtWidgets

from model.statistic_functions.form1_functions import get_products
from views.form1_view import Ui_MainWindow
from data import test2 as obj
from model.statistic_functions.form1_functions import profilul_clientilor

matplotlib.use('Qt5Agg')


class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)
        fig.tight_layout()


class Form1(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.sc = MplCanvas(self, width=5, height=4, dpi=100)
        self.ui.chart_layout.addWidget(self.sc)

        self.ui.genereazaChartButton.clicked.connect(self.check_button)
        self.get_product_items()

    def get_product_items(self):
        items = get_products()
        for j in items:
            self.ui.productComboBox.addItem(str(j))

    def check_button(self):
        if self.ui.profilulClientilorRB.isChecked():
            obj = profilul_clientilor(self.ui.productComboBox.currentText())
            x, y = obj[0], obj[1]
            self.generate_graph(x, y, kind="bar")

    def generate_graph(self, x, y, kind):
        self.sc.axes.clear()
        self.sc.axes.plot()

        if kind == "linear":
            # self.sc.axes.plot(x, y)
            pass
        elif kind == "bar":
            self.sc.axes.bar(x, y)

        self.sc.draw()
