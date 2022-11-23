# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form3.ui'
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
        self.title.setGeometry(QtCore.QRect(0, 0, 1011, 125))
        self.title.setStyleSheet("font: 87 26pt \"Segoe UI Black\";")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setWordWrap(True)
        self.title.setObjectName("title")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 320, 951, 471))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.chart_layout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.chart_layout.setContentsMargins(0, 0, 0, 0)
        self.chart_layout.setObjectName("chart_layout")
        self.profit_sau_pierdere = QtWidgets.QLabel(self.centralwidget)
        self.profit_sau_pierdere.setGeometry(QtCore.QRect(40, 40, 311, 41))
        self.profit_sau_pierdere.setStyleSheet("font: 14pt \"Nirmala UI Semilight\";")
        self.profit_sau_pierdere.setObjectName("profit_sau_pierdere")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(100, 100, 841, 211))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.title2 = QtWidgets.QLabel(self.layoutWidget)
        self.title2.setAlignment(QtCore.Qt.AlignCenter)
        self.title2.setObjectName("title2")
        self.gridLayout.addWidget(self.title2, 0, 1, 1, 1)
        self.title1 = QtWidgets.QLabel(self.layoutWidget)
        self.title1.setAlignment(QtCore.Qt.AlignCenter)
        self.title1.setObjectName("title1")
        self.gridLayout.addWidget(self.title1, 0, 0, 1, 1)
        self.clasa_de_produse_label = QtWidgets.QLabel(self.layoutWidget)
        self.clasa_de_produse_label.setStyleSheet("font: 14pt \"Nirmala UI Semilight\";")
        self.clasa_de_produse_label.setAlignment(QtCore.Qt.AlignCenter)
        self.clasa_de_produse_label.setObjectName("clasa_de_produse_label")
        self.gridLayout.addWidget(self.clasa_de_produse_label, 1, 1, 1, 1)
        self.produs_label = QtWidgets.QLabel(self.layoutWidget)
        self.produs_label.setStyleSheet("font: 14pt \"Nirmala UI Semilight\";")
        self.produs_label.setAlignment(QtCore.Qt.AlignCenter)
        self.produs_label.setObjectName("produs_label")
        self.gridLayout.addWidget(self.produs_label, 1, 0, 1, 1)
        self.ProdusCB = QtWidgets.QComboBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ProdusCB.sizePolicy().hasHeightForWidth())
        self.ProdusCB.setSizePolicy(sizePolicy)
        self.ProdusCB.setMinimumSize(QtCore.QSize(0, 0))
        self.ProdusCB.setSizeIncrement(QtCore.QSize(0, 0))
        self.ProdusCB.setStyleSheet("font: 14pt \"Nirmala UI Semilight\";")
        self.ProdusCB.setCurrentText("")
        self.ProdusCB.setMaxVisibleItems(10000)
        self.ProdusCB.setInsertPolicy(QtWidgets.QComboBox.InsertAlphabetically)
        self.ProdusCB.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.ProdusCB.setModelColumn(0)
        self.ProdusCB.setObjectName("ProdusCB")
        self.gridLayout.addWidget(self.ProdusCB, 3, 0, 1, 1)
        self.clasaProdus_CB = QtWidgets.QComboBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clasaProdus_CB.sizePolicy().hasHeightForWidth())
        self.clasaProdus_CB.setSizePolicy(sizePolicy)
        self.clasaProdus_CB.setMinimumSize(QtCore.QSize(0, 0))
        self.clasaProdus_CB.setSizeIncrement(QtCore.QSize(0, 0))
        self.clasaProdus_CB.setStyleSheet("font: 14pt \"Nirmala UI Semilight\";")
        self.clasaProdus_CB.setCurrentText("")
        self.clasaProdus_CB.setMaxVisibleItems(10000)
        self.clasaProdus_CB.setInsertPolicy(QtWidgets.QComboBox.InsertAlphabetically)
        self.clasaProdus_CB.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.clasaProdus_CB.setModelColumn(0)
        self.clasaProdus_CB.setObjectName("clasaProdus_CB")
        self.gridLayout.addWidget(self.clasaProdus_CB, 3, 1, 1, 1)
        self.produs_button = QtWidgets.QPushButton(self.layoutWidget)
        self.produs_button.setObjectName("produs_button")
        self.gridLayout.addWidget(self.produs_button, 5, 0, 1, 1)
        self.clasaPrdus_button = QtWidgets.QPushButton(self.layoutWidget)
        self.clasaPrdus_button.setObjectName("clasaPrdus_button")
        self.gridLayout.addWidget(self.clasaPrdus_button, 5, 1, 1, 1)
        self.sales_label_pr = QtWidgets.QLabel(self.layoutWidget)
        self.sales_label_pr.setStyleSheet("font: 14pt \"Nirmala UI Semilight\";")
        self.sales_label_pr.setAlignment(QtCore.Qt.AlignCenter)
        self.sales_label_pr.setObjectName("sales_label_pr")
        self.gridLayout.addWidget(self.sales_label_pr, 4, 0, 1, 1)
        self.sales_label_clpr = QtWidgets.QLabel(self.layoutWidget)
        self.sales_label_clpr.setStyleSheet("font: 14pt \"Nirmala UI Semilight\";")
        self.sales_label_clpr.setAlignment(QtCore.Qt.AlignCenter)
        self.sales_label_clpr.setObjectName("sales_label_clpr")
        self.gridLayout.addWidget(self.sales_label_clpr, 4, 1, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(670, 40, 331, 33))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget1)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.default_sales = QtWidgets.QLabel(self.layoutWidget1)
        self.default_sales.setStyleSheet("font: 14pt \"Nirmala UI Semilight\";")
        self.default_sales.setObjectName("default_sales")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.default_sales)
        self.sales = QtWidgets.QLabel(self.layoutWidget1)
        self.sales.setStyleSheet("font: 14pt \"Nirmala UI Semilight\";")
        self.sales.setObjectName("sales")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.sales)
        self.export_btn = QtWidgets.QPushButton(self.centralwidget)
        self.export_btn.setGeometry(QtCore.QRect(280, 40, 151, 41))
        self.export_btn.setObjectName("export_btn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "CAIA"))
        self.profit_sau_pierdere.setText(_translate("MainWindow", "Profit"))
        self.title2.setText(_translate("MainWindow", "Cum sunt vanzarile afectate dupa disparitia unei categorii de produse"))
        self.title1.setText(_translate("MainWindow", "Cum sunt vanzarile afectate dupa disparitia unui produs"))
        self.clasa_de_produse_label.setText(_translate("MainWindow", "Clasa de produse"))
        self.produs_label.setText(_translate("MainWindow", "Produs"))
        self.produs_button.setText(_translate("MainWindow", "Genereaza Graph"))
        self.clasaPrdus_button.setText(_translate("MainWindow", "Genereaza Graph"))
        self.sales_label_pr.setText(_translate("MainWindow", "Sales: "))
        self.sales_label_clpr.setText(_translate("MainWindow", "Sales: "))
        self.default_sales.setText(_translate("MainWindow", "Default Sales: "))
        self.sales.setText(_translate("MainWindow", "TextLabel"))
        self.export_btn.setText(_translate("MainWindow", "Export"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
