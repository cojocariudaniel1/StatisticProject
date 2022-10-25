import matplotlib

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, \
    NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from PyQt5 import QtWidgets

from model.statistic_functions.form2_functions import frecventa_categoriilor, distributia_sub_categoiilor, \
    total_sales_by_subCategory
from views.form2_view import Ui_MainWindow
from matplotlib import rcParams

rcParams.update({'figure.autolayout': True})
matplotlib.use('Qt5Agg')


class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=300):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        super(MplCanvas, self).__init__(self.fig)
        self.fig.tight_layout()


class Form2(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.sc = MplCanvas(self, width=5, height=4, dpi=100)
        self.toolbar = NavigationToolbar(self.sc, self)
        self.ui.chart_layout.addWidget(self.sc)
        self.ui.chart_layout.addWidget(self.toolbar)

        self.ui.genereazaGraphButton.clicked.connect(self.check_radio_buttons)

    def check_radio_buttons(self):
        if self.ui.distributiasubCategoriilorRB.isChecked():
            try:
                obj = distributia_sub_categoiilor()
                index = obj[0]
                sub_category = obj[1]
                df = obj[2]
                print(index)
                print(sub_category)
                for i in sub_category:
                    self.sc.axes.bar(index, df[f"{i}"])

                self.sc.draw()
                self.sc.show()
            except Exception as e:
                print(e)

        elif self.ui.frecventaCategoriilorRB.isChecked():
            obj = frecventa_categoriilor()
            y, x1, x2, x3 = obj[0], obj[1], obj[2], obj[3]
            try:
                self.sc.axes.barh(y, x1)
                self.sc.axes.barh(y, x2)
                self.sc.axes.barh(y, x3)
                # self.sc.axes.tick_params(axis="x", labelrotation=90)
                self.sc.axes.legend(["Furniture", "Office Supplies", "Technology"])
                self.sc.draw()
                self.sc.show()
            except Exception as e:
                print(e)

        elif self.ui.totalulProfVanzPeSubCategorieRB.isChecked():
            obj = total_sales_by_subCategory()
            index = obj[0]
            sales = obj[1]
            profit = obj[2]

            self.sc.axes.bar(index, sales)
            self.sc.axes.bar(index, profit)
            self.sc.axes.legend(["Sales", "Profit"])
            self.sc.axes.tick_params(axis="x", labelrotation=90)
            self.sc.draw()
            self.sc.show()
