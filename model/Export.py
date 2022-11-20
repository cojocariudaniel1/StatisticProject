import logging

from PyQt5 import QtWidgets

from model.statistic_functions.form1_functions import export_to_excel as form1_export, perioada_de_timp
from model.statistic_functions.form4_functions import export_to_excel as form4_export, evolutia_dis_vanz
from model.statistic_functions.form5_functions import evcmppc, export_to_excel as form5_export
from model.statistic_functions.form6_functions import top_5_produse_pe_subcategorie, export_to_excel as form6_export
from model.statistic_functions.form7_functions import profit_pe_an, export_to_excel as form7_export
from views.export import Ui_MainWindow


class Export(QtWidgets.QMainWindow):
    def __init__(self, form_name, data, attrs=None):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.form_name = form_name
        self.data = data
        self.check_type_trendline()
        self.attrs = attrs

        self.ui.export_button.clicked.connect(self.export_to_file)
        try:
            self.ui.polynomial_comboBox.activated.connect(self.check_type_trendline)
        except BaseException as e:
            logging.exception(e)

        self.ui.trendline_check.clicked.connect(self.check_trendline)
        self.check_trendline()

    def check_trendline(self):
        if self.ui.trendline_check.isChecked():
            self.ui.order_spin.setEnabled(True)
            self.ui.intercept_spin.setEnabled(True)
            self.ui.rsquared_checkBox.setEnabled(True)
            self.ui.backward_spin.setEnabled(True)
            self.ui.forward_spin.setEnabled(True)
            self.ui.polynomial_comboBox.setEnabled(True)
            self.ui.display_equation_checkBox.setEnabled(True)
            self.ui.period_spin.setEnabled(True)
            self.ui.name_trendline.setEnabled(True)
            self.ui.color_checkbox_trendline.setEnabled(True)
            self.ui.line_width_spin_trendline.setEnabled(True)
        else:
            self.ui.order_spin.setEnabled(False)
            self.ui.intercept_spin.setEnabled(False)
            self.ui.rsquared_checkBox.setEnabled(False)
            self.ui.backward_spin.setEnabled(False)
            self.ui.forward_spin.setEnabled(False)
            self.ui.polynomial_comboBox.setEnabled(False)
            self.ui.display_equation_checkBox.setEnabled(False)
            self.ui.period_spin.setEnabled(False)
            self.ui.name_trendline.setEnabled(False)
            self.ui.color_checkbox_trendline.setEnabled(False)
            self.ui.line_width_spin_trendline.setEnabled(False)

    def check_type_trendline(self):

        polynom = self.ui.polynomial_comboBox.currentText()

        if polynom == "polynomial":
            self.ui.order_spin.setEnabled(True)
            self.ui.intercept_spin.setEnabled(True)
            self.ui.display_equation_checkBox.setEnabled(True)
            self.ui.rsquared_checkBox.setEnabled(True)
            self.ui.forward_spin.setEnabled(True)
            self.ui.backward_spin.setEnabled(True)
        else:
            self.ui.order_spin.setEnabled(False)
        if polynom == "moving_average":
            self.ui.intercept_spin.setEnabled(False)
            self.ui.period_spin.setEnabled(True)
            self.ui.forward_spin.setEnabled(False)
            self.ui.backward_spin.setEnabled(False)
            self.ui.display_equation_checkBox.setEnabled(False)
            self.ui.rsquared_checkBox.setEnabled(False)
        else:
            self.ui.period_spin.setEnabled(False)

        if polynom == "exponential":
            self.ui.intercept_spin.setEnabled(True)
            self.ui.forward_spin.setEnabled(True)
            self.ui.backward_spin.setEnabled(True)

        if polynom == "linear":
            self.ui.intercept_spin.setEnabled(True)

        print(self.ui.polynomial_comboBox.currentText())

    def export_to_file(self):
        if self.ui.display_equation_checkBox.checkState() == 0:
            equation = False
        else:
            equation = True

        if self.ui.rsquared_checkBox.checkState() == 0:
            rsquared = False
        else:
            rsquared = True

        trend_line_attrs = {
            "type": self.ui.polynomial_comboBox.currentText(),
            "order": self.ui.order_spin.value(),
            "period": self.ui.period_spin.value(),
            "intercept": self.ui.intercept_spin.value(),
            "name": self.ui.name_trendline.text(),
            "forward": self.ui.forward_spin.value(),
            "backward": self.ui.backward_spin.value(),
            "r_square": rsquared,
            "equation": equation,
            "line_color": self.ui.color_checkbox_trendline.currentText(),
            "line_width": self.ui.line_width_spin_trendline.value()
        }
        try:
            if self.form_name == "Form4":
                folderpath = QtWidgets.QFileDialog.getSaveFileName(self, 'Select Folder')
                obj = evolutia_dis_vanz(self.data)
                if self.ui.trendline_check.isChecked():
                    if obj and folderpath:
                        form4_export(obj, folderpath, trend_line_attrs)
                else:
                    form4_export(obj, folderpath, trend_line_attrs=None)
            elif self.form_name == "Form1":
                folderpath = QtWidgets.QFileDialog.getSaveFileName(self, 'Select Folder')
                obj = perioada_de_timp(self.data)
                if self.ui.trendline_check.isChecked():
                    if obj and folderpath:
                        form1_export(obj, folderpath, trend_line_attrs)
                else:
                    form1_export(obj, folderpath, trend_line_attrs=None)

            elif self.form_name == "Form5":
                folderpath = QtWidgets.QFileDialog.getSaveFileName(self, 'Select Folder')
                obj = evcmppc(self.data, self.attrs)
                if self.ui.trendline_check.isChecked():
                    if obj and folderpath:
                        form5_export(obj, folderpath, trend_line_attrs)
                else:
                    form5_export(obj, folderpath, trend_line_attrs=None)
            elif self.form_name == "Form6":
                folderpath = QtWidgets.QFileDialog.getSaveFileName(self, 'Select Folder')
                obj = top_5_produse_pe_subcategorie(self.data)
                if self.ui.trendline_check.isChecked():
                    if obj and folderpath:
                        form6_export(obj, folderpath, trend_line_attrs)
                else:
                    form6_export(obj, folderpath, trend_line_attrs=None)
            elif self.form_name == "Form7":
                folderpath = QtWidgets.QFileDialog.getSaveFileName(self, 'Select Folder')
                obj = profit_pe_an(self.data)
                if self.ui.trendline_check.isChecked():
                    if obj and folderpath:
                        form7_export(obj, folderpath, trend_line_attrs)
                else:
                    form7_export(obj, folderpath, trend_line_attrs=None)
        except BaseException as e:
            logging.exception(e)