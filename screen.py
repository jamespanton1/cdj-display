# Hello pi
# always seem to need this

import sys
import json
import PyQt5
import os

# This gets the Qt stuff
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui


# This is our window from QtCreator
import mainwindow_auto
import playlistwindow_auto



class MainWindow(QMainWindow, mainwindow_auto.Ui_MainWindow):

    def getPlaylistNames(self):
        playlistTitles = []
        for entry in os.scandir("playlists"):
            title = (entry.path)
            splitTitle = title.rsplit('/', 1)[1]
            splitTitleSt = str(splitTitle)
            if splitTitleSt != ".DS_Store":
                playlistTitles.append(splitTitleSt)
        return playlistTitles

    def getJson(self, folder):
        with open('playlists/' + folder + '/data.json') as f:
            data = json.load(f)
        return data

    def clearTable(self):
        self.tblMain1.setRowCount(0)
        self.tblMain1.setColumnCount(0)

    def setHeaders(self, data):
        tCount = len(data["track"])
        cInt = int(tCount)
        self.tblMain1.setColumnCount(4)
        #self.tblMain1.setRowCount(cInt)
        self.tblMain1.setRowCount(cInt)
        self.tblMain1.setHorizontalHeaderLabels(["Track", "Title", "Artist", "Genre"])
        self.tblMain1.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tblMain1.setColumnWidth(0, 40)
        self.tblMain1.setColumnWidth(1, 360)
        self.tblMain1.setColumnWidth(2, 240)
        self.tblMain1.setColumnWidth(3, 135)

    def setFolderHeaders(self, data):
        tCount = len(data)
        cInt = int(tCount)
        self.tblMain1.setColumnCount(1)
        self.tblMain1.setHorizontalHeaderLabels(["Playlist"])
        self.tblMain1.setColumnWidth(0, 500)
        self.tblMain1.setRowCount(cInt)


    def setTableRows(self, data):
        i = 0
        for item in data["track"]:
            i1 = i+1
            st = str(i1)
            #self.tblMain1.setItem(i,0, QTableWidgetItem(st))
            self.tblMain1.setItem(i,0, QTableWidgetItem(st))

                #Manual way of changing colour of cell if needed
                #self.tblMain1.item(0,0).setBackground(QtGui.QColor(125,125,125))

            st = (data["track"][i]["Title"])
            self.tblMain1.setItem(i,1, QTableWidgetItem(st))



            st = (data["track"][i]["Artist"])
            self.tblMain1.setItem(i,2, QTableWidgetItem(st))



            st = (data["track"][i]["Genre"])
            self.tblMain1.setItem(i,3, QTableWidgetItem(st))




            i = i+1

    def setFolderTableRows(self, data):
        i=0
        for item in data:
            self.tblMain1.setItem(i,0, QTableWidgetItem(item))
            i = i+1

    def setFirstImage(self):
        pixmap = QPixmap('img/newPlaylist0img.png')
        self.lblImg1.setPixmap(pixmap)

    def getFolder(self, folder):
        indexes = self.tblMain1.selectionModel().selectedRows()
        for index in sorted(indexes):
            row = (index.row())
            playlist = folder[row]
            return playlist


    def getSelectedRow(self, folder):
        indexes = self.tblMain1.selectionModel().selectedRows()
        for index in sorted(indexes):
            row = (index.row())
            st = str(row)
            pixmap = QPixmap('playlists/' + folder + '/img/newPlaylist'+ st +'img.png')
            self.lblImg1.setPixmap(pixmap)
            self.lblImg1.repaint()

    def showFolders(self):
        global treeDepth
        treeDepth = "folder"
        self.clearTable()
        titles = self.getPlaylistNames()
        self.setFolderHeaders(titles)
        self.setFolderTableRows(titles)

    def select(self):
        print (treeDepth)
        global folder
        if treeDepth == "folder":
            titles = self.getPlaylistNames()
            folder = self.getFolder(titles)
            self.showPlaylist()

        if treeDepth == "playlist":
            print (folder)
            self.getSelectedRow(folder)


    def showPlaylist(self):
            global treeDepth
            treeDepth = "playlist"

            self.clearTable()
            data = self.getJson(folder)
            #self.tblMain1.itemSelectionChanged.connect(lambda: self.getSelectedRow(folder))
            self.setHeaders(data)
            self.setTableRows(data)
            #self.setFirstImage()
            #self.getSelectedRow(folder)
            treeDepth = ("playlist")


    def __init__(self):
            super(self.__class__, self).__init__()
            self.setupUi(self) # gets defined in the UI file
            self.showFolders()
            #Wait for button click
            self.selectBtn.clicked.connect(lambda: self.select())
            self.backBtn.clicked.connect(lambda: self.showFolders())



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
