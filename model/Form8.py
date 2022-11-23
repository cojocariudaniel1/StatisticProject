import matplotlib
from PyQt5 import QtWidgets
from matplotlib import rcParams
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, \
    NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

from model.statistic_functions.form5_functions import get_subcategory
from model.statistic_functions.form8_functions import pondere_vanzari, export_pondere_vanzari
from views.form8_view import Ui_MainWindow

rcParams.update({'figure.autolayout': True})
matplotlib.use('Qt5Agg')


class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=300):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        super(MplCanvas, self).__init__(self.fig)
        self.fig.tight_layout()


class Form8(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.sc = MplCanvas(self, width=5, height=4, dpi=100)
        self.toolbar = NavigationToolbar(self.sc, self)
        self.ui.chart_layout.addWidget(self.sc)
        self.ui.chart_layout.addWidget(self.toolbar)
        self.ui.genereazaGraph_Button.clicked.connect(self.generate_graph)
        self.populate_combobox()
        self.ui.export_btn.clicked.connect(self.export)

    def populate_combobox(self):
        sub_category = get_subcategory()
        for k in sub_category:
            self.ui.subCategorieCB.addItem(str(k))

    def export(self):
        folderpath = QtWidgets.QFileDialog.getSaveFileName(self, 'Select Folder')
        export_pondere_vanzari(self.ui.subCategorieCB.currentText(), folderpath)

    def generate_graph(self):
        obj = pondere_vanzari(self.ui.subCategorieCB.currentText())
        self.sc.axes.clear()
        x1 = obj[0]
        x2 = obj[1]
        print(x1, x2)
        print(type(x1))
        print(type(x2))
        labels = obj[2]
        explode = obj[3]
        self.sc.axes.pie([x1, x2], explode=explode, labels=labels, autopct='%1.1f%%',
                         shadow=True, startangle=90)

        # self.sc.axes.tick_params(axis="x", labelrotation=90)
        self.sc.draw()
        self.show()
