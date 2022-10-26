import random

import matplotlib
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, \
    NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from PyQt5 import QtCore, QtWidgets

from model.statistic_functions.form1_functions import get_products, perioada_de_timp, zona_de_distributie
from views.form1_view import Ui_MainWindow
from model.statistic_functions.form1_functions import profilul_clientilor
from matplotlib import rcParams

rcParams.update({'figure.autolayout': True})
matplotlib.use('Qt5Agg')


# Figura(grafic) efectiva care o sa apara in interfta
class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=300):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        super(MplCanvas, self).__init__(self.fig)
        self.fig.tight_layout()


class Form1(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Se creaza graficul gol
        self.sc = MplCanvas(self, width=5, height=4, dpi=100)
        # Se adauga meniul de la grafic in partea de jos
        self.toolbar = NavigationToolbar(self.sc, self)

        # Se adauga meniul si chart-ul intr-un layout din interfata
        self.ui.chart_layout.addWidget(self.sc)
        self.ui.chart_layout.addWidget(self.toolbar)

        self.ui.genereazaChartButton.clicked.connect(self.check_button)
        self.get_product_items()

    # Se primeste o lista de produse si se adauga intr-un ComboBox
    def get_product_items(self):
        items = get_products()
        for j in items:
            self.ui.productComboBox.addItem(str(j))



    def check_button(self):
        self.sc.axes.clear()
        if self.ui.profilulClientilorRB.isChecked():
            obj = profilul_clientilor(self.ui.productComboBox.currentText())
            x, y = obj[0], obj[1]
            self.sc.axes.plot()
            self.sc.axes.set_title("Profitul clientilor in functie de categorie")
            self.sc.axes.set_ylabel('Profit')
            self.sc.axes.set_xlabel('Segmet')

            # Se acceseaza functia generate_graph avand ca atribut x,y si tip-ul de chart
            self.generate_graph(x, y, kind="bar")
        elif self.ui.perioadaDeTimpRB.isChecked():
            obj = perioada_de_timp(self.ui.productComboBox.currentText())
            x, y = obj[0], obj[1]
            self.sc.axes.plot()
            self.sc.axes.set_title("Profitul clientilor in functie de data")
            self.sc.axes.set_ylabel("Profit")
            self.sc.axes.set_xlabel("Order Date")
            self.generate_graph(x, y, kind="linear")
        elif self.ui.zonaDeDistributieRB.isChecked():
            obj = zona_de_distributie(product_name=self.ui.productComboBox.currentText())
            x, y = obj[0], obj[1]
            self.sc.axes.plot()
            self.sc.axes.tick_params(axis="x", labelrotation=90)
            self.sc.axes.set_title("Profitul clientilor in functie de zona")
            self.sc.axes.set_ylabel("Profit")
            self.sc.axes.set_xlabel("Country")
            self.generate_graph(x, y, kind="bar")

    def generate_graph(self, x, y, kind):

        if kind == "linear":
            self.sc.axes.plot(x, y)
        elif kind == "bar":
            self.sc.axes.bar(x, y)

        self.sc.draw()
        self.sc.show()
