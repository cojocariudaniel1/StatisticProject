# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'export.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(430, 682)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setEnabled(True)
        self.title.setGeometry(QtCore.QRect(-281, 0, 1041, 125))
        self.title.setStyleSheet("font: 87 26pt \"Segoe UI Black\";")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setWordWrap(True)
        self.title.setObjectName("title")
        self.export_button = QtWidgets.QPushButton(self.centralwidget)
        self.export_button.setEnabled(True)
        self.export_button.setGeometry(QtCore.QRect(39, 590, 341, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(47)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.export_button.sizePolicy().hasHeightForWidth())
        self.export_button.setSizePolicy(sizePolicy)
        self.export_button.setMinimumSize(QtCore.QSize(0, 9))
        self.export_button.setStyleSheet("font: 14pt \"Nirmala UI Semilight\";")
        self.export_button.setObjectName("export_button")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(119, 120, 187, 31))
        self.label_2.setStyleSheet("font: 14pt \"Nirmala UI Semilight\";")
        self.label_2.setObjectName("label_2")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 160, 319, 410))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setStyleSheet("font: 14pt \"Nirmala UI Semilight\";")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 2)
        self.forward_spin = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.forward_spin.setStyleSheet("font: 14pt \"Nirmala UI Semilight\";")
        self.forward_spin.setDecimals(1)
        self.forward_spin.setMinimum(0.1)
        self.forward_spin.setMaximum(1.0)
        self.forward_spin.setSingleStep(0.1)
        self.forward_spin.setObjectName("forward_spin")
        self.gridLayout.addWidget(self.forward_spin, 5, 2, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        self.label_11.setStyleSheet("font: 14pt \"Nirmala UI Semilight\";")
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 11, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        self.label_12.setStyleSheet("font: 14pt \"Nirmala UI Semilight\";")
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 12, 0, 1, 1)
        self.order_spin = QtWidgets.QSpinBox(self.layoutWidget)
        self.order_spin.setStyleSheet("font: 14pt \"Nirmala UI Semilight\";")
        self.order_spin.setMinimum(1)
        self.order_spin.setMaximum(5)
        self.order_spin.setObjectName("order_spin")
        self.gridLayout.addWidget(self.order_spin, 1, 2, 1, 1)
        self.line_width_spin_trendline = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.line_width_spin_trendline.setStyleSheet("font: 14pt \"Nirmala UI Semilight\";")
        self.line_width_spin_trendline.setDecimals(1)
        self.line_width_spin_trendline.setMinimum(0.1)
        self.line_width_spin_trendline.setMaximum(20.0)
        self.line_width_spin_trendline.setSingleStep(0.1)
        self.line_width_spin_trendline.setProperty("value", 1.0)
        self.line_width_spin_trendline.setObjectName("line_width_spin_trendline")
        self.gridLayout.addWidget(self.line_width_spin_trendline, 12, 1, 1, 2)
        self.rsquared_checkBox = QtWidgets.QCheckBox(self.layoutWidget)
        self.rsquared_checkBox.setText("")
        self.rsquared_checkBox.setObjectName("rsquared_checkBox")
        self.gridLayout.addWidget(self.rsquared_checkBox, 7, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setStyleSheet("font: 14pt \"Nirmala UI Semilight\";")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.polynomial_comboBox = QtWidgets.QComboBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.polynomial_comboBox.sizePolicy().hasHeightForWidth())
        self.polynomial_comboBox.setSizePolicy(sizePolicy)
        self.polynomial_comboBox.setMinimumSize(QtCore.QSize(0, 0))
        self.polynomial_comboBox.setSizeIncrement(QtCore.QSize(0, 0))
        self.polynomial_comboBox.setStyleSheet("font: 14pt \"Nirmala UI Semilight\";")
        self.polynomial_comboBox.setCurrentText("polynomial")
        self.polynomial_comboBox.setMaxVisibleItems(10000)
        self.polynomial_comboBox.setInsertPolicy(QtWidgets.QComboBox.InsertAlphabetically)
        self.polynomial_comboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.polynomial_comboBox.setModelColumn(0)
        self.polynomial_comboBox.setObjectName("polynomial_comboBox")
        self.polynomial_comboBox.addItem("")
        self.polynomial_comboBox.addItem("")
        self.polynomial_comboBox.addItem("")
        self.polynomial_comboBox.addItem("")
        self.polynomial_comboBox.addItem("")
        self.polynomial_comboBox.addItem("")
        self.gridLayout.addWidget(self.polynomial_comboBox, 0, 1, 1, 3)
        self.color_checkbox_trendline = QtWidgets.QComboBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.color_checkbox_trendline.sizePolicy().hasHeightForWidth())
        self.color_checkbox_trendline.setSizePolicy(sizePolicy)
        self.color_checkbox_trendline.setMinimumSize(QtCore.QSize(0, 0))
        self.color_checkbox_trendline.setSizeIncrement(QtCore.QSize(0, 0))
        self.color_checkbox_trendline.setStyleSheet("font: 14pt \"Nirmala UI Semilight\";")
        self.color_checkbox_trendline.setCurrentText("red")
        self.color_checkbox_trendline.setMaxVisibleItems(10000)
        self.color_checkbox_trendline.setInsertPolicy(QtWidgets.QComboBox.InsertAlphabetically)
        self.color_checkbox_trendline.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.color_checkbox_trendline.setModelColumn(0)
        self.color_checkbox_trendline.setObjectName("color_checkbox_trendline")
        self.color_checkbox_trendline.addItem("")
        self.color_checkbox_trendline.addItem("")
        self.color_checkbox_trendline.addItem("")
        self.color_checkbox_trendline.addItem("")
        self.color_checkbox_trendline.addItem("")
        self.color_checkbox_trendline.addItem("")
        self.gridLayout.addWidget(self.color_checkbox_trendline, 11, 1, 1, 2)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setStyleSheet("font: 14pt \"Nirmala UI Semilight\";")
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 9, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setStyleSheet("font: 14pt \"Nirmala UI Semilight\";")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.display_equation_checkBox = QtWidgets.QCheckBox(self.layoutWidget)
        self.display_equation_checkBox.setText("")
        self.display_equation_checkBox.setObjectName("display_equation_checkBox")
        self.gridLayout.addWidget(self.display_equation_checkBox, 8, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setStyleSheet("font: 14pt \"Nirmala UI Semilight\";")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 2)
        self.period_spin = QtWidgets.QSpinBox(self.layoutWidget)
        self.period_spin.setStyleSheet("font: 14pt \"Nirmala UI Semilight\";")
        self.period_spin.setMinimum(1)
        self.period_spin.setMaximum(5)
        self.period_spin.setObjectName("period_spin")
        self.gridLayout.addWidget(self.period_spin, 2, 2, 1, 1)
        self.backward_spin = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.backward_spin.setStyleSheet("font: 14pt \"Nirmala UI Semilight\";")
        self.backward_spin.setDecimals(1)
        self.backward_spin.setMinimum(0.1)
        self.backward_spin.setMaximum(1.0)
        self.backward_spin.setSingleStep(0.1)
        self.backward_spin.setObjectName("backward_spin")
        self.gridLayout.addWidget(self.backward_spin, 6, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setStyleSheet("font: 14pt \"Nirmala UI Semilight\";")
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 8, 0, 1, 3)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setStyleSheet("font: 14pt \"Nirmala UI Semilight\";")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setStyleSheet("font: 14pt \"Nirmala UI Semilight\";")
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 7, 0, 1, 3)
        self.name_trendline = QtWidgets.QLineEdit(self.layoutWidget)
        self.name_trendline.setStyleSheet("font: 14pt \"Nirmala UI Semilight\";")
        self.name_trendline.setObjectName("name_trendline")
        self.gridLayout.addWidget(self.name_trendline, 4, 2, 1, 2)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget)
        self.label_13.setStyleSheet("font: 14pt \"Nirmala UI Semilight\";")
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 2, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget)
        self.label_14.setStyleSheet("font: 14pt \"Nirmala UI Semilight\";")
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 3, 0, 1, 1)
        self.intercept_spin = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.intercept_spin.setStyleSheet("font: 14pt \"Nirmala UI Semilight\";")
        self.intercept_spin.setDecimals(1)
        self.intercept_spin.setMinimum(0.1)
        self.intercept_spin.setMaximum(1.0)
        self.intercept_spin.setSingleStep(0.1)
        self.intercept_spin.setObjectName("intercept_spin")
        self.gridLayout.addWidget(self.intercept_spin, 3, 2, 1, 1)
        self.trendline_check = QtWidgets.QCheckBox(self.centralwidget)
        self.trendline_check.setGeometry(QtCore.QRect(280, 130, 70, 17))
        self.trendline_check.setText("")
        self.trendline_check.setObjectName("trendline_check")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "CAIA"))
        self.export_button.setText(_translate("MainWindow", "Export"))
        self.label_2.setText(_translate("MainWindow", "Trend Line Settings"))
        self.label_6.setToolTip(_translate("MainWindow", "The forward and backward properties set the forecast period of the trendline"))
        self.label_6.setText(_translate("MainWindow", "Forward: "))
        self.label_11.setText(_translate("MainWindow", "Color:"))
        self.label_12.setText(_translate("MainWindow", "width"))
        self.label_3.setText(_translate("MainWindow", "Type: "))
        self.polynomial_comboBox.setItemText(0, _translate("MainWindow", "polynomial"))
        self.polynomial_comboBox.setItemText(1, _translate("MainWindow", "linear"))
        self.polynomial_comboBox.setItemText(2, _translate("MainWindow", "exponential"))
        self.polynomial_comboBox.setItemText(3, _translate("MainWindow", "log"))
        self.polynomial_comboBox.setItemText(4, _translate("MainWindow", "moving_average"))
        self.polynomial_comboBox.setItemText(5, _translate("MainWindow", "power"))
        self.color_checkbox_trendline.setItemText(0, _translate("MainWindow", "red"))
        self.color_checkbox_trendline.setItemText(1, _translate("MainWindow", "green"))
        self.color_checkbox_trendline.setItemText(2, _translate("MainWindow", "blue"))
        self.color_checkbox_trendline.setItemText(3, _translate("MainWindow", "yellow"))
        self.color_checkbox_trendline.setItemText(4, _translate("MainWindow", "black"))
        self.color_checkbox_trendline.setItemText(5, _translate("MainWindow", "orange"))
        self.label_10.setText(_translate("MainWindow", "Line:"))
        self.label_5.setText(_translate("MainWindow", "Order:"))
        self.label_7.setText(_translate("MainWindow", "Backward:"))
        self.label_9.setToolTip(_translate("MainWindow", "The display_equation property displays the trendline equation on the chart"))
        self.label_9.setText(_translate("MainWindow", "Display equation: "))
        self.label_4.setText(_translate("MainWindow", "Name:"))
        self.label_8.setToolTip(_translate("MainWindow", "The display_r_squared property displays the R squared value of the trendline on the chart"))
        self.label_8.setText(_translate("MainWindow", "Display R squared: "))
        self.label_13.setText(_translate("MainWindow", "Period:"))
        self.label_14.setText(_translate("MainWindow", "Intercept:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
