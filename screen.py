# Hello pi
# always seem to need this

import sys
import json
import PyQt5

# This gets the Qt stuff
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui

# This is our window from QtCreator
import mainwindow_auto


# create class for our Raspberry Pi GUI
class MainWindow(QMainWindow, mainwindow_auto.Ui_MainWindow):
    def getJson(self):
        with open('data.json') as f:
            data = json.load(f)
        return data

    def setHeaders(self, data):
        tCount = len(data["track"])
        cInt = int(tCount)
        self.tblMain1.setColumnCount(4)
        #self.tblMain1.setRowCount(cInt)
        self.tblMain1.setRowCount(cInt)
        self.tblMain1.setHorizontalHeaderLabels(["Track", "Title", "Artist", "Genre"])
        self.tblMain1.setSelectionBehavior(QAbstractItemView.SelectRows)

    def setTableRows(self, data):
        i = 0
        for item in data["track"]:
            st = str(i)
            #self.tblMain1.setItem(i,0, QTableWidgetItem(st))
            self.tblMain1.setItem(i,0, QTableWidgetItem(st))

                #Manual way of changing colour of cell if needed
                #self.tblMain1.item(0,0).setBackground(QtGui.QColor(125,125,125))

            st = ', '.join(data["track"][i]["Title"])
            self.tblMain1.setItem(i,1, QTableWidgetItem(st))



            st = ', '.join(data["track"][i]["Artist"])
            self.tblMain1.setItem(i,2, QTableWidgetItem(st))



            st = ', '.join(data["track"][i]["Genre"])
            self.tblMain1.setItem(i,3, QTableWidgetItem(st))




            i = i+1



    def setFirstImage(self):
        pixmap = QPixmap('img/newPlaylist0img.png')
        self.lblImg1.setPixmap(pixmap)


    def getSelectedRow(self):
        indexes = self.tblMain1.selectionModel().selectedRows()
        for index in sorted(indexes):
            row = (index.row())
            st = str(row)
            pixmap = QPixmap('img/newPlaylist'+ st +'img.png')
            self.lblImg1.setPixmap(pixmap)



    def __init__(self):
            super(self.__class__, self).__init__()

            self.setupUi(self) # gets defined in the UI file
            data = self.getJson()
            self.tblMain1.itemSelectionChanged.connect(self.getSelectedRow)
            self.setHeaders(data)
            self.setTableRows(data)
            self.setFirstImage()
            self.getSelectedRow()


# I feel better having one of these
def main():
 # a new app instance
    app = QApplication(sys.argv)
    form = MainWindow()
    form.showFullScreen()
    form.show()
    # without this, the script exits immediately.
    sys.exit(app.exec_())

# python bit to figure how who started This
if __name__ == "__main__":
 main()
