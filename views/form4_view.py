# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form4.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1011, 801)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(10, 0, 1011, 125))
        self.title.setStyleSheet("font: 87 26pt \"Segoe UI Black\";")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setWordWrap(True)
        self.title.setObjectName("title")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 230, 961, 561))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.chart_layout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.chart_layout.setContentsMargins(0, 0, 0, 0)
        self.chart_layout.setObjectName("chart_layout")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(210, 120, 601, 86))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.produs_label = QtWidgets.QLabel(self.layoutWidget)
        self.produs_label.setStyleSheet("font: 14pt \"Nirmala UI Semilight\";")
        self.produs_label.setAlignment(QtCore.Qt.AlignCenter)
        self.produs_label.setObjectName("produs_label")
        self.gridLayout.addWidget(self.produs_label, 0, 0, 1, 1)
        self.productComboBox = QtWidgets.QComboBox(self.layoutWidget)
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
        self.gridLayout.addWidget(self.productComboBox, 0, 1, 1, 1)
        self.genereazaGraph_Button = QtWidgets.QPushButton(self.layoutWidget)
        self.genereazaGraph_Button.setStyleSheet("font: 14pt \"Nirmala UI Semilight\";")
        self.genereazaGraph_Button.setObjectName("genereazaGraph_Button")
        self.gridLayout.addWidget(self.genereazaGraph_Button, 1, 1, 1, 1)
        self.export_button = QtWidgets.QPushButton(self.centralwidget)
        self.export_button.setGeometry(QtCore.QRect(700, 10, 296, 33))
        self.export_button.setStyleSheet("font: 14pt \"Nirmala UI Semilight\";")
        self.export_button.setObjectName("export_button")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CAIA"))
        self.title.setText(_translate("MainWindow", "CAIA"))
        self.produs_label.setText(_translate("MainWindow", "Seleteaza Produs"))
        self.genereazaGraph_Button.setText(_translate("MainWindow", "Genereaza Graph"))
        self.export_button.setText(_translate("MainWindow", "Export"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
