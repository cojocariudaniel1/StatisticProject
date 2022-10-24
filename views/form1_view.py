# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form1.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1026, 845)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 340, 971, 491))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.chart_layout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.chart_layout.setContentsMargins(0, 0, 0, 0)
        self.chart_layout.setObjectName("chart_layout")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(130, -10, 781, 125))
        self.title.setStyleSheet("font: 87 26pt \"Segoe UI Black\";")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setWordWrap(True)
        self.title.setObjectName("title")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 90, 981, 229))
        self.widget.setObjectName("widget")
        self.main_grid = QtWidgets.QGridLayout(self.widget)
        self.main_grid.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.main_grid.setContentsMargins(0, 0, 0, 0)
        self.main_grid.setObjectName("main_grid")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.profilulClientilorRB = QtWidgets.QRadioButton(self.widget)
        self.profilulClientilorRB.setStyleSheet("font: 14pt \"Nirmala UI Semilight\";")
        self.profilulClientilorRB.setObjectName("profilulClientilorRB")
        self.gridLayout.addWidget(self.profilulClientilorRB, 0, 0, 1, 1)
        self.perioadaDeTimpRB = QtWidgets.QRadioButton(self.widget)
        self.perioadaDeTimpRB.setStyleSheet("font: 14pt \"Nirmala UI Semilight\";")
        self.perioadaDeTimpRB.setObjectName("perioadaDeTimpRB")
        self.gridLayout.addWidget(self.perioadaDeTimpRB, 1, 0, 1, 1)
        self.zonaDeDistributieRB = QtWidgets.QRadioButton(self.widget)
        self.zonaDeDistributieRB.setStyleSheet("font: 14pt \"Nirmala UI Semilight\";")
        self.zonaDeDistributieRB.setObjectName("zonaDeDistributieRB")
        self.gridLayout.addWidget(self.zonaDeDistributieRB, 2, 0, 1, 1)
        self.main_grid.addLayout(self.gridLayout, 0, 1, 1, 1)
        self.button_layout = QtWidgets.QGridLayout()
        self.button_layout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.button_layout.setContentsMargins(0, -1, 120, -1)
        self.button_layout.setHorizontalSpacing(7)
        self.button_layout.setObjectName("button_layout")
        self.productComboBox = QtWidgets.QComboBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.productComboBox.sizePolicy().hasHeightForWidth())
        self.productComboBox.setSizePolicy(sizePolicy)
        self.productComboBox.setMinimumSize(QtCore.QSize(0, 0))
        self.productComboBox.setSizeIncrement(QtCore.QSize(0, 0))
        self.productComboBox.setStyleSheet("font: 14pt \"Nirmala UI Semilight\";")
        self.productComboBox.setCurrentText("")
        self.productComboBox.setMaxVisibleItems(10000)
        self.productComboBox.setInsertPolicy(QtWidgets.QComboBox.InsertAlphabetically)
        self.productComboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.productComboBox.setModelColumn(0)
        self.productComboBox.setObjectName("productComboBox")
        self.button_layout.addWidget(self.productComboBox, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setStyleSheet("font: 14pt \"Nirmala UI Semilight\";")
        self.label_2.setObjectName("label_2")
        self.button_layout.addWidget(self.label_2, 0, 0, 1, 1)
        self.main_grid.addLayout(self.button_layout, 0, 0, 1, 1)
        self.genereazaChartButton = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.genereazaChartButton.sizePolicy().hasHeightForWidth())
        self.genereazaChartButton.setSizePolicy(sizePolicy)
        self.genereazaChartButton.setMinimumSize(QtCore.QSize(0, 50))
        self.genereazaChartButton.setStyleSheet("font: 14pt \"Nirmala UI Semilight\";")
        self.genereazaChartButton.setObjectName("genereazaChartButton")
        self.main_grid.addWidget(self.genereazaChartButton, 1, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CAIA"))
        self.title.setText(_translate("MainWindow", "CAIA"))
        self.profilulClientilorRB.setText(_translate("MainWindow", "Profilul clienților"))
        self.perioadaDeTimpRB.setText(_translate("MainWindow", "Perioada de timp"))
        self.zonaDeDistributieRB.setText(_translate("MainWindow", "Zona de distribuție"))
        self.label_2.setText(_translate("MainWindow", "Selectaza Produs"))
        self.genereazaChartButton.setText(_translate("MainWindow", "Genereaza Chart"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
