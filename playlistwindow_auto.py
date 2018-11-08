# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'playlistwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PlaylistWindow(object):
    def setupUi(self, PlaylistWindow):
        PlaylistWindow.setObjectName("PlaylistWindow")
        PlaylistWindow.resize(800, 480)
        self.centralWidget = QtWidgets.QWidget(PlaylistWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.playlistTable = QtWidgets.QTableWidget(self.centralWidget)
        self.playlistTable.setGeometry(QtCore.QRect(250, 0, 551, 481))
        self.playlistTable.setObjectName("playlistTable")
        self.playlistTable.setColumnCount(0)
        self.playlistTable.setRowCount(0)
        self.goButton = QtWidgets.QPushButton(self.centralWidget)
        self.goButton.setGeometry(QtCore.QRect(0, 320, 251, 161))
        self.goButton.setObjectName("goButton")
        self.syncButton = QtWidgets.QPushButton(self.centralWidget)
        self.syncButton.setGeometry(QtCore.QRect(0, 140, 251, 181))
        self.syncButton.setObjectName("syncButton")
        PlaylistWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(PlaylistWindow)
        QtCore.QMetaObject.connectSlotsByName(PlaylistWindow)

    def retranslateUi(self, PlaylistWindow):
        _translate = QtCore.QCoreApplication.translate
        PlaylistWindow.setWindowTitle(_translate("PlaylistWindow", "PlaylistWindow"))
        self.goButton.setText(_translate("PlaylistWindow", "Go"))
        self.syncButton.setText(_translate("PlaylistWindow", "Sync"))

