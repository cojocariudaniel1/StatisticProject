import matplotlib
from PyQt5 import QtWidgets
from matplotlib import rcParams
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, \
    NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

from model.Export import Export
from model.statistic_functions.form3_functions import get_category
from model.statistic_functions.form7_functions import profit_pe_an
from views.form7_view import Ui_MainWindow

rcParams.update({'figure.autolayout': True})
matplotlib.use('Qt5Agg')


class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=300):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        super(MplCanvas, self).__init__(self.fig)
        self.fig.tight_layout()


class Form7(QtWidgets.QMainWindow):
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
        self.ui.export_button.clicked.connect(self.export)

    def populate_combobox(self):
        product_category = get_category()
        for k in product_category:
            self.ui.categorieProdusCB.addItem(str(k))

    def generate_graph(self):
        obj = profit_pe_an(self.ui.categorieProdusCB.currentText())
        self.sc.axes.clear()
        x = obj[0]
        y = obj[1]
        self.sc.axes.plot(x, y)
        # self.sc.axes.tick_params(axis="x", labelrotation=90)
        self.sc.draw()
        self.show()

    def export(self):
        self.new_window = Export("Form7", self.ui.categorieProdusCB.currentText())
        self.new_window.show()
