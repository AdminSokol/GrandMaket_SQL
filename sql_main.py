import datetime
import os
import time

import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import QPoint, Qt, QByteArray
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QDialog, QAbstractItemView, QTableWidgetItem, QTableWidget
import sqlite3

from loko import Ui_Forms
from plus_del import Plus_del
from stock_miscellaneous import Stock

sqlite_connection_02 = sqlite3.connect("setting.db")
cursor_02 = sqlite_connection_02.cursor()
sqlite_connection_01 = sqlite3.connect("id.db")
cursor_01 = sqlite_connection_01.cursor()
today = datetime.datetime.today()


class Test1(QtWidgets.QTableWidget):
    def __init__(self, parent=None):
        QtWidgets.QTableWidget.__init__(self, parent)  ##Test

    def mousePressEvent(self, e):
        it = self.itemAt(e.pos())
        try:
            if e.button() == Qt.RightButton:
                if it.column() == 0:
                    fuck = QtWidgets.QMenu(self)
                    fuck.setGeometry(QtCore.QRect(20, 20, 20, 20))
                    low = fuck.addAction("Удалить строчку")
                    action = fuck.exec_(self.mapToGlobal(e.pos()))
                    if action == low:
                        rama = it.tableWidget()
                        sqlite_connection = sqlite3.connect("loko_and_poezd.db")
                        cursor = sqlite_connection.cursor()
                        iter = it.text()
                        cursor.execute(f"""DELETE FROM lokotrain1 WHERE ID='{iter}'""")
                        sqlite_connection.commit()
                        rama.setRowCount(0)
                        users = cursor.execute("SELECT * FROM lokotrain1")
                        for row_number, order in enumerate(users):
                            rama.insertRow(row_number)
                            for column_number, data in enumerate(order):
                                item = QtWidgets.QTableWidgetItem(str(data))
                                item.setTextAlignment(Qt.AlignCenter)
                                if (column_number == 1):
                                    pix = Ui_MainWindow().getImageLabel(data)
                                    rama.setCellWidget(row_number, column_number, pix)
                                else:
                                    rama.setItem(row_number, column_number, item)
                if it.column() == 2:
                    iter = it.text()
                    Form = QtWidgets.QDialog(self)
                    form = Ui_Forms()
                    form.setupUi(Form)
                    Form.setWindowFlags(Form.windowFlags() |
                                       QtCore.Qt.WindowMinimizeButtonHint |
                                       QtCore.Qt.WindowSystemMenuHint)
                    Form.show()
                    sqlite_connection = sqlite3.connect("id.db")
                    cursor = sqlite_connection.cursor()
                    def all():
                        global row_number001
                        form.tableWidget.setRowCount(0)
                        users = cursor.execute(
                            f"""SELECT ID,datas,repair,redukt,master,userid,hours FROM TO1 WHERE loko='{iter}' ORDER BY DATE('%d.%m.%Y')""")
                        for row_number001, order in enumerate(users):
                            form.tableWidget.insertRow(row_number001)
                            for column_number, data in enumerate(order):
                                cell = QtWidgets.QTableWidgetItem(str(data))
                                form.tableWidget.setItem(row_number001, column_number, cell)
                                cell.setTextAlignment(Qt.AlignCenter)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(0,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(1,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(2,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(3,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(4,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(5,
                                                                                         QtWidgets.QHeaderView.Stretch)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(6,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                            form.tableWidget.selectRow(row_number001)
                            pool = int(row_number001 + 1)
                            form.label_kol.setText(f"Количество записей: {str(pool)}")
                        form.tableWidget.clearSelection()
                    def plan():
                        form.tableWidget.setRowCount(0)
                        users = cursor.execute(
                            f"""SELECT ID,datas,repair,redukt,master,userid,hours FROM TO1 WHERE loko='{iter}' AND repair='План' ORDER BY DATE('%d.%m.%Y')""")
                        for row_number001, order in enumerate(users):
                            form.tableWidget.insertRow(row_number001)
                            for column_number, data in enumerate(order):
                                cell = QtWidgets.QTableWidgetItem(str(data))
                                form.tableWidget.setItem(row_number001, column_number, cell)
                                cell.setTextAlignment(Qt.AlignCenter)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(0,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(1,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(2,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(3,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(4,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(5,
                                                                                         QtWidgets.QHeaderView.Stretch)
                            form.tableWidget.selectRow(row_number001)
                            pool = int(row_number001 + 1)
                            form.label_kol.setText(f"Количество записей: {str(pool)}")
                        form.tableWidget.clearSelection()
                    def vneplan():
                        form.tableWidget.setRowCount(0)
                        users = cursor.execute(
                            f"""SELECT ID,datas,repair,redukt,master,userid,hours FROM TO1 WHERE loko='{iter}' AND repair='Внеплан' ORDER BY DATE('%d.%m.%Y')""")
                        for row_number001, order in enumerate(users):
                            form.tableWidget.insertRow(row_number001)
                            for column_number, data in enumerate(order):
                                cell = QtWidgets.QTableWidgetItem(str(data))
                                form.tableWidget.setItem(row_number001, column_number, cell)
                                cell.setTextAlignment(Qt.AlignCenter)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(0,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(1,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(2,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(3,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(4,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(5,
                                                                                         QtWidgets.QHeaderView.Stretch)
                            form.tableWidget.selectRow(row_number001)
                            pool = int(row_number001 + 1)
                            form.label_kol.setText(f"Количество записей: {str(pool)}")
                        form.tableWidget.clearSelection()
                    def repair():
                        form.tableWidget.setRowCount(0)
                        users = cursor.execute(
                            f"""SELECT ID,datas,repair,redukt,master,userid,hours FROM TO1 WHERE loko='{iter}' AND repair='Ремонт' ORDER BY DATE('%d.%m.%Y')""")
                        for row_number001, order in enumerate(users):
                            form.tableWidget.insertRow(row_number001)
                            for column_number, data in enumerate(order):
                                cell = QtWidgets.QTableWidgetItem(str(data))
                                form.tableWidget.setItem(row_number001, column_number, cell)
                                cell.setTextAlignment(Qt.AlignCenter)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(0,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(1,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(2,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(3,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(4,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(5,
                                                                                         QtWidgets.QHeaderView.Stretch)
                            form.tableWidget.selectRow(row_number001)
                            pool = int(row_number001 + 1)
                            form.label_kol.setText(f"Количество записей: {str(pool)}")
                        form.tableWidget.clearSelection()
                    all()
                    form.pushButton.clicked.connect(all)
                    form.pushButton_2.clicked.connect(plan)
                    form.pushButton_3.clicked.connect(vneplan)
                    form.pushButton_4.clicked.connect(repair)
                    form.lineEdit.setText(str(iter))
                    hour = cursor.execute(
                        f"""SELECT SUM(hours) FROM TO1 WHERE loko='{iter}'""")
                    intel = hour.fetchall()
                    rom = int()
                    for number in range(len(intel)):
                        try:
                            a = int(intel[number][0])
                            rom += a
                        except:
                            pass
                    form.lineEdit_2.setText(str(rom))
                    def plus():
                        form.tableWidget.setRowCount(0)
                        cursor.execute(f"""INSERT INTO TO1 VALUES (NULL,'{iter}','','','','','','')""")
                        sqlite_connection.commit()
                        all()
                    def minus():
                        form.tableWidget.setRowCount(0)
                        cursor.execute("""DELETE FROM TO1 WHERE repair=''""")
                        sqlite_connection.commit()
                        all()
                    def save():
                        try:
                            for i in range(int(row_number001) + 1):
                                ID = form.tableWidget.item(i, 0).text()
                                datas = form.tableWidget.item(i, 1).text()
                                repair = form.tableWidget.item(i, 2).text()
                                redukt = form.tableWidget.item(i, 3).text()
                                master = form.tableWidget.item(i, 4).text()
                                userid = form.tableWidget.item(i, 5).text()
                                hours = form.tableWidget.item(i, 6).text()
                                cursor.execute(
                                    f"""UPDATE TO1 SET datas='{datas}',loko='{iter}',repair='{repair}',redukt='{redukt}',master='{master}',userid='{userid}',hours='{hours}' WHERE ID='{ID}'""")
                            sqlite_connection.commit()
                        except:
                            pass
                    form.pushButton_plus.clicked.connect(plus)
                    form.pushButton_minus.clicked.connect(minus)
                    form.pushButton_save.clicked.connect(save)
                    Form.exec()
            QtWidgets.QTableWidget.mousePressEvent(self, e)
        except:
            pass

class Test2(QtWidgets.QTableWidget):
    def __init__(self, parent=None):
        QtWidgets.QTableWidget.__init__(self, parent)  ##Test

    def mousePressEvent(self, e):
        it = self.itemAt(e.pos())
        try:
            if e.button() == Qt.RightButton:
                if it.column() == 0:
                    fuck = QtWidgets.QMenu(self)
                    fuck.setGeometry(QtCore.QRect(20, 20, 20, 20))
                    low = fuck.addAction("Удалить строчку")
                    action = fuck.exec_(self.mapToGlobal(e.pos()))
                    if action == low:
                        rama = it.tableWidget()
                        sqlite_connection = sqlite3.connect("loko_and_poezd.db")
                        cursor = sqlite_connection.cursor()
                        iter = it.text()
                        cursor.execute(f"""DELETE FROM lokotrain2 WHERE ID='{iter}'""")
                        sqlite_connection.commit()
                        it.tableWidget().setRowCount(0)
                        users = cursor.execute("SELECT * FROM lokotrain2")
                        for row_number, order in enumerate(users):
                            rama.insertRow(row_number)
                            for column_number, data in enumerate(order):
                                item = QtWidgets.QTableWidgetItem(str(data))
                                item.setTextAlignment(Qt.AlignCenter)
                                if (column_number == 1):
                                    pix = Ui_MainWindow().getImageLabel(data)
                                    rama.setCellWidget(row_number, column_number, pix)
                                else:
                                    rama.setItem(row_number, column_number, item)
                if it.column() == 2:
                    iter = it.text()
                    Form = QtWidgets.QDialog(self)
                    form = Ui_Forms()
                    form.setupUi(Form)
                    Form.setWindowFlags(Form.windowFlags() |
                                        QtCore.Qt.WindowMinimizeButtonHint |
                                        QtCore.Qt.WindowSystemMenuHint)
                    Form.show()
                    sqlite_connection = sqlite3.connect("id.db")
                    cursor = sqlite_connection.cursor()
                    def all():
                        global row_number002
                        form.tableWidget.setRowCount(0)
                        users = cursor.execute(
                            f"""SELECT ID,datas,repair,redukt,master,userid,hours FROM TO2 WHERE loko='{iter}' ORDER BY DATE('%d.%m.%Y')""")
                        for row_number002, order in enumerate(users):
                            form.tableWidget.insertRow(row_number002)
                            for column_number, data in enumerate(order):
                                cell = QtWidgets.QTableWidgetItem(str(data))
                                form.tableWidget.setItem(row_number002, column_number, cell)
                                cell.setTextAlignment(Qt.AlignCenter)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(0,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(1,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(2,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(3,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(4,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(5,
                                                                                         QtWidgets.QHeaderView.Stretch)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(6,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                            form.tableWidget.selectRow(row_number002)
                            pool = int(row_number002 + 1)
                            form.label_kol.setText(f"Количество записей: {str(pool)}")
                        form.tableWidget.clearSelection()
                    def plan():
                        form.tableWidget.setRowCount(0)
                        users = cursor.execute(
                            f"""SELECT ID,datas,repair,redukt,master,userid,hours FROM TO2 WHERE loko='{iter}' AND repair='План' ORDER BY DATE('%d.%m.%Y')""")
                        for row_number002, order in enumerate(users):
                            form.tableWidget.insertRow(row_number002)
                            for column_number, data in enumerate(order):
                                cell = QtWidgets.QTableWidgetItem(str(data))
                                form.tableWidget.setItem(row_number002, column_number, cell)
                                cell.setTextAlignment(Qt.AlignCenter)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(0,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(1,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(2,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(3,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(4,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(5,
                                                                                         QtWidgets.QHeaderView.Stretch)
                            form.tableWidget.selectRow(row_number002)
                            pool = int(row_number002 + 1)
                            form.label_kol.setText(f"Количество записей: {str(pool)}")
                        form.tableWidget.clearSelection()
                    def vneplan():
                        form.tableWidget.setRowCount(0)
                        users = cursor.execute(
                            f"""SELECT ID,datas,repair,redukt,master,userid,hours FROM TO2 WHERE loko='{iter}' AND repair='Внеплан' ORDER BY DATE('%d.%m.%Y')""")
                        for row_number002, order in enumerate(users):
                            form.tableWidget.insertRow(row_number002)
                            for column_number, data in enumerate(order):
                                cell = QtWidgets.QTableWidgetItem(str(data))
                                form.tableWidget.setItem(row_number002, column_number, cell)
                                cell.setTextAlignment(Qt.AlignCenter)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(0,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(1,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(2,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(3,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(4,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(5,
                                                                                         QtWidgets.QHeaderView.Stretch)
                            form.tableWidget.selectRow(row_number002)
                            pool = int(row_number002 + 1)
                            form.label_kol.setText(f"Количество записей: {str(pool)}")
                        form.tableWidget.clearSelection()
                    def repair():
                        form.tableWidget.setRowCount(0)
                        users = cursor.execute(
                            f"""SELECT ID,datas,repair,redukt,master,userid,hours FROM TO2 WHERE loko='{iter}' AND repair='Ремонт' ORDER BY DATE('%d.%m.%Y')""")
                        for row_number002, order in enumerate(users):
                            form.tableWidget.insertRow(row_number002)
                            for column_number, data in enumerate(order):
                                cell = QtWidgets.QTableWidgetItem(str(data))
                                form.tableWidget.setItem(row_number002, column_number, cell)
                                cell.setTextAlignment(Qt.AlignCenter)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(0,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(1,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(2,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(3,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(4,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(5,
                                                                                         QtWidgets.QHeaderView.Stretch)
                            form.tableWidget.selectRow(row_number002)
                            pool = int(row_number002 + 1)
                            form.label_kol.setText(f"Количество записей: {str(pool)}")
                        form.tableWidget.clearSelection()
                    all()
                    form.pushButton.clicked.connect(all)
                    form.pushButton_2.clicked.connect(plan)
                    form.pushButton_3.clicked.connect(vneplan)
                    form.pushButton_4.clicked.connect(repair)
                    form.lineEdit.setText(str(iter))
                    hour = cursor.execute(
                        f"""SELECT SUM(hours) FROM TO2 WHERE loko='{iter}'""")
                    intel = hour.fetchall()
                    rom = int()
                    for number in range(len(intel)):
                        try:
                            a = int(intel[number][0])
                            rom += a
                        except:
                            pass
                    form.lineEdit_2.setText(str(rom))
                    def plus():
                        form.tableWidget.setRowCount(0)
                        cursor.execute(f"""INSERT INTO TO2 VALUES (NULL,'{iter}','','','','','','')""")
                        sqlite_connection.commit()
                        all()
                    def minus():
                        form.tableWidget.setRowCount(0)
                        cursor.execute("""DELETE FROM TO2 WHERE repair=''""")
                        sqlite_connection.commit()
                        all()
                    def save():
                        try:
                            for i in range(int(row_number002) + 1):
                                ID = form.tableWidget.item(i, 0).text()
                                datas = form.tableWidget.item(i, 1).text()
                                repair = form.tableWidget.item(i, 2).text()
                                redukt = form.tableWidget.item(i, 3).text()
                                master = form.tableWidget.item(i, 4).text()
                                userid = form.tableWidget.item(i, 5).text()
                                hours = form.tableWidget.item(i, 6).text()
                                cursor.execute(
                                    f"""UPDATE TO2 SET datas='{datas}',loko='{iter}',repair='{repair}',redukt='{redukt}',master='{master}',userid='{userid}',hours='{hours}' WHERE ID='{ID}'""")
                            sqlite_connection.commit()
                        except:
                            pass
                    form.pushButton_plus.clicked.connect(plus)
                    form.pushButton_minus.clicked.connect(minus)
                    form.pushButton_save.clicked.connect(save)
                    Form.exec()
            QtWidgets.QTableWidget.mousePressEvent(self, e)
        except:
            pass

class Test3(QtWidgets.QTableWidget):
    def __init__(self, parent=None):
        QtWidgets.QTableWidget.__init__(self, parent)  ##Test

    def mousePressEvent(self, e):
        it = self.itemAt(e.pos())
        try:
            if e.button() == Qt.RightButton:
                if it.column() == 0:
                    fuck = QtWidgets.QMenu(self)
                    fuck.setGeometry(QtCore.QRect(20, 20, 20, 20))
                    low = fuck.addAction("Удалить строчку")
                    action = fuck.exec_(self.mapToGlobal(e.pos()))
                    if action == low:
                        rama = it.tableWidget()
                        sqlite_connection = sqlite3.connect("loko_and_poezd.db")
                        cursor = sqlite_connection.cursor()
                        iter = it.text()
                        cursor.execute(f"""DELETE FROM lokotrain3 WHERE ID='{iter}'""")
                        sqlite_connection.commit()
                        it.tableWidget().setRowCount(0)
                        users = cursor.execute("SELECT * FROM lokotrain3")
                        for row_number, order in enumerate(users):
                            rama.insertRow(row_number)
                            for column_number, data in enumerate(order):
                                item = QtWidgets.QTableWidgetItem(str(data))
                                item.setTextAlignment(Qt.AlignCenter)
                                if (column_number == 1):
                                    pix = Ui_MainWindow().getImageLabel(data)
                                    rama.setCellWidget(row_number, column_number, pix)
                                else:
                                    rama.setItem(row_number, column_number, item)
                if it.column() == 2:
                    iter = it.text()
                    Form = QtWidgets.QDialog(self)
                    form = Ui_Forms()
                    form.setupUi(Form)
                    Form.setWindowFlags(Form.windowFlags() |
                                        QtCore.Qt.WindowMinimizeButtonHint |
                                        QtCore.Qt.WindowSystemMenuHint)
                    Form.show()
                    sqlite_connection = sqlite3.connect("id.db")
                    cursor = sqlite_connection.cursor()
                    def all():
                        global row_number003
                        form.tableWidget.setRowCount(0)
                        users = cursor.execute(
                            f"""SELECT ID,datas,repair,redukt,master,userid,hours FROM TO3 WHERE loko='{iter}' ORDER BY DATE('%d.%m.%Y')""")
                        for row_number003, order in enumerate(users):
                            form.tableWidget.insertRow(row_number003)
                            for column_number, data in enumerate(order):
                                cell = QtWidgets.QTableWidgetItem(str(data))
                                form.tableWidget.setItem(row_number003, column_number, cell)
                                cell.setTextAlignment(Qt.AlignCenter)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(0,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(1,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(2,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(3,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(4,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(5,
                                                                                         QtWidgets.QHeaderView.Stretch)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(6,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                            form.tableWidget.selectRow(row_number003)
                            pool = int(row_number003 + 1)
                            form.label_kol.setText(f"Количество записей: {str(pool)}")
                        form.tableWidget.clearSelection()
                    def plan():
                        form.tableWidget.setRowCount(0)
                        users = cursor.execute(
                            f"""SELECT ID,datas,repair,redukt,master,userid,hours FROM TO3 WHERE loko='{iter}' AND repair='План' ORDER BY DATE('%d.%m.%Y')""")
                        for row_number003, order in enumerate(users):
                            form.tableWidget.insertRow(row_number003)
                            for column_number, data in enumerate(order):
                                cell = QtWidgets.QTableWidgetItem(str(data))
                                form.tableWidget.setItem(row_number003, column_number, cell)
                                cell.setTextAlignment(Qt.AlignCenter)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(0,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(1,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(2,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(3,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(4,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(5,
                                                                                         QtWidgets.QHeaderView.Stretch)
                            form.tableWidget.selectRow(row_number003)
                            pool = int(row_number003 + 1)
                            form.label_kol.setText(f"Количество записей: {str(pool)}")
                        form.tableWidget.clearSelection()
                    def vneplan():
                        form.tableWidget.setRowCount(0)
                        users = cursor.execute(
                            f"""SELECT ID,datas,repair,redukt,master,userid,hours FROM TO3 WHERE loko='{iter}' AND repair='Внеплан' ORDER BY DATE('%d.%m.%Y')""")
                        for row_number003, order in enumerate(users):
                            form.tableWidget.insertRow(row_number003)
                            for column_number, data in enumerate(order):
                                cell = QtWidgets.QTableWidgetItem(str(data))
                                form.tableWidget.setItem(row_number003, column_number, cell)
                                cell.setTextAlignment(Qt.AlignCenter)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(0,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(1,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(2,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(3,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(4,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(5,
                                                                                         QtWidgets.QHeaderView.Stretch)
                            form.tableWidget.selectRow(row_number003)
                            pool = int(row_number003 + 1)
                            form.label_kol.setText(f"Количество записей: {str(pool)}")
                        form.tableWidget.clearSelection()
                    def repair():
                        form.tableWidget.setRowCount(0)
                        users = cursor.execute(
                            f"""SELECT ID,datas,repair,redukt,master,userid,hours FROM TO3 WHERE loko='{iter}' AND repair='Ремонт' ORDER BY DATE('%d.%m.%Y')""")
                        for row_number003, order in enumerate(users):
                            form.tableWidget.insertRow(row_number003)
                            for column_number, data in enumerate(order):
                                cell = QtWidgets.QTableWidgetItem(str(data))
                                form.tableWidget.setItem(row_number003, column_number, cell)
                                cell.setTextAlignment(Qt.AlignCenter)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(0,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(1,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(2,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(3,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(4,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(5,
                                                                                         QtWidgets.QHeaderView.Stretch)
                            form.tableWidget.selectRow(row_number003)
                            pool = int(row_number003 + 1)
                            form.label_kol.setText(f"Количество записей: {str(pool)}")
                        form.tableWidget.clearSelection()
                    all()
                    form.pushButton.clicked.connect(all)
                    form.pushButton_2.clicked.connect(plan)
                    form.pushButton_3.clicked.connect(vneplan)
                    form.pushButton_4.clicked.connect(repair)
                    form.lineEdit.setText(str(iter))
                    hour = cursor.execute(
                        f"""SELECT SUM(hours) FROM TO3 WHERE loko='{iter}'""")
                    intel = hour.fetchall()
                    rom = int()
                    for number in range(len(intel)):
                        try:
                            a = int(intel[number][0])
                            rom += a
                        except:
                            pass
                    form.lineEdit_2.setText(str(rom))
                    def plus():
                        form.tableWidget.setRowCount(0)
                        cursor.execute(f"""INSERT INTO TO3 VALUES (NULL,'{iter}','','','','','','')""")
                        sqlite_connection.commit()
                        all()
                    def minus():
                        form.tableWidget.setRowCount(0)
                        cursor.execute("""DELETE FROM TO3 WHERE repair=''""")
                        sqlite_connection.commit()
                        all()
                    def save():
                        try:
                            for i in range(int(row_number003) + 1):
                                ID = form.tableWidget.item(i, 0).text()
                                datas = form.tableWidget.item(i, 1).text()
                                repair = form.tableWidget.item(i, 2).text()
                                redukt = form.tableWidget.item(i, 3).text()
                                master = form.tableWidget.item(i, 4).text()
                                userid = form.tableWidget.item(i, 5).text()
                                hours = form.tableWidget.item(i, 6).text()
                                cursor.execute(
                                    f"""UPDATE TO3 SET datas='{datas}',loko='{iter}',repair='{repair}',redukt='{redukt}',master='{master}',userid='{userid}',hours='{hours}' WHERE ID='{ID}'""")
                            sqlite_connection.commit()
                        except:
                            pass
                    form.pushButton_plus.clicked.connect(plus)
                    form.pushButton_minus.clicked.connect(minus)
                    form.pushButton_save.clicked.connect(save)
                    Form.exec()
            QtWidgets.QTableWidget.mousePressEvent(self, e)
        except:
            pass

class Test4(QtWidgets.QTableWidget):
    def __init__(self, parent=None):
        QtWidgets.QTableWidget.__init__(self, parent)  ##Test

    def mousePressEvent(self, e):
        it = self.itemAt(e.pos())
        try:
            if e.button() == Qt.RightButton:
                if it.column() == 0:
                    fuck = QtWidgets.QMenu(self)
                    fuck.setGeometry(QtCore.QRect(20, 20, 20, 20))
                    low = fuck.addAction("Удалить строчку")
                    action = fuck.exec_(self.mapToGlobal(e.pos()))
                    if action == low:
                        rama = it.tableWidget()
                        sqlite_connection = sqlite3.connect("loko_and_poezd.db")
                        cursor = sqlite_connection.cursor()
                        iter = it.text()
                        cursor.execute(f"""DELETE FROM lokotrain4 WHERE ID='{iter}'""")
                        sqlite_connection.commit()
                        it.tableWidget().setRowCount(0)
                        users = cursor.execute("SELECT * FROM lokotrain4")
                        for row_number, order in enumerate(users):
                            rama.insertRow(row_number)
                            for column_number, data in enumerate(order):
                                item = QtWidgets.QTableWidgetItem(str(data))
                                item.setTextAlignment(Qt.AlignCenter)
                                if (column_number == 1):
                                    pix = Ui_MainWindow().getImageLabel(data)
                                    rama.setCellWidget(row_number, column_number, pix)
                                else:
                                    rama.setItem(row_number, column_number, item)
                if it.column() == 2:
                    iter = it.text()
                    Form = QtWidgets.QDialog(self)
                    form = Ui_Forms()
                    form.setupUi(Form)
                    Form.setWindowFlags(Form.windowFlags() |
                                        QtCore.Qt.WindowMinimizeButtonHint |
                                        QtCore.Qt.WindowSystemMenuHint)
                    Form.show()
                    sqlite_connection = sqlite3.connect("id.db")
                    cursor = sqlite_connection.cursor()
                    def all():
                        global row_number004
                        form.tableWidget.setRowCount(0)
                        users = cursor.execute(
                            f"""SELECT ID,datas,repair,redukt,master,userid,hours FROM TO4 WHERE loko='{iter}' ORDER BY DATE('%d.%m.%Y')""")
                        for row_number004, order in enumerate(users):
                            form.tableWidget.insertRow(row_number004)
                            for column_number, data in enumerate(order):
                                cell = QtWidgets.QTableWidgetItem(str(data))
                                form.tableWidget.setItem(row_number004, column_number, cell)
                                cell.setTextAlignment(Qt.AlignCenter)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(0,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(1,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(2,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(3,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(4,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(5,
                                                                                         QtWidgets.QHeaderView.Stretch)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(6,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                            form.tableWidget.selectRow(row_number004)
                            pool = int(row_number004 + 1)
                            form.label_kol.setText(f"Количество записей: {str(pool)}")
                        form.tableWidget.clearSelection()
                    def plan():
                        form.tableWidget.setRowCount(0)
                        users = cursor.execute(
                            f"""SELECT ID,datas,repair,redukt,master,userid,hours FROM TO4 WHERE loko='{iter}' AND repair='План' ORDER BY DATE('%d.%m.%Y')""")
                        for row_number004, order in enumerate(users):
                            form.tableWidget.insertRow(row_number004)
                            for column_number, data in enumerate(order):
                                cell = QtWidgets.QTableWidgetItem(str(data))
                                form.tableWidget.setItem(row_number004, column_number, cell)
                                cell.setTextAlignment(Qt.AlignCenter)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(0,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(1,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(2,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(3,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(4,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(5,
                                                                                         QtWidgets.QHeaderView.Stretch)
                            form.tableWidget.selectRow(row_number004)
                            pool = int(row_number004 + 1)
                            form.label_kol.setText(f"Количество записей: {str(pool)}")
                        form.tableWidget.clearSelection()
                    def vneplan():
                        form.tableWidget.setRowCount(0)
                        users = cursor.execute(
                            f"""SELECT ID,datas,repair,redukt,master,userid,hours FROM TO4 WHERE loko='{iter}' AND repair='Внеплан' ORDER BY DATE('%d.%m.%Y')""")
                        for row_number004, order in enumerate(users):
                            form.tableWidget.insertRow(row_number004)
                            for column_number, data in enumerate(order):
                                cell = QtWidgets.QTableWidgetItem(str(data))
                                form.tableWidget.setItem(row_number004, column_number, cell)
                                cell.setTextAlignment(Qt.AlignCenter)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(0,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(1,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(2,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(3,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(4,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(5,
                                                                                         QtWidgets.QHeaderView.Stretch)
                            form.tableWidget.selectRow(row_number004)
                            pool = int(row_number004 + 1)
                            form.label_kol.setText(f"Количество записей: {str(pool)}")
                        form.tableWidget.clearSelection()
                    def repair():
                        form.tableWidget.setRowCount(0)
                        users = cursor.execute(
                            f"""SELECT ID,datas,repair,redukt,master,userid,hours FROM TO4 WHERE loko='{iter}' AND repair='Ремонт' ORDER BY DATE('%d.%m.%Y')""")
                        for row_number004, order in enumerate(users):
                            form.tableWidget.insertRow(row_number004)
                            for column_number, data in enumerate(order):
                                cell = QtWidgets.QTableWidgetItem(str(data))
                                form.tableWidget.setItem(row_number004, column_number, cell)
                                cell.setTextAlignment(Qt.AlignCenter)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(0,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(1,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(2,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(3,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(4,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(5,
                                                                                         QtWidgets.QHeaderView.Stretch)
                            form.tableWidget.selectRow(row_number004)
                            pool = int(row_number004 + 1)
                            form.label_kol.setText(f"Количество записей: {str(pool)}")
                        form.tableWidget.clearSelection()
                    all()
                    form.pushButton.clicked.connect(all)
                    form.pushButton_2.clicked.connect(plan)
                    form.pushButton_3.clicked.connect(vneplan)
                    form.pushButton_4.clicked.connect(repair)
                    form.lineEdit.setText(str(iter))
                    hour = cursor.execute(
                        f"""SELECT SUM(hours) FROM TO4 WHERE loko='{iter}'""")
                    intel = hour.fetchall()
                    rom = int()
                    for number in range(len(intel)):
                        try:
                            a = int(intel[number][0])
                            rom += a
                        except:
                            pass
                    form.lineEdit_2.setText(str(rom))
                    def plus():
                        form.tableWidget.setRowCount(0)
                        cursor.execute(f"""INSERT INTO TO4 VALUES (NULL,'{iter}','','','','','','')""")
                        sqlite_connection.commit()
                        all()
                    def minus():
                        form.tableWidget.setRowCount(0)
                        cursor.execute("""DELETE FROM TO4 WHERE repair=''""")
                        sqlite_connection.commit()
                        all()
                    def save():
                        try:
                            for i in range(int(row_number004) + 1):
                                ID = form.tableWidget.item(i, 0).text()
                                datas = form.tableWidget.item(i, 1).text()
                                repair = form.tableWidget.item(i, 2).text()
                                redukt = form.tableWidget.item(i, 3).text()
                                master = form.tableWidget.item(i, 4).text()
                                userid = form.tableWidget.item(i, 5).text()
                                hours = form.tableWidget.item(i, 6).text()
                                cursor.execute(
                                    f"""UPDATE TO4 SET datas='{datas}',loko='{iter}',repair='{repair}',redukt='{redukt}',master='{master}',userid='{userid}',hours='{hours}' WHERE ID='{ID}'""")
                            sqlite_connection.commit()
                        except:
                            pass
                    form.pushButton_plus.clicked.connect(plus)
                    form.pushButton_minus.clicked.connect(minus)
                    form.pushButton_save.clicked.connect(save)
                    Form.exec()
            QtWidgets.QTableWidget.mousePressEvent(self, e)
        except:
            pass

class Test5(QtWidgets.QTableWidget):
    def __init__(self, parent=None):
        QtWidgets.QTableWidget.__init__(self, parent)  ##Test

    def mousePressEvent(self, e):
        it = self.itemAt(e.pos())
        try:
            if e.button() == Qt.RightButton:
                if it.column() == 0:
                    fuck = QtWidgets.QMenu(self)
                    fuck.setGeometry(QtCore.QRect(20, 20, 20, 20))
                    low = fuck.addAction("Удалить строчку")
                    action = fuck.exec_(self.mapToGlobal(e.pos()))
                    if action == low:
                        rama = it.tableWidget()
                        sqlite_connection = sqlite3.connect("loko_and_poezd.db")
                        cursor = sqlite_connection.cursor()
                        iter = it.text()
                        cursor.execute(f"""DELETE FROM lokotrain5 WHERE ID='{iter}'""")
                        sqlite_connection.commit()
                        it.tableWidget().setRowCount(0)
                        users = cursor.execute("SELECT * FROM lokotrain5")
                        for row_number, order in enumerate(users):
                            rama.insertRow(row_number)
                            for column_number, data in enumerate(order):
                                item = QtWidgets.QTableWidgetItem(str(data))
                                item.setTextAlignment(Qt.AlignCenter)
                                if (column_number == 1):
                                    pix = Ui_MainWindow().getImageLabel(data)
                                    rama.setCellWidget(row_number, column_number, pix)
                                else:
                                    rama.setItem(row_number, column_number, item)
                if it.column() == 2:
                    iter = it.text()
                    Form = QtWidgets.QDialog(self)
                    form = Ui_Forms()
                    form.setupUi(Form)
                    Form.setWindowFlags(Form.windowFlags() |
                                        QtCore.Qt.WindowMinimizeButtonHint |
                                        QtCore.Qt.WindowSystemMenuHint)
                    Form.show()
                    sqlite_connection = sqlite3.connect("id.db")
                    cursor = sqlite_connection.cursor()
                    def all():
                        global row_number005
                        form.tableWidget.setRowCount(0)
                        users = cursor.execute(
                            f"""SELECT ID,datas,repair,redukt,master,userid,hours FROM TO5 WHERE loko='{iter}' ORDER BY DATE('%d.%m.%Y')""")
                        for row_number005, order in enumerate(users):
                            form.tableWidget.insertRow(row_number005)
                            for column_number, data in enumerate(order):
                                cell = QtWidgets.QTableWidgetItem(str(data))
                                form.tableWidget.setItem(row_number005, column_number, cell)
                                cell.setTextAlignment(Qt.AlignCenter)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(0,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(1,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(2,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(3,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(4,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(5,
                                                                                         QtWidgets.QHeaderView.Stretch)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(6,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                            form.tableWidget.selectRow(row_number005)
                            pool = int(row_number005 + 1)
                            form.label_kol.setText(f"Количество записей: {str(pool)}")
                        form.tableWidget.clearSelection()
                    def plan():
                        form.tableWidget.setRowCount(0)
                        users = cursor.execute(
                            f"""SELECT ID,datas,repair,redukt,master,userid,hours FROM TO5 WHERE loko='{iter}' AND repair='План' ORDER BY DATE('%d.%m.%Y')""")
                        for row_number005, order in enumerate(users):
                            form.tableWidget.insertRow(row_number005)
                            for column_number, data in enumerate(order):
                                cell = QtWidgets.QTableWidgetItem(str(data))
                                form.tableWidget.setItem(row_number005, column_number, cell)
                                cell.setTextAlignment(Qt.AlignCenter)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(0,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(1,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(2,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(3,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(4,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(5,
                                                                                         QtWidgets.QHeaderView.Stretch)
                            form.tableWidget.selectRow(row_number005)
                            pool = int(row_number005 + 1)
                            form.label_kol.setText(f"Количество записей: {str(pool)}")
                        form.tableWidget.clearSelection()
                    def vneplan():
                        form.tableWidget.setRowCount(0)
                        users = cursor.execute(
                            f"""SELECT ID,datas,repair,redukt,master,userid,hours FROM TO5 WHERE loko='{iter}' AND repair='Внеплан' ORDER BY DATE('%d.%m.%Y')""")
                        for row_number005, order in enumerate(users):
                            form.tableWidget.insertRow(row_number005)
                            for column_number, data in enumerate(order):
                                cell = QtWidgets.QTableWidgetItem(str(data))
                                form.tableWidget.setItem(row_number005, column_number, cell)
                                cell.setTextAlignment(Qt.AlignCenter)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(0,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(1,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(2,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(3,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(4,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(5,
                                                                                         QtWidgets.QHeaderView.Stretch)
                            form.tableWidget.selectRow(row_number005)
                            pool = int(row_number005 + 1)
                            form.label_kol.setText(f"Количество записей: {str(pool)}")
                        form.tableWidget.clearSelection()
                    def repair():
                        form.tableWidget.setRowCount(0)
                        users = cursor.execute(
                            f"""SELECT ID,datas,repair,redukt,master,userid,hours FROM TO5 WHERE loko='{iter}' AND repair='Ремонт' ORDER BY DATE('%d.%m.%Y')""")
                        for row_number005, order in enumerate(users):
                            form.tableWidget.insertRow(row_number005)
                            for column_number, data in enumerate(order):
                                cell = QtWidgets.QTableWidgetItem(str(data))
                                form.tableWidget.setItem(row_number005, column_number, cell)
                                cell.setTextAlignment(Qt.AlignCenter)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(0,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(1,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(2,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(3,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(4,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(5,
                                                                                         QtWidgets.QHeaderView.Stretch)
                            form.tableWidget.selectRow(row_number005)
                            pool = int(row_number005 + 1)
                            form.label_kol.setText(f"Количество записей: {str(pool)}")
                        form.tableWidget.clearSelection()
                    all()
                    form.pushButton.clicked.connect(all)
                    form.pushButton_2.clicked.connect(plan)
                    form.pushButton_3.clicked.connect(vneplan)
                    form.pushButton_4.clicked.connect(repair)
                    form.lineEdit.setText(str(iter))
                    hour = cursor.execute(
                        f"""SELECT SUM(hours) FROM TO5 WHERE loko='{iter}'""")
                    intel = hour.fetchall()
                    rom = int()
                    for number in range(len(intel)):
                        try:
                            a = int(intel[number][0])
                            rom += a
                        except:
                            pass
                    form.lineEdit_2.setText(str(rom))
                    def plus():
                        form.tableWidget.setRowCount(0)
                        cursor.execute(f"""INSERT INTO TO5 VALUES (NULL,'{iter}','','','','','','')""")
                        sqlite_connection.commit()
                        all()
                    def minus():
                        form.tableWidget.setRowCount(0)
                        cursor.execute("""DELETE FROM TO5 WHERE repair=''""")
                        sqlite_connection.commit()
                        all()
                    def save():
                        try:
                            for i in range(int(row_number005) + 1):
                                ID = form.tableWidget.item(i, 0).text()
                                datas = form.tableWidget.item(i, 1).text()
                                repair = form.tableWidget.item(i, 2).text()
                                redukt = form.tableWidget.item(i, 3).text()
                                master = form.tableWidget.item(i, 4).text()
                                userid = form.tableWidget.item(i, 5).text()
                                hours = form.tableWidget.item(i, 6).text()
                                cursor.execute(
                                    f"""UPDATE TO5 SET datas='{datas}',loko='{iter}',repair='{repair}',redukt='{redukt}',master='{master}',userid='{userid}',hours='{hours}' WHERE ID='{ID}'""")
                            sqlite_connection.commit()
                        except:
                            pass
                    form.pushButton_plus.clicked.connect(plus)
                    form.pushButton_minus.clicked.connect(minus)
                    form.pushButton_save.clicked.connect(save)
                    Form.exec()
            QtWidgets.QTableWidget.mousePressEvent(self, e)
        except:
            pass

class Test6(QtWidgets.QTableWidget):
    def __init__(self, parent=None):
        QtWidgets.QTableWidget.__init__(self, parent)  ##Test

    def mousePressEvent(self, e):
        it = self.itemAt(e.pos())
        try:
            if e.button() == Qt.RightButton:
                if it.column() == 0:
                    fuck = QtWidgets.QMenu(self)
                    fuck.setGeometry(QtCore.QRect(20, 20, 20, 20))
                    low = fuck.addAction("Удалить строчку")
                    action = fuck.exec_(self.mapToGlobal(e.pos()))
                    if action == low:
                        rama = it.tableWidget()
                        sqlite_connection = sqlite3.connect("loko_and_poezd.db")
                        cursor = sqlite_connection.cursor()
                        iter = it.text()
                        cursor.execute(f"""DELETE FROM lokotrain6 WHERE ID='{iter}'""")
                        sqlite_connection.commit()
                        it.tableWidget().setRowCount(0)
                        users = cursor.execute("SELECT * FROM lokotrain6")
                        for row_number, order in enumerate(users):
                            rama.insertRow(row_number)
                            for column_number, data in enumerate(order):
                                item = QtWidgets.QTableWidgetItem(str(data))
                                item.setTextAlignment(Qt.AlignCenter)
                                if (column_number == 1):
                                    pix = Ui_MainWindow().getImageLabel(data)
                                    rama.setCellWidget(row_number, column_number, pix)
                                else:
                                    rama.setItem(row_number, column_number, item)
                if it.column() == 2:
                    iter = it.text()
                    Form = QtWidgets.QDialog(self)
                    form = Ui_Forms()
                    form.setupUi(Form)
                    Form.setWindowFlags(Form.windowFlags() |
                                        QtCore.Qt.WindowMinimizeButtonHint |
                                        QtCore.Qt.WindowSystemMenuHint)
                    Form.show()
                    sqlite_connection = sqlite3.connect("id.db")
                    cursor = sqlite_connection.cursor()
                    def all():
                        global row_number006
                        form.tableWidget.setRowCount(0)
                        users = cursor.execute(
                            f"""SELECT ID,datas,repair,redukt,master,userid,hours FROM TO6 WHERE loko='{iter}' ORDER BY DATE('%d.%m.%Y')""")
                        for row_number006, order in enumerate(users):
                            form.tableWidget.insertRow(row_number006)
                            for column_number, data in enumerate(order):
                                cell = QtWidgets.QTableWidgetItem(str(data))
                                form.tableWidget.setItem(row_number006, column_number, cell)
                                cell.setTextAlignment(Qt.AlignCenter)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(0,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(1,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(2,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(3,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(4,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(5,
                                                                                         QtWidgets.QHeaderView.Stretch)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(6,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                            form.tableWidget.selectRow(row_number006)
                            pool = int(row_number006 + 1)
                            form.label_kol.setText(f"Количество записей: {str(pool)}")
                        form.tableWidget.clearSelection()
                    def plan():
                        form.tableWidget.setRowCount(0)
                        users = cursor.execute(
                            f"""SELECT ID,datas,repair,redukt,master,userid,hours FROM TO6 WHERE loko='{iter}' AND repair='План' ORDER BY DATE('%d.%m.%Y')""")
                        for row_number006, order in enumerate(users):
                            form.tableWidget.insertRow(row_number006)
                            for column_number, data in enumerate(order):
                                cell = QtWidgets.QTableWidgetItem(str(data))
                                form.tableWidget.setItem(row_number006, column_number, cell)
                                cell.setTextAlignment(Qt.AlignCenter)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(0,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(1,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(2,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(3,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(4,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(5,
                                                                                         QtWidgets.QHeaderView.Stretch)
                            form.tableWidget.selectRow(row_number006)
                            pool = int(row_number006 + 1)
                            form.label_kol.setText(f"Количество записей: {str(pool)}")
                        form.tableWidget.clearSelection()
                    def vneplan():
                        form.tableWidget.setRowCount(0)
                        users = cursor.execute(
                            f"""SELECT ID,datas,repair,redukt,master,userid,hours FROM TO6 WHERE loko='{iter}' AND repair='Внеплан' ORDER BY DATE('%d.%m.%Y')""")
                        for row_number006, order in enumerate(users):
                            form.tableWidget.insertRow(row_number006)
                            for column_number, data in enumerate(order):
                                cell = QtWidgets.QTableWidgetItem(str(data))
                                form.tableWidget.setItem(row_number006, column_number, cell)
                                cell.setTextAlignment(Qt.AlignCenter)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(0,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(1,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(2,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(3,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(4,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(5,
                                                                                         QtWidgets.QHeaderView.Stretch)
                            form.tableWidget.selectRow(row_number006)
                            pool = int(row_number006 + 1)
                            form.label_kol.setText(f"Количество записей: {str(pool)}")
                        form.tableWidget.clearSelection()
                    def repair():
                        form.tableWidget.setRowCount(0)
                        users = cursor.execute(
                            f"""SELECT ID,datas,repair,redukt,master,userid,hours FROM TO6 WHERE loko='{iter}' AND repair='Ремонт' ORDER BY DATE('%d.%m.%Y')""")
                        for row_number006, order in enumerate(users):
                            form.tableWidget.insertRow(row_number006)
                            for column_number, data in enumerate(order):
                                cell = QtWidgets.QTableWidgetItem(str(data))
                                form.tableWidget.setItem(row_number006, column_number, cell)
                                cell.setTextAlignment(Qt.AlignCenter)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(0,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(1,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(2,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(3,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(4,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(5,
                                                                                         QtWidgets.QHeaderView.Stretch)
                            form.tableWidget.selectRow(row_number006)
                            pool = int(row_number006 + 1)
                            form.label_kol.setText(f"Количество записей: {str(pool)}")
                        form.tableWidget.clearSelection()
                    all()
                    form.pushButton.clicked.connect(all)
                    form.pushButton_2.clicked.connect(plan)
                    form.pushButton_3.clicked.connect(vneplan)
                    form.pushButton_4.clicked.connect(repair)
                    form.lineEdit.setText(str(iter))
                    hour = cursor.execute(
                        f"""SELECT SUM(hours) FROM TO6 WHERE loko='{iter}'""")
                    intel = hour.fetchall()
                    rom = int()
                    for number in range(len(intel)):
                        try:
                            a = int(intel[number][0])
                            rom += a
                        except:
                            pass
                    form.lineEdit_2.setText(str(rom))
                    def plus():
                        form.tableWidget.setRowCount(0)
                        cursor.execute(f"""INSERT INTO TO6 VALUES (NULL,'{iter}','','','','','','')""")
                        sqlite_connection.commit()
                        all()
                    def minus():
                        form.tableWidget.setRowCount(0)
                        cursor.execute("""DELETE FROM TO6 WHERE repair=''""")
                        sqlite_connection.commit()
                        all()
                    def save():
                        try:
                            for i in range(int(row_number006) + 1):
                                ID = form.tableWidget.item(i, 0).text()
                                datas = form.tableWidget.item(i, 1).text()
                                repair = form.tableWidget.item(i, 2).text()
                                redukt = form.tableWidget.item(i, 3).text()
                                master = form.tableWidget.item(i, 4).text()
                                userid = form.tableWidget.item(i, 5).text()
                                hours = form.tableWidget.item(i, 6).text()
                                cursor.execute(
                                    f"""UPDATE TO6 SET datas='{datas}',loko='{iter}',repair='{repair}',redukt='{redukt}',master='{master}',userid='{userid}',hours='{hours}' WHERE ID='{ID}'""")
                            sqlite_connection.commit()
                        except:
                            pass
                    form.pushButton_plus.clicked.connect(plus)
                    form.pushButton_minus.clicked.connect(minus)
                    form.pushButton_save.clicked.connect(save)
                    Form.exec()
            QtWidgets.QTableWidget.mousePressEvent(self, e)
        except:
            pass

class Test7(QtWidgets.QTableWidget):
    def __init__(self, parent=None):
        QtWidgets.QTableWidget.__init__(self, parent)  ##Test

    def mousePressEvent(self, e):
        it = self.itemAt(e.pos())
        try:
            if e.button() == Qt.RightButton:
                if it.column() == 0:
                    fuck = QtWidgets.QMenu(self)
                    fuck.setGeometry(QtCore.QRect(20, 20, 20, 20))
                    low = fuck.addAction("Удалить строчку")
                    action = fuck.exec_(self.mapToGlobal(e.pos()))
                    if action == low:
                        rama = it.tableWidget()
                        sqlite_connection = sqlite3.connect("loko_and_poezd.db")
                        cursor = sqlite_connection.cursor()
                        iter = it.text()
                        cursor.execute(f"""DELETE FROM lokotrain7 WHERE ID='{iter}'""")
                        sqlite_connection.commit()
                        it.tableWidget().setRowCount(0)
                        users = cursor.execute("SELECT * FROM lokotrain7")
                        for row_number, order in enumerate(users):
                            rama.insertRow(row_number)
                            for column_number, data in enumerate(order):
                                item = QtWidgets.QTableWidgetItem(str(data))
                                item.setTextAlignment(Qt.AlignCenter)
                                if (column_number == 1):
                                    pix = Ui_MainWindow().getImageLabel(data)
                                    rama.setCellWidget(row_number, column_number, pix)
                                else:
                                    rama.setItem(row_number, column_number, item)
                if it.column() == 2:
                    iter = it.text()
                    Form = QtWidgets.QDialog(self)
                    form = Ui_Forms()
                    form.setupUi(Form)
                    Form.setWindowFlags(Form.windowFlags() |
                                        QtCore.Qt.WindowMinimizeButtonHint |
                                        QtCore.Qt.WindowSystemMenuHint)
                    Form.show()
                    sqlite_connection = sqlite3.connect("id.db")
                    cursor = sqlite_connection.cursor()
                    def all():
                        global row_number007
                        form.tableWidget.setRowCount(0)
                        users = cursor.execute(
                            f"""SELECT ID,datas,repair,redukt,master,userid,hours FROM TO7 WHERE loko='{iter}' ORDER BY DATE('%d.%m.%Y')""")
                        for row_number007, order in enumerate(users):
                            form.tableWidget.insertRow(row_number007)
                            for column_number, data in enumerate(order):
                                cell = QtWidgets.QTableWidgetItem(str(data))
                                form.tableWidget.setItem(row_number007, column_number, cell)
                                cell.setTextAlignment(Qt.AlignCenter)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(0,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(1,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(2,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(3,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(4,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(5,
                                                                                         QtWidgets.QHeaderView.Stretch)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(6,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                            form.tableWidget.selectRow(row_number007)
                            pool = int(row_number007 + 1)
                            form.label_kol.setText(f"Количество записей: {str(pool)}")
                        form.tableWidget.clearSelection()
                    def plan():
                        form.tableWidget.setRowCount(0)
                        users = cursor.execute(
                            f"""SELECT ID,datas,repair,redukt,master,userid,hours FROM TO7 WHERE loko='{iter}' AND repair='План' ORDER BY DATE('%d.%m.%Y')""")
                        for row_number007, order in enumerate(users):
                            form.tableWidget.insertRow(row_number007)
                            for column_number, data in enumerate(order):
                                cell = QtWidgets.QTableWidgetItem(str(data))
                                form.tableWidget.setItem(row_number007, column_number, cell)
                                cell.setTextAlignment(Qt.AlignCenter)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(0,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(1,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(2,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(3,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(4,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(5,
                                                                                         QtWidgets.QHeaderView.Stretch)
                            form.tableWidget.selectRow(row_number007)
                            pool = int(row_number007 + 1)
                            form.label_kol.setText(f"Количество записей: {str(pool)}")
                        form.tableWidget.clearSelection()
                    def vneplan():
                        form.tableWidget.setRowCount(0)
                        users = cursor.execute(
                            f"""SELECT ID,datas,repair,redukt,master,userid,hours FROM TO7 WHERE loko='{iter}' AND repair='Внеплан' ORDER BY DATE('%d.%m.%Y')""")
                        for row_number007, order in enumerate(users):
                            form.tableWidget.insertRow(row_number007)
                            for column_number, data in enumerate(order):
                                cell = QtWidgets.QTableWidgetItem(str(data))
                                form.tableWidget.setItem(row_number007, column_number, cell)
                                cell.setTextAlignment(Qt.AlignCenter)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(0,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(1,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(2,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(3,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(4,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(5,
                                                                                         QtWidgets.QHeaderView.Stretch)
                            form.tableWidget.selectRow(row_number007)
                            pool = int(row_number007 + 1)
                            form.label_kol.setText(f"Количество записей: {str(pool)}")
                        form.tableWidget.clearSelection()
                    def repair():
                        form.tableWidget.setRowCount(0)
                        users = cursor.execute(
                            f"""SELECT ID,datas,repair,redukt,master,userid,hours FROM TO7 WHERE loko='{iter}' AND repair='Ремонт' ORDER BY DATE('%d.%m.%Y')""")
                        for row_number007, order in enumerate(users):
                            form.tableWidget.insertRow(row_number007)
                            for column_number, data in enumerate(order):
                                cell = QtWidgets.QTableWidgetItem(str(data))
                                form.tableWidget.setItem(row_number007, column_number, cell)
                                cell.setTextAlignment(Qt.AlignCenter)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(0,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(1,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(2,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(3,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(4,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(5,
                                                                                         QtWidgets.QHeaderView.Stretch)
                            form.tableWidget.selectRow(row_number007)
                            pool = int(row_number007 + 1)
                            form.label_kol.setText(f"Количество записей: {str(pool)}")
                        form.tableWidget.clearSelection()
                    all()
                    form.pushButton.clicked.connect(all)
                    form.pushButton_2.clicked.connect(plan)
                    form.pushButton_3.clicked.connect(vneplan)
                    form.pushButton_4.clicked.connect(repair)
                    form.lineEdit.setText(str(iter))
                    hour = cursor.execute(
                        f"""SELECT SUM(hours) FROM TO7 WHERE loko='{iter}'""")
                    intel = hour.fetchall()
                    rom = int()
                    for number in range(len(intel)):
                        try:
                            a = int(intel[number][0])
                            rom += a
                        except:
                            pass
                    form.lineEdit_2.setText(str(rom))
                    def plus():
                        form.tableWidget.setRowCount(0)
                        cursor.execute(f"""INSERT INTO TO7 VALUES (NULL,'{iter}','','','','','','')""")
                        sqlite_connection.commit()
                        all()
                    def minus():
                        form.tableWidget.setRowCount(0)
                        cursor.execute("""DELETE FROM TO7 WHERE repair=''""")
                        sqlite_connection.commit()
                        all()
                    def save():
                        try:
                            for i in range(int(row_number007) + 1):
                                ID = form.tableWidget.item(i, 0).text()
                                datas = form.tableWidget.item(i, 1).text()
                                repair = form.tableWidget.item(i, 2).text()
                                redukt = form.tableWidget.item(i, 3).text()
                                master = form.tableWidget.item(i, 4).text()
                                userid = form.tableWidget.item(i, 5).text()
                                hours = form.tableWidget.item(i, 6).text()
                                cursor.execute(
                                    f"""UPDATE TO7 SET datas='{datas}',loko='{iter}',repair='{repair}',redukt='{redukt}',master='{master}',userid='{userid}',hours='{hours}' WHERE ID='{ID}'""")
                            sqlite_connection.commit()
                        except:
                            pass
                    form.pushButton_plus.clicked.connect(plus)
                    form.pushButton_minus.clicked.connect(minus)
                    form.pushButton_save.clicked.connect(save)
                    Form.exec()
            QtWidgets.QTableWidget.mousePressEvent(self, e)
        except:
            pass

class Test8(QtWidgets.QTableWidget):
    def __init__(self, parent=None):
        QtWidgets.QTableWidget.__init__(self, parent)  ##Test

    def mousePressEvent(self, e):
        it = self.itemAt(e.pos())
        try:
            if e.button() == Qt.RightButton:
                if it.column() == 0:
                    fuck = QtWidgets.QMenu(self)
                    fuck.setGeometry(QtCore.QRect(20, 20, 20, 20))
                    low = fuck.addAction("Удалить строчку")
                    action = fuck.exec_(self.mapToGlobal(e.pos()))
                    if action == low:
                        rama = it.tableWidget()
                        sqlite_connection = sqlite3.connect("loko_and_poezd.db")
                        cursor = sqlite_connection.cursor()
                        iter = it.text()
                        cursor.execute(f"""DELETE FROM lokotrain8 WHERE ID='{iter}'""")
                        sqlite_connection.commit()
                        it.tableWidget().setRowCount(0)
                        users = cursor.execute("SELECT * FROM lokotrain8")
                        for row_number, order in enumerate(users):
                            rama.insertRow(row_number)
                            for column_number, data in enumerate(order):
                                item = QtWidgets.QTableWidgetItem(str(data))
                                item.setTextAlignment(Qt.AlignCenter)
                                if (column_number == 1):
                                    pix = Ui_MainWindow().getImageLabel(data)
                                    rama.setCellWidget(row_number, column_number, pix)
                                else:
                                    rama.setItem(row_number, column_number, item)
                if it.column() == 2:
                    iter = it.text()
                    Form = QtWidgets.QDialog(self)
                    form = Ui_Forms()
                    form.setupUi(Form)
                    Form.setWindowFlags(Form.windowFlags() |
                                        QtCore.Qt.WindowMinimizeButtonHint |
                                        QtCore.Qt.WindowSystemMenuHint)
                    Form.show()
                    sqlite_connection = sqlite3.connect("id.db")
                    cursor = sqlite_connection.cursor()
                    def all():
                        global row_number008
                        form.tableWidget.setRowCount(0)
                        users = cursor.execute(
                            f"""SELECT ID,datas,repair,redukt,master,userid,hours FROM TO8 WHERE loko='{iter}' ORDER BY DATE('%d.%m.%Y')""")
                        for row_number008, order in enumerate(users):
                            form.tableWidget.insertRow(row_number008)
                            for column_number, data in enumerate(order):
                                cell = QtWidgets.QTableWidgetItem(str(data))
                                form.tableWidget.setItem(row_number008, column_number, cell)
                                cell.setTextAlignment(Qt.AlignCenter)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(0,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(1,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(2,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(3,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(4,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(5,
                                                                                         QtWidgets.QHeaderView.Stretch)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(6,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                            form.tableWidget.selectRow(row_number008)
                            pool = int(row_number008 + 1)
                            form.label_kol.setText(f"Количество записей: {str(pool)}")
                        form.tableWidget.clearSelection()
                    def plan():
                        form.tableWidget.setRowCount(0)
                        users = cursor.execute(
                            f"""SELECT ID,datas,repair,redukt,master,userid,hours FROM TO8 WHERE loko='{iter}' AND repair='План' ORDER BY DATE('%d.%m.%Y')""")
                        for row_number008, order in enumerate(users):
                            form.tableWidget.insertRow(row_number008)
                            for column_number, data in enumerate(order):
                                cell = QtWidgets.QTableWidgetItem(str(data))
                                form.tableWidget.setItem(row_number008, column_number, cell)
                                cell.setTextAlignment(Qt.AlignCenter)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(0,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(1,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(2,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(3,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(4,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(5,
                                                                                         QtWidgets.QHeaderView.Stretch)
                            form.tableWidget.selectRow(row_number008)
                            pool = int(row_number008 + 1)
                            form.label_kol.setText(f"Количество записей: {str(pool)}")
                        form.tableWidget.clearSelection()
                    def vneplan():
                        form.tableWidget.setRowCount(0)
                        users = cursor.execute(
                            f"""SELECT ID,datas,repair,redukt,master,userid,hours FROM TO7 WHERE loko='{iter}' AND repair='Внеплан' ORDER BY DATE('%d.%m.%Y')""")
                        for row_number008, order in enumerate(users):
                            form.tableWidget.insertRow(row_number008)
                            for column_number, data in enumerate(order):
                                cell = QtWidgets.QTableWidgetItem(str(data))
                                form.tableWidget.setItem(row_number008, column_number, cell)
                                cell.setTextAlignment(Qt.AlignCenter)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(0,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(1,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(2,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(3,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(4,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(5,
                                                                                         QtWidgets.QHeaderView.Stretch)
                            form.tableWidget.selectRow(row_number008)
                            pool = int(row_number008 + 1)
                            form.label_kol.setText(f"Количество записей: {str(pool)}")
                        form.tableWidget.clearSelection()
                    def repair():
                        form.tableWidget.setRowCount(0)
                        users = cursor.execute(
                            f"""SELECT ID,datas,repair,redukt,master,userid,hours FROM TO8 WHERE loko='{iter}' AND repair='Ремонт' ORDER BY DATE('%d.%m.%Y')""")
                        for row_number008, order in enumerate(users):
                            form.tableWidget.insertRow(row_number008)
                            for column_number, data in enumerate(order):
                                cell = QtWidgets.QTableWidgetItem(str(data))
                                form.tableWidget.setItem(row_number008, column_number, cell)
                                cell.setTextAlignment(Qt.AlignCenter)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(0,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(1,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(2,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(3,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(4,
                                                                                         QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.horizontalHeader().setSectionResizeMode(5,
                                                                                         QtWidgets.QHeaderView.Stretch)
                            form.tableWidget.selectRow(row_number008)
                            pool = int(row_number008 + 1)
                            form.label_kol.setText(f"Количество записей: {str(pool)}")
                        form.tableWidget.clearSelection()
                    all()
                    form.pushButton.clicked.connect(all)
                    form.pushButton_2.clicked.connect(plan)
                    form.pushButton_3.clicked.connect(vneplan)
                    form.pushButton_4.clicked.connect(repair)
                    form.lineEdit.setText(str(iter))
                    hour = cursor.execute(
                        f"""SELECT SUM(hours) FROM TO8 WHERE loko='{iter}'""")
                    intel = hour.fetchall()
                    rom = int()
                    for number in range(len(intel)):
                        try:
                            a = int(intel[number][0])
                            rom += a
                        except:
                            pass
                    form.lineEdit_2.setText(str(rom))
                    def plus():
                        form.tableWidget.setRowCount(0)
                        cursor.execute(f"""INSERT INTO TO8 VALUES (NULL,'{iter}','','','','','','')""")
                        sqlite_connection.commit()
                        all()
                    def minus():
                        form.tableWidget.setRowCount(0)
                        cursor.execute("""DELETE FROM TO8 WHERE repair=''""")
                        sqlite_connection.commit()
                        all()
                    def save():
                        try:
                            for i in range(int(row_number008) + 1):
                                ID = form.tableWidget.item(i, 0).text()
                                datas = form.tableWidget.item(i, 1).text()
                                repair = form.tableWidget.item(i, 2).text()
                                redukt = form.tableWidget.item(i, 3).text()
                                master = form.tableWidget.item(i, 4).text()
                                userid = form.tableWidget.item(i, 5).text()
                                hours = form.tableWidget.item(i, 6).text()
                                cursor.execute(
                                    f"""UPDATE TO8 SET datas='{datas}',loko='{iter}',repair='{repair}',redukt='{redukt}',master='{master}',userid='{userid}',hours='{hours}' WHERE ID='{ID}'""")
                            sqlite_connection.commit()
                        except:
                            pass
                    form.pushButton_plus.clicked.connect(plus)
                    form.pushButton_minus.clicked.connect(minus)
                    form.pushButton_save.clicked.connect(save)
                    Form.exec()
            QtWidgets.QTableWidget.mousePressEvent(self, e)
        except:
            pass

class TestDetalis(QtWidgets.QTableWidget):
    def __init__(self, parent=None):
        QtWidgets.QTableWidget.__init__(self, parent)  ##Test

    def mousePressEvent(self, e):
        it = self.itemAt(e.pos())
        try:
            if e.button() == Qt.RightButton:
                levels = cursor_01.execute(
                    f"""SELECT levels FROM autorization WHERE online='True'""").fetchone()
                if it.column() == 0:
                    if levels[0] == "2" or  levels[0] == "3":
                        fuck = QtWidgets.QMenu(self)
                        fuck.setGeometry(QtCore.QRect(20, 20, 20, 20))
                        low = fuck.addAction("Удалить строчку")
                        action = fuck.exec_(self.mapToGlobal(e.pos()))
                    if action == low:
                        rama = it.tableWidget()
                        sqlite_connection = sqlite3.connect("id.db")
                        cursor = sqlite_connection.cursor()
                        iter = it.text()
                        cursor.execute(f"""DELETE FROM orders WHERE ID='{iter}'""")
                        sqlite_connection.commit()
                        it.tableWidget().setRowCount(0)
                        users = cursor.execute("SELECT ID,NULL,orderid,tip,datem,userid,total FROM orders")
                        for row_number, order in enumerate(users):
                            rama.insertRow(row_number)
                            for column_number, data in enumerate(order):
                                item = QtWidgets.QTableWidgetItem(str(data))
                                item.setTextAlignment(Qt.AlignCenter)
                                if (column_number == 1):
                                    pass
                                else:
                                    rama.setItem(row_number, column_number, item)
                        users = cursor.execute("SELECT foto FROM orders")
                        a = users.fetchall()
                        for i in range(len(a)):
                            if str(a[i][0]) != "None":
                                label = QLabel()
                                label.setText("")
                                label.setScaledContents(True)
                                pix = QPixmap(f"{a[i][0]}")
                                label.setPixmap(pix)
                                rama.setCellWidget(i, 1, label)
                            else:
                                pass
                        def journal_plus_del(artic):
                            #if lvl == 3 or lvl == 2:
                            Form = QtWidgets.QDialog(MainWindow)
                            form = Plus_del()
                            form.setupUi(Form)
                            Form.setWindowFlags(Form.windowFlags() |
                                                QtCore.Qt.WindowMinimizeButtonHint |
                                                QtCore.Qt.WindowSystemMenuHint)
                            if artic!="None":
                                all = cursor.execute(f"SELECT * FROM plus_del WHERE articul='{artic}'")
                            else:
                                all = cursor.execute(f"SELECT * FROM plus_del")
                            for row_number, order in enumerate(all):
                                form.tableWidget.insertRow(row_number)
                                for column_number, data in enumerate(order):
                                    cell = QtWidgets.QTableWidgetItem(str(data))
                                    form.tableWidget.setItem(row_number, column_number, cell)
                                    cell.setTextAlignment(Qt.AlignCenter)
                                form.tableWidget.selectRow(row_number)
                            form.tableWidget.horizontalHeader().setSectionResizeMode(0,
                                                                                     QtWidgets.QHeaderView.ResizeToContents)
                            form.tableWidget.horizontalHeader().setSectionResizeMode(1,
                                                                                     QtWidgets.QHeaderView.Stretch)
                            form.tableWidget.horizontalHeader().setSectionResizeMode(2,
                                                                                     QtWidgets.QHeaderView.Stretch)
                            form.tableWidget.horizontalHeader().setSectionResizeMode(3,
                                                                                     QtWidgets.QHeaderView.Stretch)
                            try:
                                form.tableWidget.scrollToItem(form.tableWidget.item(0, 0), QAbstractItemView.PositionAtTop)
                                form.tableWidget.clearSelection()
                            except:
                                pass
                            Form.show()
                            Form.exec()
                        def pushing_detali():
                            for i in range(row_number+1):
                                column_number=2
                                articul = rama.item(i,column_number).text()
                                pushButton_detalis = QtWidgets.QPushButton(f"Привоз/Расход\n{articul}")
                                column_number=6
                                if pushButton_detalis!=None:
                                    pushButton_detalis.clicked.connect(lambda ch, btn=pushButton_detalis: journal_plus_del(str(btn.text()).replace("Привоз/Расход\n","")))
                                    rama.setCellWidget(i, column_number, pushButton_detalis)
                        pushing_detali()
                if it.column() == 2:
                    if levels[0] == "2" or  levels[0] == "3":
                        fuck = QtWidgets.QMenu(self)
                        fuck.setGeometry(QtCore.QRect(20, 20, 20, 20))
                        image = fuck.addAction("Добавить/изменить картинку")
                        image_del = fuck.addAction("Удалить картинку")
                        pow = fuck.addAction("Добавить несколько деталей")
                        low = fuck.addAction("Убрать несколько деталей")
                        invent = fuck.addAction("Инвентаризация детали")
                        detal = fuck.addAction("О детали")
                        action = fuck.exec_(self.mapToGlobal(e.pos()))
                    if action == invent:
                        Form, App = uic.loadUiType("invent.ui")
                        app = QDialog(self)
                        form = Form()
                        form.setupUi(app)
                        app.show()

                        def like():
                            let = form.lineEdit.text()
                            iter = it.text()
                            try:
                                sqlite_connection = sqlite3.connect("id.db")
                                cursor = sqlite_connection.cursor()
                                inventar = (it.tableWidget().item(it.row(), 5)).text()
                                text_invent = "Инвентаризация"
                                let_check = str(let).replace("-","")
                                pux = cursor.execute(f"""SELECT userid,kol FROM orders WHERE orderid='{iter}'""").fetchone()
                                pux = pux[1] - pux[0]
                                if let_check.isdigit():
                                    cursor.execute(f"""UPDATE orders SET kol=(kol-'{int(inventar)}') WHERE orderid='{iter}'""")
                                    cursor.execute(f"""UPDATE orders SET kol=(kol +'{let}') WHERE orderid='{iter}'""")
                                    cursor.execute(f"""UPDATE orders SET userid=(kol - '{int(pux)}') WHERE orderid='{iter}'""")
                                    cursor.execute(f"""INSERT INTO plus_del VALUES ('{iter}','{text_invent}','{let}','{today.strftime("%d.%m.%Y-%Hh %Mm")}')""")
                                    sqlite_connection.commit()
                                if inventar == "":
                                    (it.tableWidget().item(it.row(), 5)).setText(str(int(0) + int(let)))
                                else:
                                    (it.tableWidget().item(it.row(), 5)).setText(str(int(let)))
                            except:
                                pass
                            app.close()

                        def end():
                            app.close()

                        form.pushButton.clicked.connect(like)
                        form.pushButton_2.clicked.connect(end)
                        app.exec()
                    if action == pow:
                        Form, App = uic.loadUiType("plus.ui")
                        app = QDialog(self)
                        form = Form()
                        form.setupUi(app)
                        app.show()

                        def like():
                            let = form.lineEdit.text()
                            iter = it.text()
                            try:
                                sqlite_connection = sqlite3.connect("id.db")
                                username = cursor_01.execute(
                                    f"""SELECT login FROM autorization WHERE online='True'""").fetchone()
                                cursor = sqlite_connection.cursor()
                                cursor.execute(f"""UPDATE orders SET kol=(kol +'{let}') WHERE orderid='{iter}'""")
                                cursor.execute(f"""UPDATE orders SET userid=(userid + '{let}') WHERE orderid='{iter}'""")
                                cursor.execute(f"""INSERT INTO plus_del VALUES ('{iter}','{username[0]}','{let}','{today.strftime("%d.%m.%Y-%Hh %Mm")}')""")
                                sqlite_connection.commit()
                                plus = (it.tableWidget().item(it.row(), 5)).text()
                                if plus == "":
                                    (it.tableWidget().item(it.row(), 5)).setText(str(int(0) + int(let)))
                                else:
                                    (it.tableWidget().item(it.row(), 5)).setText(str(int(plus) + int(let)))
                            except:
                                pass
                            app.close()

                        def end():
                            app.close()

                        form.pushButton.clicked.connect(like)
                        form.pushButton_2.clicked.connect(end)
                        app.exec()
                    if action == low:
                        Form, App = uic.loadUiType("minus.ui")
                        app = QDialog(self)
                        form = Form()
                        form.setupUi(app)
                        app.show()

                        def like():
                            let = form.lineEdit.text()
                            iter = it.text()
                            try:
                                sqlite_connection = sqlite3.connect("id.db")
                                username = cursor_01.execute(f"""SELECT login FROM autorization WHERE online='True'""").fetchone()
                                cursor = sqlite_connection.cursor()
                                cursor.execute(f"""UPDATE orders SET kol=(kol -'{let}') WHERE orderid='{iter}'""")
                                cursor.execute(f"""UPDATE orders SET userid=(userid - '{let}') WHERE orderid='{iter}'""")
                                cursor.execute(f"""INSERT INTO plus_del VALUES ('{iter}','{username[0]}',-'{let}','{today.strftime("%d.%m.%Y-%Hh %Mm")}')""")
                                sqlite_connection.commit()
                                minus = (it.tableWidget().item(it.row(), 5)).text()
                                (it.tableWidget().item(it.row(), 5)).setText(str(int(minus) - int(let)))
                            except:
                                pass
                            app.close()

                        def end():
                            app.close()

                        form.pushButton.clicked.connect(like)
                        form.pushButton_2.clicked.connect(end)
                        app.exec()
                    if action == detal:
                        if it.column() == 2:
                            iter = it.text()
                            Form, App = uic.loadUiType("detali.ui")
                            app = QtWidgets.QDialog(self)
                            form = Form()
                            form.setupUi(app)
                            app.setWindowFlags(app.windowFlags() |
                                                QtCore.Qt.WindowMinimizeButtonHint |
                                                QtCore.Qt.WindowSystemMenuHint)
                            app.show()
                            username = cursor_01.execute(
                                f"""SELECT login FROM autorization WHERE online='True'""").fetchone()
                            value = cursor_02.execute(
                                f"""SELECT font,title_font,color_table,color_table_selection,width_loko,width_detal,width_masters,image_size,rgb,rgb_selection FROM setting WHERE user='{username[0]}'""").fetchone()
                            font = QtGui.QFont()
                            font.setFamily("Times New Roman")
                            font.setPointSize(value[0])
                            form.tableWidget.setFont(font)
                            form.tableWidget.setStyleSheet("QTableWidget {\n"
                                    "border-radius: 15px;\n"
                                    "background-color: rgb(72, 73, 74)}\n"
                                    "\n"
                                    "QHeaderView::section {\n"
                                    f"    background-color: {value[8]};\n"
                                    "    padding: 4px;\n"
                                    f"    font-size: {value[1]}pt;\n"
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
                                    f"    background-color: {value[8]};\n"
                                    "}\n"
                                    "QTableWidget::item:selected {\n"
                                    f"    background-color: {value[9]};\n"
                                    "    color:rgb(0, 0, 0);\n"
                                    "}")
                            sqlite_connection = sqlite3.connect("id.db")
                            cursor = sqlite_connection.cursor()
                            sqlite_connection.commit()
                            users = cursor.execute(
                                f"""SELECT datas,loko,repair,userid FROM TO1 WHERE userid like '%{iter}%'""")
                            low = users.fetchall()
                            users1 = cursor.execute(
                                f"""SELECT datas,loko,repair,userid FROM TO2 WHERE userid like '%{iter}%'""")
                            low1 = users1.fetchall()
                            users2 = cursor.execute(
                                f"""SELECT datas,loko,repair,userid FROM TO3 WHERE userid like '%{iter}%'""")
                            low2 = users2.fetchall()
                            users3 = cursor.execute(
                                f"""SELECT datas,loko,repair,userid FROM TO4 WHERE userid like '%{iter}%'""")
                            low3 = users3.fetchall()
                            users4 = cursor.execute(
                                f"""SELECT datas,loko,repair,userid FROM TO5 WHERE userid like '%{iter}%'""")
                            low4 = users4.fetchall()
                            users5 = cursor.execute(
                                f"""SELECT datas,loko,repair,userid FROM TO6 WHERE userid like '%{iter}%'""")
                            low5 = users5.fetchall()
                            users6 = cursor.execute(
                                f"""SELECT datas,loko,repair,userid FROM TO7 WHERE userid like '%{iter}%'""")
                            low6 = users6.fetchall()
                            users7 = cursor.execute(
                                f"""SELECT datas,loko,repair,userid FROM TO8 WHERE userid like '%{iter}%'""")
                            low7 = users7.fetchall()
                            pow = low + low1 + low2 + low3 + low4 + low5 + low6 + low7
                            like = []
                            for n in range(len(pow)):
                                i = 0
                                try:
                                    pux = pow[n][3].split(",")
                                except:
                                    pux = pow[n][3]
                                try:
                                    for r in range(len(pux)):
                                        trying = pux[r]
                                        if iter in trying:
                                            a = trying.split("_")
                                            d = str((a[0] + ",") * int(a[1]))
                                            c = d.split(",")
                                            for p in range(len(c)):
                                                l = str(c[p]).replace(' ','')
                                                if str(iter) == l:
                                                    i += 1
                                    if i > 0:
                                        like.append(i)
                                except:
                                    i = 1
                                    like.append(i)
                            cursor.execute("""DELETE FROM poll WHERE ID > -1""")
                            sqlite_connection.commit()
                            for r in range(len(like)):
                                cursor.execute("""INSERT INTO poll VALUES (NULL,'','','','')""")
                            sqlite_connection.commit()
                            for r in range(len(like)):
                                try:
                                    try:
                                        if datetime.datetime.strptime(str(pow[r][0]), '%d.%m.%Y'):
                                            cursor.execute(
                                        f"""UPDATE poll SET one='{datetime.datetime.strptime(str(pow[r][0]), '%d.%m.%Y').strftime('%Y-%m-%d')}',two='{str(pow[r][1])}',three='{str(pow[r][2])}',foo='{str(like[r])}' WHERE ID='{r + 1}'""")
                                    except:
                                        cursor.execute(
                                        f"""UPDATE poll SET one='{datetime.datetime.strptime(str(pow[r][0]), '%d.%m.%y').strftime('%Y-%m-%d')}',two='{str(pow[r][1])}',three='{str(pow[r][2])}',foo='{str(like[r])}' WHERE ID='{r + 1}'""")
                                except:
                                    pass
                            sqlite_connection.commit()

                            def all():
                                form.tableWidget.setRowCount(0)
                                users00 = cursor.execute(
                                    f"""SELECT one,two,three,foo FROM poll ORDER BY one""")
                                for row_number8, order in enumerate(users00):
                                    form.tableWidget.insertRow(row_number8)
                                    for column_number, data in enumerate(order):
                                        cell = QtWidgets.QTableWidgetItem(str(data))
                                        form.tableWidget.setItem(row_number8, column_number, cell)
                                        cell.setTextAlignment(Qt.AlignCenter)
                                        form.tableWidget.horizontalHeader().setSectionResizeMode(0,
                                                                                                 QtWidgets.QHeaderView.Stretch)
                                        form.tableWidget.horizontalHeader().setSectionResizeMode(1,
                                                                                                 QtWidgets.QHeaderView.Stretch)
                                        form.tableWidget.horizontalHeader().setSectionResizeMode(2,
                                                                                                 QtWidgets.QHeaderView.Stretch)
                                        form.tableWidget.horizontalHeader().setSectionResizeMode(3,
                                                                                                 QtWidgets.QHeaderView.Stretch)
                                    form.tableWidget.selectRow(row_number8)
                                form.tableWidget.clearSelection()

                            def plan():
                                form.tableWidget.setRowCount(0)
                                users00 = cursor.execute(
                                    f"""SELECT one,two,three,foo FROM poll WHERE three='План' ORDER BY one""")
                                for row_number8, order in enumerate(users00):
                                    form.tableWidget.insertRow(row_number8)
                                    for column_number, data in enumerate(order):
                                        cell = QtWidgets.QTableWidgetItem(str(data))
                                        form.tableWidget.setItem(row_number8, column_number, cell)
                                        cell.setTextAlignment(Qt.AlignCenter)
                                        form.tableWidget.horizontalHeader().setSectionResizeMode(0,
                                                                                                 QtWidgets.QHeaderView.Stretch)
                                        form.tableWidget.horizontalHeader().setSectionResizeMode(1,
                                                                                                 QtWidgets.QHeaderView.Stretch)
                                        form.tableWidget.horizontalHeader().setSectionResizeMode(2,
                                                                                                 QtWidgets.QHeaderView.Stretch)
                                        form.tableWidget.horizontalHeader().setSectionResizeMode(3,
                                                                                                 QtWidgets.QHeaderView.Stretch)
                                    form.tableWidget.selectRow(row_number8)
                                form.tableWidget.clearSelection()

                            def vneplan():
                                form.tableWidget.setRowCount(0)
                                users00 = cursor.execute(
                                    f"""SELECT one,two,three,foo FROM poll WHERE three='Внеплан' ORDER BY one""")
                                for row_number8, order in enumerate(users00):
                                    form.tableWidget.insertRow(row_number8)
                                    for column_number, data in enumerate(order):
                                        cell = QtWidgets.QTableWidgetItem(str(data))
                                        form.tableWidget.setItem(row_number8, column_number, cell)
                                        cell.setTextAlignment(Qt.AlignCenter)
                                        form.tableWidget.horizontalHeader().setSectionResizeMode(0,
                                                                                                 QtWidgets.QHeaderView.Stretch)
                                        form.tableWidget.horizontalHeader().setSectionResizeMode(1,
                                                                                                 QtWidgets.QHeaderView.Stretch)
                                        form.tableWidget.horizontalHeader().setSectionResizeMode(2,
                                                                                                 QtWidgets.QHeaderView.Stretch)
                                        form.tableWidget.horizontalHeader().setSectionResizeMode(3,
                                                                                                 QtWidgets.QHeaderView.Stretch)
                                    form.tableWidget.selectRow(row_number8)
                                form.tableWidget.clearSelection()

                            def repair():
                                form.tableWidget.setRowCount(0)
                                users00 = cursor.execute(
                                    f"""SELECT one,two,three,foo FROM poll WHERE three='Ремонт' ORDER BY one""")
                                for row_number8, order in enumerate(users00):
                                    form.tableWidget.insertRow(row_number8)
                                    for column_number, data in enumerate(order):
                                        cell = QtWidgets.QTableWidgetItem(str(data))
                                        form.tableWidget.setItem(row_number8, column_number, cell)
                                        cell.setTextAlignment(Qt.AlignCenter)
                                        form.tableWidget.horizontalHeader().setSectionResizeMode(0,
                                                                                                 QtWidgets.QHeaderView.Stretch)
                                        form.tableWidget.horizontalHeader().setSectionResizeMode(1,
                                                                                                 QtWidgets.QHeaderView.Stretch)
                                        form.tableWidget.horizontalHeader().setSectionResizeMode(2,
                                                                                                 QtWidgets.QHeaderView.Stretch)
                                        form.tableWidget.horizontalHeader().setSectionResizeMode(3,
                                                                                                 QtWidgets.QHeaderView.Stretch)
                                    form.tableWidget.selectRow(row_number8)
                                form.tableWidget.clearSelection()

                            all()
                            hour = cursor.execute(
                                f"""SELECT tip FROM orders WHERE orderid='{iter}'""")
                            intel = hour.fetchall()
                            form.lineEdit.setText(str(intel[0][0]))
                            form.lineEdit_2.setText(str(iter))
                            form.pushButton.clicked.connect(all)
                            form.pushButton_2.clicked.connect(plan)
                            form.pushButton_3.clicked.connect(vneplan)
                            form.pushButton_4.clicked.connect(repair)
                            app.exec()
                    if action == image:
                        apps = QtWidgets.QDialog(self)
                        wb_patch = \
                            QtWidgets.QFileDialog.getOpenFileName(self, "Выбор фотки детали", os.getcwd(),
                                                                  "Image (*.png *.jpg *.jpeg)")[0]
                        apps.close()
                        if wb_patch:
                            path_dir = os.getcwd()
                            path_dir = os.path.split(path_dir)[1]
                            foto = wb_patch.split(f'{path_dir}/')[1]
                            iter = it.text()
                            sqlite_connection = sqlite3.connect("id.db")
                            cursor = sqlite_connection.cursor()
                            cursor.execute(f"""UPDATE orders SET foto='{foto}' WHERE orderid='{iter}'""")
                            sqlite_connection.commit()
                            for i in range(1):
                                if str(foto) != "None":
                                    label = QLabel()
                                    label.setText("")
                                    label.setScaledContents(True)
                                    pix = QPixmap(f"{foto}")
                                    label.setPixmap(pix)
                                    it.tableWidget().setCellWidget(it.row(), 1, label)
                    if action == image_del:
                        iter = it.text()
                        sqlite_connection = sqlite3.connect("id.db")
                        cursor = sqlite_connection.cursor()
                        cursor.execute(f"""UPDATE orders SET foto='' WHERE orderid='{iter}'""")
                        sqlite_connection.commit()
                        label = QLabel()
                        label.setText("")
                        it.tableWidget().setCellWidget(it.row(), 1, label)
                if it.column() == 4:
                    fuck = QtWidgets.QMenu(self)
                    fuck.setGeometry(QtCore.QRect(20, 20, 20, 20))
                    sqlite_connection = sqlite3.connect("id.db")
                    cursor = sqlite_connection.cursor()
                    users = cursor.execute("""SELECT models FROM models_loko""")
                    pickle = users.fetchall()
                    add = []
                    for number, lul in enumerate(pickle):
                        a = fuck.addAction(str(pickle[number][0]))
                        add.append(a)
                    action = fuck.exec_(self.mapToGlobal(e.pos()))
                    for number, lul in enumerate(pickle):
                        if action == add[number]:
                            if it.text() == "":
                                it.setText(str(pickle[number][0]))
                            else:
                                it.setText((str(it.text()) + "," + str(pickle[number][0])).replace(",,",","))
            if e.button():
                if it.column() == 1:
                    it.tableWidget().setEditTriggers(QTableWidgetItem.NoEditTriggers)
                if it.column() == 5:
                    it.tableWidget().setEditTriggers(QTableWidgetItem.NoEditTriggers)
            QtWidgets.QTableWidget.mousePressEvent(self, e)
        except:
            pass
    def keyPressEvent(self, e):
        try:
            if e.key():
                e.nativeVirtualKey().setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
                )
            QtWidgets.QTableWidget.keyPressEvent(self, e)
        except:
            pass

class TestMasters(QtWidgets.QTableWidget):
    def __init__(self, parent=None):
        QtWidgets.QTableWidget.__init__(self, parent)  ##Test

    def mousePressEvent(self, e):
        it = self.itemAt(e.pos())
        try:
            if e.button() == Qt.RightButton:
                if it.column() == 0:
                    fuck = QtWidgets.QMenu(self)
                    fuck.setGeometry(QtCore.QRect(20, 20, 20, 20))
                    low = fuck.addAction("Удалить строчку")
                    action = fuck.exec_(self.mapToGlobal(e.pos()))
                    if action == low:
                        rama = it.tableWidget()
                        sqlite_connection = sqlite3.connect("id.db")
                        cursor = sqlite_connection.cursor()
                        iter = it.text()
                        cursor.execute(f"""DELETE FROM masters WHERE ID='{iter}'""")
                        sqlite_connection.commit()
                        it.tableWidget().setRowCount(0)
                        users = cursor.execute("SELECT * FROM masters")
                        for row_number9, order in enumerate(users):
                            rama.insertRow(row_number9)
                            for column_number, data in enumerate(order):
                                cell = QtWidgets.QTableWidgetItem(str(data))
                                rama.setItem(row_number9, column_number, cell)
                                cell.setTextAlignment(Qt.AlignCenter)
            QtWidgets.QTableWidget.mousePressEvent(self, e)
        except:
            pass

class Test_Stock_1(QtWidgets.QTableWidget):
    def __init__(self, parent=None):
        QtWidgets.QTableWidget.__init__(self, parent)  ##Test

    def mousePressEvent(self, e):
        it = self.itemAt(e.pos())
        try:
            if e.button() == Qt.RightButton:
                if it.column() == 0:
                    fuck = QtWidgets.QMenu(self)
                    fuck.setGeometry(QtCore.QRect(20, 20, 20, 20))
                    low = fuck.addAction("Удалить строчку")
                    action = fuck.exec_(self.mapToGlobal(e.pos()))
                    if action == low:
                        rama = it.tableWidget()
                        sqlite_connection = sqlite3.connect("stok.db")
                        cursor = sqlite_connection.cursor()
                        iter = it.text()
                        cursor.execute(f"""DELETE FROM rolling_stock WHERE ID='{iter}'""") ###
                        sqlite_connection.commit()
                        it.tableWidget().setRowCount(0)
                        users = cursor.execute("SELECT * FROM rolling_stock") ###
                        for row_number, order in enumerate(users):
                            rama.insertRow(row_number)
                            for column_number, data in enumerate(order):
                                cell = QtWidgets.QTableWidgetItem(str(data))
                                rama.setItem(row_number, column_number, cell)
                                cell.setTextAlignment(Qt.AlignCenter)
                if it.column() == 1:
                    levels = cursor_01.execute(
                    f"""SELECT levels FROM autorization WHERE online='True'""").fetchone()
                    if levels[0] == "2" or  levels[0] == "3":
                        fuck = QtWidgets.QMenu(self)
                        fuck.setGeometry(QtCore.QRect(20, 20, 20, 20))
                        detal_plus = fuck.addAction("Добавить несколько деталей")
                        detal_minus = fuck.addAction("Убрать несколько деталей")
                        invent = fuck.addAction("Инвентаризация детали")
                        detal = fuck.addAction("О детали")
                        action = fuck.exec_(self.mapToGlobal(e.pos()))
                    if action == detal_plus:
                        Form, App = uic.loadUiType("plus.ui")
                        app = QDialog(self)
                        form = Form()
                        form.setupUi(app)
                        app.show()

                        def like():
                            let = form.lineEdit.text()
                            iter = it.text()
                            try:
                                sqlite_connection = sqlite3.connect("stok.db")
                                cursor = sqlite_connection.cursor()
                                let_check = str(let).replace("-","")
                                username = cursor_01.execute(
                                f"""SELECT login FROM autorization WHERE online='True'""").fetchone()
                                if let_check.isdigit():
                                    cursor.execute(f"""UPDATE rolling_stock SET quantity=(quantity + '{let}') WHERE articul='{iter}'""")
                                    cursor.execute(f"""INSERT INTO all_invent_rolling VALUES ('{iter}','{username[0]}','{let}','{today.strftime("%d.%m.%Y-%Hh %Mm")}')""")
                                    sqlite_connection.commit()
                                plus = (it.tableWidget().item(it.row(), 3)).text()
                                if plus == "":
                                    (it.tableWidget().item(it.row(), 3)).setText(str(int(0) + int(let)))
                                else:
                                    (it.tableWidget().item(it.row(), 3)).setText(str(int(plus) + int(let)))
                            except:
                                pass
                            app.close()

                        def end():
                            app.close()

                        form.pushButton.clicked.connect(like)
                        form.pushButton_2.clicked.connect(end)
                        app.exec()
                    if action == detal_minus:
                        Form, App = uic.loadUiType("minus.ui")
                        app = QDialog(self)
                        form = Form()
                        form.setupUi(app)
                        app.show()

                        def like():
                            let = form.lineEdit.text()
                            iter = it.text()
                            try:
                                sqlite_connection = sqlite3.connect("stok.db")
                                cursor = sqlite_connection.cursor()
                                let_check = str(let).replace("-","")
                                username = cursor_01.execute(
                                f"""SELECT login FROM autorization WHERE online='True'""").fetchone()
                                if let_check.isdigit():
                                    cursor.execute(f"""UPDATE rolling_stock SET quantity=(quantity - '{let}') WHERE articul='{iter}'""")
                                    cursor.execute(f"""INSERT INTO all_invent_rolling VALUES ('{iter}','{username[0]}',-'{let}','{today.strftime("%d.%m.%Y-%Hh %Mm")}')""")
                                    sqlite_connection.commit()
                                minus = (it.tableWidget().item(it.row(), 3)).text()
                                (it.tableWidget().item(it.row(), 3)).setText(str(int(minus) - int(let)))
                            except:
                                pass
                            app.close()

                        def end():
                            app.close()

                        form.pushButton.clicked.connect(like)
                        form.pushButton_2.clicked.connect(end)
                        app.exec()
                    if action == detal:
                        iter = it.text()
                        Forms = QtWidgets.QDialog(self)
                        form = Stock()
                        form.setupUi(Forms)
                        Forms.setWindowFlags(Forms.windowFlags() |
                                            QtCore.Qt.WindowMinimizeButtonHint |
                                            QtCore.Qt.WindowSystemMenuHint)
                        Forms.show()
                        sqlite_connection = sqlite3.connect("stok.db")
                        cursor = sqlite_connection.cursor()
                        form.tableWidget.horizontalHeader().setSectionResizeMode(0,
                                                                                 QtWidgets.QHeaderView.Stretch)
                        form.tableWidget.horizontalHeader().setSectionResizeMode(1,
                                                                                 QtWidgets.QHeaderView.ResizeToContents)
                        form.tableWidget.horizontalHeader().setSectionResizeMode(2,
                                                                                 QtWidgets.QHeaderView.ResizeToContents)
                        form.lineEdit.setText(str(iter)) ##Артикул
                        form.lineEdit_2.setText(str(it.tableWidget().item(it.row(),2).text())) ##Наименование

                        def all():
                            global row_number021
                            form.tableWidget.setRowCount(0)
                            users = cursor.execute(
                                f"""SELECT master,plus_del,datas FROM all_invent_rolling WHERE articul='{iter}' ORDER BY DATE('%d.%m.%Y')""")
                            for row_number021, order in enumerate(users):
                                form.tableWidget.insertRow(row_number021)
                                for column_number, data in enumerate(order):
                                    cell = QtWidgets.QTableWidgetItem(str(data))
                                    form.tableWidget.setItem(row_number021, column_number, cell)
                                    cell.setTextAlignment(Qt.AlignCenter)
                                    form.tableWidget.horizontalHeader().setSectionResizeMode(0,
                                                                                             QtWidgets.QHeaderView.Stretch)
                                    form.tableWidget.horizontalHeader().setSectionResizeMode(1,
                                                                                             QtWidgets.QHeaderView.ResizeToContents)
                                    form.tableWidget.horizontalHeader().setSectionResizeMode(2,
                                                                                             QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.selectRow(row_number021)
                                pool = int(row_number021 + 1)
                                form.label_kol.setText(f"Количество записей: {str(pool)}")
                            try:
                                form.tableWidget.scrollToItem(form.tableWidget.item(row_number021, 0), QAbstractItemView.PositionAtTop)
                                form.tableWidget.selectRow(row_number021)
                                form.tableWidget.clearSelection()
                            except:
                                pass


                        def clicks():
                            row_num = form.tableWidget.currentRow()
                            form.tableWidget.selectRow(row_num)
                        form.tableWidget.clicked.connect(clicks)


                        def minus():
                            sqlite_connection = sqlite3.connect("stok.db")
                            cursor = sqlite_connection.cursor()
                            row_num = form.tableWidget.currentRow()
                            list_del = []
                            for j in range(form.tableWidget.columnCount()):
                                poof = form.tableWidget.item(row_num, j).text()
                                list_del.append(poof)
                            cursor.execute(f"""DELETE FROM all_invent_rolling WHERE articul='{iter}' AND master='{list_del[0]}' AND plus_del='{list_del[1]}' AND datas='{list_del[2]}'""")
                            sqlite_connection.commit()
                            form.tableWidget.setRowCount(0)
                            all()

                        all()

                        form.pushButton_minus.clicked.connect(minus)
                        Forms.exec()
                    if action == invent:
                        iter = it.text()
                        Form, App = uic.loadUiType("invent.ui")
                        app = QDialog(self)
                        form = Form()
                        form.setupUi(app)
                        app.show()
                        def like():
                            let = form.lineEdit.text()
                            try:
                                sqlite_connection = sqlite3.connect("stok.db")
                                cursor = sqlite_connection.cursor()
                                text_invent = "Инвентаризация"
                                let_check = str(let).replace("-","")
                                #username = cursor_01.execute(
                                #f"""SELECT login FROM autorization WHERE online='True'""").fetchone()
                                if let_check.isdigit():
                                    cursor.execute(f"""UPDATE rolling_stock SET quantity=('{let}') WHERE articul='{iter}'""")
                                    cursor.execute(f"""INSERT INTO all_invent_rolling VALUES ('{iter}','{text_invent}','{let}','{today.strftime("%d.%m.%Y-%Hh %Mm")}')""")
                                    sqlite_connection.commit()
                                (it.tableWidget().item(it.row(), 3)).setText(str(int(let)))
                            except:
                                pass
                            app.close()
                        def end():
                            app.close()
                        form.pushButton.clicked.connect(like)
                        form.pushButton_2.clicked.connect(end)
                        app.exec()
            if e.button():
                if it.column() == 3:
                    it.tableWidget().setEditTriggers(QTableWidgetItem.NoEditTriggers)
            QtWidgets.QTableWidget.mousePressEvent(self, e)
        except:
            pass
    def keyPressEvent(self, e):
        try:
            if e.key():
                e.nativeVirtualKey().setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
                )
            QtWidgets.QTableWidget.keyPressEvent(self, e)
        except:
            pass

class Test_Stock_2(QtWidgets.QTableWidget):
    def __init__(self, parent=None):
        QtWidgets.QTableWidget.__init__(self, parent)  ##Test

    def mousePressEvent(self, e):
        it = self.itemAt(e.pos())
        try:
            if e.button() == Qt.RightButton:
                if it.column() == 0:
                    fuck = QtWidgets.QMenu(self)
                    fuck.setGeometry(QtCore.QRect(20, 20, 20, 20))
                    low = fuck.addAction("Удалить строчку")
                    action = fuck.exec_(self.mapToGlobal(e.pos()))
                    if action == low:
                        rama = it.tableWidget()
                        sqlite_connection = sqlite3.connect("stok.db")
                        cursor = sqlite_connection.cursor()
                        iter = it.text()
                        cursor.execute(f"""DELETE FROM electrical_engineering WHERE ID='{iter}'""") ###
                        sqlite_connection.commit()
                        it.tableWidget().setRowCount(0)
                        users = cursor.execute("SELECT * FROM electrical_engineering") ###
                        for row_number, order in enumerate(users):
                            rama.insertRow(row_number)
                            for column_number, data in enumerate(order):
                                cell = QtWidgets.QTableWidgetItem(str(data))
                                rama.setItem(row_number, column_number, cell)
                                cell.setTextAlignment(Qt.AlignCenter)
                if it.column() == 1:
                    levels = cursor_01.execute(
                    f"""SELECT levels FROM autorization WHERE online='True'""").fetchone()
                    if levels[0] == "2" or  levels[0] == "3":
                        fuck = QtWidgets.QMenu(self)
                        fuck.setGeometry(QtCore.QRect(20, 20, 20, 20))
                        detal_plus = fuck.addAction("Добавить несколько деталей")
                        detal_minus = fuck.addAction("Убрать несколько деталей")
                        invent = fuck.addAction("Инвентаризация детали")
                        detal = fuck.addAction("О детали")
                        action = fuck.exec_(self.mapToGlobal(e.pos()))
                    if action == detal_plus:
                        Form, App = uic.loadUiType("plus.ui")
                        app = QDialog(self)
                        form = Form()
                        form.setupUi(app)
                        app.show()

                        def like():
                            let = form.lineEdit.text()
                            iter = it.text()
                            try:
                                sqlite_connection = sqlite3.connect("stok.db")
                                cursor = sqlite_connection.cursor()
                                let_check = str(let).replace("-","")
                                username = cursor_01.execute(
                                f"""SELECT login FROM autorization WHERE online='True'""").fetchone()
                                if let_check.isdigit():
                                    cursor.execute(f"""UPDATE electrical_engineering SET quantity=(quantity + '{let}') WHERE articul='{iter}'""")
                                    cursor.execute(f"""INSERT INTO all_invent_electrical VALUES ('{iter}','{username[0]}','{let}','{today.strftime("%d.%m.%Y-%Hh %Mm")}')""")
                                    sqlite_connection.commit()
                                plus = (it.tableWidget().item(it.row(), 3)).text()
                                if plus == "":
                                    (it.tableWidget().item(it.row(), 3)).setText(str(int(0) + int(let)))
                                else:
                                    (it.tableWidget().item(it.row(), 3)).setText(str(int(plus) + int(let)))
                            except:
                                pass
                            app.close()

                        def end():
                            app.close()

                        form.pushButton.clicked.connect(like)
                        form.pushButton_2.clicked.connect(end)
                        app.exec()
                    if action == detal_minus:
                        Form, App = uic.loadUiType("minus.ui")
                        app = QDialog(self)
                        form = Form()
                        form.setupUi(app)
                        app.show()

                        def like():
                            let = form.lineEdit.text()
                            iter = it.text()
                            try:
                                sqlite_connection = sqlite3.connect("stok.db")
                                cursor = sqlite_connection.cursor()
                                let_check = str(let).replace("-","")
                                username = cursor_01.execute(
                                f"""SELECT login FROM autorization WHERE online='True'""").fetchone()
                                if let_check.isdigit():
                                    cursor.execute(f"""UPDATE electrical_engineering SET quantity=(quantity - '{let}') WHERE articul='{iter}'""")
                                    cursor.execute(f"""INSERT INTO all_invent_electrical VALUES ('{iter}','{username[0]}',-'{let}','{today.strftime("%d.%m.%Y-%Hh %Mm")}')""")
                                    sqlite_connection.commit()
                                minus = (it.tableWidget().item(it.row(), 3)).text()
                                (it.tableWidget().item(it.row(), 3)).setText(str(int(minus) - int(let)))
                            except:
                                pass
                            app.close()

                        def end():
                            app.close()

                        form.pushButton.clicked.connect(like)
                        form.pushButton_2.clicked.connect(end)
                        app.exec()
                    if action == detal:
                        iter = it.text()
                        Forms = QtWidgets.QDialog(self)
                        form = Stock()
                        form.setupUi(Forms)
                        Forms.setWindowFlags(Forms.windowFlags() |
                                            QtCore.Qt.WindowMinimizeButtonHint |
                                            QtCore.Qt.WindowSystemMenuHint)
                        Forms.show()
                        sqlite_connection = sqlite3.connect("stok.db")
                        cursor = sqlite_connection.cursor()
                        form.tableWidget.horizontalHeader().setSectionResizeMode(0,
                                                                                 QtWidgets.QHeaderView.Stretch)
                        form.tableWidget.horizontalHeader().setSectionResizeMode(1,
                                                                                 QtWidgets.QHeaderView.ResizeToContents)
                        form.tableWidget.horizontalHeader().setSectionResizeMode(2,
                                                                                 QtWidgets.QHeaderView.ResizeToContents)
                        form.lineEdit.setText(str(iter)) ##Артикул
                        form.lineEdit_2.setText(str(it.tableWidget().item(it.row(),2).text())) ##Наименование

                        def all():
                            global row_number021
                            form.tableWidget.setRowCount(0)
                            users = cursor.execute(
                                f"""SELECT master,plus_del,datas FROM all_invent_electrical WHERE articul='{iter}' ORDER BY DATE('%d.%m.%Y')""")
                            for row_number021, order in enumerate(users):
                                form.tableWidget.insertRow(row_number021)
                                for column_number, data in enumerate(order):
                                    cell = QtWidgets.QTableWidgetItem(str(data))
                                    form.tableWidget.setItem(row_number021, column_number, cell)
                                    cell.setTextAlignment(Qt.AlignCenter)
                                    form.tableWidget.horizontalHeader().setSectionResizeMode(0,
                                                                                             QtWidgets.QHeaderView.Stretch)
                                    form.tableWidget.horizontalHeader().setSectionResizeMode(1,
                                                                                             QtWidgets.QHeaderView.ResizeToContents)
                                    form.tableWidget.horizontalHeader().setSectionResizeMode(2,
                                                                                             QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.selectRow(row_number021)
                                pool = int(row_number021 + 1)
                                form.label_kol.setText(f"Количество записей: {str(pool)}")
                            try:
                                form.tableWidget.scrollToItem(form.tableWidget.item(row_number021, 0), QAbstractItemView.PositionAtTop)
                                form.tableWidget.selectRow(row_number021)
                                form.tableWidget.clearSelection()
                            except:
                                pass


                        def clicks():
                            row_num = form.tableWidget.currentRow()
                            form.tableWidget.selectRow(row_num)
                        form.tableWidget.clicked.connect(clicks)


                        def minus():
                            sqlite_connection = sqlite3.connect("stok.db")
                            cursor = sqlite_connection.cursor()
                            row_num = form.tableWidget.currentRow()
                            list_del = []
                            for j in range(form.tableWidget.columnCount()):
                                poof = form.tableWidget.item(row_num, j).text()
                                list_del.append(poof)
                            cursor.execute(f"""DELETE FROM all_invent_electrical WHERE articul='{iter}' AND master='{list_del[0]}' AND plus_del='{list_del[1]}' AND datas='{list_del[2]}'""")
                            sqlite_connection.commit()
                            form.tableWidget.setRowCount(0)
                            all()

                        all()

                        form.pushButton_minus.clicked.connect(minus)
                        Forms.exec()
                    if action == invent:
                        iter = it.text()
                        Form, App = uic.loadUiType("invent.ui")
                        app = QDialog(self)
                        form = Form()
                        form.setupUi(app)
                        app.show()
                        def like():
                            let = form.lineEdit.text()
                            try:
                                sqlite_connection = sqlite3.connect("stok.db")
                                cursor = sqlite_connection.cursor()
                                text_invent = "Инвентаризация"
                                let_check = str(let).replace("-","")
                                #username = cursor_01.execute(
                                #f"""SELECT login FROM autorization WHERE online='True'""").fetchone()
                                if let_check.isdigit():
                                    cursor.execute(f"""UPDATE electrical_engineering SET quantity=('{let}') WHERE articul='{iter}'""")
                                    cursor.execute(f"""INSERT INTO all_invent_electrical VALUES ('{iter}','{text_invent}','{let}','{today.strftime("%d.%m.%Y-%Hh %Mm")}')""")
                                    sqlite_connection.commit()
                                (it.tableWidget().item(it.row(), 3)).setText(str(int(let)))
                            except:
                                pass
                            app.close()
                        def end():
                            app.close()
                        form.pushButton.clicked.connect(like)
                        form.pushButton_2.clicked.connect(end)
                        app.exec()
            if e.button():
                if it.column() == 3:
                    it.tableWidget().setEditTriggers(QTableWidgetItem.NoEditTriggers)
            QtWidgets.QTableWidget.mousePressEvent(self, e)
        except:
            pass
    def keyPressEvent(self, e):
        try:
            if e.key():
                e.nativeVirtualKey().setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
                )
            QtWidgets.QTableWidget.keyPressEvent(self, e)
        except:
            pass

class Test_Stock_3(QtWidgets.QTableWidget):
    def __init__(self, parent=None):
        QtWidgets.QTableWidget.__init__(self, parent)  ##Test

    def mousePressEvent(self, e):
        it = self.itemAt(e.pos())
        try:
            if e.button() == Qt.RightButton:
                if it.column() == 0:
                    fuck = QtWidgets.QMenu(self)
                    fuck.setGeometry(QtCore.QRect(20, 20, 20, 20))
                    low = fuck.addAction("Удалить строчку")
                    action = fuck.exec_(self.mapToGlobal(e.pos()))
                    if action == low:
                        rama = it.tableWidget()
                        sqlite_connection = sqlite3.connect("stok.db")
                        cursor = sqlite_connection.cursor()
                        iter = it.text()
                        cursor.execute(f"""DELETE FROM travel_materials WHERE ID='{iter}'""") ###
                        sqlite_connection.commit()
                        it.tableWidget().setRowCount(0)
                        users = cursor.execute("SELECT * FROM travel_materials") ###
                        for row_number, order in enumerate(users):
                            rama.insertRow(row_number)
                            for column_number, data in enumerate(order):
                                cell = QtWidgets.QTableWidgetItem(str(data))
                                rama.setItem(row_number, column_number, cell)
                                cell.setTextAlignment(Qt.AlignCenter)
                if it.column() == 1:
                    levels = cursor_01.execute(
                    f"""SELECT levels FROM autorization WHERE online='True'""").fetchone()
                    if levels[0] == "2" or  levels[0] == "3":
                        fuck = QtWidgets.QMenu(self)
                        fuck.setGeometry(QtCore.QRect(20, 20, 20, 20))
                        detal_plus = fuck.addAction("Добавить несколько деталей")
                        detal_minus = fuck.addAction("Убрать несколько деталей")
                        invent = fuck.addAction("Инвентаризация детали")
                        detal = fuck.addAction("О детали")
                        action = fuck.exec_(self.mapToGlobal(e.pos()))
                    if action == detal_plus:
                        Form, App = uic.loadUiType("plus.ui")
                        app = QDialog(self)
                        form = Form()
                        form.setupUi(app)
                        app.show()

                        def like():
                            let = form.lineEdit.text()
                            iter = it.text()
                            try:
                                sqlite_connection = sqlite3.connect("stok.db")
                                cursor = sqlite_connection.cursor()
                                let_check = str(let).replace("-","")
                                username = cursor_01.execute(
                                f"""SELECT login FROM autorization WHERE online='True'""").fetchone()
                                if let_check.isdigit():
                                    cursor.execute(f"""UPDATE travel_materials SET quantity=(quantity + '{let}') WHERE articul='{iter}'""")
                                    cursor.execute(f"""INSERT INTO all_invent_travel  VALUES ('{iter}','{username[0]}','{let}','{today.strftime("%d.%m.%Y-%Hh %Mm")}')""")
                                    sqlite_connection.commit()
                                plus = (it.tableWidget().item(it.row(), 3)).text()
                                if plus == "":
                                    (it.tableWidget().item(it.row(), 3)).setText(str(int(0) + int(let)))
                                else:
                                    (it.tableWidget().item(it.row(), 3)).setText(str(int(plus) + int(let)))
                            except:
                                pass
                            app.close()

                        def end():
                            app.close()

                        form.pushButton.clicked.connect(like)
                        form.pushButton_2.clicked.connect(end)
                        app.exec()
                    if action == detal_minus:
                        Form, App = uic.loadUiType("minus.ui")
                        app = QDialog(self)
                        form = Form()
                        form.setupUi(app)
                        app.show()

                        def like():
                            let = form.lineEdit.text()
                            iter = it.text()
                            try:
                                sqlite_connection = sqlite3.connect("stok.db")
                                cursor = sqlite_connection.cursor()
                                let_check = str(let).replace("-","")
                                username = cursor_01.execute(
                                f"""SELECT login FROM autorization WHERE online='True'""").fetchone()
                                if let_check.isdigit():
                                    cursor.execute(f"""UPDATE travel_materials SET quantity=(quantity - '{let}') WHERE articul='{iter}'""")
                                    cursor.execute(f"""INSERT INTO all_invent_travel VALUES ('{iter}','{username[0]}',-'{let}','{today.strftime("%d.%m.%Y-%Hh %Mm")}')""")
                                    sqlite_connection.commit()
                                minus = (it.tableWidget().item(it.row(), 3)).text()
                                (it.tableWidget().item(it.row(), 3)).setText(str(int(minus) - int(let)))
                            except:
                                pass
                            app.close()

                        def end():
                            app.close()

                        form.pushButton.clicked.connect(like)
                        form.pushButton_2.clicked.connect(end)
                        app.exec()
                    if action == detal:
                        iter = it.text()
                        Forms = QtWidgets.QDialog(self)
                        form = Stock()
                        form.setupUi(Forms)
                        Forms.setWindowFlags(Forms.windowFlags() |
                                            QtCore.Qt.WindowMinimizeButtonHint |
                                            QtCore.Qt.WindowSystemMenuHint)
                        Forms.show()
                        sqlite_connection = sqlite3.connect("stok.db")
                        cursor = sqlite_connection.cursor()
                        form.tableWidget.horizontalHeader().setSectionResizeMode(0,
                                                                                 QtWidgets.QHeaderView.Stretch)
                        form.tableWidget.horizontalHeader().setSectionResizeMode(1,
                                                                                 QtWidgets.QHeaderView.ResizeToContents)
                        form.tableWidget.horizontalHeader().setSectionResizeMode(2,
                                                                                 QtWidgets.QHeaderView.ResizeToContents)
                        form.lineEdit.setText(str(iter)) ##Артикул
                        form.lineEdit_2.setText(str(it.tableWidget().item(it.row(),2).text())) ##Наименование

                        def all():
                            global row_number021
                            form.tableWidget.setRowCount(0)
                            users = cursor.execute(
                                f"""SELECT master,plus_del,datas FROM all_invent_travel WHERE articul='{iter}' ORDER BY DATE('%d.%m.%Y')""")
                            for row_number021, order in enumerate(users):
                                form.tableWidget.insertRow(row_number021)
                                for column_number, data in enumerate(order):
                                    cell = QtWidgets.QTableWidgetItem(str(data))
                                    form.tableWidget.setItem(row_number021, column_number, cell)
                                    cell.setTextAlignment(Qt.AlignCenter)
                                    form.tableWidget.horizontalHeader().setSectionResizeMode(0,
                                                                                             QtWidgets.QHeaderView.Stretch)
                                    form.tableWidget.horizontalHeader().setSectionResizeMode(1,
                                                                                             QtWidgets.QHeaderView.ResizeToContents)
                                    form.tableWidget.horizontalHeader().setSectionResizeMode(2,
                                                                                             QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.selectRow(row_number021)
                                pool = int(row_number021 + 1)
                                form.label_kol.setText(f"Количество записей: {str(pool)}")
                            try:
                                form.tableWidget.scrollToItem(form.tableWidget.item(row_number021, 0), QAbstractItemView.PositionAtTop)
                                form.tableWidget.selectRow(row_number021)
                                form.tableWidget.clearSelection()
                            except:
                                pass


                        def clicks():
                            row_num = form.tableWidget.currentRow()
                            form.tableWidget.selectRow(row_num)
                        form.tableWidget.clicked.connect(clicks)


                        def minus():
                            sqlite_connection = sqlite3.connect("stok.db")
                            cursor = sqlite_connection.cursor()
                            row_num = form.tableWidget.currentRow()
                            list_del = []
                            for j in range(form.tableWidget.columnCount()):
                                poof = form.tableWidget.item(row_num, j).text()
                                list_del.append(poof)
                            cursor.execute(f"""DELETE FROM all_invent_travel WHERE articul='{iter}' AND master='{list_del[0]}' AND plus_del='{list_del[1]}' AND datas='{list_del[2]}'""")
                            sqlite_connection.commit()
                            form.tableWidget.setRowCount(0)
                            all()

                        all()

                        form.pushButton_minus.clicked.connect(minus)
                        Forms.exec()
                    if action == invent:
                        iter = it.text()
                        Form, App = uic.loadUiType("invent.ui")
                        app = QDialog(self)
                        form = Form()
                        form.setupUi(app)
                        app.show()
                        def like():
                            let = form.lineEdit.text()
                            try:
                                sqlite_connection = sqlite3.connect("stok.db")
                                cursor = sqlite_connection.cursor()
                                text_invent = "Инвентаризация"
                                let_check = str(let).replace("-","")
                                #username = cursor_01.execute(
                                #f"""SELECT login FROM autorization WHERE online='True'""").fetchone()
                                if let_check.isdigit():
                                    cursor.execute(f"""UPDATE travel_materials SET quantity=('{let}') WHERE articul='{iter}'""")
                                    cursor.execute(f"""INSERT INTO all_invent_travel VALUES ('{iter}','{text_invent}','{let}','{today.strftime("%d.%m.%Y-%Hh %Mm")}')""")
                                    sqlite_connection.commit()
                                (it.tableWidget().item(it.row(), 3)).setText(str(int(let)))
                            except:
                                pass
                            app.close()
                        def end():
                            app.close()
                        form.pushButton.clicked.connect(like)
                        form.pushButton_2.clicked.connect(end)
                        app.exec()
            if e.button():
                if it.column() == 3:
                    it.tableWidget().setEditTriggers(QTableWidgetItem.NoEditTriggers)
            QtWidgets.QTableWidget.mousePressEvent(self, e)
        except:
            pass
    def keyPressEvent(self, e):
        try:
            if e.key():
                e.nativeVirtualKey().setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
                )
            QtWidgets.QTableWidget.keyPressEvent(self, e)
        except:
            pass

class Test_Stock_4(QtWidgets.QTableWidget):
    def __init__(self, parent=None):
        QtWidgets.QTableWidget.__init__(self, parent)  ##Test

    def mousePressEvent(self, e):
        it = self.itemAt(e.pos())
        try:
            if e.button() == Qt.RightButton:
                if it.column() == 0:
                    fuck = QtWidgets.QMenu(self)
                    fuck.setGeometry(QtCore.QRect(20, 20, 20, 20))
                    low = fuck.addAction("Удалить строчку")
                    action = fuck.exec_(self.mapToGlobal(e.pos()))
                    if action == low:
                        rama = it.tableWidget()
                        sqlite_connection = sqlite3.connect("stok.db")
                        cursor = sqlite_connection.cursor()
                        iter = it.text()
                        cursor.execute(f"""DELETE FROM consumables WHERE ID='{iter}'""") ###
                        sqlite_connection.commit()
                        it.tableWidget().setRowCount(0)
                        users = cursor.execute("SELECT * FROM consumables") ###
                        for row_number, order in enumerate(users):
                            rama.insertRow(row_number)
                            for column_number, data in enumerate(order):
                                cell = QtWidgets.QTableWidgetItem(str(data))
                                rama.setItem(row_number, column_number, cell)
                                cell.setTextAlignment(Qt.AlignCenter)
                if it.column() == 1:
                    levels = cursor_01.execute(
                    f"""SELECT levels FROM autorization WHERE online='True'""").fetchone()
                    if levels[0] == "2" or  levels[0] == "3":
                        fuck = QtWidgets.QMenu(self)
                        fuck.setGeometry(QtCore.QRect(20, 20, 20, 20))
                        detal_plus = fuck.addAction("Добавить несколько деталей")
                        detal_minus = fuck.addAction("Убрать несколько деталей")
                        invent = fuck.addAction("Инвентаризация детали")
                        detal = fuck.addAction("О детали")
                        action = fuck.exec_(self.mapToGlobal(e.pos()))
                    if action == detal_plus:
                        Form, App = uic.loadUiType("plus.ui")
                        app = QDialog(self)
                        form = Form()
                        form.setupUi(app)
                        app.show()

                        def like():
                            let = form.lineEdit.text()
                            iter = it.text()
                            try:
                                sqlite_connection = sqlite3.connect("stok.db")
                                cursor = sqlite_connection.cursor()
                                let_check = str(let).replace("-","")
                                username = cursor_01.execute(
                                f"""SELECT login FROM autorization WHERE online='True'""").fetchone()
                                if let_check.isdigit():
                                    cursor.execute(f"""UPDATE consumables SET quantity=(quantity + '{let}') WHERE articul='{iter}'""")
                                    cursor.execute(f"""INSERT INTO all_invent_consumables VALUES ('{iter}','{username[0]}','{let}','{today.strftime("%d.%m.%Y-%Hh %Mm")}')""")
                                    sqlite_connection.commit()
                                plus = (it.tableWidget().item(it.row(), 3)).text()
                                if plus == "":
                                    (it.tableWidget().item(it.row(), 3)).setText(str(int(0) + int(let)))
                                else:
                                    (it.tableWidget().item(it.row(), 3)).setText(str(int(plus) + int(let)))
                            except:
                                pass
                            app.close()

                        def end():
                            app.close()

                        form.pushButton.clicked.connect(like)
                        form.pushButton_2.clicked.connect(end)
                        app.exec()
                    if action == detal_minus:
                        Form, App = uic.loadUiType("minus.ui")
                        app = QDialog(self)
                        form = Form()
                        form.setupUi(app)
                        app.show()

                        def like():
                            let = form.lineEdit.text()
                            iter = it.text()
                            try:
                                sqlite_connection = sqlite3.connect("stok.db")
                                cursor = sqlite_connection.cursor()
                                let_check = str(let).replace("-","")
                                username = cursor_01.execute(
                                f"""SELECT login FROM autorization WHERE online='True'""").fetchone()
                                if let_check.isdigit():
                                    cursor.execute(f"""UPDATE consumables SET quantity=(quantity - '{let}') WHERE articul='{iter}'""")
                                    cursor.execute(f"""INSERT INTO all_invent_consumables VALUES ('{iter}','{username[0]}',-'{let}','{today.strftime("%d.%m.%Y-%Hh %Mm")}')""")
                                    sqlite_connection.commit()
                                minus = (it.tableWidget().item(it.row(), 3)).text()
                                (it.tableWidget().item(it.row(), 3)).setText(str(int(minus) - int(let)))
                            except:
                                pass
                            app.close()

                        def end():
                            app.close()

                        form.pushButton.clicked.connect(like)
                        form.pushButton_2.clicked.connect(end)
                        app.exec()
                    if action == detal:
                        iter = it.text()
                        Forms = QtWidgets.QDialog(self)
                        form = Stock()
                        form.setupUi(Forms)
                        Forms.setWindowFlags(Forms.windowFlags() |
                                            QtCore.Qt.WindowMinimizeButtonHint |
                                            QtCore.Qt.WindowSystemMenuHint)
                        Forms.show()
                        sqlite_connection = sqlite3.connect("stok.db")
                        cursor = sqlite_connection.cursor()
                        form.tableWidget.horizontalHeader().setSectionResizeMode(0,
                                                                                 QtWidgets.QHeaderView.Stretch)
                        form.tableWidget.horizontalHeader().setSectionResizeMode(1,
                                                                                 QtWidgets.QHeaderView.ResizeToContents)
                        form.tableWidget.horizontalHeader().setSectionResizeMode(2,
                                                                                 QtWidgets.QHeaderView.ResizeToContents)
                        form.lineEdit.setText(str(iter)) ##Артикул
                        form.lineEdit_2.setText(str(it.tableWidget().item(it.row(),2).text())) ##Наименование

                        def all():
                            global row_number021
                            form.tableWidget.setRowCount(0)
                            users = cursor.execute(
                                f"""SELECT master,plus_del,datas FROM all_invent_consumables WHERE articul='{iter}' ORDER BY DATE('%d.%m.%Y')""")
                            for row_number021, order in enumerate(users):
                                form.tableWidget.insertRow(row_number021)
                                for column_number, data in enumerate(order):
                                    cell = QtWidgets.QTableWidgetItem(str(data))
                                    form.tableWidget.setItem(row_number021, column_number, cell)
                                    cell.setTextAlignment(Qt.AlignCenter)
                                    form.tableWidget.horizontalHeader().setSectionResizeMode(0,
                                                                                             QtWidgets.QHeaderView.Stretch)
                                    form.tableWidget.horizontalHeader().setSectionResizeMode(1,
                                                                                             QtWidgets.QHeaderView.ResizeToContents)
                                    form.tableWidget.horizontalHeader().setSectionResizeMode(2,
                                                                                             QtWidgets.QHeaderView.ResizeToContents)
                                form.tableWidget.selectRow(row_number021)
                                pool = int(row_number021 + 1)
                                form.label_kol.setText(f"Количество записей: {str(pool)}")
                            try:
                                form.tableWidget.scrollToItem(form.tableWidget.item(row_number021, 0), QAbstractItemView.PositionAtTop)
                                form.tableWidget.selectRow(row_number021)
                                form.tableWidget.clearSelection()
                            except:
                                pass


                        def clicks():
                            row_num = form.tableWidget.currentRow()
                            form.tableWidget.selectRow(row_num)
                        form.tableWidget.clicked.connect(clicks)


                        def minus():
                            sqlite_connection = sqlite3.connect("stok.db")
                            cursor = sqlite_connection.cursor()
                            row_num = form.tableWidget.currentRow()
                            list_del = []
                            for j in range(form.tableWidget.columnCount()):
                                poof = form.tableWidget.item(row_num, j).text()
                                list_del.append(poof)
                            cursor.execute(f"""DELETE FROM all_invent_consumables WHERE articul='{iter}' AND master='{list_del[0]}' AND plus_del='{list_del[1]}' AND datas='{list_del[2]}'""")
                            sqlite_connection.commit()
                            form.tableWidget.setRowCount(0)
                            all()

                        all()

                        form.pushButton_minus.clicked.connect(minus)
                        Forms.exec()
                    if action == invent:
                        iter = it.text()
                        Form, App = uic.loadUiType("invent.ui")
                        app = QDialog(self)
                        form = Form()
                        form.setupUi(app)
                        app.show()
                        def like():
                            let = form.lineEdit.text()
                            try:
                                sqlite_connection = sqlite3.connect("stok.db")
                                cursor = sqlite_connection.cursor()
                                text_invent = "Инвентаризация"
                                let_check = str(let).replace("-","")
                                #username = cursor_01.execute(
                                #f"""SELECT login FROM autorization WHERE online='True'""").fetchone()
                                if let_check.isdigit():
                                    cursor.execute(f"""UPDATE consumables SET quantity=('{let}') WHERE articul='{iter}'""")
                                    cursor.execute(f"""INSERT INTO all_invent_consumables VALUES ('{iter}','{text_invent}','{let}','{today.strftime("%d.%m.%Y-%Hh %Mm")}')""")
                                    sqlite_connection.commit()
                                (it.tableWidget().item(it.row(), 3)).setText(str(int(let)))
                            except:
                                pass
                            app.close()
                        def end():
                            app.close()
                        form.pushButton.clicked.connect(like)
                        form.pushButton_2.clicked.connect(end)
                        app.exec()
            if e.button():
                if it.column() == 3:
                    it.tableWidget().setEditTriggers(QTableWidgetItem.NoEditTriggers)
            QtWidgets.QTableWidget.mousePressEvent(self, e)
        except:
            pass
    def keyPressEvent(self, e):
        try:
            if e.key():
                e.nativeVirtualKey().setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
                )
            QtWidgets.QTableWidget.keyPressEvent(self, e)
        except:
            pass

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        username = cursor_01.execute(f"""SELECT login FROM autorization WHERE online='True'""").fetchone()
        value = cursor_02.execute(
            f"""SELECT font,title_font,color_table,color_table_selection,width_loko,width_detal,width_masters,image_size, rgb, rgb_selection, width_stok FROM setting WHERE user='{username[0]}'""").fetchone()
        label_setting = (value[4] - 1311)
        label_setting_det = (value[5] - 1321)
        label_setting_loko = (value[6] - 1030)
        label_setting_stok = (value[10] - 1030)
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(1449, 798)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("sql_maket/train.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QMainWindow {\n"
"background-color: rgb(50, 50, 50);}")
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        palette = QtGui.QPalette()
        self.centralwidget.setPalette(palette)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.centralwidget.setFont(font)
        self.centralwidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.centralwidget.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 50, 1451, 751))
        palette = QtGui.QPalette()
        self.tabWidget.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tabWidget.setToolTip("")
        self.tabWidget.setStatusTip("")
        self.tabWidget.setWhatsThis("")
        self.tabWidget.setAccessibleName("")
        self.tabWidget.setStyleSheet("QTabWidget::pane {\n"
"background-color: rgb(255, 205, 2);\n"
"}\n"
"QTabBar::tab {\n"
"border-radius: 3px;\n"
"background:rgb(128, 102, 255);\n"
"margin-left: 20px;\n"
"min-width: 30ex;\n"
"min-height: 8ex;\n"
"color:white\n"
"}\n"
"QTabBar::tab:selected {\n"
"background-color: rgb(128, 102, 255);\n"
"border: 2px solid rgb(169, 254, 255);\n"
"}\n"
"QTabBar::tab:hover {\n"
"    background-color:rgb(175, 105, 255);\n"
"}")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget_3 = QtWidgets.QTabWidget(self.tab_4)
        self.tabWidget_3.setGeometry(QtCore.QRect(0, 20, 1481, 661))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget_3.setFont(font)
        self.tabWidget_3.setStyleSheet("QTabWidget::pane {\n"
"background-color: rgb(226, 151, 0);\n"
"}\n"
"QTabBar::tab {\n"
"border-radius: 3px;\n"
"background:rgb(226, 151, 0);\n"
"margin-left: 20px;\n"
"min-width: 30ex;\n"
"min-height: 8ex;\n"
"color:white\n"
"}\n"
"QTabBar::tab:selected {\n"
"background-color: rgb(226, 151, 0);\n"
"border: 2px solid rgb(169, 254, 255)\n"
"}\n"
"QTabBar::tab:hover {\n"
"    background-color:rgb(255, 221, 24);\n"
"}\n"
"")
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_13 = QtWidgets.QWidget()
        self.tab_13.setObjectName("tab_13")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.tab_13)
        self.lineEdit_10.setGeometry(QtCore.QRect(20, 20, 251, 31))
        self.lineEdit_10.setStyleSheet("QLineEdit {\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 3px;}")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.pushButton_39 = QtWidgets.QPushButton(self.tab_13)
        self.pushButton_39.setGeometry(QtCore.QRect(280, 20, 31, 31))
        self.pushButton_39.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:hover {\n"
"    background-color: rgb(229, 229, 229);\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 255, 255);}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:\\Users\\User\\PycharmProjects\\SQL_Maket\\sql_maket/Search.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_39.setIcon(icon1)
        self.pushButton_39.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_39.setCheckable(True)
        self.pushButton_39.setChecked(True)
        self.pushButton_39.setObjectName("pushButton_39")
        self.pushButton_40 = QtWidgets.QPushButton(self.tab_13)
        self.pushButton_40.setGeometry(QtCore.QRect(320, 20, 31, 31))
        self.pushButton_40.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:hover {\n"
"    background-color: rgb(229, 229, 229);\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 255, 255);}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:\\Users\\User\\PycharmProjects\\SQL_Maket\\sql_maket/musor.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_40.setIcon(icon2)
        self.pushButton_40.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_40.setCheckable(True)
        self.pushButton_40.setChecked(True)
        self.pushButton_40.setObjectName("pushButton_40")
        self.tableWidget_10 = Test1(self.tab_13)
        self.tableWidget_10.setGeometry(QtCore.QRect(20, 70, value[4], 551))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_10.sizePolicy().hasHeightForWidth())
        self.tableWidget_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(value[0])
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
f"    background-color: {value[8]};\n"
"    padding: 4px;\n"
f"    font-size: {value[1]}pt;\n"
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
f"    background-color: {value[8]};\n"
"}\n"
"QTableWidget::item:selected {\n"
f"    background-color: {value[9]};\n"
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
        self.pushButton_41 = QtWidgets.QPushButton(self.tab_13)
        self.pushButton_41.setGeometry(QtCore.QRect(label_setting+1343, 520, 71, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_41.sizePolicy().hasHeightForWidth())
        self.pushButton_41.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setUnderline(False)
        font.setStrikeOut(True)
        self.pushButton_41.setFont(font)
        self.pushButton_41.setStyleSheet("QPushButton {\n"
"    background-color: rgb(134, 140, 140);\n"
"    border-radius: 5px;\n"
"    color: rgb(222, 6, 10);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(122, 122, 122);\n"
"    color: rgb(222, 6, 10)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(134, 140, 140);}")
        self.pushButton_41.setObjectName("pushButton_41")
        self.frame_15 = QtWidgets.QFrame(self.tab_13)
        self.frame_15.setGeometry(QtCore.QRect(1430, 130, 1461, 1021))
        self.frame_15.setStyleSheet("\n"
"background-color: rgb(50, 50, 50);")
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.frame = QtWidgets.QFrame(self.tab_13)
        self.frame.setGeometry(QtCore.QRect(-90, -140, 1541, 891))
        self.frame.setStyleSheet("background-color: rgb(50, 50, 50)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(label_setting+1210, 170, 321, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("QLabel {\n"
"    color: rgb(255, 255, 255);}")
        self.label_10.setObjectName("label_10")
        self.pushButton_save_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_save_3.setGeometry(QtCore.QRect(450, 160, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_save_3.setFont(font)
        self.pushButton_save_3.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:hover {\n"
"    background-color: rgb(229, 229, 229);\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 255, 255);}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("C:\\Users\\User\\PycharmProjects\\SQL_Maket\\sql_maket/save.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_save_3.setIcon(icon3)
        self.pushButton_save_3.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_save_3.setCheckable(True)
        self.pushButton_save_3.setChecked(True)
        self.pushButton_save_3.setAutoDefault(False)
        self.pushButton_save_3.setDefault(False)
        self.pushButton_save_3.setFlat(False)
        self.pushButton_save_3.setObjectName("pushButton_save_3")
        self.pushButton_42 = QtWidgets.QPushButton(self.tab_13)
        self.pushButton_42.setGeometry(QtCore.QRect(label_setting+1343, 570, 71, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_42.sizePolicy().hasHeightForWidth())
        self.pushButton_42.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton_42.setFont(font)
        self.pushButton_42.setStyleSheet("QPushButton {\n"
"    background-color: rgb(134, 140, 140);\n"
"    border-radius: 5px;\n"
"    color: rgb(97, 255, 107);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(122, 122, 122);\n"
"    color: rgb(97, 255, 107)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(134, 140, 140);}")
        self.pushButton_42.setCheckable(False)
        self.pushButton_42.setAutoRepeat(False)
        self.pushButton_42.setAutoExclusive(False)
        self.pushButton_42.setObjectName("pushButton_42")
        self.frame_15.raise_()
        self.frame.raise_()
        self.lineEdit_10.raise_()
        self.pushButton_39.raise_()
        self.pushButton_40.raise_()
        self.tableWidget_10.raise_()
        self.pushButton_41.raise_()
        self.pushButton_42.raise_()
        self.tabWidget_3.addTab(self.tab_13, "")
        self.tab_14 = QtWidgets.QWidget()
        self.tab_14.setObjectName("tab_14")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.tab_14)
        self.lineEdit_11.setGeometry(QtCore.QRect(20, 20, 251, 31))
        self.lineEdit_11.setStyleSheet("QLineEdit {\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 3px;}")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.pushButton_43 = QtWidgets.QPushButton(self.tab_14)
        self.pushButton_43.setGeometry(QtCore.QRect(280, 20, 31, 31))
        self.pushButton_43.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:hover {\n"
"    background-color: rgb(229, 229, 229);\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 255, 255);}")
        self.pushButton_43.setIcon(icon1)
        self.pushButton_43.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_43.setCheckable(True)
        self.pushButton_43.setChecked(True)
        self.pushButton_43.setObjectName("pushButton_43")
        self.pushButton_49 = QtWidgets.QPushButton(self.tab_14)
        self.pushButton_49.setGeometry(QtCore.QRect(320, 20, 31, 31))
        self.pushButton_49.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:hover {\n"
"    background-color: rgb(229, 229, 229);\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 255, 255);}")
        self.pushButton_49.setIcon(icon2)
        self.pushButton_49.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_49.setCheckable(True)
        self.pushButton_49.setChecked(True)
        self.pushButton_49.setObjectName("pushButton_49")
        self.label_11 = QtWidgets.QLabel(self.tab_14)
        self.label_11.setGeometry(QtCore.QRect(label_setting+1120, 30, 321, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("QLabel {\n"
"    color: rgb(255, 255, 255);}")
        self.label_11.setObjectName("label_11")
        self.pushButton_55 = QtWidgets.QPushButton(self.tab_14)
        self.pushButton_55.setGeometry(QtCore.QRect(label_setting+1343, 520, 71, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_55.sizePolicy().hasHeightForWidth())
        self.pushButton_55.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setUnderline(False)
        font.setStrikeOut(True)
        self.pushButton_55.setFont(font)
        self.pushButton_55.setStyleSheet("QPushButton {\n"
"    background-color: rgb(134, 140, 140);\n"
"    border-radius: 5px;\n"
"    color: rgb(222, 6, 10);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(122, 122, 122);\n"
"    color: rgb(222, 6, 10)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(134, 140, 140);}")
        self.pushButton_55.setObjectName("pushButton_55")
        self.pushButton_56 = QtWidgets.QPushButton(self.tab_14)
        self.pushButton_56.setGeometry(QtCore.QRect(label_setting+1343, 570, 71, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_56.sizePolicy().hasHeightForWidth())
        self.pushButton_56.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton_56.setFont(font)
        self.pushButton_56.setStyleSheet("QPushButton {\n"
"    background-color: rgb(134, 140, 140);\n"
"    border-radius: 5px;\n"
"    color: rgb(97, 255, 107);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(122, 122, 122);\n"
"    color: rgb(97, 255, 107)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(134, 140, 140);}")
        self.pushButton_56.setCheckable(False)
        self.pushButton_56.setAutoRepeat(False)
        self.pushButton_56.setAutoExclusive(False)
        self.pushButton_56.setObjectName("pushButton_56")
        self.tableWidget_11 = Test2(self.tab_14)
        self.tableWidget_11.setGeometry(QtCore.QRect(20, 70, value[4], 551))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(value[0])
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget_11.setFont(font)
        self.tableWidget_11.setStyleSheet("QTableWidget {\n"
"border-radius: 15px;\n"
"background-color: rgb(72, 73, 74)}\n"
"\n"
"QHeaderView::section {\n"
f"    background-color: {value[8]};\n"
"    padding: 4px;\n"
f"    font-size: {value[1]}pt;\n"
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
f"    background-color: {value[8]};\n"
"}\n"
"QTableWidget::item:selected {\n"
f"    background-color: {value[9]};\n"
"    color:rgb(0, 0, 0);\n"
"}")
        self.tableWidget_11.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget_11.setObjectName("tableWidget_11")
        self.tableWidget_11.setColumnCount(6)
        self.tableWidget_11.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_11.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_11.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_11.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_11.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_11.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_11.setHorizontalHeaderItem(5, item)
        self.tableWidget_11.horizontalHeader().setDefaultSectionSize(187)
        self.tableWidget_11.horizontalHeader().setHighlightSections(False)
        self.tableWidget_11.verticalHeader().setVisible(False)
        self.frame_3 = QtWidgets.QFrame(self.tab_14)
        self.frame_3.setGeometry(QtCore.QRect(0, -220, 1461, 1021))
        self.frame_3.setStyleSheet("\n"
"background-color: rgb(50, 50, 50);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.pushButton_save_4 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_save_4.setGeometry(QtCore.QRect(360, 240, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_save_4.setFont(font)
        self.pushButton_save_4.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:hover {\n"
"    background-color: rgb(229, 229, 229);\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 255, 255);}")
        self.pushButton_save_4.setIcon(icon3)
        self.pushButton_save_4.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_save_4.setCheckable(True)
        self.pushButton_save_4.setChecked(True)
        self.pushButton_save_4.setAutoDefault(False)
        self.pushButton_save_4.setDefault(False)
        self.pushButton_save_4.setFlat(False)
        self.pushButton_save_4.setObjectName("pushButton_save_4")
        self.frame_3.raise_()
        self.lineEdit_11.raise_()
        self.pushButton_43.raise_()
        self.pushButton_49.raise_()
        self.label_11.raise_()
        self.pushButton_55.raise_()
        self.tableWidget_11.raise_()
        self.pushButton_56.raise_()
        self.tabWidget_3.addTab(self.tab_14, "")
        self.tab_15 = QtWidgets.QWidget()
        self.tab_15.setObjectName("tab_15")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.tab_15)
        self.lineEdit_12.setGeometry(QtCore.QRect(20, 20, 251, 31))
        self.lineEdit_12.setStyleSheet("QLineEdit {\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 3px;}")
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.pushButton_44 = QtWidgets.QPushButton(self.tab_15)
        self.pushButton_44.setGeometry(QtCore.QRect(280, 20, 31, 31))
        self.pushButton_44.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:hover {\n"
"    background-color: rgb(229, 229, 229);\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 255, 255);}")
        self.pushButton_44.setIcon(icon1)
        self.pushButton_44.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_44.setCheckable(True)
        self.pushButton_44.setChecked(True)
        self.pushButton_44.setObjectName("pushButton_44")
        self.pushButton_50 = QtWidgets.QPushButton(self.tab_15)
        self.pushButton_50.setGeometry(QtCore.QRect(320, 20, 31, 31))
        self.pushButton_50.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:hover {\n"
"    background-color: rgb(229, 229, 229);\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 255, 255);}")
        self.pushButton_50.setIcon(icon2)
        self.pushButton_50.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_50.setCheckable(True)
        self.pushButton_50.setChecked(True)
        self.pushButton_50.setObjectName("pushButton_50")
        self.label_12 = QtWidgets.QLabel(self.tab_15)
        self.label_12.setGeometry(QtCore.QRect(label_setting+1120, 30, 321, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("QLabel {\n"
"    color: rgb(255, 255, 255);}")
        self.label_12.setObjectName("label_12")
        self.pushButton_57 = QtWidgets.QPushButton(self.tab_15)
        self.pushButton_57.setGeometry(QtCore.QRect(label_setting+1343, 520, 71, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_57.sizePolicy().hasHeightForWidth())
        self.pushButton_57.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setUnderline(False)
        font.setStrikeOut(True)
        self.pushButton_57.setFont(font)
        self.pushButton_57.setStyleSheet("QPushButton {\n"
"    background-color: rgb(134, 140, 140);\n"
"    border-radius: 5px;\n"
"    color: rgb(222, 6, 10);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(122, 122, 122);\n"
"    color: rgb(222, 6, 10)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(134, 140, 140);}")
        self.pushButton_57.setObjectName("pushButton_57")
        self.pushButton_58 = QtWidgets.QPushButton(self.tab_15)
        self.pushButton_58.setGeometry(QtCore.QRect(label_setting+1343, 570, 71, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_58.sizePolicy().hasHeightForWidth())
        self.pushButton_58.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton_58.setFont(font)
        self.pushButton_58.setStyleSheet("QPushButton {\n"
"    background-color: rgb(134, 140, 140);\n"
"    border-radius: 5px;\n"
"    color: rgb(97, 255, 107);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(122, 122, 122);\n"
"    color: rgb(97, 255, 107)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(134, 140, 140);}")
        self.pushButton_58.setCheckable(False)
        self.pushButton_58.setAutoRepeat(False)
        self.pushButton_58.setAutoExclusive(False)
        self.pushButton_58.setObjectName("pushButton_58")
        self.tableWidget_12 = Test3(self.tab_15)
        self.tableWidget_12.setGeometry(QtCore.QRect(20, 70, value[4], 551))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(value[0])
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget_12.setFont(font)
        self.tableWidget_12.setStyleSheet("QTableWidget {\n"
"border-radius: 15px;\n"
"background-color: rgb(72, 73, 74)}\n"
"\n"
"QHeaderView::section {\n"
f"    background-color: {value[8]};\n"
"    padding: 4px;\n"
f"    font-size: {value[1]}pt;\n"
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
f"    background-color: {value[8]};\n"
"}\n"
"QTableWidget::item:selected {\n"
f"    background-color: {value[9]};\n"
"    color:rgb(0, 0, 0);\n"
"}")
        self.tableWidget_12.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget_12.setObjectName("tableWidget_12")
        self.tableWidget_12.setColumnCount(6)
        self.tableWidget_12.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_12.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_12.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_12.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_12.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_12.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_12.setHorizontalHeaderItem(5, item)
        self.tableWidget_12.horizontalHeader().setDefaultSectionSize(187)
        self.tableWidget_12.horizontalHeader().setHighlightSections(False)
        self.tableWidget_12.verticalHeader().setVisible(False)
        self.frame_16 = QtWidgets.QFrame(self.tab_15)
        self.frame_16.setGeometry(QtCore.QRect(-30, -80, 1501, 1021))
        self.frame_16.setStyleSheet("\n"
"background-color: rgb(50, 50, 50);")
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.pushButton_save_5 = QtWidgets.QPushButton(self.frame_16)
        self.pushButton_save_5.setGeometry(QtCore.QRect(390, 100, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_save_5.setFont(font)
        self.pushButton_save_5.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:hover {\n"
"    background-color: rgb(229, 229, 229);\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 255, 255);}")
        self.pushButton_save_5.setIcon(icon3)
        self.pushButton_save_5.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_save_5.setCheckable(True)
        self.pushButton_save_5.setChecked(True)
        self.pushButton_save_5.setAutoDefault(False)
        self.pushButton_save_5.setDefault(False)
        self.pushButton_save_5.setFlat(False)
        self.pushButton_save_5.setObjectName("pushButton_save_5")
        self.frame_16.raise_()
        self.lineEdit_12.raise_()
        self.pushButton_44.raise_()
        self.pushButton_50.raise_()
        self.label_12.raise_()
        self.pushButton_57.raise_()
        self.tableWidget_12.raise_()
        self.pushButton_58.raise_()
        self.tabWidget_3.addTab(self.tab_15, "")
        self.tab_16 = QtWidgets.QWidget()
        self.tab_16.setObjectName("tab_16")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.tab_16)
        self.lineEdit_13.setGeometry(QtCore.QRect(20, 20, 251, 31))
        self.lineEdit_13.setStyleSheet("QLineEdit {\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 3px;}")
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.pushButton_45 = QtWidgets.QPushButton(self.tab_16)
        self.pushButton_45.setGeometry(QtCore.QRect(280, 20, 31, 31))
        self.pushButton_45.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:hover {\n"
"    background-color: rgb(229, 229, 229);\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 255, 255);}")
        self.pushButton_45.setIcon(icon1)
        self.pushButton_45.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_45.setCheckable(True)
        self.pushButton_45.setChecked(True)
        self.pushButton_45.setObjectName("pushButton_45")
        self.pushButton_51 = QtWidgets.QPushButton(self.tab_16)
        self.pushButton_51.setGeometry(QtCore.QRect(320, 20, 31, 31))
        self.pushButton_51.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:hover {\n"
"    background-color: rgb(229, 229, 229);\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 255, 255);}")
        self.pushButton_51.setIcon(icon2)
        self.pushButton_51.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_51.setCheckable(True)
        self.pushButton_51.setChecked(True)
        self.pushButton_51.setObjectName("pushButton_51")
        self.label_13 = QtWidgets.QLabel(self.tab_16)
        self.label_13.setGeometry(QtCore.QRect(label_setting+1120, 30, 321, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("QLabel {\n"
"    color: rgb(255, 255, 255);}")
        self.label_13.setObjectName("label_13")
        self.pushButton_59 = QtWidgets.QPushButton(self.tab_16)
        self.pushButton_59.setGeometry(QtCore.QRect(label_setting+1343, 520, 71, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_59.sizePolicy().hasHeightForWidth())
        self.pushButton_59.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setUnderline(False)
        font.setStrikeOut(True)
        self.pushButton_59.setFont(font)
        self.pushButton_59.setStyleSheet("QPushButton {\n"
"    background-color: rgb(134, 140, 140);\n"
"    border-radius: 5px;\n"
"    color: rgb(222, 6, 10);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(122, 122, 122);\n"
"    color: rgb(222, 6, 10)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(134, 140, 140);}")
        self.pushButton_59.setObjectName("pushButton_59")
        self.pushButton_60 = QtWidgets.QPushButton(self.tab_16)
        self.pushButton_60.setGeometry(QtCore.QRect(label_setting+1343, 570, 71, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_60.sizePolicy().hasHeightForWidth())
        self.pushButton_60.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton_60.setFont(font)
        self.pushButton_60.setStyleSheet("QPushButton {\n"
"    background-color: rgb(134, 140, 140);\n"
"    border-radius: 5px;\n"
"    color: rgb(97, 255, 107);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(122, 122, 122);\n"
"    color: rgb(97, 255, 107)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(134, 140, 140);}")
        self.pushButton_60.setCheckable(False)
        self.pushButton_60.setAutoRepeat(False)
        self.pushButton_60.setAutoExclusive(False)
        self.pushButton_60.setObjectName("pushButton_60")
        self.tableWidget_13 = Test4(self.tab_16)
        self.tableWidget_13.setGeometry(QtCore.QRect(20, 70, value[4], 551))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(value[0])
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget_13.setFont(font)
        self.tableWidget_13.setStyleSheet("QTableWidget {\n"
"border-radius: 15px;\n"
"background-color: rgb(72, 73, 74)}\n"
"\n"
"QHeaderView::section {\n"
f"    background-color: {value[8]};\n"
"    padding: 4px;\n"
f"    font-size: {value[1]}pt;\n"
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
f"    background-color: {value[8]};\n"
"}\n"
"QTableWidget::item:selected {\n"
f"    background-color: {value[9]};\n"
"    color:rgb(0, 0, 0);\n"
"}")
        self.tableWidget_13.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget_13.setObjectName("tableWidget_13")
        self.tableWidget_13.setColumnCount(6)
        self.tableWidget_13.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_13.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_13.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_13.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_13.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_13.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_13.setHorizontalHeaderItem(5, item)
        self.tableWidget_13.horizontalHeader().setDefaultSectionSize(187)
        self.tableWidget_13.horizontalHeader().setHighlightSections(False)
        self.tableWidget_13.verticalHeader().setVisible(False)
        self.frame_18 = QtWidgets.QFrame(self.tab_16)
        self.frame_18.setGeometry(QtCore.QRect(-10, -130, 1461, 1021))
        self.frame_18.setStyleSheet("\n"
"background-color: rgb(50, 50, 50);")
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.pushButton_save_6 = QtWidgets.QPushButton(self.frame_18)
        self.pushButton_save_6.setGeometry(QtCore.QRect(370, 150, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_save_6.setFont(font)
        self.pushButton_save_6.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:hover {\n"
"    background-color: rgb(229, 229, 229);\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 255, 255);}")
        self.pushButton_save_6.setIcon(icon3)
        self.pushButton_save_6.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_save_6.setCheckable(True)
        self.pushButton_save_6.setChecked(True)
        self.pushButton_save_6.setAutoDefault(False)
        self.pushButton_save_6.setDefault(False)
        self.pushButton_save_6.setFlat(False)
        self.pushButton_save_6.setObjectName("pushButton_save_6")
        self.frame_18.raise_()
        self.lineEdit_13.raise_()
        self.pushButton_45.raise_()
        self.pushButton_51.raise_()
        self.label_13.raise_()
        self.pushButton_59.raise_()
        self.tableWidget_13.raise_()
        self.pushButton_60.raise_()
        self.tabWidget_3.addTab(self.tab_16, "")
        self.tab_17 = QtWidgets.QWidget()
        self.tab_17.setObjectName("tab_17")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.tab_17)
        self.lineEdit_14.setGeometry(QtCore.QRect(20, 20, 251, 31))
        self.lineEdit_14.setStyleSheet("QLineEdit {\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 3px;}")
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.pushButton_46 = QtWidgets.QPushButton(self.tab_17)
        self.pushButton_46.setGeometry(QtCore.QRect(280, 20, 31, 31))
        self.pushButton_46.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:hover {\n"
"    background-color: rgb(229, 229, 229);\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 255, 255);}")
        self.pushButton_46.setIcon(icon1)
        self.pushButton_46.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_46.setCheckable(True)
        self.pushButton_46.setChecked(True)
        self.pushButton_46.setObjectName("pushButton_46")
        self.pushButton_52 = QtWidgets.QPushButton(self.tab_17)
        self.pushButton_52.setGeometry(QtCore.QRect(320, 20, 31, 31))
        self.pushButton_52.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:hover {\n"
"    background-color: rgb(229, 229, 229);\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 255, 255);}")
        self.pushButton_52.setIcon(icon2)
        self.pushButton_52.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_52.setCheckable(True)
        self.pushButton_52.setChecked(True)
        self.pushButton_52.setObjectName("pushButton_52")
        self.label_14 = QtWidgets.QLabel(self.tab_17)
        self.label_14.setGeometry(QtCore.QRect(label_setting+1120, 30, 321, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("QLabel {\n"
"    color: rgb(255, 255, 255);}")
        self.label_14.setObjectName("label_14")
        self.pushButton_61 = QtWidgets.QPushButton(self.tab_17)
        self.pushButton_61.setGeometry(QtCore.QRect(label_setting+1343, 520, 71, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_61.sizePolicy().hasHeightForWidth())
        self.pushButton_61.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setUnderline(False)
        font.setStrikeOut(True)
        self.pushButton_61.setFont(font)
        self.pushButton_61.setStyleSheet("QPushButton {\n"
"    background-color: rgb(134, 140, 140);\n"
"    border-radius: 5px;\n"
"    color: rgb(222, 6, 10);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(122, 122, 122);\n"
"    color: rgb(222, 6, 10)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(134, 140, 140);}")
        self.pushButton_61.setObjectName("pushButton_61")
        self.pushButton_62 = QtWidgets.QPushButton(self.tab_17)
        self.pushButton_62.setGeometry(QtCore.QRect(label_setting+1343, 570, 71, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_62.sizePolicy().hasHeightForWidth())
        self.pushButton_62.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton_62.setFont(font)
        self.pushButton_62.setStyleSheet("QPushButton {\n"
"    background-color: rgb(134, 140, 140);\n"
"    border-radius: 5px;\n"
"    color: rgb(97, 255, 107);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(122, 122, 122);\n"
"    color: rgb(97, 255, 107)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(134, 140, 140);}")
        self.pushButton_62.setCheckable(False)
        self.pushButton_62.setAutoRepeat(False)
        self.pushButton_62.setAutoExclusive(False)
        self.pushButton_62.setObjectName("pushButton_62")
        self.tableWidget_14 = Test5(self.tab_17)
        self.tableWidget_14.setGeometry(QtCore.QRect(20, 70, value[4], 551))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(value[0])
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget_14.setFont(font)
        self.tableWidget_14.setStyleSheet("QTableWidget {\n"
"border-radius: 15px;\n"
"background-color: rgb(72, 73, 74)}\n"
"\n"
"QHeaderView::section {\n"
f"    background-color: {value[8]};\n"
"    padding: 4px;\n"
f"    font-size: {value[1]}pt;\n"
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
f"    background-color: {value[8]};\n"
"}\n"
"QTableWidget::item:selected {\n"
f"    background-color: {value[9]};\n"
"    color:rgb(0, 0, 0);\n"
"}")
        self.tableWidget_14.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget_14.setObjectName("tableWidget_14")
        self.tableWidget_14.setColumnCount(6)
        self.tableWidget_14.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_14.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_14.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_14.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_14.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_14.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_14.setHorizontalHeaderItem(5, item)
        self.tableWidget_14.horizontalHeader().setDefaultSectionSize(187)
        self.tableWidget_14.horizontalHeader().setHighlightSections(False)
        self.tableWidget_14.verticalHeader().setVisible(False)
        self.frame_19 = QtWidgets.QFrame(self.tab_17)
        self.frame_19.setGeometry(QtCore.QRect(-10, -140, 1461, 1021))
        self.frame_19.setStyleSheet("\n"
"background-color: rgb(50, 50, 50);")
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.pushButton_save_7 = QtWidgets.QPushButton(self.frame_19)
        self.pushButton_save_7.setGeometry(QtCore.QRect(370, 160, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_save_7.setFont(font)
        self.pushButton_save_7.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:hover {\n"
"    background-color: rgb(229, 229, 229);\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 255, 255);}")
        self.pushButton_save_7.setIcon(icon3)
        self.pushButton_save_7.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_save_7.setCheckable(True)
        self.pushButton_save_7.setChecked(True)
        self.pushButton_save_7.setAutoDefault(False)
        self.pushButton_save_7.setDefault(False)
        self.pushButton_save_7.setFlat(False)
        self.pushButton_save_7.setObjectName("pushButton_save_7")
        self.frame_19.raise_()
        self.lineEdit_14.raise_()
        self.pushButton_46.raise_()
        self.pushButton_52.raise_()
        self.label_14.raise_()
        self.pushButton_61.raise_()
        self.tableWidget_14.raise_()
        self.pushButton_62.raise_()
        self.tabWidget_3.addTab(self.tab_17, "")
        self.tab_18 = QtWidgets.QWidget()
        self.tab_18.setObjectName("tab_18")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.tab_18)
        self.lineEdit_15.setGeometry(QtCore.QRect(20, 20, 251, 31))
        self.lineEdit_15.setStyleSheet("QLineEdit {\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 3px;}")
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.pushButton_47 = QtWidgets.QPushButton(self.tab_18)
        self.pushButton_47.setGeometry(QtCore.QRect(280, 20, 31, 31))
        self.pushButton_47.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:hover {\n"
"    background-color: rgb(229, 229, 229);\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 255, 255);}")
        self.pushButton_47.setIcon(icon1)
        self.pushButton_47.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_47.setCheckable(True)
        self.pushButton_47.setChecked(True)
        self.pushButton_47.setObjectName("pushButton_47")
        self.pushButton_53 = QtWidgets.QPushButton(self.tab_18)
        self.pushButton_53.setGeometry(QtCore.QRect(320, 20, 31, 31))
        self.pushButton_53.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:hover {\n"
"    background-color: rgb(229, 229, 229);\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 255, 255);}")
        self.pushButton_53.setIcon(icon2)
        self.pushButton_53.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_53.setCheckable(True)
        self.pushButton_53.setChecked(True)
        self.pushButton_53.setObjectName("pushButton_53")
        self.label_15 = QtWidgets.QLabel(self.tab_18)
        self.label_15.setGeometry(QtCore.QRect(label_setting+1120, 30, 321, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("QLabel {\n"
"    color: rgb(255, 255, 255);}")
        self.label_15.setObjectName("label_15")
        self.pushButton_63 = QtWidgets.QPushButton(self.tab_18)
        self.pushButton_63.setGeometry(QtCore.QRect(label_setting+1343, 520, 71, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_63.sizePolicy().hasHeightForWidth())
        self.pushButton_63.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setUnderline(False)
        font.setStrikeOut(True)
        self.pushButton_63.setFont(font)
        self.pushButton_63.setStyleSheet("QPushButton {\n"
"    background-color: rgb(134, 140, 140);\n"
"    border-radius: 5px;\n"
"    color: rgb(222, 6, 10);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(122, 122, 122);\n"
"    color: rgb(222, 6, 10)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(134, 140, 140);}")
        self.pushButton_63.setObjectName("pushButton_63")
        self.pushButton_64 = QtWidgets.QPushButton(self.tab_18)
        self.pushButton_64.setGeometry(QtCore.QRect(label_setting+1343, 570, 71, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_64.sizePolicy().hasHeightForWidth())
        self.pushButton_64.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton_64.setFont(font)
        self.pushButton_64.setStyleSheet("QPushButton {\n"
"    background-color: rgb(134, 140, 140);\n"
"    border-radius: 5px;\n"
"    color: rgb(97, 255, 107);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(122, 122, 122);\n"
"    color: rgb(97, 255, 107)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(134, 140, 140);}")
        self.pushButton_64.setCheckable(False)
        self.pushButton_64.setAutoRepeat(False)
        self.pushButton_64.setAutoExclusive(False)
        self.pushButton_64.setObjectName("pushButton_64")
        self.tableWidget_15 = Test6(self.tab_18)
        self.tableWidget_15.setGeometry(QtCore.QRect(20, 70, value[4], 551))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(value[0])
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget_15.setFont(font)
        self.tableWidget_15.setStyleSheet("QTableWidget {\n"
"border-radius: 15px;\n"
"background-color: rgb(72, 73, 74)}\n"
"\n"
"QHeaderView::section {\n"
f"    background-color: {value[8]};\n"
"    padding: 4px;\n"
f"    font-size: {value[1]}pt;\n"
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
f"    background-color: {value[8]};\n"
"}\n"
"QTableWidget::item:selected {\n"
f"    background-color: {value[9]};\n"
"    color:rgb(0, 0, 0);\n"
"}")
        self.tableWidget_15.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget_15.setObjectName("tableWidget_15")
        self.tableWidget_15.setColumnCount(6)
        self.tableWidget_15.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_15.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_15.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_15.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_15.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_15.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_15.setHorizontalHeaderItem(5, item)
        self.tableWidget_15.horizontalHeader().setDefaultSectionSize(187)
        self.tableWidget_15.horizontalHeader().setHighlightSections(False)
        self.tableWidget_15.verticalHeader().setVisible(False)
        self.frame_20 = QtWidgets.QFrame(self.tab_18)
        self.frame_20.setGeometry(QtCore.QRect(0, -80, 1461, 1021))
        self.frame_20.setStyleSheet("\n"
"background-color: rgb(50, 50, 50);")
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.pushButton_save_8 = QtWidgets.QPushButton(self.frame_20)
        self.pushButton_save_8.setGeometry(QtCore.QRect(360, 100, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_save_8.setFont(font)
        self.pushButton_save_8.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:hover {\n"
"    background-color: rgb(229, 229, 229);\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 255, 255);}")
        self.pushButton_save_8.setIcon(icon3)
        self.pushButton_save_8.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_save_8.setCheckable(True)
        self.pushButton_save_8.setChecked(True)
        self.pushButton_save_8.setAutoDefault(False)
        self.pushButton_save_8.setDefault(False)
        self.pushButton_save_8.setFlat(False)
        self.pushButton_save_8.setObjectName("pushButton_save_8")
        self.frame_20.raise_()
        self.lineEdit_15.raise_()
        self.pushButton_47.raise_()
        self.pushButton_53.raise_()
        self.label_15.raise_()
        self.pushButton_63.raise_()
        self.tableWidget_15.raise_()
        self.pushButton_64.raise_()
        self.tabWidget_3.addTab(self.tab_18, "")
        self.tab_19 = QtWidgets.QWidget()
        self.tab_19.setObjectName("tab_19")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.tab_19)
        self.lineEdit_16.setGeometry(QtCore.QRect(20, 20, 251, 31))
        self.lineEdit_16.setStyleSheet("QLineEdit {\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 3px;}")
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.pushButton_48 = QtWidgets.QPushButton(self.tab_19)
        self.pushButton_48.setGeometry(QtCore.QRect(280, 20, 31, 31))
        self.pushButton_48.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:hover {\n"
"    background-color: rgb(229, 229, 229);\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 255, 255);}")
        self.pushButton_48.setIcon(icon1)
        self.pushButton_48.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_48.setCheckable(True)
        self.pushButton_48.setChecked(True)
        self.pushButton_48.setObjectName("pushButton_48")
        self.pushButton_54 = QtWidgets.QPushButton(self.tab_19)
        self.pushButton_54.setGeometry(QtCore.QRect(320, 20, 31, 31))
        self.pushButton_54.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:hover {\n"
"    background-color: rgb(229, 229, 229);\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 255, 255);}")
        self.pushButton_54.setIcon(icon2)
        self.pushButton_54.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_54.setCheckable(True)
        self.pushButton_54.setChecked(True)
        self.pushButton_54.setObjectName("pushButton_54")
        self.label_16 = QtWidgets.QLabel(self.tab_19)
        self.label_16.setGeometry(QtCore.QRect(label_setting+1120, 30, 321, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("QLabel {\n"
"    color: rgb(255, 255, 255);}")
        self.label_16.setObjectName("label_16")
        self.pushButton_65 = QtWidgets.QPushButton(self.tab_19)
        self.pushButton_65.setGeometry(QtCore.QRect(label_setting+1343, 520, 71, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_65.sizePolicy().hasHeightForWidth())
        self.pushButton_65.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setUnderline(False)
        font.setStrikeOut(True)
        self.pushButton_65.setFont(font)
        self.pushButton_65.setStyleSheet("QPushButton {\n"
"    background-color: rgb(134, 140, 140);\n"
"    border-radius: 5px;\n"
"    color: rgb(222, 6, 10);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(122, 122, 122);\n"
"    color: rgb(222, 6, 10)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(134, 140, 140);}")
        self.pushButton_65.setObjectName("pushButton_65")
        self.pushButton_66 = QtWidgets.QPushButton(self.tab_19)
        self.pushButton_66.setGeometry(QtCore.QRect(label_setting+1343, 570, 71, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_66.sizePolicy().hasHeightForWidth())
        self.pushButton_66.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton_66.setFont(font)
        self.pushButton_66.setStyleSheet("QPushButton {\n"
"    background-color: rgb(134, 140, 140);\n"
"    border-radius: 5px;\n"
"    color: rgb(97, 255, 107);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(122, 122, 122);\n"
"    color: rgb(97, 255, 107)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(134, 140, 140);}")
        self.pushButton_66.setCheckable(False)
        self.pushButton_66.setAutoRepeat(False)
        self.pushButton_66.setAutoExclusive(False)
        self.pushButton_66.setObjectName("pushButton_66")
        self.tableWidget_16 = Test7(self.tab_19)
        self.tableWidget_16.setGeometry(QtCore.QRect(20, 70, value[4], 551))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(value[0])
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget_16.setFont(font)
        self.tableWidget_16.setStyleSheet("QTableWidget {\n"
"border-radius: 15px;\n"
"background-color: rgb(72, 73, 74)}\n"
"\n"
"QHeaderView::section {\n"
f"    background-color: {value[8]};\n"
"    padding: 4px;\n"
f"    font-size: {value[1]}pt;\n"
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
f"    background-color: {value[8]};\n"
"}\n"
"QTableWidget::item:selected {\n"
f"    background-color: {value[9]};\n"
"    color:rgb(0, 0, 0);\n"
"}")
        self.tableWidget_16.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget_16.setObjectName("tableWidget_16")
        self.tableWidget_16.setColumnCount(6)
        self.tableWidget_16.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_16.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_16.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_16.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_16.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_16.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_16.setHorizontalHeaderItem(5, item)
        self.tableWidget_16.horizontalHeader().setDefaultSectionSize(187)
        self.tableWidget_16.horizontalHeader().setHighlightSections(False)
        self.tableWidget_16.verticalHeader().setVisible(False)
        self.frame_21 = QtWidgets.QFrame(self.tab_19)
        self.frame_21.setGeometry(QtCore.QRect(0, -130, 1461, 1021))
        self.frame_21.setStyleSheet("\n"
"background-color: rgb(50, 50, 50);")
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.pushButton_save_9 = QtWidgets.QPushButton(self.frame_21)
        self.pushButton_save_9.setGeometry(QtCore.QRect(360, 150, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_save_9.setFont(font)
        self.pushButton_save_9.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:hover {\n"
"    background-color: rgb(229, 229, 229);\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 255, 255);}")
        self.pushButton_save_9.setIcon(icon3)
        self.pushButton_save_9.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_save_9.setCheckable(True)
        self.pushButton_save_9.setChecked(True)
        self.pushButton_save_9.setAutoDefault(False)
        self.pushButton_save_9.setDefault(False)
        self.pushButton_save_9.setFlat(False)
        self.pushButton_save_9.setObjectName("pushButton_save_9")
        self.frame_21.raise_()
        self.lineEdit_16.raise_()
        self.pushButton_48.raise_()
        self.pushButton_54.raise_()
        self.label_16.raise_()
        self.pushButton_65.raise_()
        self.tableWidget_16.raise_()
        self.pushButton_66.raise_()
        self.tabWidget_3.addTab(self.tab_19, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_17.setGeometry(QtCore.QRect(20, 20, 251, 31))
        self.lineEdit_17.setStyleSheet("QLineEdit {\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 3px;}")
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.pushButton_69 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_69.setGeometry(QtCore.QRect(280, 20, 31, 31))
        self.pushButton_69.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:hover {\n"
"    background-color: rgb(229, 229, 229);\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 255, 255);}")
        self.pushButton_69.setIcon(icon1)
        self.pushButton_69.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_69.setCheckable(True)
        self.pushButton_69.setChecked(True)
        self.pushButton_69.setObjectName("pushButton_69")
        self.pushButton_70 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_70.setGeometry(QtCore.QRect(320, 20, 31, 31))
        self.pushButton_70.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:hover {\n"
"    background-color: rgb(229, 229, 229);\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 255, 255);}")
        self.pushButton_70.setIcon(icon2)
        self.pushButton_70.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_70.setCheckable(True)
        self.pushButton_70.setChecked(True)
        self.pushButton_70.setObjectName("pushButton_70")
        self.tableWidget_3 = Test8(self.tab_3)
        self.tableWidget_3.setGeometry(QtCore.QRect(20, 70, value[4], 551))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(value[0])
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget_3.setFont(font)
        self.tableWidget_3.setStyleSheet("QTableWidget {\n"
"border-radius: 15px;\n"
"background-color: rgb(72, 73, 74)}\n"
"\n"
"QHeaderView::section {\n"
f"    background-color: {value[8]};\n"
"    padding: 4px;\n"
f"    font-size: {value[1]}pt;\n"
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
f"    background-color: {value[8]};\n"
"}\n"
"QTableWidget::item:selected {\n"
f"    background-color: {value[9]};\n"
"    color:rgb(0, 0, 0);\n"
"}")
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(6)
        self.tableWidget_3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(5, item)
        self.tableWidget_3.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_3.horizontalHeader().setDefaultSectionSize(187)
        self.tableWidget_3.horizontalHeader().setHighlightSections(False)
        self.tableWidget_3.verticalHeader().setVisible(False)
        self.frame_23 = QtWidgets.QFrame(self.tab_3)
        self.frame_23.setGeometry(QtCore.QRect(0, -10, 1461, 1031))
        self.frame_23.setStyleSheet("\n"
"background-color: rgb(50, 50, 50);")
        self.frame_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.pushButton_71 = QtWidgets.QPushButton(self.frame_23)
        self.pushButton_71.setGeometry(QtCore.QRect(label_setting+1343, 530, 71, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_71.sizePolicy().hasHeightForWidth())
        self.pushButton_71.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setUnderline(False)
        font.setStrikeOut(True)
        self.pushButton_71.setFont(font)
        self.pushButton_71.setStyleSheet("QPushButton {\n"
"    background-color: rgb(134, 140, 140);\n"
"    border-radius: 5px;\n"
"    color: rgb(222, 6, 10);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(122, 122, 122);\n"
"    color: rgb(222, 6, 10)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(134, 140, 140);}")
        self.pushButton_71.setObjectName("pushButton_71")
        self.label_17 = QtWidgets.QLabel(self.frame_23)
        self.label_17.setGeometry(QtCore.QRect(label_setting+1120, 40, 311, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("QLabel {\n"
"    color: rgb(255, 255, 255);}")
        self.label_17.setObjectName("label_17")
        self.pushButton_save_10 = QtWidgets.QPushButton(self.frame_23)
        self.pushButton_save_10.setGeometry(QtCore.QRect(360, 30, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_save_10.setFont(font)
        self.pushButton_save_10.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:hover {\n"
"    background-color: rgb(229, 229, 229);\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 255, 255);}")
        self.pushButton_save_10.setIcon(icon3)
        self.pushButton_save_10.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_save_10.setCheckable(True)
        self.pushButton_save_10.setChecked(True)
        self.pushButton_save_10.setAutoDefault(False)
        self.pushButton_save_10.setDefault(False)
        self.pushButton_save_10.setFlat(False)
        self.pushButton_save_10.setObjectName("pushButton_save_10")
        self.pushButton_72 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_72.setGeometry(QtCore.QRect(label_setting+1343, 570, 71, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_72.sizePolicy().hasHeightForWidth())
        self.pushButton_72.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton_72.setFont(font)
        self.pushButton_72.setStyleSheet("QPushButton {\n"
"    background-color: rgb(134, 140, 140);\n"
"    border-radius: 5px;\n"
"    color: rgb(97, 255, 107);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(122, 122, 122);\n"
"    color: rgb(97, 255, 107)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(134, 140, 140);}")
        self.pushButton_72.setCheckable(False)
        self.pushButton_72.setAutoRepeat(False)
        self.pushButton_72.setAutoExclusive(False)
        self.pushButton_72.setObjectName("pushButton_72")
        self.frame_23.raise_()
        self.lineEdit_17.raise_()
        self.pushButton_69.raise_()
        self.pushButton_70.raise_()
        self.tableWidget_3.raise_()
        self.pushButton_72.raise_()
        self.tabWidget_3.addTab(self.tab_3, "")
        self.frame_4 = QtWidgets.QFrame(self.tab_4)
        self.frame_4.setGeometry(QtCore.QRect(0, -100, 2191, 761))
        self.frame_4.setStyleSheet("\n"
"background-color: rgb(50, 50, 50);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.frame_5 = QtWidgets.QFrame(self.tab_4)
        self.frame_5.setGeometry(QtCore.QRect(-20, 570, 1631, 1131))
        self.frame_5.setStyleSheet("\n"
"background-color: rgb(50, 50, 50);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.frame_5.raise_()
        self.frame_4.raise_()
        self.tabWidget_3.raise_()
        self.tabWidget.addTab(self.tab_4, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setStyleSheet("QWidget{color: rgb(12, 12, 12);}")
        self.tab.setObjectName("tab")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(label_setting_det+1350, 640, 71, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color: rgb(134, 140, 140);\n"
"    border-radius: 5px;\n"
"    color: rgb(97, 255, 107);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(122, 122, 122);\n"
"    color: rgb(97, 255, 107)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(134, 140, 140);}")
        self.pushButton.setCheckable(False)
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setAutoExclusive(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(label_setting_det+1350, 590, 71, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setUnderline(False)
        font.setStrikeOut(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    background-color: rgb(134, 140, 140);\n"
"    border-radius: 5px;\n"
"    color: rgb(222, 6, 10);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(122, 122, 122);\n"
"    color: rgb(222, 6, 10)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(134, 140, 140);}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(20, 20, 251, 31))
        self.lineEdit.setStyleSheet("QLineEdit {\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 3px;}")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab)
        self.pushButton_3.setGeometry(QtCore.QRect(280, 20, 31, 31))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:hover {\n"
"    background-color: rgb(229, 229, 229);\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 255, 255);}")
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setChecked(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.tableWidget = TestDetalis(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(20, 70, value[5], 616))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(value[0])
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget.setFont(font)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setStyleSheet("QTableWidget {\n"
"border-radius: 15px;\n"
"background-color: rgb(72, 73, 74)}\n"
"\n"
"QHeaderView::section {\n"
f"    background-color: {value[8]};\n"
"    padding: 4px;\n"
f"    font-size: {value[1]}pt;\n"
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
f"    background-color: {value[8]};\n"
"}\n"
"QTableWidget::item:selected {\n"
f"    background-color: {value[9]};\n"
"    color:rgb(0, 0, 0);\n"
"}")
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(203)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(49)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(36)
        self.tableWidget.verticalHeader().setMinimumSectionSize(34)
        self.pushButton_9 = QtWidgets.QPushButton(self.tab)
        self.pushButton_9.setGeometry(QtCore.QRect(320, 20, 31, 31))
        self.pushButton_9.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:hover {\n"
"    background-color: rgb(229, 229, 229);\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 255, 255);}")
        self.pushButton_9.setIcon(icon2)
        self.pushButton_9.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_9.setCheckable(True)
        self.pushButton_9.setChecked(True)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_save = QtWidgets.QPushButton(self.tab)
        self.pushButton_save.setGeometry(QtCore.QRect(360, 20, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_save.setFont(font)
        self.pushButton_save.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:hover {\n"
"    background-color: rgb(229, 229, 229);\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 255, 255);}")
        self.pushButton_save.setIcon(icon3)
        self.pushButton_save.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_save.setCheckable(True)
        self.pushButton_save.setChecked(True)
        self.pushButton_save.setObjectName("pushButton_save")
        self.frame_2 = QtWidgets.QFrame(self.tab)
        self.frame_2.setGeometry(QtCore.QRect(-1, -1, 1461, 741))
        self.frame_2.setStyleSheet("\n"
"background-color: rgb(50, 50, 50);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(label_setting_det+1090, 30, 241, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n"
"    color: rgb(255, 255, 255);}")
        self.label.setObjectName("label")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_11.setGeometry(QtCore.QRect(400, 21, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:hover {\n"
"    background-color: rgb(229, 229, 229);\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 255, 255);}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("C:\\Users\\User\\PycharmProjects\\SQL_Maket\\sql_maket/reload.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_11.setIcon(icon4)
        self.pushButton_11.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_11.setCheckable(True)
        self.pushButton_11.setChecked(True)
        self.pushButton_11.setObjectName("pushButton_11")
        self.frame_2.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.lineEdit.raise_()
        self.pushButton_3.raise_()
        self.tableWidget.raise_()
        self.pushButton_9.raise_()
        self.pushButton_save.raise_()
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 20, 251, 31))
        self.lineEdit_2.setStyleSheet("QLineEdit {\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 3px;}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4.setGeometry(QtCore.QRect(280, 20, 31, 31))
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:hover {\n"
"    background-color: rgb(229, 229, 229);\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 255, 255);}")
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_4.setCheckable(True)
        self.pushButton_4.setChecked(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.tableWidget_2 = TestMasters(self.tab_2)
        self.tableWidget_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(value[0])
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget_2.setFont(font)
        self.tableWidget_2.setToolTip("")
        self.tableWidget_2.setStatusTip("")
        self.tableWidget_2.setGeometry(QtCore.QRect(20, 70, value[6], 521))
        self.tableWidget_2.setStyleSheet("QTableWidget {\n"
"border-radius: 15px;\n"
"background-color: rgb(72, 73, 74)}\n"
"\n"
"QHeaderView::section {\n"
f"    background-color: {value[8]};\n"
"    padding: 4px;\n"
f"    font-size: {value[1]}pt;\n"
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
f"    background-color: {value[8]};\n"
"}\n"
"QTableWidget::item:selected {\n"
f"    background-color: {value[9]};\n"
"    color:rgb(0, 0, 0);\n"
"}")
        self.tableWidget_2.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(3)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(343)
        self.tableWidget_2.horizontalHeader().setHighlightSections(False)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.pushButton_10 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_10.setGeometry(QtCore.QRect(320, 20, 31, 31))
        self.pushButton_10.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:hover {\n"
"    background-color: rgb(229, 229, 229);\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 255, 255);}")
        self.pushButton_10.setIcon(icon2)
        self.pushButton_10.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_10.setCheckable(True)
        self.pushButton_10.setChecked(True)
        self.pushButton_10.setObjectName("pushButton_10")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(label_setting_loko+840, 30, 241, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel {\n"
"    color: rgb(255, 255, 255);}")
        self.label_2.setObjectName("label_2")
        self.frame_6 = QtWidgets.QFrame(self.tab_2)
        self.frame_6.setGeometry(QtCore.QRect(0, 0, 1461, 741))
        self.frame_6.setStyleSheet("\n"
"background-color: rgb(50, 50, 50);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.pushButton_save_2 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_save_2.setGeometry(QtCore.QRect(360, 20, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_save_2.setFont(font)
        self.pushButton_save_2.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:hover {\n"
"    background-color: rgb(229, 229, 229);\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 255, 255);}")
        self.pushButton_save_2.setIcon(icon3)
        self.pushButton_save_2.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_save_2.setCheckable(True)
        self.pushButton_save_2.setChecked(True)
        self.pushButton_save_2.setObjectName("pushButton_save_2")
        self.pushButton_67 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_67.setGeometry(QtCore.QRect(label_setting_loko+1060, 490, 71, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_67.sizePolicy().hasHeightForWidth())
        self.pushButton_67.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setUnderline(False)
        font.setStrikeOut(True)
        self.pushButton_67.setFont(font)
        self.pushButton_67.setStyleSheet("QPushButton {\n"
"    background-color: rgb(134, 140, 140);\n"
"    border-radius: 5px;\n"
"    color: rgb(222, 6, 10);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(122, 122, 122);\n"
"    color: rgb(222, 6, 10)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(134, 140, 140);}")
        self.pushButton_67.setObjectName("pushButton_67")
        self.pushButton_68 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_68.setGeometry(QtCore.QRect(label_setting_loko+1060, 540, 71, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_68.sizePolicy().hasHeightForWidth())
        self.pushButton_68.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton_68.setFont(font)
        self.pushButton_68.setStyleSheet("QPushButton {\n"
"    background-color: rgb(134, 140, 140);\n"
"    border-radius: 5px;\n"
"    color: rgb(97, 255, 107);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(122, 122, 122);\n"
"    color: rgb(97, 255, 107)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(134, 140, 140);}")
        self.pushButton_68.setCheckable(False)
        self.pushButton_68.setAutoRepeat(False)
        self.pushButton_68.setAutoExclusive(False)
        self.pushButton_68.setObjectName("pushButton_68")
        self.frame_6.raise_()
        self.lineEdit_2.raise_()
        self.pushButton_4.raise_()
        self.tableWidget_2.raise_()
        self.pushButton_10.raise_()
        self.label_2.raise_()
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_5.setGeometry(QtCore.QRect(40, 40, 400, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 5px;}\n"
"QPushButton:hover {\n"
"    background-color: rgb(229, 229, 229);\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 255, 255);}")
        self.pushButton_5.setIconSize(QtCore.QSize(100, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_6.setGeometry(QtCore.QRect(520, 40, 400, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;}\n"
"QPushButton:hover {\n"
"    background-color: rgb(229, 229, 229);\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 255, 255);}")
        self.pushButton_6.setIconSize(QtCore.QSize(100, 30))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_13 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_13.setGeometry(QtCore.QRect(1010, 40, 400, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;}\n"
"QPushButton:hover {\n"
"    background-color: rgb(229, 229, 229);\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 255, 255);}")
        self.pushButton_13.setIconSize(QtCore.QSize(100, 30))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_14.setGeometry(QtCore.QRect(1010, 130, 400, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_14.sizePolicy().hasHeightForWidth())
        self.pushButton_14.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_14.setAutoFillBackground(False)
        self.pushButton_14.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(229, 229, 229);\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 255, 255);}")
        self.pushButton_14.setIconSize(QtCore.QSize(50, 40))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_8.setGeometry(QtCore.QRect(40, 130, 400, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_8.setAutoFillBackground(False)
        self.pushButton_8.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(229, 229, 229);\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 255, 255);}")
        self.pushButton_8.setIconSize(QtCore.QSize(50, 40))
        self.pushButton_8.setObjectName("pushButton_8")
        self.frame_22 = QtWidgets.QFrame(self.tab_5)
        self.frame_22.setGeometry(QtCore.QRect(-10, -70, 1461, 1021))
        self.frame_22.setStyleSheet("\n"
"background-color: rgb(50, 50, 50);")
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.pushButton_12 = QtWidgets.QPushButton(self.frame_22)
        self.pushButton_12.setGeometry(QtCore.QRect(530, 200, 400, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet("QPushButton{\n"
                                         "    background-color: rgb(255, 255, 255);\n"
                                         "border-radius: 5px;}\n"
                                         "QPushButton:hover {\n"
                                         "    background-color: rgb(229, 229, 229);\n"
                                         "    color:rgb(0, 0, 0)}\n"
                                         "QPushButton:pressed {\n"
                                         "    background-color: rgb(255, 255, 255);}")
        self.pushButton_12.setIconSize(QtCore.QSize(100, 35))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_22)
        self.pushButton_7.setGeometry(QtCore.QRect(40, 710, 400, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("QPushButton{\n"
                                         "    background-color: rgb(255, 170, 0);\n"
                                         "border-radius: 5px;}\n"
                                         "QPushButton:hover {\n"
                                         "    background-color: rgb(229, 229, 229);\n"
                                         "    color:rgb(0, 0, 0)}\n"
                                         "QPushButton:pressed {\n"
                                         "    background-color: rgb(255, 255, 255);}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_23 = QtWidgets.QLabel(self.frame_22)
        self.label_23.setGeometry(QtCore.QRect(90, 762, 341, 20))
        self.label_23.setStyleSheet("QLabel {\n"
"    color: rgb(255, 0, 0);}")
        self.label_23.setObjectName("label_23")
        self.frame_22.raise_()
        self.pushButton_5.raise_()
        self.pushButton_6.raise_()
        self.pushButton_13.raise_()
        self.pushButton_8.raise_()
        self.pushButton_14.raise_()
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setEnabled(True)
        self.tab_8.setAutoFillBackground(False)
        self.tab_8.setStyleSheet("")
        self.tab_8.setObjectName("tab_8")
        self.frame_9 = QtWidgets.QFrame(self.tab_8)
        self.frame_9.setGeometry(QtCore.QRect(0, 0, 1461, 741))
        self.frame_9.setStyleSheet("")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.tabWidget_4 = QtWidgets.QTabWidget(self.frame_9)
        self.tabWidget_4.setGeometry(QtCore.QRect(0, 20, 1481, 661))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget_4.setFont(font)
        self.tabWidget_4.setStyleSheet("QTabWidget::pane {\n"
"background-color:rgb(85, 255, 127);\n"
"}\n"
"QTabBar::tab {\n"
"border-radius: 3px;\n"
"background:rgb(82, 172, 255);\n"
"margin-left: 20px;\n"
"min-width: 45ex;\n"
"min-height: 8ex;\n"
"color:white\n"
"}\n"
"QTabBar::tab:selected {\n"
"background-color: rgb(82, 172, 255);\n"
"border: 2px solid rgb(129, 255, 169)\n"
"}\n"
"QTabBar::tab:hover {\n"
"    background-color:rgb(82, 230, 255);\n"
"}\n"
"")
        self.tabWidget_4.setIconSize(QtCore.QSize(16, 16))
        self.tabWidget_4.setUsesScrollButtons(True)
        self.tabWidget_4.setObjectName("tabWidget_4")
        self.tab_20 = QtWidgets.QWidget()
        self.tab_20.setObjectName("tab_20")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.tab_20)
        self.lineEdit_18.setGeometry(QtCore.QRect(20, 20, 251, 31))
        self.lineEdit_18.setStyleSheet("QLineEdit {\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 3px;}")
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.pushButton_76 = QtWidgets.QPushButton(self.tab_20)
        self.pushButton_76.setGeometry(QtCore.QRect(280, 20, 31, 31))
        self.pushButton_76.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:hover {\n"
"    background-color: rgb(229, 229, 229);\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 255, 255);}")
        self.pushButton_76.setIcon(icon1)
        self.pushButton_76.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_76.setCheckable(True)
        self.pushButton_76.setChecked(True)
        self.pushButton_76.setObjectName("pushButton_76")
        self.pushButton_77 = QtWidgets.QPushButton(self.tab_20)
        self.pushButton_77.setGeometry(QtCore.QRect(320, 20, 31, 31))
        self.pushButton_77.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:hover {\n"
"    background-color: rgb(229, 229, 229);\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 255, 255);}")
        self.pushButton_77.setIcon(icon2)
        self.pushButton_77.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_77.setCheckable(True)
        self.pushButton_77.setChecked(True)
        self.pushButton_77.setObjectName("pushButton_77")
        self.pushButton_78 = QtWidgets.QPushButton(self.tab_20)
        self.pushButton_78.setGeometry(QtCore.QRect(1343, 520, 71, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_78.sizePolicy().hasHeightForWidth())
        self.pushButton_78.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setUnderline(False)
        font.setStrikeOut(True)
        self.pushButton_78.setFont(font)
        self.pushButton_78.setStyleSheet("QPushButton {\n"
"    background-color: rgb(134, 140, 140);\n"
"    border-radius: 5px;\n"
"    color: rgb(222, 6, 10);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(122, 122, 122);\n"
"    color: rgb(222, 6, 10)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(134, 140, 140);}")
        self.pushButton_78.setObjectName("pushButton_78")
        self.frame_24 = QtWidgets.QFrame(self.tab_20)
        self.frame_24.setGeometry(QtCore.QRect(1430, 130, 1461, 1021))
        self.frame_24.setStyleSheet("\n"
"background-color: rgb(50, 50, 50);")
        self.frame_24.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_24.setObjectName("frame_24")
        self.frame_10 = QtWidgets.QFrame(self.tab_20)
        self.frame_10.setGeometry(QtCore.QRect(-90, -140, 1541, 891))
        self.frame_10.setStyleSheet("")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.lineEdit_22 = QtWidgets.QLineEdit(self.frame_10)
        self.lineEdit_22.setGeometry(QtCore.QRect(110, 160, 251, 31))
        self.lineEdit_22.setStyleSheet("QLineEdit {\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 3px;}")
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.pushButton_79 = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_79.setGeometry(QtCore.QRect(370, 160, 31, 31))
        self.pushButton_79.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:hover {\n"
"    background-color: rgb(229, 229, 229);\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 255, 255);}")
        self.pushButton_79.setIcon(icon1)
        self.pushButton_79.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_79.setCheckable(True)
        self.pushButton_79.setChecked(True)
        self.pushButton_79.setObjectName("pushButton_79")
        self.pushButton_92 = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_92.setGeometry(QtCore.QRect(410, 160, 31, 31))
        self.pushButton_92.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:hover {\n"
"    background-color: rgb(229, 229, 229);\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 255, 255);}")
        self.pushButton_92.setIcon(icon2)
        self.pushButton_92.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_92.setCheckable(True)
        self.pushButton_92.setChecked(True)
        self.pushButton_92.setObjectName("pushButton_92")
        self.pushButton_save_11 = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_save_11.setGeometry(QtCore.QRect(450, 160, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_save_11.setFont(font)
        self.pushButton_save_11.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:hover {\n"
"    background-color: rgb(229, 229, 229);\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 255, 255);}")
        self.pushButton_save_11.setIcon(icon3)
        self.pushButton_save_11.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_save_11.setCheckable(True)
        self.pushButton_save_11.setChecked(True)
        self.pushButton_save_11.setAutoDefault(False)
        self.pushButton_save_11.setDefault(False)
        self.pushButton_save_11.setFlat(False)
        self.pushButton_save_11.setObjectName("pushButton_save_11")
        self.tableWidget_21 = Test_Stock_1(self.frame_10)
        self.tableWidget_21.setGeometry(QtCore.QRect(110, 210, value[10], 551))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget_21.setFont(font)
        self.tableWidget_21.setStyleSheet("QTableWidget {\n"
"border-radius: 15px;\n"
"background-color: rgb(72, 73, 74)}\n"
"\n"
"QHeaderView::section {\n"
f"    background-color: {value[8]};\n"
"    padding: 4px;\n"
f"    font-size: {value[1]}pt;\n"
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
f"    background-color: {value[8]};\n"
"}\n"
"QTableWidget::item:selected {\n"
f"    background-color: {value[9]};\n"
"    color:rgb(0, 0, 0);\n"
"}")
        self.tableWidget_21.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget_21.setObjectName("tableWidget_21")
        self.tableWidget_21.setColumnCount(4)
        self.tableWidget_21.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_21.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_21.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_21.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_21.setHorizontalHeaderItem(3, item)
        self.tableWidget_21.horizontalHeader().setDefaultSectionSize(187)
        self.tableWidget_21.horizontalHeader().setHighlightSections(False)
        self.tableWidget_21.verticalHeader().setVisible(False)
        self.pushButton_101 = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_101.setGeometry(QtCore.QRect(label_setting_stok+1160, 660, 71, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_101.sizePolicy().hasHeightForWidth())
        self.pushButton_101.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setUnderline(False)
        font.setStrikeOut(True)
        self.pushButton_101.setFont(font)
        self.pushButton_101.setStyleSheet("QPushButton {\n"
"    background-color: rgb(134, 140, 140);\n"
"    border-radius: 5px;\n"
"    color: rgb(222, 6, 10);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(122, 122, 122);\n"
"    color: rgb(222, 6, 10)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(134, 140, 140);}")
        self.pushButton_101.setObjectName("pushButton_101")
        self.pushButton_102 = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_102.setGeometry(QtCore.QRect(label_setting_stok+1160, 710, 71, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_102.sizePolicy().hasHeightForWidth())
        self.pushButton_102.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton_102.setFont(font)
        self.pushButton_102.setStyleSheet("QPushButton {\n"
"    background-color: rgb(134, 140, 140);\n"
"    border-radius: 5px;\n"
"    color: rgb(97, 255, 107);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(122, 122, 122);\n"
"    color: rgb(97, 255, 107)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(134, 140, 140);}")
        self.pushButton_102.setCheckable(False)
        self.pushButton_102.setAutoRepeat(False)
        self.pushButton_102.setAutoExclusive(False)
        self.pushButton_102.setObjectName("pushButton_102")
        self.label_31 = QtWidgets.QLabel(self.frame_10)
        self.label_31.setGeometry(QtCore.QRect(label_setting_stok+930, 170, 321, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet("QLabel {\n"
"    color: rgb(255, 255, 255);}")
        self.label_31.setObjectName("label_31")
        self.label_24 = QtWidgets.QLabel(self.frame_10)
        self.label_24.setGeometry(QtCore.QRect(90, 140, 1491, 900))
        self.label_24.setText("")
        self.label_24.setPixmap(QtGui.QPixmap("sql_maket/полотно.png"))
        self.label_24.setObjectName("label_24")
        self.label_24.raise_()
        self.lineEdit_22.raise_()
        self.pushButton_79.raise_()
        self.pushButton_92.raise_()
        self.pushButton_save_11.raise_()
        self.pushButton_101.raise_()
        self.pushButton_102.raise_()
        self.tableWidget_21.raise_()
        self.label_31.raise_()
        self.tabWidget_4.addTab(self.tab_20, "")
        self.tab_21 = QtWidgets.QWidget()
        self.tab_21.setObjectName("tab_21")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.tab_21)
        self.lineEdit_19.setGeometry(QtCore.QRect(20, 20, 251, 31))
        self.lineEdit_19.setStyleSheet("QLineEdit {\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 3px;}")
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.pushButton_80 = QtWidgets.QPushButton(self.tab_21)
        self.pushButton_80.setGeometry(QtCore.QRect(280, 20, 31, 31))
        self.pushButton_80.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:hover {\n"
"    background-color: rgb(229, 229, 229);\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 255, 255);}")
        self.pushButton_80.setIcon(icon1)
        self.pushButton_80.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_80.setCheckable(True)
        self.pushButton_80.setChecked(True)
        self.pushButton_80.setObjectName("pushButton_80")
        self.pushButton_81 = QtWidgets.QPushButton(self.tab_21)
        self.pushButton_81.setGeometry(QtCore.QRect(320, 20, 31, 31))
        self.pushButton_81.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:hover {\n"
"    background-color: rgb(229, 229, 229);\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 255, 255);}")
        self.pushButton_81.setIcon(icon2)
        self.pushButton_81.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_81.setCheckable(True)
        self.pushButton_81.setChecked(True)
        self.pushButton_81.setObjectName("pushButton_81")
        self.label_28 = QtWidgets.QLabel(self.tab_21)
        self.label_28.setGeometry(QtCore.QRect(1120, 30, 321, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("QLabel {\n"
"    color: rgb(255, 255, 255);}")
        self.label_28.setObjectName("label_28")
        self.pushButton_82 = QtWidgets.QPushButton(self.tab_21)
        self.pushButton_82.setGeometry(QtCore.QRect(1343, 520, 71, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_82.sizePolicy().hasHeightForWidth())
        self.pushButton_82.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setUnderline(False)
        font.setStrikeOut(True)
        self.pushButton_82.setFont(font)
        self.pushButton_82.setStyleSheet("QPushButton {\n"
"    background-color: rgb(134, 140, 140);\n"
"    border-radius: 5px;\n"
"    color: rgb(222, 6, 10);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(122, 122, 122);\n"
"    color: rgb(222, 6, 10)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(134, 140, 140);}")
        self.pushButton_82.setObjectName("pushButton_82")
        self.pushButton_83 = QtWidgets.QPushButton(self.tab_21)
        self.pushButton_83.setGeometry(QtCore.QRect(1343, 570, 71, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_83.sizePolicy().hasHeightForWidth())
        self.pushButton_83.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton_83.setFont(font)
        self.pushButton_83.setStyleSheet("QPushButton {\n"
"    background-color: rgb(134, 140, 140);\n"
"    border-radius: 5px;\n"
"    color: rgb(97, 255, 107);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(122, 122, 122);\n"
"    color: rgb(97, 255, 107)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(134, 140, 140);}")
        self.pushButton_83.setCheckable(False)
        self.pushButton_83.setAutoRepeat(False)
        self.pushButton_83.setAutoExclusive(False)
        self.pushButton_83.setObjectName("pushButton_83")
        self.tableWidget_18 = QtWidgets.QTableWidget(self.tab_21)
        self.tableWidget_18.setGeometry(QtCore.QRect(20, 70, 1311, 551))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget_18.setFont(font)
        self.tableWidget_18.setStyleSheet("QTableWidget {\n"
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
        self.tableWidget_18.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget_18.setObjectName("tableWidget_18")
        self.tableWidget_18.setColumnCount(6)
        self.tableWidget_18.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_18.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_18.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_18.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_18.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_18.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_18.setHorizontalHeaderItem(5, item)
        self.tableWidget_18.horizontalHeader().setDefaultSectionSize(187)
        self.tableWidget_18.horizontalHeader().setHighlightSections(False)
        self.tableWidget_18.verticalHeader().setVisible(False)
        self.frame_11 = QtWidgets.QFrame(self.tab_21)
        self.frame_11.setGeometry(QtCore.QRect(0, -220, 1461, 1021))
        self.frame_11.setStyleSheet("")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.lineEdit_23 = QtWidgets.QLineEdit(self.frame_11)
        self.lineEdit_23.setGeometry(QtCore.QRect(20, 240, 251, 31))
        self.lineEdit_23.setStyleSheet("QLineEdit {\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 3px;}")
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.pushButton_93 = QtWidgets.QPushButton(self.frame_11)
        self.pushButton_93.setGeometry(QtCore.QRect(280, 240, 31, 31))
        self.pushButton_93.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:hover {\n"
"    background-color: rgb(229, 229, 229);\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 255, 255);}")
        self.pushButton_93.setIcon(icon1)
        self.pushButton_93.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_93.setCheckable(True)
        self.pushButton_93.setChecked(True)
        self.pushButton_93.setObjectName("pushButton_93")
        self.pushButton_94 = QtWidgets.QPushButton(self.frame_11)
        self.pushButton_94.setGeometry(QtCore.QRect(320, 240, 31, 31))
        self.pushButton_94.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:hover {\n"
"    background-color: rgb(229, 229, 229);\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 255, 255);}")
        self.pushButton_94.setIcon(icon2)
        self.pushButton_94.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_94.setCheckable(True)
        self.pushButton_94.setChecked(True)
        self.pushButton_94.setObjectName("pushButton_94")
        self.pushButton_save_12 = QtWidgets.QPushButton(self.frame_11)
        self.pushButton_save_12.setGeometry(QtCore.QRect(360, 240, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_save_12.setFont(font)
        self.pushButton_save_12.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:hover {\n"
"    background-color: rgb(229, 229, 229);\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 255, 255);}")
        self.pushButton_save_12.setIcon(icon3)
        self.pushButton_save_12.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_save_12.setCheckable(True)
        self.pushButton_save_12.setChecked(True)
        self.pushButton_save_12.setAutoDefault(False)
        self.pushButton_save_12.setDefault(False)
        self.pushButton_save_12.setFlat(False)
        self.pushButton_save_12.setObjectName("pushButton_save_12")
        self.tableWidget_22 = Test_Stock_2(self.frame_11)
        self.tableWidget_22.setGeometry(QtCore.QRect(20, 290, value[10], 551))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget_22.setFont(font)
        self.tableWidget_22.setStyleSheet("QTableWidget {\n"
"border-radius: 15px;\n"
"background-color: rgb(72, 73, 74)}\n"
"\n"
"QHeaderView::section {\n"
f"    background-color: {value[8]};\n"
"    padding: 4px;\n"
f"    font-size: {value[1]}pt;\n"
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
f"    background-color: {value[8]};\n"
"}\n"
"QTableWidget::item:selected {\n"
f"    background-color: {value[9]};\n"
"    color:rgb(0, 0, 0);\n"
"}")
        self.tableWidget_22.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget_22.setObjectName("tableWidget_22")
        self.tableWidget_22.setColumnCount(4)
        self.tableWidget_22.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_22.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_22.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_22.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_22.setHorizontalHeaderItem(3, item)
        self.tableWidget_22.horizontalHeader().setDefaultSectionSize(187)
        self.tableWidget_22.horizontalHeader().setHighlightSections(False)
        self.tableWidget_22.verticalHeader().setVisible(False)
        self.pushButton_103 = QtWidgets.QPushButton(self.frame_11)
        self.pushButton_103.setGeometry(QtCore.QRect(label_setting_stok+1070, 790, 71, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_103.sizePolicy().hasHeightForWidth())
        self.pushButton_103.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton_103.setFont(font)
        self.pushButton_103.setStyleSheet("QPushButton {\n"
"    background-color: rgb(134, 140, 140);\n"
"    border-radius: 5px;\n"
"    color: rgb(97, 255, 107);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(122, 122, 122);\n"
"    color: rgb(97, 255, 107)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(134, 140, 140);}")
        self.pushButton_103.setCheckable(False)
        self.pushButton_103.setAutoRepeat(False)
        self.pushButton_103.setAutoExclusive(False)
        self.pushButton_103.setObjectName("pushButton_103")
        self.pushButton_104 = QtWidgets.QPushButton(self.frame_11)
        self.pushButton_104.setGeometry(QtCore.QRect(label_setting_stok+1070, 740, 71, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_104.sizePolicy().hasHeightForWidth())
        self.pushButton_104.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setUnderline(False)
        font.setStrikeOut(True)
        self.pushButton_104.setFont(font)
        self.pushButton_104.setStyleSheet("QPushButton {\n"
"    background-color: rgb(134, 140, 140);\n"
"    border-radius: 5px;\n"
"    color: rgb(222, 6, 10);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(122, 122, 122);\n"
"    color: rgb(222, 6, 10)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(134, 140, 140);}")
        self.pushButton_104.setObjectName("pushButton_104")
        self.label_32 = QtWidgets.QLabel(self.frame_11)
        self.label_32.setGeometry(QtCore.QRect(label_setting_stok+840, 250, 321, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_32.setFont(font)
        self.label_32.setStyleSheet("QLabel {\n"
"    color: rgb(255, 255, 255);}")
        self.label_32.setObjectName("label_32")
        self.label_25 = QtWidgets.QLabel(self.frame_11)
        self.label_25.setGeometry(QtCore.QRect(0, 220, 1491, 731))
        self.label_25.setText("")
        self.label_25.setPixmap(QtGui.QPixmap("sql_maket/полотно.png"))
        self.label_25.setObjectName("label_25")
        self.label_25.raise_()
        self.label_32.raise_()
        self.lineEdit_23.raise_()
        self.pushButton_93.raise_()
        self.pushButton_94.raise_()
        self.pushButton_save_12.raise_()
        self.tableWidget_22.raise_()
        self.pushButton_103.raise_()
        self.pushButton_104.raise_()
        self.tabWidget_4.addTab(self.tab_21, "")
        self.tab_22 = QtWidgets.QWidget()
        self.tab_22.setObjectName("tab_22")
        self.lineEdit_20 = QtWidgets.QLineEdit(self.tab_22)
        self.lineEdit_20.setGeometry(QtCore.QRect(20, 20, 251, 31))
        self.lineEdit_20.setStyleSheet("QLineEdit {\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 3px;}")
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.pushButton_84 = QtWidgets.QPushButton(self.tab_22)
        self.pushButton_84.setGeometry(QtCore.QRect(280, 20, 31, 31))
        self.pushButton_84.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:hover {\n"
"    background-color: rgb(229, 229, 229);\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 255, 255);}")
        self.pushButton_84.setIcon(icon1)
        self.pushButton_84.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_84.setCheckable(True)
        self.pushButton_84.setChecked(True)
        self.pushButton_84.setObjectName("pushButton_84")
        self.pushButton_85 = QtWidgets.QPushButton(self.tab_22)
        self.pushButton_85.setGeometry(QtCore.QRect(320, 20, 31, 31))
        self.pushButton_85.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:hover {\n"
"    background-color: rgb(229, 229, 229);\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 255, 255);}")
        self.pushButton_85.setIcon(icon2)
        self.pushButton_85.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_85.setCheckable(True)
        self.pushButton_85.setChecked(True)
        self.pushButton_85.setObjectName("pushButton_85")
        self.label_29 = QtWidgets.QLabel(self.tab_22)
        self.label_29.setGeometry(QtCore.QRect(1120, 30, 321, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("QLabel {\n"
"    color: rgb(255, 255, 255);}")
        self.label_29.setObjectName("label_29")
        self.pushButton_86 = QtWidgets.QPushButton(self.tab_22)
        self.pushButton_86.setGeometry(QtCore.QRect(1343, 520, 71, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_86.sizePolicy().hasHeightForWidth())
        self.pushButton_86.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setUnderline(False)
        font.setStrikeOut(True)
        self.pushButton_86.setFont(font)
        self.pushButton_86.setStyleSheet("QPushButton {\n"
"    background-color: rgb(134, 140, 140);\n"
"    border-radius: 5px;\n"
"    color: rgb(222, 6, 10);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(122, 122, 122);\n"
"    color: rgb(222, 6, 10)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(134, 140, 140);}")
        self.pushButton_86.setObjectName("pushButton_86")
        self.pushButton_87 = QtWidgets.QPushButton(self.tab_22)
        self.pushButton_87.setGeometry(QtCore.QRect(1343, 570, 71, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_87.sizePolicy().hasHeightForWidth())
        self.pushButton_87.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton_87.setFont(font)
        self.pushButton_87.setStyleSheet("QPushButton {\n"
"    background-color: rgb(134, 140, 140);\n"
"    border-radius: 5px;\n"
"    color: rgb(97, 255, 107);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(122, 122, 122);\n"
"    color: rgb(97, 255, 107)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(134, 140, 140);}")
        self.pushButton_87.setCheckable(False)
        self.pushButton_87.setAutoRepeat(False)
        self.pushButton_87.setAutoExclusive(False)
        self.pushButton_87.setObjectName("pushButton_87")
        self.tableWidget_19 = QtWidgets.QTableWidget(self.tab_22)
        self.tableWidget_19.setGeometry(QtCore.QRect(20, 70, 1311, 551))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget_19.setFont(font)
        self.tableWidget_19.setStyleSheet("QTableWidget {\n"
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
        self.tableWidget_19.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget_19.setObjectName("tableWidget_19")
        self.tableWidget_19.setColumnCount(6)
        self.tableWidget_19.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_19.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_19.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_19.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_19.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_19.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_19.setHorizontalHeaderItem(5, item)
        self.tableWidget_19.horizontalHeader().setDefaultSectionSize(187)
        self.tableWidget_19.horizontalHeader().setHighlightSections(False)
        self.tableWidget_19.verticalHeader().setVisible(False)
        self.frame_25 = QtWidgets.QFrame(self.tab_22)
        self.frame_25.setGeometry(QtCore.QRect(-30, -80, 1501, 1021))
        self.frame_25.setStyleSheet("")
        self.frame_25.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_25.setObjectName("frame_25")
        self.lineEdit_24 = QtWidgets.QLineEdit(self.frame_25)
        self.lineEdit_24.setGeometry(QtCore.QRect(50, 100, 251, 31))
        self.lineEdit_24.setStyleSheet("QLineEdit {\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 3px;}")
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.pushButton_95 = QtWidgets.QPushButton(self.frame_25)
        self.pushButton_95.setGeometry(QtCore.QRect(310, 100, 31, 31))
        self.pushButton_95.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:hover {\n"
"    background-color: rgb(229, 229, 229);\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 255, 255);}")
        self.pushButton_95.setIcon(icon1)
        self.pushButton_95.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_95.setCheckable(True)
        self.pushButton_95.setChecked(True)
        self.pushButton_95.setObjectName("pushButton_95")
        self.pushButton_96 = QtWidgets.QPushButton(self.frame_25)
        self.pushButton_96.setGeometry(QtCore.QRect(350, 100, 31, 31))
        self.pushButton_96.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:hover {\n"
"    background-color: rgb(229, 229, 229);\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 255, 255);}")
        self.pushButton_96.setIcon(icon2)
        self.pushButton_96.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_96.setCheckable(True)
        self.pushButton_96.setChecked(True)
        self.pushButton_96.setObjectName("pushButton_96")
        self.pushButton_save_13 = QtWidgets.QPushButton(self.frame_25)
        self.pushButton_save_13.setGeometry(QtCore.QRect(390, 100, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_save_13.setFont(font)
        self.pushButton_save_13.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:hover {\n"
"    background-color: rgb(229, 229, 229);\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 255, 255);}")
        self.pushButton_save_13.setIcon(icon3)
        self.pushButton_save_13.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_save_13.setCheckable(True)
        self.pushButton_save_13.setChecked(True)
        self.pushButton_save_13.setAutoDefault(False)
        self.pushButton_save_13.setDefault(False)
        self.pushButton_save_13.setFlat(False)
        self.pushButton_save_13.setObjectName("pushButton_save_13")
        self.tableWidget_23 = Test_Stock_3(self.frame_25)
        self.tableWidget_23.setGeometry(QtCore.QRect(50, 150, value[10], 551))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget_23.setFont(font)
        self.tableWidget_23.setStyleSheet("QTableWidget {\n"
"border-radius: 15px;\n"
"background-color: rgb(72, 73, 74)}\n"
"\n"
"QHeaderView::section {\n"
f"    background-color: {value[8]};\n"
"    padding: 4px;\n"
f"    font-size: {value[1]}pt;\n"
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
f"    background-color: {value[8]};\n"
"}\n"
"QTableWidget::item:selected {\n"
f"    background-color: {value[9]};\n"
"    color:rgb(0, 0, 0);\n"
"}")
        self.tableWidget_23.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget_23.setObjectName("tableWidget_23")
        self.tableWidget_23.setColumnCount(4)
        self.tableWidget_23.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_23.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_23.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_23.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_23.setHorizontalHeaderItem(3, item)
        self.tableWidget_23.horizontalHeader().setDefaultSectionSize(187)
        self.tableWidget_23.horizontalHeader().setHighlightSections(False)
        self.tableWidget_23.verticalHeader().setVisible(False)
        self.pushButton_105 = QtWidgets.QPushButton(self.frame_25)
        self.pushButton_105.setGeometry(QtCore.QRect(label_setting_stok+1100, 600, 71, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_105.sizePolicy().hasHeightForWidth())
        self.pushButton_105.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setUnderline(False)
        font.setStrikeOut(True)
        self.pushButton_105.setFont(font)
        self.pushButton_105.setStyleSheet("QPushButton {\n"
"    background-color: rgb(134, 140, 140);\n"
"    border-radius: 5px;\n"
"    color: rgb(222, 6, 10);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(122, 122, 122);\n"
"    color: rgb(222, 6, 10)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(134, 140, 140);}")
        self.pushButton_105.setObjectName("pushButton_105")
        self.pushButton_106 = QtWidgets.QPushButton(self.frame_25)
        self.pushButton_106.setGeometry(QtCore.QRect(label_setting_stok+1100, 650, 71, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_106.sizePolicy().hasHeightForWidth())
        self.pushButton_106.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton_106.setFont(font)
        self.pushButton_106.setStyleSheet("QPushButton {\n"
"    background-color: rgb(134, 140, 140);\n"
"    border-radius: 5px;\n"
"    color: rgb(97, 255, 107);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(122, 122, 122);\n"
"    color: rgb(97, 255, 107)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(134, 140, 140);}")
        self.pushButton_106.setCheckable(False)
        self.pushButton_106.setAutoRepeat(False)
        self.pushButton_106.setAutoExclusive(False)
        self.pushButton_106.setObjectName("pushButton_106")
        self.label_33 = QtWidgets.QLabel(self.frame_25)
        self.label_33.setGeometry(QtCore.QRect(label_setting_stok+870, 110, 321, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_33.setFont(font)
        self.label_33.setStyleSheet("QLabel {\n"
"    color: rgb(255, 255, 255);}")
        self.label_33.setObjectName("label_33")
        self.label_26 = QtWidgets.QLabel(self.frame_25)
        self.label_26.setGeometry(QtCore.QRect(30, 80, 1491, 701))
        self.label_26.setText("")
        self.label_26.setPixmap(QtGui.QPixmap("sql_maket/полотно.png"))
        self.label_26.setObjectName("label_26")
        self.label_26.raise_()
        self.label_33.raise_()
        self.tableWidget_23.raise_()
        self.lineEdit_24.raise_()
        self.pushButton_95.raise_()
        self.pushButton_96.raise_()
        self.pushButton_save_13.raise_()
        self.pushButton_105.raise_()
        self.pushButton_106.raise_()
        self.tabWidget_4.addTab(self.tab_22, "")
        self.tab_23 = QtWidgets.QWidget()
        self.tab_23.setObjectName("tab_23")
        self.lineEdit_21 = QtWidgets.QLineEdit(self.tab_23)
        self.lineEdit_21.setGeometry(QtCore.QRect(20, 20, 251, 31))
        self.lineEdit_21.setStyleSheet("QLineEdit {\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 3px;}")
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.pushButton_88 = QtWidgets.QPushButton(self.tab_23)
        self.pushButton_88.setGeometry(QtCore.QRect(280, 20, 31, 31))
        self.pushButton_88.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:hover {\n"
"    background-color: rgb(229, 229, 229);\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 255, 255);}")
        self.pushButton_88.setIcon(icon1)
        self.pushButton_88.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_88.setCheckable(True)
        self.pushButton_88.setChecked(True)
        self.pushButton_88.setObjectName("pushButton_88")
        self.pushButton_89 = QtWidgets.QPushButton(self.tab_23)
        self.pushButton_89.setGeometry(QtCore.QRect(320, 20, 31, 31))
        self.pushButton_89.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:hover {\n"
"    background-color: rgb(229, 229, 229);\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 255, 255);}")
        self.pushButton_89.setIcon(icon2)
        self.pushButton_89.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_89.setCheckable(True)
        self.pushButton_89.setChecked(True)
        self.pushButton_89.setObjectName("pushButton_89")
        self.label_30 = QtWidgets.QLabel(self.tab_23)
        self.label_30.setGeometry(QtCore.QRect(1120, 30, 321, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("QLabel {\n"
"    color: rgb(255, 255, 255);}")
        self.label_30.setObjectName("label_30")
        self.pushButton_90 = QtWidgets.QPushButton(self.tab_23)
        self.pushButton_90.setGeometry(QtCore.QRect(1343, 520, 71, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_90.sizePolicy().hasHeightForWidth())
        self.pushButton_90.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setUnderline(False)
        font.setStrikeOut(True)
        self.pushButton_90.setFont(font)
        self.pushButton_90.setStyleSheet("QPushButton {\n"
"    background-color: rgb(134, 140, 140);\n"
"    border-radius: 5px;\n"
"    color: rgb(222, 6, 10);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(122, 122, 122);\n"
"    color: rgb(222, 6, 10)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(134, 140, 140);}")
        self.pushButton_90.setObjectName("pushButton_90")
        self.pushButton_91 = QtWidgets.QPushButton(self.tab_23)
        self.pushButton_91.setGeometry(QtCore.QRect(1343, 570, 71, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_91.sizePolicy().hasHeightForWidth())
        self.pushButton_91.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton_91.setFont(font)
        self.pushButton_91.setStyleSheet("QPushButton {\n"
"    background-color: rgb(134, 140, 140);\n"
"    border-radius: 5px;\n"
"    color: rgb(97, 255, 107);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(122, 122, 122);\n"
"    color: rgb(97, 255, 107)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(134, 140, 140);}")
        self.pushButton_91.setCheckable(False)
        self.pushButton_91.setAutoRepeat(False)
        self.pushButton_91.setAutoExclusive(False)
        self.pushButton_91.setObjectName("pushButton_91")
        self.tableWidget_20 = QtWidgets.QTableWidget(self.tab_23)
        self.tableWidget_20.setGeometry(QtCore.QRect(20, 70, 1311, 551))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget_20.setFont(font)
        self.tableWidget_20.setStyleSheet("QTableWidget {\n"
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
        self.tableWidget_20.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget_20.setObjectName("tableWidget_20")
        self.tableWidget_20.setColumnCount(6)
        self.tableWidget_20.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_20.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_20.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_20.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_20.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_20.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_20.setHorizontalHeaderItem(5, item)
        self.tableWidget_20.horizontalHeader().setDefaultSectionSize(187)
        self.tableWidget_20.horizontalHeader().setHighlightSections(False)
        self.tableWidget_20.verticalHeader().setVisible(False)
        self.frame_26 = QtWidgets.QFrame(self.tab_23)
        self.frame_26.setGeometry(QtCore.QRect(-10, -130, 1461, 1021))
        self.frame_26.setStyleSheet("")
        self.frame_26.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_26.setObjectName("frame_26")
        self.lineEdit_25 = QtWidgets.QLineEdit(self.frame_26)
        self.lineEdit_25.setGeometry(QtCore.QRect(30, 150, 251, 31))
        self.lineEdit_25.setStyleSheet("QLineEdit {\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 3px;}")
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.pushButton_97 = QtWidgets.QPushButton(self.frame_26)
        self.pushButton_97.setGeometry(QtCore.QRect(290, 150, 31, 31))
        self.pushButton_97.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:hover {\n"
"    background-color: rgb(229, 229, 229);\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 255, 255);}")
        self.pushButton_97.setIcon(icon1)
        self.pushButton_97.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_97.setCheckable(True)
        self.pushButton_97.setChecked(True)
        self.pushButton_97.setObjectName("pushButton_97")
        self.pushButton_98 = QtWidgets.QPushButton(self.frame_26)
        self.pushButton_98.setGeometry(QtCore.QRect(330, 150, 31, 31))
        self.pushButton_98.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:hover {\n"
"    background-color: rgb(229, 229, 229);\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 255, 255);}")
        self.pushButton_98.setIcon(icon2)
        self.pushButton_98.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_98.setCheckable(True)
        self.pushButton_98.setChecked(True)
        self.pushButton_98.setObjectName("pushButton_98")
        self.pushButton_save_14 = QtWidgets.QPushButton(self.frame_26)
        self.pushButton_save_14.setGeometry(QtCore.QRect(370, 150, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_save_14.setFont(font)
        self.pushButton_save_14.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:hover {\n"
"    background-color: rgb(229, 229, 229);\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 255, 255);}")
        self.pushButton_save_14.setIcon(icon3)
        self.pushButton_save_14.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_save_14.setCheckable(True)
        self.pushButton_save_14.setChecked(True)
        self.pushButton_save_14.setAutoDefault(False)
        self.pushButton_save_14.setDefault(False)
        self.pushButton_save_14.setFlat(False)
        self.pushButton_save_14.setObjectName("pushButton_save_14")
        self.tableWidget_24 = Test_Stock_4(self.frame_26)
        self.tableWidget_24.setGeometry(QtCore.QRect(30, 200, value[10], 551))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget_24.setFont(font)
        self.tableWidget_24.setStyleSheet("QTableWidget {\n"
"border-radius: 15px;\n"
"background-color: rgb(72, 73, 74)}\n"
"\n"
"QHeaderView::section {\n"
f"    background-color: {value[8]};\n"
"    padding: 4px;\n"
f"    font-size: {value[1]}pt;\n"
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
f"    background-color: {value[8]};\n"
"}\n"
"QTableWidget::item:selected {\n"
f"    background-color: {value[9]};\n"
"    color:rgb(0, 0, 0);\n"
"}")
        self.tableWidget_24.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget_24.setObjectName("tableWidget_24")
        self.tableWidget_24.setColumnCount(4)
        self.tableWidget_24.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_24.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_24.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_24.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_24.setHorizontalHeaderItem(3, item)
        self.tableWidget_24.horizontalHeader().setDefaultSectionSize(187)
        self.tableWidget_24.horizontalHeader().setHighlightSections(False)
        self.tableWidget_24.verticalHeader().setVisible(False)
        self.pushButton_199 = QtWidgets.QPushButton(self.frame_26)
        self.pushButton_199.setGeometry(QtCore.QRect(label_setting_stok+1080, 700, 71, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_199.sizePolicy().hasHeightForWidth())
        self.pushButton_199.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton_199.setFont(font)
        self.pushButton_199.setStyleSheet("QPushButton {\n"
"    background-color: rgb(134, 140, 140);\n"
"    border-radius: 5px;\n"
"    color: rgb(97, 255, 107);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(122, 122, 122);\n"
"    color: rgb(97, 255, 107)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(134, 140, 140);}")
        self.pushButton_199.setCheckable(False)
        self.pushButton_199.setAutoRepeat(False)
        self.pushButton_199.setAutoExclusive(False)
        self.pushButton_199.setObjectName("pushButton_199")
        self.pushButton_100 = QtWidgets.QPushButton(self.frame_26)
        self.pushButton_100.setGeometry(QtCore.QRect(label_setting_stok+1080, 650, 71, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_100.sizePolicy().hasHeightForWidth())
        self.pushButton_100.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setUnderline(False)
        font.setStrikeOut(True)
        self.pushButton_100.setFont(font)
        self.pushButton_100.setStyleSheet("QPushButton {\n"
"    background-color: rgb(134, 140, 140);\n"
"    border-radius: 5px;\n"
"    color: rgb(222, 6, 10);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(122, 122, 122);\n"
"    color: rgb(222, 6, 10)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(134, 140, 140);}")
        self.pushButton_100.setObjectName("pushButton_100")
        self.label_34 = QtWidgets.QLabel(self.frame_26)
        self.label_34.setGeometry(QtCore.QRect(label_setting_stok+850, 160, 321, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_34.setFont(font)
        self.label_34.setStyleSheet("QLabel {\n"
"    color: rgb(255, 255, 255);}")
        self.label_34.setObjectName("label_34")
        self.label_27 = QtWidgets.QLabel(self.frame_26)
        self.label_27.setGeometry(QtCore.QRect(10, 130, 1491, 691))
        self.label_27.setText("")
        self.label_27.setPixmap(QtGui.QPixmap("sql_maket/полотно.png"))
        self.label_27.setObjectName("label_27")
        self.label_27.raise_()
        self.label_34.raise_()
        self.lineEdit_25.raise_()
        self.pushButton_97.raise_()
        self.pushButton_98.raise_()
        self.pushButton_save_14.raise_()
        self.tableWidget_24.raise_()
        self.pushButton_199.raise_()
        self.pushButton_100.raise_()
        self.tabWidget_4.addTab(self.tab_23, "")
        self.label_0023 = QtWidgets.QLabel(self.frame_9)
        self.label_0023.setGeometry(QtCore.QRect(-34, 0, 1491, 1000))
        self.label_0023.setText("")
        self.label_0023.setPixmap(QtGui.QPixmap("sql_maket/полотно.png"))
        self.label_0023.setObjectName("label_0023")
        self.label_0023.raise_()
        self.tabWidget_4.raise_()
        self.tabWidget.addTab(self.tab_8, "")
        self.frame_17 = QtWidgets.QFrame(self.centralwidget)
        self.frame_17.setGeometry(QtCore.QRect(-170, 33, 1621, 611))
        self.frame_17.setStyleSheet("\n"
"background-color: rgb(50, 50, 50);")
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.frame_8 = QtWidgets.QFrame(self.frame_17)
        self.frame_8.setGeometry(QtCore.QRect(170, -1, 1451, 2))
        self.frame_8.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.pushButton_99 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_99.setGeometry(QtCore.QRect(1325, 0, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_99.setFont(font)
        self.pushButton_99.setStyleSheet("QPushButton {\n"
"background-color: rgb(33, 76, 90);\n"
	"border-radius: 3px;\n"
	"color:rgb(0, 0, 0)}\n"
"QPushButton:hover {\n"
	"background-color:rgb(255, 170, 0);\n"
	"color:rgb(0, 0, 0)}\n"
"QPushButton:pressed {\n"
	"background-color:rgb(243, 162, 0);}")
        self.pushButton_99.setCheckable(True)
        self.pushButton_99.setChecked(True)
        self.pushButton_99.setObjectName("pushButton_99")
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_74 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_74.setGeometry(QtCore.QRect(1370, 0, 36, 31))
        self.pushButton_74.setFont(font)
        self.pushButton_74.setStyleSheet("QPushButton {\n"
"    background-color: rgb(33, 76, 90);\n"
"    border-radius: 3px;\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:hover {\n"
"    background-color: rgb(33, 95, 95);\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(33, 100, 100);}")
        self.pushButton_74.setCheckable(True)
        self.pushButton_74.setChecked(True)
        self.pushButton_74.setObjectName("pushButton_74")
        self.pushButton_73 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_73.setGeometry(QtCore.QRect(1410, 0, 36, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_73.setFont(font)
        self.pushButton_73.setStyleSheet("QPushButton {\n"
"    background-color: rgb(33, 76, 90);\n"
"    border-radius: 3px;\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:hover {\n"
"    background-color: rgb(255, 61, 61);\n"
"    color:rgb(0, 0, 0)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(33, 95, 95);}")
        self.pushButton_73.setCheckable(True)
        self.pushButton_73.setChecked(True)
        self.pushButton_73.setObjectName("pushButton_73")
        self.frame_7 = QtWidgets.QFrame(self.centralwidget)
        self.frame_7.setGeometry(QtCore.QRect(0, 0, 1451, 34))
        self.frame_7.setStyleSheet("QFrame {background-color: rgb(33, 76, 90);}")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.label_51 = QtWidgets.QLabel(self.frame_7)
        self.label_51.setGeometry(QtCore.QRect(10, 0, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(13)
        font.setItalic(False)
        font.setKerning(True)
        self.label_51.setFont(font)
        self.label_51.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_51.setObjectName("label_51")
        self.frame_7.raise_()
        self.frame_17.raise_()
        self.tabWidget.raise_()
        self.pushButton_99.raise_()
        self.pushButton_74.raise_()
        self.pushButton_73.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)
        corn1 = QtGui.QPixmap("sql_maket/04.png")
        corn2 = QtGui.QPixmap("sql_maket/01.png")
        corn3 = QtGui.QPixmap("sql_maket/03.png")
        corn4 = QtGui.QPixmap("sql_maket/02.png")
        corn_setting=(value[4]-1311)
        self.label_01 = QtWidgets.QLabel(self.tab_13)
        self.label_01.setGeometry(QtCore.QRect(9, 57, 31, 31))
        self.label_01.setText("")
        self.label_01.setPixmap(corn1)
        self.label_02 = QtWidgets.QLabel(self.tab_13)
        self.label_02.setGeometry(QtCore.QRect(9, 605, 31, 31))
        self.label_02.setText("")
        self.label_02.setPixmap(corn2)
        self.label_03 = QtWidgets.QLabel(self.tab_13)
        self.label_03.setGeometry(QtCore.QRect(corn_setting+1318, 56, 31, 31))
        self.label_03.setText("")
        self.label_03.setPixmap(corn3)
        self.label_04 = QtWidgets.QLabel(self.tab_13)
        self.label_04.setGeometry(QtCore.QRect(corn_setting+1321, 605, 21, 31))
        self.label_04.setText("")
        self.label_04.setPixmap(corn4)
        self.label_011 = QtWidgets.QLabel(self.tab_14)
        self.label_011.setGeometry(QtCore.QRect(9, 57, 31, 31))
        self.label_011.setText("")
        self.label_011.setPixmap(corn1)
        self.label_012 = QtWidgets.QLabel(self.tab_14)
        self.label_012.setGeometry(QtCore.QRect(9, 605, 31, 31))
        self.label_012.setText("")
        self.label_012.setPixmap(corn2)
        self.label_013 = QtWidgets.QLabel(self.tab_14)
        self.label_013.setGeometry(QtCore.QRect(corn_setting+1318, 56, 31, 31))
        self.label_013.setText("")
        self.label_013.setPixmap(corn3)
        self.label_014 = QtWidgets.QLabel(self.tab_14)
        self.label_014.setGeometry(QtCore.QRect(corn_setting+1321, 605, 21, 31))
        self.label_014.setText("")
        self.label_014.setPixmap(corn4)
        self.label_021 = QtWidgets.QLabel(self.tab_15)
        self.label_021.setGeometry(QtCore.QRect(9, 57, 31, 31))
        self.label_021.setText("")
        self.label_021.setPixmap(corn1)
        self.label_022 = QtWidgets.QLabel(self.tab_15)
        self.label_022.setGeometry(QtCore.QRect(9, 605, 31, 31))
        self.label_022.setText("")
        self.label_022.setPixmap(corn2)
        self.label_023 = QtWidgets.QLabel(self.tab_15)
        self.label_023.setGeometry(QtCore.QRect(corn_setting+1318, 56, 31, 31))
        self.label_023.setText("")
        self.label_023.setPixmap(corn3)
        self.label_024 = QtWidgets.QLabel(self.tab_15)
        self.label_024.setGeometry(QtCore.QRect(corn_setting+1321, 605, 21, 31))
        self.label_024.setText("")
        self.label_024.setPixmap(corn4)
        self.label_031 = QtWidgets.QLabel(self.tab_16)
        self.label_031.setGeometry(QtCore.QRect(9, 57, 31, 31))
        self.label_031.setText("")
        self.label_031.setPixmap(corn1)
        self.label_032 = QtWidgets.QLabel(self.tab_16)
        self.label_032.setGeometry(QtCore.QRect(9, 605, 31, 31))
        self.label_032.setText("")
        self.label_032.setPixmap(corn2)
        self.label_033 = QtWidgets.QLabel(self.tab_16)
        self.label_033.setGeometry(QtCore.QRect(corn_setting+1318, 56, 31, 31))
        self.label_033.setText("")
        self.label_033.setPixmap(corn3)
        self.label_034 = QtWidgets.QLabel(self.tab_16)
        self.label_034.setGeometry(QtCore.QRect(corn_setting+1321, 605, 21, 31))
        self.label_034.setText("")
        self.label_034.setPixmap(corn4)
        self.label_041 = QtWidgets.QLabel(self.tab_17)
        self.label_041.setGeometry(QtCore.QRect(9, 57, 31, 31))
        self.label_041.setText("")
        self.label_041.setPixmap(corn1)
        self.label_042 = QtWidgets.QLabel(self.tab_17)
        self.label_042.setGeometry(QtCore.QRect(9, 605, 31, 31))
        self.label_042.setText("")
        self.label_042.setPixmap(corn2)
        self.label_043 = QtWidgets.QLabel(self.tab_17)
        self.label_043.setGeometry(QtCore.QRect(corn_setting+1318, 56, 31, 31))
        self.label_043.setText("")
        self.label_043.setPixmap(corn3)
        self.label_044 = QtWidgets.QLabel(self.tab_17)
        self.label_044.setGeometry(QtCore.QRect(corn_setting+1321, 605, 21, 31))
        self.label_044.setText("")
        self.label_044.setPixmap(corn4)
        self.label_051 = QtWidgets.QLabel(self.tab_18)
        self.label_051.setGeometry(QtCore.QRect(9, 57, 31, 31))
        self.label_051.setText("")
        self.label_051.setPixmap(corn1)
        self.label_052 = QtWidgets.QLabel(self.tab_18)
        self.label_052.setGeometry(QtCore.QRect(9, 605, 31, 31))
        self.label_052.setText("")
        self.label_052.setPixmap(corn2)
        self.label_053 = QtWidgets.QLabel(self.tab_18)
        self.label_053.setGeometry(QtCore.QRect(corn_setting+1318, 56, 31, 31))
        self.label_053.setText("")
        self.label_053.setPixmap(corn3)
        self.label_054 = QtWidgets.QLabel(self.tab_18)
        self.label_054.setGeometry(QtCore.QRect(corn_setting+1321, 605, 21, 31))
        self.label_054.setText("")
        self.label_054.setPixmap(corn4)
        self.label_061 = QtWidgets.QLabel(self.tab_19)
        self.label_061.setGeometry(QtCore.QRect(9, 57, 31, 31))
        self.label_061.setText("")
        self.label_061.setPixmap(corn1)
        self.label_062 = QtWidgets.QLabel(self.tab_19)
        self.label_062.setGeometry(QtCore.QRect(9, 605, 31, 31))
        self.label_062.setText("")
        self.label_062.setPixmap(corn2)
        self.label_063 = QtWidgets.QLabel(self.tab_19)
        self.label_063.setGeometry(QtCore.QRect(corn_setting+1318, 56, 31, 31))
        self.label_063.setText("")
        self.label_063.setPixmap(corn3)
        self.label_064 = QtWidgets.QLabel(self.tab_19)
        self.label_064.setGeometry(QtCore.QRect(corn_setting+1321, 605, 21, 31))
        self.label_064.setText("")
        self.label_064.setPixmap(corn4)
        self.label_071 = QtWidgets.QLabel(self.tab_3)
        self.label_071.setGeometry(QtCore.QRect(9, 57, 31, 31))
        self.label_071.setText("")
        self.label_071.setPixmap(corn1)
        self.label_072 = QtWidgets.QLabel(self.tab_3)
        self.label_072.setGeometry(QtCore.QRect(9, 605, 31, 31))
        self.label_072.setText("")
        self.label_072.setPixmap(corn2)
        self.label_073 = QtWidgets.QLabel(self.tab_3)
        self.label_073.setGeometry(QtCore.QRect(corn_setting+1318, 56, 31, 31))
        self.label_073.setText("")
        self.label_073.setPixmap(corn3)
        self.label_074 = QtWidgets.QLabel(self.tab_3)
        self.label_074.setGeometry(QtCore.QRect(corn_setting+1321, 605, 21, 31))
        self.label_074.setText("")
        self.label_074.setPixmap(corn4)
        self.label_det1 = QtWidgets.QLabel(self.tab)
        self.label_det1.setGeometry(QtCore.QRect(9, 57, 31, 31))
        self.label_det1.setText("")
        self.label_det1.setPixmap(corn1)
        self.label_det2 = QtWidgets.QLabel(self.tab)
        self.label_det2.setGeometry(QtCore.QRect(9, 670, 31, 31))
        self.label_det2.setText("")
        self.label_det2.setPixmap(corn2)
        self.label_det3 = QtWidgets.QLabel(self.tab)
        self.label_det3.setGeometry(QtCore.QRect(label_setting_det+1328, 56, 21, 28))
        self.label_det3.setText("")
        self.label_det3.setPixmap(corn3)
        self.label_det4 = QtWidgets.QLabel(self.tab)
        self.label_det4.setGeometry(QtCore.QRect(label_setting_det+1331, 671, 19, 31))
        self.label_det4.setText("")
        self.label_det4.setPixmap(corn4)
        self.label_mast1 = QtWidgets.QLabel(self.tab_2)
        self.label_mast1.setGeometry(QtCore.QRect(9, 57, 31, 31))
        self.label_mast1.setText("")
        self.label_mast1.setPixmap(corn1)
        self.label_mast2 = QtWidgets.QLabel(self.tab_2)
        self.label_mast2.setGeometry(QtCore.QRect(9, 575, 31, 31))
        self.label_mast2.setText("")
        self.label_mast2.setPixmap(corn2)
        self.label_mast3 = QtWidgets.QLabel(self.tab_2)
        self.label_mast3.setGeometry(QtCore.QRect(label_setting_loko+1035, 57, 31, 31))
        self.label_mast3.setText("")
        self.label_mast3.setPixmap(corn3)
        self.label_mast4 = QtWidgets.QLabel(self.tab_2)
        self.label_mast4.setGeometry(QtCore.QRect(label_setting_loko+1040, 575, 21, 31))
        self.label_mast4.setText("")
        self.label_mast4.setPixmap(corn4)
        self.label_stock_1 = QtWidgets.QLabel(self.tab_8)
        self.label_stock_1.setGeometry(QtCore.QRect(9, 104, 31, 31))
        self.label_stock_1.setText("")
        self.label_stock_1.setPixmap(corn1)
        self.label_stock_2 = QtWidgets.QLabel(self.tab_8)
        self.label_stock_2.setGeometry(QtCore.QRect(9, 652, 31, 31))
        self.label_stock_2.setText("")
        self.label_stock_2.setPixmap(corn2)
        self.label_stock_3 = QtWidgets.QLabel(self.tab_8)
        self.label_stock_3.setGeometry(QtCore.QRect(label_setting_stok+1040, 104, 31, 31))
        self.label_stock_3.setText("")
        self.label_stock_3.setPixmap(corn3)
        self.label_stock_4 = QtWidgets.QLabel(self.tab_8)
        self.label_stock_4.setGeometry(QtCore.QRect(label_setting_stok+1040, 652, 31, 31))
        self.label_stock_4.setText("")
        self.label_stock_4.setPixmap(corn4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def getImageLabel(self, image):
        imageLabel = QLabel()
        imageLabel.setText("")
        imageLabel.setScaledContents(True)
        pixmap = QPixmap()
        if pixmap.loadFromData(image, "png"):
            pixmap.loadFromData(image, "png")
        elif pixmap.loadFromData(image, "jpg"):
            pixmap.loadFromData(image, "jpg")
        elif pixmap.loadFromData(image, "jpeg"):
            pixmap.loadFromData(image, "jpeg")
        imageLabel.setPixmap(pixmap)
        return imageLabel

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "База данных ЖД"))
        self.pushButton_39.setText(_translate("MainWindow", "🔍"))
        self.pushButton_40.setText(_translate("MainWindow", "🗑"))
        self.tableWidget_10.setSortingEnabled(False)
        item = self.tableWidget_10.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "№"))
        item = self.tableWidget_10.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Локо"))
        item = self.tableWidget_10.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "№ локо"))
        item = self.tableWidget_10.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Тип"))
        item = self.tableWidget_10.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Модель"))
        item = self.tableWidget_10.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Комментарий"))
        self.pushButton_41.setText(_translate("MainWindow", "-"))
        self.label_10.setText(_translate("MainWindow", "Количество записей:"))
        self.pushButton_save_3.setText(_translate("MainWindow", "💾"))
        self.pushButton_42.setText(_translate("MainWindow", "+"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_13), _translate("MainWindow", "Система 1"))
        self.pushButton_43.setText(_translate("MainWindow", "🔍"))
        self.pushButton_49.setText(_translate("MainWindow", "🗑"))
        self.label_11.setText(_translate("MainWindow", "Количество записей:"))
        self.pushButton_55.setText(_translate("MainWindow", "-"))
        self.pushButton_56.setText(_translate("MainWindow", "+"))
        item = self.tableWidget_11.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "№"))
        item = self.tableWidget_11.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Локо"))
        item = self.tableWidget_11.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "№ локо"))
        item = self.tableWidget_11.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Тип"))
        item = self.tableWidget_11.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Модель"))
        item = self.tableWidget_11.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Комментарий"))
        self.pushButton_save_4.setText(_translate("MainWindow", "💾"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_14), _translate("MainWindow", "Система 2"))
        self.pushButton_44.setText(_translate("MainWindow", "🔍"))
        self.pushButton_50.setText(_translate("MainWindow", "🗑"))
        self.label_12.setText(_translate("MainWindow", "Количество записей:"))
        self.label_23.setText(_translate("MainWindow", 'Обнуляет количество всех деталей в таблице "Детали"!'))
        self.pushButton_57.setText(_translate("MainWindow", "-"))
        self.pushButton_58.setText(_translate("MainWindow", "+"))
        item = self.tableWidget_12.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "№"))
        item = self.tableWidget_12.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Локо"))
        item = self.tableWidget_12.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "№ локо"))
        item = self.tableWidget_12.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Тип"))
        item = self.tableWidget_12.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Модель"))
        item = self.tableWidget_12.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Комментарий"))
        self.pushButton_save_5.setText(_translate("MainWindow", "💾"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_15), _translate("MainWindow", "Система 3"))
        self.pushButton_45.setText(_translate("MainWindow", "🔍"))
        self.pushButton_51.setText(_translate("MainWindow", "🗑"))
        self.label_13.setText(_translate("MainWindow", "Количество записей:"))
        self.pushButton_59.setText(_translate("MainWindow", "-"))
        self.pushButton_60.setText(_translate("MainWindow", "+"))
        item = self.tableWidget_13.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "№"))
        item = self.tableWidget_13.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Локо"))
        item = self.tableWidget_13.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "№ локо"))
        item = self.tableWidget_13.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Тип"))
        item = self.tableWidget_13.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Модель"))
        item = self.tableWidget_13.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Комментарий"))
        self.pushButton_save_6.setText(_translate("MainWindow", "💾"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_16), _translate("MainWindow", "Система 4"))
        self.pushButton_46.setText(_translate("MainWindow", "🔍"))
        self.pushButton_52.setText(_translate("MainWindow", "🗑"))
        self.label_14.setText(_translate("MainWindow", "Количество записей:"))
        self.pushButton_61.setText(_translate("MainWindow", "-"))
        self.pushButton_62.setText(_translate("MainWindow", "+"))
        item = self.tableWidget_14.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "№"))
        item = self.tableWidget_14.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Локо"))
        item = self.tableWidget_14.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "№ локо"))
        item = self.tableWidget_14.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Тип"))
        item = self.tableWidget_14.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Модель"))
        item = self.tableWidget_14.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Комментарий"))
        self.pushButton_save_7.setText(_translate("MainWindow", "💾"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_17), _translate("MainWindow", "Система 5"))
        self.pushButton_47.setText(_translate("MainWindow", "🔍"))
        self.pushButton_53.setText(_translate("MainWindow", "🗑"))
        self.label_15.setText(_translate("MainWindow", "Количество записей:"))
        self.pushButton_63.setText(_translate("MainWindow", "-"))
        self.pushButton_64.setText(_translate("MainWindow", "+"))
        item = self.tableWidget_15.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "№"))
        item = self.tableWidget_15.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Локо"))
        item = self.tableWidget_15.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "№ локо"))
        item = self.tableWidget_15.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Тип"))
        item = self.tableWidget_15.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Модель"))
        item = self.tableWidget_15.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Комментарий"))
        self.pushButton_save_8.setText(_translate("MainWindow", "💾"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_18), _translate("MainWindow", "Система 6"))
        self.pushButton_48.setText(_translate("MainWindow", "🔍"))
        self.pushButton_54.setText(_translate("MainWindow", "🗑"))
        self.label_16.setText(_translate("MainWindow", "Количество записей:"))
        self.pushButton_65.setText(_translate("MainWindow", "-"))
        self.pushButton_66.setText(_translate("MainWindow", "+"))
        item = self.tableWidget_16.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "№"))
        item = self.tableWidget_16.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Локо"))
        item = self.tableWidget_16.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "№ локо"))
        item = self.tableWidget_16.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Тип"))
        item = self.tableWidget_16.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Модель"))
        item = self.tableWidget_16.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Комментарий"))
        self.pushButton_save_9.setText(_translate("MainWindow", "💾"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_19), _translate("MainWindow", "Система 7"))
        self.pushButton_69.setText(_translate("MainWindow", "🔍"))
        self.pushButton_70.setText(_translate("MainWindow", "🗑"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "№"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Локо"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "№ локо"))
        item = self.tableWidget_3.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Тип"))
        item = self.tableWidget_3.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Модель"))
        item = self.tableWidget_3.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Комментарий"))
        self.pushButton_71.setText(_translate("MainWindow", "-"))
        self.label_17.setText(_translate("MainWindow", "Количество записей:"))
        self.pushButton_save_10.setText(_translate("MainWindow", "💾"))
        self.pushButton_72.setText(_translate("MainWindow", "+"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_3), _translate("MainWindow", "Локодром"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Локо"))
        self.pushButton.setText(_translate("MainWindow", "+"))
        self.pushButton_2.setText(_translate("MainWindow", "-"))
        self.pushButton_3.setText(_translate("MainWindow", "🔍"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "№"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Фото"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Артикул"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Тип детали"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Модель"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Количество"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Детали"))
        self.pushButton_9.setText(_translate("MainWindow", "🗑"))
        self.pushButton_save.setText(_translate("MainWindow", "💾"))
        self.label.setText(_translate("MainWindow", "Количество записей:"))
        self.pushButton_11.setText(_translate("MainWindow", "↺"))
        self.pushButton_7.setText(_translate("MainWindow", "Обнулить все детали"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Детали"))
        self.pushButton_4.setText(_translate("MainWindow", "🔍"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "№"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ФИО"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Должность"))
        self.pushButton_10.setText(_translate("MainWindow", "🗑"))
        self.label_2.setText(_translate("MainWindow", "Количество записей:"))
        self.pushButton_save_2.setText(_translate("MainWindow", "💾"))
        self.pushButton_67.setText(_translate("MainWindow", "-"))
        self.pushButton_68.setText(_translate("MainWindow", "+"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Мастера"))
        self.pushButton_5.setText(_translate("MainWindow", "Авторизация"))
        self.pushButton_6.setText(_translate("MainWindow", "Входы в БД"))
        self.pushButton_13.setText(_translate("MainWindow", "Типы локомотивов"))
        self.pushButton_14.setText(_translate("MainWindow", "Сделать копию базы"))
        self.pushButton_8.setText(_translate("MainWindow", "Статистика по привозу/расходу деталей"))
        self.pushButton_12.setText(_translate("MainWindow", "Журнал ТО"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Другое"))
        self.pushButton_76.setText(_translate("MainWindow", "🔍"))
        self.pushButton_77.setText(_translate("MainWindow", "🗑"))
        self.pushButton_78.setText(_translate("MainWindow", "-"))
        self.pushButton_79.setText(_translate("MainWindow", "🔍"))
        self.pushButton_92.setText(_translate("MainWindow", "🗑"))
        self.pushButton_save_11.setText(_translate("MainWindow", "💾"))
        item = self.tableWidget_21.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "№"))
        item = self.tableWidget_21.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Артикул"))
        item = self.tableWidget_21.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Наименование"))
        item = self.tableWidget_21.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Количество"))
        self.pushButton_101.setText(_translate("MainWindow", "-"))
        self.pushButton_102.setText(_translate("MainWindow", "+"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_20), _translate("MainWindow", "Подвижной состав"))
        self.pushButton_80.setText(_translate("MainWindow", "🔍"))
        self.pushButton_81.setText(_translate("MainWindow", "🗑"))
        self.label_28.setText(_translate("MainWindow", "Количество записей:"))
        self.pushButton_82.setText(_translate("MainWindow", "-"))
        self.pushButton_83.setText(_translate("MainWindow", "+"))
        item = self.tableWidget_18.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "№"))
        item = self.tableWidget_18.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Локо"))
        item = self.tableWidget_18.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "№ локо"))
        item = self.tableWidget_18.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Тип"))
        item = self.tableWidget_18.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Модель"))
        item = self.tableWidget_18.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Комментарий"))
        self.pushButton_93.setText(_translate("MainWindow", "🔍"))
        self.pushButton_94.setText(_translate("MainWindow", "🗑"))
        self.pushButton_save_12.setText(_translate("MainWindow", "💾"))
        item = self.tableWidget_22.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "№"))
        item = self.tableWidget_22.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Артикул"))
        item = self.tableWidget_22.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Наименование"))
        item = self.tableWidget_22.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Количество"))
        self.pushButton_103.setText(_translate("MainWindow", "+"))
        self.pushButton_104.setText(_translate("MainWindow", "-"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_21), _translate("MainWindow", "Электроника"))
        self.pushButton_84.setText(_translate("MainWindow", "🔍"))
        self.pushButton_85.setText(_translate("MainWindow", "🗑"))
        self.label_29.setText(_translate("MainWindow", "Количество записей:"))
        self.pushButton_86.setText(_translate("MainWindow", "-"))
        self.pushButton_87.setText(_translate("MainWindow", "+"))
        item = self.tableWidget_19.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "№"))
        item = self.tableWidget_19.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Локо"))
        item = self.tableWidget_19.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "№ локо"))
        item = self.tableWidget_19.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Тип"))
        item = self.tableWidget_19.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Модель"))
        item = self.tableWidget_19.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Комментарий"))
        self.pushButton_95.setText(_translate("MainWindow", "🔍"))
        self.pushButton_96.setText(_translate("MainWindow", "🗑"))
        self.pushButton_save_13.setText(_translate("MainWindow", "💾"))
        item = self.tableWidget_23.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "№"))
        item = self.tableWidget_23.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Артикул"))
        item = self.tableWidget_23.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Наименование"))
        item = self.tableWidget_23.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Количество"))
        self.pushButton_105.setText(_translate("MainWindow", "-"))
        self.pushButton_106.setText(_translate("MainWindow", "+"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_22), _translate("MainWindow", "Путевые материалы"))
        self.pushButton_88.setText(_translate("MainWindow", "🔍"))
        self.pushButton_89.setText(_translate("MainWindow", "🗑"))
        self.label_30.setText(_translate("MainWindow", "Количество записей:"))
        self.pushButton_90.setText(_translate("MainWindow", "-"))
        self.pushButton_91.setText(_translate("MainWindow", "+"))
        item = self.tableWidget_20.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "№"))
        item = self.tableWidget_20.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Локо"))
        item = self.tableWidget_20.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "№ локо"))
        item = self.tableWidget_20.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Тип"))
        item = self.tableWidget_20.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Модель"))
        item = self.tableWidget_20.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Комментарий"))
        self.pushButton_97.setText(_translate("MainWindow", "🔍"))
        self.pushButton_98.setText(_translate("MainWindow", "🗑"))
        self.pushButton_save_14.setText(_translate("MainWindow", "💾"))
        item = self.tableWidget_24.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "№"))
        item = self.tableWidget_24.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Артикул"))
        item = self.tableWidget_24.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Наименование"))
        item = self.tableWidget_24.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Количество"))
        self.label_31.setText(_translate("MainWindow", "Количество записей:"))
        self.label_32.setText(_translate("MainWindow", "Количество записей:"))
        self.label_33.setText(_translate("MainWindow", "Количество записей:"))
        self.label_34.setText(_translate("MainWindow", "Количество записей:"))
        self.pushButton_199.setText(_translate("MainWindow", "+"))
        self.pushButton_100.setText(_translate("MainWindow", "-"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_23), _translate("MainWindow", "Расходники"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), _translate("MainWindow", "Склад"))
        self.pushButton_99.setText(_translate("MainWindow", "🚇"))
        self.pushButton_74.setText(_translate("MainWindow", "-"))
        self.pushButton_73.setText(_translate("MainWindow", "X"))
        self.label_51.setText(_translate("MainWindow", "База данных ЖД"))

class ExampleApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.start = QPoint(0, 0)  # +
        self.pressing = False  # +

    # + vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
    def mousePressEvent(self, event):
        if (event.pos()).y() <= 34 :
            self.start = self.mapToGlobal(event.pos())
            self.pressing = True

    def mouseMoveEvent(self, event):
        if self.pressing:
            self.end = self.mapToGlobal(event.pos())
            self.movement = self.end - self.start
            self.setGeometry(self.mapToGlobal(self.movement).x(),
                             self.mapToGlobal(self.movement).y(),
                             self.width(),
                             self.height())
            self.start = self.end

    def mouseReleaseEvent(self, QMouseEvent):
        self.pressing = False

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
