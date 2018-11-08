# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.tblMain1 = QtWidgets.QTableWidget(self.centralWidget)
        self.tblMain1.setGeometry(QtCore.QRect(0, 29, 800, 361))
        self.tblMain1.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblMain1.setTabKeyNavigation(False)
        self.tblMain1.setProperty("showDropIndicator", False)
        self.tblMain1.setDragDropOverwriteMode(False)
        self.tblMain1.setObjectName("tblMain1")
        self.tblMain1.setColumnCount(0)
        self.tblMain1.setRowCount(0)
        self.lblImg1 = QtWidgets.QLabel(self.centralWidget)
        self.lblImg1.setGeometry(QtCore.QRect(137, 390, 660, 90))
        self.lblImg1.setText("")
        self.lblImg1.setObjectName("lblImg1")
        self.scrollUpBtn = QtWidgets.QPushButton(self.centralWidget)
        self.scrollUpBtn.setGeometry(QtCore.QRect(0, 390, 71, 91))
        self.scrollUpBtn.setObjectName("scrollUpBtn")
        self.scrollDownBtn = QtWidgets.QPushButton(self.centralWidget)
        self.scrollDownBtn.setGeometry(QtCore.QRect(60, 390, 71, 91))
        self.scrollDownBtn.setObjectName("scrollDownBtn")
        self.selectBtn = QtWidgets.QPushButton(self.centralWidget)
        self.selectBtn.setGeometry(QtCore.QRect(670, 0, 131, 31))
        self.selectBtn.setObjectName("selectBtn")
        self.backBtn = QtWidgets.QPushButton(self.centralWidget)
        self.backBtn.setGeometry(QtCore.QRect(560, 0, 114, 32))
        self.backBtn.setObjectName("backBtn")
        self.titleLbl = QtWidgets.QLabel(self.centralWidget)
        self.titleLbl.setGeometry(QtCore.QRect(10, 8, 491, 16))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.titleLbl.setFont(font)
        self.titleLbl.setObjectName("titleLbl")
        MainWindow.setCentralWidget(self.centralWidget)
        self.actionImport = QtWidgets.QAction(MainWindow)
        self.actionImport.setObjectName("actionImport")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.scrollUpBtn.setText(_translate("MainWindow", "▲"))
        self.scrollDownBtn.setText(_translate("MainWindow", "▼"))
        self.selectBtn.setText(_translate("MainWindow", "Select"))
        self.backBtn.setText(_translate("MainWindow", "↩"))
        self.titleLbl.setText(_translate("MainWindow", "House And Deep Oct 18"))
        self.actionImport.setText(_translate("MainWindow", "Import"))

