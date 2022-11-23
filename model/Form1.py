from datetime import datetime

import matplotlib
import xlsxwriter
from PyQt5 import QtWidgets
from matplotlib import rcParams
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, \
    NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

from model.Export import Export
from model.statistic_functions.form1_functions import get_products, perioada_de_timp, zona_de_distributie, \
    export_to_excel, exporta_profilui_clientilor, export_zona_de_distributie

from model.statistic_functions.form1_functions import profilul_clientilor
from views.form1_view import Ui_MainWindow

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
        self.ui.export_button.hide()
        self.ui.export_btn.hide()
        # Se creaza graficul gol
        self.sc = MplCanvas(self, width=5, height=4, dpi=100)
        # Se adauga meniul de la grafic in partea de jos
        self.toolbar = NavigationToolbar(self.sc, self)

        # Se adauga meniul si chart-ul intr-un layout din interfata
        self.ui.chart_layout.addWidget(self.sc)
        self.ui.chart_layout.addWidget(self.toolbar)

        self.ui.genereazaChartButton.clicked.connect(self.check_button)
        self.get_product_items()

        self.ui.productComboBox.activated[str].connect(self.reset_date)
        self.ui.profilulClientilorRB.clicked.connect(self.reset_date)
        self.ui.zonaDeDistributieRB.clicked.connect(self.reset_date)

        self.ui.export_button.clicked.connect(self.export)
        self.ui.export_btn.clicked.connect(self.export2)

    def export(self):
        self.new_window = Export("Form1", self.ui.productComboBox.currentText())
        self.new_window.show()

    def reset_date(self):
        try:
            self.ui.dateEdit_max.setDateTime(datetime(2000, 1, 1))
            self.ui.dateEdit_min.setDateTime(datetime(2000, 1, 1))
            self.ui.dateEdit_max.setEnabled(False)
            self.ui.dateEdit_min.setEnabled(False)
        except Exception as e:
            print(e)

    # Se primeste o lista de produse si se adauga intr-un ComboBox
    def get_product_items(self):
        items = get_products()
        for j in items:
            self.ui.productComboBox.addItem(str(j))

    def export2(self):
        if self.ui.profilulClientilorRB.isChecked():
            folderpath = QtWidgets.QFileDialog.getSaveFileName(self, 'Select Folder')
            obj = profilul_clientilor(self.ui.productComboBox.currentText())
            exporta_profilui_clientilor(obj, folderpath)
        elif self.ui.zonaDeDistributieRB.isChecked():
            folderpath = QtWidgets.QFileDialog.getSaveFileName(self, 'Select Folder')
            export_zona_de_distributie(self.ui.productComboBox.currentText(), folderpath)


    def check_button(self):
        self.sc.axes.clear()
        if self.ui.profilulClientilorRB.isChecked():
            obj = profilul_clientilor(self.ui.productComboBox.currentText())
            x, y = obj[0][0], obj[0][1]
            self.sc.axes.plot()
            self.sc.axes.set_title("Profitul clientilor in functie de categorie")
            self.sc.axes.set_ylabel('Profit')
            self.sc.axes.set_xlabel('Segmet')

            # Se acceseaza functia generate_graph avand ca atribut x,y si tip-ul de chart
            self.generate_graph(x, y, kind="bar")
        elif self.ui.perioadaDeTimpRB.isChecked():
            print('test')
            date = datetime(2000, 1, 1)
            if self.ui.dateEdit_min.dateTime().toPyDateTime() == (
                    date) and self.ui.dateEdit_max.dateTime().toPyDateTime() == date:
                obj = perioada_de_timp(self.ui.productComboBox.currentText())
                self.ui.dateEdit_min.setDateTime(obj[2])
                self.ui.dateEdit_max.setDateTime(obj[3])
                self.ui.dateEdit_min.setEnabled(True)
                self.ui.dateEdit_max.setEnabled(True)
                x, y = obj[0], obj[1]
                self.sc.axes.plot()
                self.sc.axes.set_title("Profitul clientilor in functie de data")
                self.sc.axes.set_ylabel("Profit")
                self.sc.axes.set_xlabel("Order Date")
                self.generate_graph(x, y, kind="linear")
            else:
                obj = perioada_de_timp(self.ui.productComboBox.currentText(),
                                       self.ui.dateEdit_min.dateTime().toPyDateTime(),
                                       self.ui.dateEdit_max.dateTime().toPyDateTime())
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
        if self.ui.perioadaDeTimpRB.isChecked():
            self.ui.export_btn.hide()
            self.ui.export_button.show()

        else:
            self.ui.export_button.hide()
        if self.ui.profilulClientilorRB.isChecked():
            self.ui.export_btn.show()
            self.ui.export_button.hide()
        if self.ui.zonaDeDistributieRB.isChecked():
            self.ui.export_btn.show()
            self.ui.export_button.hide()

        if kind == "linear":
            self.sc.axes.plot(x, y)
        elif kind == "bar":
            self.sc.axes.bar(x, y)

        self.sc.draw()
        self.sc.show()


