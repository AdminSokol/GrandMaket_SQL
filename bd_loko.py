from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sqlite3
import binascii
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog, QApplication, QLabel, QMainWindow, QGraphicsPixmapItem, QGraphicsItem
from functools import partial

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(1449, 798)
        self.tableWidget_10 = QtWidgets.QTableWidget(MainWindow)
        self.tableWidget_10.setGeometry(QtCore.QRect(20, 70, 1311, 551))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_10.sizePolicy().hasHeightForWidth())
        self.tableWidget_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget_10.setFont(font)
        self.tableWidget_10.setToolTip("")
        self.tableWidget_10.setStatusTip("")
        self.tableWidget_10.setStyleSheet("QTableWidget {\n"
"border-radius: 15px;\n"
"background-color: rgb(72, 73, 74)}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: rgb(255, 255, 255);\n"
"    padding: 4px;\n"
"    font-size: 11pt;\n"
"    font-family: Times New Roman;\n"
"    border-bottom: 1px solid rgb(0, 0, 0);\n"
"    border-right: 1px solid rgb(0, 0, 0);\n"
"}\n"
"\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border-top: 1px solid rgb(0, 0, 0);\n"
"}\n"
"\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border-left: 1px solid rgb(0, 0, 0);\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QTableWidget::item:selected {\n"
"    background-color: rgb(170, 255, 255);\n"
"    color:rgb(0, 0, 0);\n"
"}")
        self.tableWidget_10.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget_10.setAutoScroll(True)
        self.tableWidget_10.setProperty("showDropIndicator", True)
        self.tableWidget_10.setDragDropOverwriteMode(True)
        self.tableWidget_10.setAlternatingRowColors(False)
        self.tableWidget_10.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tableWidget_10.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tableWidget_10.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget_10.setShowGrid(True)
        self.tableWidget_10.setWordWrap(True)
        self.tableWidget_10.setObjectName("tableWidget_10")
        self.tableWidget_10.setColumnCount(6)
        self.tableWidget_10.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_10.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_10.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_10.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_10.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_10.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_10.setHorizontalHeaderItem(5, item)
        self.tableWidget_10.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_10.horizontalHeader().setDefaultSectionSize(161)
        self.tableWidget_10.horizontalHeader().setHighlightSections(False)
        self.tableWidget_10.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_10.verticalHeader().setVisible(False)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
