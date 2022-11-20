import matplotlib
from PyQt5 import QtWidgets
from matplotlib import rcParams
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, \
    NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

from model.statistic_functions.form5_functions import get_subcategory
from model.statistic_functions.form6_functions import top_5_produse_pe_subcategorie
from views.form6_view import Ui_MainWindow

rcParams.update({'figure.autolayout': True})
matplotlib.use('Qt5Agg')


class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=300):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        super(MplCanvas, self).__init__(self.fig)
        self.fig.tight_layout()


class Form6(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.sc = MplCanvas(self, width=5, height=4, dpi=100)
        self.toolbar = NavigationToolbar(self.sc, self)
        self.ui.chart_layout.addWidget(self.sc)
        self.ui.chart_layout.addWidget(self.toolbar)
        self.ui.genereazaGraph_Button.clicked.connect(self.generate_graph)
        self.get_subcategory()

    def get_subcategory(self):
        subcategory = get_subcategory()
        for j in subcategory:
            self.ui.subCategory_CB.addItem(str(j))

    def generate_graph(self):
        obj = top_5_produse_pe_subcategorie(self.ui.subCategory_CB.currentText())
        self.sc.axes.clear()
        x = obj[0]
        y = obj[1]
        self.sc.axes.plot(x, y)
        self.sc.axes.tick_params(axis="x", labelrotation=90)
        self.sc.draw()
        self.show()
