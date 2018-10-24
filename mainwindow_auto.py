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
        MainWindow.resize(800, 470)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.tblMain1 = QtWidgets.QTableWidget(self.centralWidget)
        self.tblMain1.setGeometry(QtCore.QRect(0, 0, 800, 260))
        self.tblMain1.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblMain1.setTabKeyNavigation(False)
        self.tblMain1.setProperty("showDropIndicator", False)
        self.tblMain1.setDragDropOverwriteMode(False)
        self.tblMain1.setObjectName("tblMain1")
        self.tblMain1.setColumnCount(0)
        self.tblMain1.setRowCount(0)
        self.lblImg1 = QtWidgets.QLabel(self.centralWidget)
        self.lblImg1.setGeometry(QtCore.QRect(0, 260, 800, 150))
        self.lblImg1.setText("")
        self.lblImg1.setObjectName("lblImg1")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

