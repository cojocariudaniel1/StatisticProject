import random

import matplotlib
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, \
    NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from PyQt5 import QtCore, QtWidgets

from model.statistic_functions.form3_functions import get_sales, scoatere_produs, get_products, get_category, \
    scoatere_categorie
from views.form3_view import Ui_MainWindow
from matplotlib import rcParams

rcParams.update({'figure.autolayout': True})
matplotlib.use('Qt5Agg')


class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=300):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        super(MplCanvas, self).__init__(self.fig)
        self.fig.tight_layout()


class Form3(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.sc = MplCanvas(self, width=5, height=4, dpi=100)
        self.toolbar = NavigationToolbar(self.sc, self)
        self.ui.chart_layout.addWidget(self.sc)
        self.ui.chart_layout.addWidget(self.toolbar)

        self.ui.produs_button.clicked.connect(self.produs_button)
        self.ui.clasaPrdus_button.clicked.connect(self.categorie_button)
        self.ui.sales_label_pr.setText(f"Sales: 0")
        self.ui.sales_label_clpr.setText(f"Sales: 0")
        self.ui.sales.setText(str(get_sales()))
        self.populate_combobox()


    def populate_combobox(self):
        product_category = get_category()
        for k in product_category:
            self.ui.clasaProdus_CB.addItem(str(k))

        prducts = get_products()
        for j in prducts:
            self.ui.ProdusCB.addItem(str(j))


    def categorie_button(self):
        self.sc.axes.clear()
        obj = scoatere_categorie(self.ui.clasaProdus_CB.currentText())
        date = obj[0]
        sum = obj[1]
        max= obj[2]
        total_sum = obj[3]
        #Calculare profit/pierdere
        if int(self.ui.sales.text()) > total_sum:
            self.ui.profit_sau_pierdere.setText(f"Pierdere: {str(int(self.ui.sales.text()) - total_sum)}")
        else:
            self.ui.profit_sau_pierdere.setText(f"Profit: {str(total_sum - int(self.ui.sales.text()))}")

        #Seteaza suma totala
        self.ui.sales_label_clpr.setText(f"Sales: {total_sum}")
        self.sc.axes.bar(date,sum)
        self.sc.axes.bar(date,max)
        self.sc.draw()
        self.show()

    def produs_button(self):
        self.sc.axes.clear()
        obj = scoatere_produs(self.ui.ProdusCB.currentText())
        date = obj[0]
        sum = obj[1]
        max = obj[2]
        total_sum = obj[3]
        if int(self.ui.sales.text()) > total_sum:
            self.ui.profit_sau_pierdere.setText(f"Pierdere: {str(int(self.ui.sales.text()) - total_sum)}")
        else:
            self.ui.profit_sau_pierdere.setText(f"Profit: {str(total_sum - int(self.ui.sales.text()))}")

        self.ui.sales_label_pr.setText(f"Sales: {total_sum}")

        self.sc.axes.bar(date,sum)
        self.sc.axes.bar(date,max)
        self.sc.draw()
        self.show()
