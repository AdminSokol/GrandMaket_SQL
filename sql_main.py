import datetime
from datetime import date

from PyQt5 import uic, QtWidgets, QtCore
from PyQt5.uic.properties import QtGui
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTabWidget, QTableWidgetItem, QWidget, \
    QStyledItemDelegate, QDialog, QAbstractItemView
import sqlite3


class Test(QtWidgets.QTableWidget):
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
                        cursor.execute(f"""DELETE FROM TO1 WHERE ID='{iter}'""")
                        sqlite_connection.commit()
                        it.tableWidget().setRowCount(0)
                        users = cursor.execute("SELECT * FROM TO1")
                        for row_number, order in enumerate(users):
                            rama.insertRow(row_number)
                            for column_number, data in enumerate(order):
                                cell = QtWidgets.QTableWidgetItem(str(data))
                                rama.setItem(row_number, column_number, cell)
                                cell.setTextAlignment(Qt.AlignCenter)
                if it.column() == 7:
                    fuck = QtWidgets.QMenu(self)
                    fuck.setGeometry(QtCore.QRect(20, 20, 20, 20))
                    today = date.today()
                    lol = fuck.addAction(today.strftime("%d.%m.%Y"))
                    action = fuck.exec_(self.mapToGlobal(e.pos()))
                    if action == lol:
                        it.setText(today.strftime("%d.%m.%Y"))
                if it.column() == 2:
                    fuck = QtWidgets.QMenu(self)
                    fuck.setGeometry(QtCore.QRect(20, 20, 20, 20))
                    TO1 = fuck.addAction("План")
                    TO2 = fuck.addAction("Внеплан")
                    TO3 = fuck.addAction("Ремонт")
                    action = fuck.exec_(self.mapToGlobal(e.pos()))
                    if action == TO1:
                        it.setText("План")
                    if action == TO2:
                        it.setText("Внеплан")
                    if action == TO3:
                        it.setText("Ремонт")
                if it.column() == 3:
                    fuck = QtWidgets.QMenu(self)
                    fuck.setGeometry(QtCore.QRect(20, 20, 20, 20))
                    pl = fuck.addAction("+")
                    min = fuck.addAction("-")
                    action = fuck.exec_(self.mapToGlobal(e.pos()))
                    if action == pl:
                        it.setText("+")
                    if action == min:
                        it.setText("-")
                if it.column() == 1:
                    iter = it.text()
                    Form, App = uic.loadUiType("loko.ui")
                    app = QtWidgets.QDialog()
                    form = Form()
                    form.setupUi(app)
                    app.show()
                    sqlite_connection = sqlite3.connect("id.db")
                    cursor = sqlite_connection.cursor()
                    users = cursor.execute(
                        f"""SELECT ID,repair,master,userid,hours,datas FROM TO1 WHERE loko='{iter}' ORDER BY datas DESC LIMIT 6""")
                    for row_number1, order in enumerate(users):
                        form.tableWidget.insertRow(row_number1)
                        for column_number, data in enumerate(order):
                            cell = QtWidgets.QTableWidgetItem(str(data))
                            form.tableWidget.setItem(row_number1, column_number, cell)
                            cell.setTextAlignment(Qt.AlignCenter)
                            form.tableWidget.horizontalHeader().setSectionResizeMode(0,
                                                                                     QtWidgets.QHeaderView.ResizeToContents)
                            form.tableWidget.horizontalHeader().setSectionResizeMode(1,
                                                                                     QtWidgets.QHeaderView.ResizeToContents)
                            form.tableWidget.horizontalHeader().setSectionResizeMode(2,
                                                                                     QtWidgets.QHeaderView.ResizeToContents)
                            form.tableWidget.horizontalHeader().setSectionResizeMode(3,
                                                                                     QtWidgets.QHeaderView.Stretch)
                            form.tableWidget.horizontalHeader().setSectionResizeMode(4,
                                                                                     QtWidgets.QHeaderView.ResizeToContents)
                            form.tableWidget.horizontalHeader().setSectionResizeMode(5,
                                                                                     QtWidgets.QHeaderView.ResizeToContents)
                    form.lineEdit.setText(str(iter))
                    hour = cursor.execute(
                        f"""SELECT SUM(hours) FROM TO1 WHERE loko='{iter}'""")
                    intel = hour.fetchall()
                    rom = int()
                    for number, lul in enumerate(intel):
                        try:
                            a = int(intel[number][0])
                            rom += a
                        except:
                            pass
                    form.lineEdit_2.setText(str(rom))
                    app.exec()
                if it.column() == 4:
                    fuck = QtWidgets.QMenu(self)
                    fuck.setGeometry(QtCore.QRect(20, 20, 20, 20))
                    sqlite_connection = sqlite3.connect("id.db")
                    cursor = sqlite_connection.cursor()
                    users = cursor.execute("""SELECT fio FROM masters""")
                    pickle = users.fetchall()
                    add = []
                    for number, lul in enumerate(pickle):
                        a = fuck.addAction(str(pickle[number][0]))
                        add.append(a)
                    action = fuck.exec_(self.mapToGlobal(e.pos()))
                    for number, lul in enumerate(pickle):
                        if action == add[number]:
                            it.setText(str(pickle[number][0]))
            QtWidgets.QTableWidget.mousePressEvent(self, e)
        except:
            pass


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
                        sqlite_connection = sqlite3.connect("id.db")
                        cursor = sqlite_connection.cursor()
                        iter = it.text()
                        cursor.execute(f"""DELETE FROM TO2 WHERE ID='{iter}'""")
                        sqlite_connection.commit()
                        it.tableWidget().setRowCount(0)
                        users = cursor.execute("SELECT * FROM TO2")
                        for row_number2, order in enumerate(users):
                            rama.insertRow(row_number2)
                            for column_number, data in enumerate(order):
                                cell = QtWidgets.QTableWidgetItem(str(data))
                                rama.setItem(row_number2, column_number, cell)
                                cell.setTextAlignment(Qt.AlignCenter)
                if it.column() == 7:
                    fuck = QtWidgets.QMenu(self)
                    fuck.setGeometry(QtCore.QRect(20, 20, 20, 20))
                    today = date.today()
                    lol = fuck.addAction(today.strftime("%d.%m.%Y"))
                    action = fuck.exec_(self.mapToGlobal(e.pos()))
                    if action == lol:
                        it.setText(today.strftime("%d.%m.%Y"))
                if it.column() == 2:
                    fuck = QtWidgets.QMenu(self)
                    fuck.setGeometry(QtCore.QRect(20, 20, 20, 20))
                    TO1 = fuck.addAction("План")
                    TO2 = fuck.addAction("Внеплан")
                    TO3 = fuck.addAction("Ремонт")
                    action = fuck.exec_(self.mapToGlobal(e.pos()))
                    if action == TO1:
                        it.setText("План")
                    if action == TO2:
                        it.setText("Внеплан")
                    if action == TO3:
                        it.setText("Ремонт")
                if it.column() == 3:
                    fuck = QtWidgets.QMenu(self)
                    fuck.setGeometry(QtCore.QRect(20, 20, 20, 20))
                    pl = fuck.addAction("+")
                    min = fuck.addAction("-")
                    action = fuck.exec_(self.mapToGlobal(e.pos()))
                    if action == pl:
                        it.setText("+")
                    if action == min:
                        it.setText("-")
                if it.column() == 1:
                    iter = it.text()
                    Form, App = uic.loadUiType("loko.ui")
                    app = QtWidgets.QDialog()
                    form = Form()
                    form.setupUi(app)
                    app.show()
                    sqlite_connection = sqlite3.connect("id.db")
                    cursor = sqlite_connection.cursor()
                    users = cursor.execute(
                        f"""SELECT ID,repair,master,userid,hours,datas FROM TO2 WHERE loko='{iter}' ORDER BY datas DESC LIMIT 6""")
                    for row_number2, order in enumerate(users):
                        form.tableWidget.insertRow(row_number2)
                        for column_number, data in enumerate(order):
                            cell = QtWidgets.QTableWidgetItem(str(data))
                            form.tableWidget.setItem(row_number2, column_number, cell)
                            cell.setTextAlignment(Qt.AlignCenter)
                            form.tableWidget.horizontalHeader().setSectionResizeMode(0,
                                                                                     QtWidgets.QHeaderView.ResizeToContents)
                            form.tableWidget.horizontalHeader().setSectionResizeMode(1,
                                                                                     QtWidgets.QHeaderView.ResizeToContents)
                            form.tableWidget.horizontalHeader().setSectionResizeMode(2,
                                                                                     QtWidgets.QHeaderView.ResizeToContents)
                            form.tableWidget.horizontalHeader().setSectionResizeMode(3,
                                                                                     QtWidgets.QHeaderView.Stretch)
                            form.tableWidget.horizontalHeader().setSectionResizeMode(4,
                                                                                     QtWidgets.QHeaderView.ResizeToContents)
                            form.tableWidget.horizontalHeader().setSectionResizeMode(5,
                                                                                     QtWidgets.QHeaderView.ResizeToContents)
                    form.lineEdit.setText(str(iter))
                    hour = cursor.execute(
                        f"""SELECT SUM(hours) FROM TO2 WHERE loko='{iter}'""")
                    intel = hour.fetchall()
                    rom = int()
                    for number, lul in enumerate(intel):
                        try:
                            a = int(intel[number][0])
                            rom += a
                        except:
                            pass
                    form.lineEdit_2.setText(str(rom))
                    app.exec()
                if it.column() == 4:
                    fuck = QtWidgets.QMenu(self)
                    fuck.setGeometry(QtCore.QRect(20, 20, 20, 20))
                    sqlite_connection = sqlite3.connect("id.db")
                    cursor = sqlite_connection.cursor()
                    users = cursor.execute("""SELECT fio FROM masters""")
                    pickle = users.fetchall()
                    add = []
                    for number, lul in enumerate(pickle):
                        a = fuck.addAction(str(pickle[number][0]))
                        add.append(a)
                    action = fuck.exec_(self.mapToGlobal(e.pos()))
                    for number, lul in enumerate(pickle):
                        if action == add[number]:
                            it.setText(str(pickle[number][0]))
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
                        sqlite_connection = sqlite3.connect("id.db")
                        cursor = sqlite_connection.cursor()
                        iter = it.text()
                        cursor.execute(f"""DELETE FROM TO3 WHERE ID='{iter}'""")
                        sqlite_connection.commit()
                        it.tableWidget().setRowCount(0)
                        users = cursor.execute("SELECT * FROM TO3")
                        for row_number3, order in enumerate(users):
                            rama.insertRow(row_number3)
                            for column_number, data in enumerate(order):
                                cell = QtWidgets.QTableWidgetItem(str(data))
                                rama.setItem(row_number3, column_number, cell)
                                cell.setTextAlignment(Qt.AlignCenter)
                if it.column() == 7:
                    fuck = QtWidgets.QMenu(self)
                    fuck.setGeometry(QtCore.QRect(20, 20, 20, 20))
                    today = date.today()
                    lol = fuck.addAction(today.strftime("%d.%m.%Y"))
                    action = fuck.exec_(self.mapToGlobal(e.pos()))
                    if action == lol:
                        it.setText(today.strftime("%d.%m.%Y"))
                if it.column() == 2:
                    fuck = QtWidgets.QMenu(self)
                    fuck.setGeometry(QtCore.QRect(20, 20, 20, 20))
                    TO1 = fuck.addAction("План")
                    TO2 = fuck.addAction("Внеплан")
                    TO3 = fuck.addAction("Ремонт")
                    action = fuck.exec_(self.mapToGlobal(e.pos()))
                    if action == TO1:
                        it.setText("План")
                    if action == TO2:
                        it.setText("Внеплан")
                    if action == TO3:
                        it.setText("Ремонт")
                if it.column() == 3:
                    fuck = QtWidgets.QMenu(self)
                    fuck.setGeometry(QtCore.QRect(20, 20, 20, 20))
                    pl = fuck.addAction("+")
                    min = fuck.addAction("-")
                    action = fuck.exec_(self.mapToGlobal(e.pos()))
                    if action == pl:
                        it.setText("+")
                    if action == min:
                        it.setText("-")
                if it.column() == 1:
                    iter = it.text()
                    Form, App = uic.loadUiType("loko.ui")
                    app = QtWidgets.QDialog()
                    form = Form()
                    form.setupUi(app)
                    app.show()
                    sqlite_connection = sqlite3.connect("id.db")
                    cursor = sqlite_connection.cursor()
                    users = cursor.execute(
                        f"""SELECT ID,repair,master,userid,hours,datas FROM TO3 WHERE loko='{iter}' ORDER BY datas DESC LIMIT 6""")
                    for row_number3, order in enumerate(users):
                        form.tableWidget.insertRow(row_number3)
                        for column_number, data in enumerate(order):
                            cell = QtWidgets.QTableWidgetItem(str(data))
                            form.tableWidget.setItem(row_number3, column_number, cell)
                            cell.setTextAlignment(Qt.AlignCenter)
                            form.tableWidget.horizontalHeader().setSectionResizeMode(0,
                                                                                     QtWidgets.QHeaderView.ResizeToContents)
                            form.tableWidget.horizontalHeader().setSectionResizeMode(1,
                                                                                     QtWidgets.QHeaderView.ResizeToContents)
                            form.tableWidget.horizontalHeader().setSectionResizeMode(2,
                                                                                     QtWidgets.QHeaderView.ResizeToContents)
                            form.tableWidget.horizontalHeader().setSectionResizeMode(3,
                                                                                     QtWidgets.QHeaderView.Stretch)
                            form.tableWidget.horizontalHeader().setSectionResizeMode(4,
                                                                                     QtWidgets.QHeaderView.ResizeToContents)
                            form.tableWidget.horizontalHeader().setSectionResizeMode(5,
                                                                                     QtWidgets.QHeaderView.ResizeToContents)
                    form.lineEdit.setText(str(iter))
                    hour = cursor.execute(
                        f"""SELECT SUM(hours) FROM TO3 WHERE loko='{iter}'""")
                    intel = hour.fetchall()
                    rom = int()
                    for number, lul in enumerate(intel):
                        try:
                            a = int(intel[number][0])
                            rom += a
                        except:
                            pass
                    form.lineEdit_2.setText(str(rom))
                    app.exec()
                if it.column() == 4:
                    fuck = QtWidgets.QMenu(self)
                    fuck.setGeometry(QtCore.QRect(20, 20, 20, 20))
                    sqlite_connection = sqlite3.connect("id.db")
                    cursor = sqlite_connection.cursor()
                    users = cursor.execute("""SELECT fio FROM masters""")
                    pickle = users.fetchall()
                    add = []
                    for number, lul in enumerate(pickle):
                        a = fuck.addAction(str(pickle[number][0]))
                        add.append(a)
                    action = fuck.exec_(self.mapToGlobal(e.pos()))
                    for number, lul in enumerate(pickle):
                        if action == add[number]:
                            it.setText(str(pickle[number][0]))
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
                        sqlite_connection = sqlite3.connect("id.db")
                        cursor = sqlite_connection.cursor()
                        iter = it.text()
                        cursor.execute(f"""DELETE FROM TO4 WHERE ID='{iter}'""")
                        sqlite_connection.commit()
                        it.tableWidget().setRowCount(0)
                        users = cursor.execute("SELECT * FROM TO4")
                        for row_number4, order in enumerate(users):
                            rama.insertRow(row_number4)
                            for column_number, data in enumerate(order):
                                cell = QtWidgets.QTableWidgetItem(str(data))
                                rama.setItem(row_number4, column_number, cell)
                                cell.setTextAlignment(Qt.AlignCenter)
                if it.column() == 7:
                    fuck = QtWidgets.QMenu(self)
                    fuck.setGeometry(QtCore.QRect(20, 20, 20, 20))
                    today = date.today()
                    lol = fuck.addAction(today.strftime("%d.%m.%Y"))
                    action = fuck.exec_(self.mapToGlobal(e.pos()))
                    if action == lol:
                        it.setText(today.strftime("%d.%m.%Y"))
                if it.column() == 2:
                    fuck = QtWidgets.QMenu(self)
                    fuck.setGeometry(QtCore.QRect(20, 20, 20, 20))
                    TO1 = fuck.addAction("План")
                    TO2 = fuck.addAction("Внеплан")
                    TO3 = fuck.addAction("Ремонт")
                    action = fuck.exec_(self.mapToGlobal(e.pos()))
                    if action == TO1:
                        it.setText("План")
                    if action == TO2:
                        it.setText("Внеплан")
                    if action == TO3:
                        it.setText("Ремонт")
                if it.column() == 3:
                    fuck = QtWidgets.QMenu(self)
                    fuck.setGeometry(QtCore.QRect(20, 20, 20, 20))
                    pl = fuck.addAction("+")
                    min = fuck.addAction("-")
                    action = fuck.exec_(self.mapToGlobal(e.pos()))
                    if action == pl:
                        it.setText("+")
                    if action == min:
                        it.setText("-")
                if it.column() == 1:
                    iter = it.text()
                    Form, App = uic.loadUiType("loko.ui")
                    app = QtWidgets.QDialog()
                    form = Form()
                    form.setupUi(app)
                    app.show()
                    sqlite_connection = sqlite3.connect("id.db")
                    cursor = sqlite_connection.cursor()
                    users = cursor.execute(
                        f"""SELECT ID,repair,master,userid,hours,datas FROM TO4 WHERE loko='{iter}' ORDER BY datas DESC LIMIT 6""")
                    for row_number4, order in enumerate(users):
                        form.tableWidget.insertRow(row_number4)
                        for column_number, data in enumerate(order):
                            cell = QtWidgets.QTableWidgetItem(str(data))
                            form.tableWidget.setItem(row_number4, column_number, cell)
                            cell.setTextAlignment(Qt.AlignCenter)
                            form.tableWidget.horizontalHeader().setSectionResizeMode(0,
                                                                                     QtWidgets.QHeaderView.ResizeToContents)
                            form.tableWidget.horizontalHeader().setSectionResizeMode(1,
                                                                                     QtWidgets.QHeaderView.ResizeToContents)
                            form.tableWidget.horizontalHeader().setSectionResizeMode(2,
                                                                                     QtWidgets.QHeaderView.ResizeToContents)
                            form.tableWidget.horizontalHeader().setSectionResizeMode(3,
                                                                                     QtWidgets.QHeaderView.Stretch)
                            form.tableWidget.horizontalHeader().setSectionResizeMode(4,
                                                                                     QtWidgets.QHeaderView.ResizeToContents)
                            form.tableWidget.horizontalHeader().setSectionResizeMode(5,
                                                                                     QtWidgets.QHeaderView.ResizeToContents)
                    form.lineEdit.setText(str(iter))
                    hour = cursor.execute(
                        f"""SELECT SUM(hours) FROM TO4 WHERE loko='{iter}'""")
                    intel = hour.fetchall()
                    rom = int()
                    for number, lul in enumerate(intel):
                        try:
                            a = int(intel[number][0])
                            rom += a
                        except:
                            pass
                    form.lineEdit_2.setText(str(rom))
                    app.exec()
                if it.column() == 4:
                    fuck = QtWidgets.QMenu(self)
                    fuck.setGeometry(QtCore.QRect(20, 20, 20, 20))
                    sqlite_connection = sqlite3.connect("id.db")
                    cursor = sqlite_connection.cursor()
                    users = cursor.execute("""SELECT fio FROM masters""")
                    pickle = users.fetchall()
                    add = []
                    for number, lul in enumerate(pickle):
                        a = fuck.addAction(str(pickle[number][0]))
                        add.append(a)
                    action = fuck.exec_(self.mapToGlobal(e.pos()))
                    for number, lul in enumerate(pickle):
                        if action == add[number]:
                            it.setText(str(pickle[number][0]))
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
                        sqlite_connection = sqlite3.connect("id.db")
                        cursor = sqlite_connection.cursor()
                        iter = it.text()
                        cursor.execute(f"""DELETE FROM TO5 WHERE ID='{iter}'""")
                        sqlite_connection.commit()
                        it.tableWidget().setRowCount(0)
                        users = cursor.execute("SELECT * FROM TO5")
                        for row_number5, order in enumerate(users):
                            rama.insertRow(row_number5)
                            for column_number, data in enumerate(order):
                                cell = QtWidgets.QTableWidgetItem(str(data))
                                rama.setItem(row_number5, column_number, cell)
                                cell.setTextAlignment(Qt.AlignCenter)
                if it.column() == 7:
                    fuck = QtWidgets.QMenu(self)
                    fuck.setGeometry(QtCore.QRect(20, 20, 20, 20))
                    today = date.today()
                    lol = fuck.addAction(today.strftime("%d.%m.%Y"))
                    action = fuck.exec_(self.mapToGlobal(e.pos()))
                    if action == lol:
                        it.setText(today.strftime("%d.%m.%Y"))
                if it.column() == 2:
                    fuck = QtWidgets.QMenu(self)
                    fuck.setGeometry(QtCore.QRect(20, 20, 20, 20))
                    TO1 = fuck.addAction("План")
                    TO2 = fuck.addAction("Внеплан")
                    TO3 = fuck.addAction("Ремонт")
                    action = fuck.exec_(self.mapToGlobal(e.pos()))
                    if action == TO1:
                        it.setText("План")
                    if action == TO2:
                        it.setText("Внеплан")
                    if action == TO3:
                        it.setText("Ремонт")
                if it.column() == 3:
                    fuck = QtWidgets.QMenu(self)
                    fuck.setGeometry(QtCore.QRect(20, 20, 20, 20))
                    pl = fuck.addAction("+")
                    min = fuck.addAction("-")
                    action = fuck.exec_(self.mapToGlobal(e.pos()))
                    if action == pl:
                        it.setText("+")
                    if action == min:
                        it.setText("-")
                if it.column() == 1:
                    iter = it.text()
                    Form, App = uic.loadUiType("loko.ui")
                    app = QtWidgets.QDialog()
                    form = Form()
                    form.setupUi(app)
                    app.show()
                    sqlite_connection = sqlite3.connect("id.db")
                    cursor = sqlite_connection.cursor()
                    users = cursor.execute(
                        f"""SELECT ID,repair,master,userid,hours,datas FROM TO5 WHERE loko='{iter}' ORDER BY datas DESC LIMIT 6""")
                    for row_number5, order in enumerate(users):
                        form.tableWidget.insertRow(row_number5)
                        for column_number, data in enumerate(order):
                            cell = QtWidgets.QTableWidgetItem(str(data))
                            form.tableWidget.setItem(row_number5, column_number, cell)
                            cell.setTextAlignment(Qt.AlignCenter)
                            form.tableWidget.horizontalHeader().setSectionResizeMode(0,
                                                                                     QtWidgets.QHeaderView.ResizeToContents)
                            form.tableWidget.horizontalHeader().setSectionResizeMode(1,
                                                                                     QtWidgets.QHeaderView.ResizeToContents)
                            form.tableWidget.horizontalHeader().setSectionResizeMode(2,
                                                                                     QtWidgets.QHeaderView.ResizeToContents)
                            form.tableWidget.horizontalHeader().setSectionResizeMode(3,
                                                                                     QtWidgets.QHeaderView.Stretch)
                            form.tableWidget.horizontalHeader().setSectionResizeMode(4,
                                                                                     QtWidgets.QHeaderView.ResizeToContents)
                            form.tableWidget.horizontalHeader().setSectionResizeMode(5,
                                                                                     QtWidgets.QHeaderView.ResizeToContents)
                    form.lineEdit.setText(str(iter))
                    hour = cursor.execute(
                        f"""SELECT SUM(hours) FROM TO5 WHERE loko='{iter}'""")
                    intel = hour.fetchall()
                    rom = int()
                    for number, lul in enumerate(intel):
                        try:
                            a = int(intel[number][0])
                            rom += a
                        except:
                            pass
                    form.lineEdit_2.setText(str(rom))
                    app.exec()
                if it.column() == 4:
                    fuck = QtWidgets.QMenu(self)
                    fuck.setGeometry(QtCore.QRect(20, 20, 20, 20))
                    sqlite_connection = sqlite3.connect("id.db")
                    cursor = sqlite_connection.cursor()
                    users = cursor.execute("""SELECT fio FROM masters""")
                    pickle = users.fetchall()
                    add = []
                    for number, lul in enumerate(pickle):
                        a = fuck.addAction(str(pickle[number][0]))
                        add.append(a)
                    action = fuck.exec_(self.mapToGlobal(e.pos()))
                    for number, lul in enumerate(pickle):
                        if action == add[number]:
                            it.setText(str(pickle[number][0]))
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
                        sqlite_connection = sqlite3.connect("id.db")
                        cursor = sqlite_connection.cursor()
                        iter = it.text()
                        cursor.execute(f"""DELETE FROM TO6 WHERE ID='{iter}'""")
                        sqlite_connection.commit()
                        it.tableWidget().setRowCount(0)
                        users = cursor.execute("SELECT * FROM TO6")
                        for row_number5, order in enumerate(users):
                            rama.insertRow(row_number5)
                            for column_number, data in enumerate(order):
                                cell = QtWidgets.QTableWidgetItem(str(data))
                                rama.setItem(row_number5, column_number, cell)
                                cell.setTextAlignment(Qt.AlignCenter)
                if it.column() == 7:
                    fuck = QtWidgets.QMenu(self)
                    fuck.setGeometry(QtCore.QRect(20, 20, 20, 20))
                    today = date.today()
                    lol = fuck.addAction(today.strftime("%d.%m.%Y"))
                    action = fuck.exec_(self.mapToGlobal(e.pos()))
                    if action == lol:
                        it.setText(today.strftime("%d.%m.%Y"))
                if it.column() == 2:
                    fuck = QtWidgets.QMenu(self)
                    fuck.setGeometry(QtCore.QRect(20, 20, 20, 20))
                    TO1 = fuck.addAction("План")
                    TO2 = fuck.addAction("Внеплан")
                    TO3 = fuck.addAction("Ремонт")
                    action = fuck.exec_(self.mapToGlobal(e.pos()))
                    if action == TO1:
                        it.setText("План")
                    if action == TO2:
                        it.setText("Внеплан")
                    if action == TO3:
                        it.setText("Ремонт")
                if it.column() == 3:
                    fuck = QtWidgets.QMenu(self)
                    fuck.setGeometry(QtCore.QRect(20, 20, 20, 20))
                    pl = fuck.addAction("+")
                    min = fuck.addAction("-")
                    action = fuck.exec_(self.mapToGlobal(e.pos()))
                    if action == pl:
                        it.setText("+")
                    if action == min:
                        it.setText("-")
                if it.column() == 1:
                    iter = it.text()
                    Form, App = uic.loadUiType("loko.ui")
                    app = QtWidgets.QDialog()
                    form = Form()
                    form.setupUi(app)
                    app.show()
                    sqlite_connection = sqlite3.connect("id.db")
                    cursor = sqlite_connection.cursor()
                    users = cursor.execute(
                        f"""SELECT ID,repair,master,userid,hours,datas FROM TO6 WHERE loko='{iter}' ORDER BY datas DESC LIMIT 6""")
                    for row_number5, order in enumerate(users):
                        form.tableWidget.insertRow(row_number5)
                        for column_number, data in enumerate(order):
                            cell = QtWidgets.QTableWidgetItem(str(data))
                            form.tableWidget.setItem(row_number5, column_number, cell)
                            cell.setTextAlignment(Qt.AlignCenter)
                            form.tableWidget.horizontalHeader().setSectionResizeMode(0,
                                                                                     QtWidgets.QHeaderView.ResizeToContents)
                            form.tableWidget.horizontalHeader().setSectionResizeMode(1,
                                                                                     QtWidgets.QHeaderView.ResizeToContents)
                            form.tableWidget.horizontalHeader().setSectionResizeMode(2,
                                                                                     QtWidgets.QHeaderView.ResizeToContents)
                            form.tableWidget.horizontalHeader().setSectionResizeMode(3,
                                                                                     QtWidgets.QHeaderView.Stretch)
                            form.tableWidget.horizontalHeader().setSectionResizeMode(4,
                                                                                     QtWidgets.QHeaderView.ResizeToContents)
                            form.tableWidget.horizontalHeader().setSectionResizeMode(5,
                                                                                     QtWidgets.QHeaderView.ResizeToContents)
                    form.lineEdit.setText(str(iter))
                    hour = cursor.execute(
                        f"""SELECT SUM(hours) FROM TO6 WHERE loko='{iter}'""")
                    intel = hour.fetchall()
                    rom = int()
                    for number, lul in enumerate(intel):
                        try:
                            a = int(intel[number][0])
                            rom += a
                        except:
                            pass
                    form.lineEdit_2.setText(str(rom))
                    app.exec()
                if it.column() == 4:
                    fuck = QtWidgets.QMenu(self)
                    fuck.setGeometry(QtCore.QRect(20, 20, 20, 20))
                    sqlite_connection = sqlite3.connect("id.db")
                    cursor = sqlite_connection.cursor()
                    users = cursor.execute("""SELECT fio FROM masters""")
                    pickle = users.fetchall()
                    add = []
                    for number, lul in enumerate(pickle):
                        a = fuck.addAction(str(pickle[number][0]))
                        add.append(a)
                    action = fuck.exec_(self.mapToGlobal(e.pos()))
                    for number, lul in enumerate(pickle):
                        if action == add[number]:
                            it.setText(str(pickle[number][0]))
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
                        sqlite_connection = sqlite3.connect("id.db")
                        cursor = sqlite_connection.cursor()
                        iter = it.text()
                        cursor.execute(f"""DELETE FROM TO7 WHERE ID='{iter}'""")
                        sqlite_connection.commit()
                        it.tableWidget().setRowCount(0)
                        users = cursor.execute("SELECT * FROM TO7")
                        for row_number6, order in enumerate(users):
                            rama.insertRow(row_number6)
                            for column_number, data in enumerate(order):
                                cell = QtWidgets.QTableWidgetItem(str(data))
                                rama.setItem(row_number6, column_number, cell)
                                cell.setTextAlignment(Qt.AlignCenter)
                if it.column() == 7:
                    fuck = QtWidgets.QMenu(self)
                    fuck.setGeometry(QtCore.QRect(20, 20, 20, 20))
                    today = date.today()
                    lol = fuck.addAction(today.strftime("%d.%m.%Y"))
                    action = fuck.exec_(self.mapToGlobal(e.pos()))
                    if action == lol:
                        it.setText(today.strftime("%d.%m.%Y"))
                if it.column() == 2:
                    fuck = QtWidgets.QMenu(self)
                    fuck.setGeometry(QtCore.QRect(20, 20, 20, 20))
                    TO1 = fuck.addAction("План")
                    TO2 = fuck.addAction("Внеплан")
                    TO3 = fuck.addAction("Ремонт")
                    action = fuck.exec_(self.mapToGlobal(e.pos()))
                    if action == TO1:
                        it.setText("План")
                    if action == TO2:
                        it.setText("Внеплан")
                    if action == TO3:
                        it.setText("Ремонт")
                if it.column() == 3:
                    fuck = QtWidgets.QMenu(self)
                    fuck.setGeometry(QtCore.QRect(20, 20, 20, 20))
                    pl = fuck.addAction("+")
                    min = fuck.addAction("-")
                    action = fuck.exec_(self.mapToGlobal(e.pos()))
                    if action == pl:
                        it.setText("+")
                    if action == min:
                        it.setText("-")
                if it.column() == 1:
                    iter = it.text()
                    Form, App = uic.loadUiType("loko.ui")
                    app = QtWidgets.QDialog()
                    form = Form()
                    form.setupUi(app)
                    app.show()
                    sqlite_connection = sqlite3.connect("id.db")
                    cursor = sqlite_connection.cursor()
                    users = cursor.execute(
                        f"""SELECT ID,repair,master,userid,hours,datas FROM TO7 WHERE loko='{iter}' ORDER BY datas DESC LIMIT 6""")
                    for row_number6, order in enumerate(users):
                        form.tableWidget.insertRow(row_number6)
                        for column_number, data in enumerate(order):
                            cell = QtWidgets.QTableWidgetItem(str(data))
                            form.tableWidget.setItem(row_number6, column_number, cell)
                            cell.setTextAlignment(Qt.AlignCenter)
                            form.tableWidget.horizontalHeader().setSectionResizeMode(0,
                                                                                     QtWidgets.QHeaderView.ResizeToContents)
                            form.tableWidget.horizontalHeader().setSectionResizeMode(1,
                                                                                     QtWidgets.QHeaderView.ResizeToContents)
                            form.tableWidget.horizontalHeader().setSectionResizeMode(2,
                                                                                     QtWidgets.QHeaderView.ResizeToContents)
                            form.tableWidget.horizontalHeader().setSectionResizeMode(3,
                                                                                     QtWidgets.QHeaderView.Stretch)
                            form.tableWidget.horizontalHeader().setSectionResizeMode(4,
                                                                                     QtWidgets.QHeaderView.ResizeToContents)
                            form.tableWidget.horizontalHeader().setSectionResizeMode(5,
                                                                                     QtWidgets.QHeaderView.ResizeToContents)
                    form.lineEdit.setText(str(iter))
                    hour = cursor.execute(
                        f"""SELECT SUM(hours) FROM TO7 WHERE loko='{iter}'""")
                    intel = hour.fetchall()
                    rom = int()
                    for number, lul in enumerate(intel):
                        try:
                            a = int(intel[number][0])
                            rom += a
                        except:
                            pass
                    form.lineEdit_2.setText(str(rom))
                    app.exec()
                if it.column() == 4:
                    fuck = QtWidgets.QMenu(self)
                    fuck.setGeometry(QtCore.QRect(20, 20, 20, 20))
                    sqlite_connection = sqlite3.connect("id.db")
                    cursor = sqlite_connection.cursor()
                    users = cursor.execute("""SELECT fio FROM masters""")
                    pickle = users.fetchall()
                    add = []
                    for number, lul in enumerate(pickle):
                        a = fuck.addAction(str(pickle[number][0]))
                        add.append(a)
                    action = fuck.exec_(self.mapToGlobal(e.pos()))
                    for number, lul in enumerate(pickle):
                        if action == add[number]:
                            it.setText(str(pickle[number][0]))
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
                        sqlite_connection = sqlite3.connect("id.db")
                        cursor = sqlite_connection.cursor()
                        iter = it.text()
                        cursor.execute(f"""DELETE FROM TO8 WHERE ID='{iter}'""")
                        sqlite_connection.commit()
                        it.tableWidget().setRowCount(0)
                        users = cursor.execute("SELECT * FROM TO8")
                        for row_number7, order in enumerate(users):
                            rama.insertRow(row_number7)
                            for column_number, data in enumerate(order):
                                cell = QtWidgets.QTableWidgetItem(str(data))
                                rama.setItem(row_number7, column_number, cell)
                                cell.setTextAlignment(Qt.AlignCenter)
                if it.column() == 7:
                    fuck = QtWidgets.QMenu(self)
                    fuck.setGeometry(QtCore.QRect(20, 20, 20, 20))
                    today = date.today()
                    lol = fuck.addAction(today.strftime("%d.%m.%Y"))
                    action = fuck.exec_(self.mapToGlobal(e.pos()))
                    if action == lol:
                        it.setText(today.strftime("%d.%m.%Y"))
                if it.column() == 2:
                    fuck = QtWidgets.QMenu(self)
                    fuck.setGeometry(QtCore.QRect(20, 20, 20, 20))
                    TO1 = fuck.addAction("План")
                    TO2 = fuck.addAction("Внеплан")
                    TO3 = fuck.addAction("Ремонт")
                    action = fuck.exec_(self.mapToGlobal(e.pos()))
                    if action == TO1:
                        it.setText("План")
                    if action == TO2:
                        it.setText("Внеплан")
                    if action == TO3:
                        it.setText("Ремонт")
                if it.column() == 3:
                    fuck = QtWidgets.QMenu(self)
                    fuck.setGeometry(QtCore.QRect(20, 20, 20, 20))
                    pl = fuck.addAction("+")
                    min = fuck.addAction("-")
                    action = fuck.exec_(self.mapToGlobal(e.pos()))
                    if action == pl:
                        it.setText("+")
                    if action == min:
                        it.setText("-")
                if it.column() == 1:
                    iter = it.text()
                    Form, App = uic.loadUiType("loko.ui")
                    app = QtWidgets.QDialog()
                    form = Form()
                    form.setupUi(app)
                    app.show()
                    sqlite_connection = sqlite3.connect("id.db")
                    cursor = sqlite_connection.cursor()
                    users = cursor.execute(
                        f"""SELECT ID,repair,master,userid,hours,datas FROM TO8 WHERE loko='{iter}' ORDER BY datas DESC LIMIT 6""")
                    for row_number7, order in enumerate(users):
                        form.tableWidget.insertRow(row_number7)
                        for column_number, data in enumerate(order):
                            cell = QtWidgets.QTableWidgetItem(str(data))
                            form.tableWidget.setItem(row_number7, column_number, cell)
                            cell.setTextAlignment(Qt.AlignCenter)
                            form.tableWidget.horizontalHeader().setSectionResizeMode(0,
                                                                                     QtWidgets.QHeaderView.ResizeToContents)
                            form.tableWidget.horizontalHeader().setSectionResizeMode(1,
                                                                                     QtWidgets.QHeaderView.ResizeToContents)
                            form.tableWidget.horizontalHeader().setSectionResizeMode(2,
                                                                                     QtWidgets.QHeaderView.ResizeToContents)
                            form.tableWidget.horizontalHeader().setSectionResizeMode(3,
                                                                                     QtWidgets.QHeaderView.Stretch)
                            form.tableWidget.horizontalHeader().setSectionResizeMode(4,
                                                                                     QtWidgets.QHeaderView.ResizeToContents)
                            form.tableWidget.horizontalHeader().setSectionResizeMode(5,
                                                                                     QtWidgets.QHeaderView.ResizeToContents)
                    form.lineEdit.setText(str(iter))
                    hour = cursor.execute(
                        f"""SELECT SUM(hours) FROM TO8 WHERE loko='{iter}'""")
                    intel = hour.fetchall()
                    rom = int()
                    for number, lul in enumerate(intel):
                        try:
                            a = int(intel[number][0])
                            rom += a
                        except:
                            pass
                    form.lineEdit_2.setText(str(rom))
                    app.exec()
                if it.column() == 4:
                    fuck = QtWidgets.QMenu(self)
                    fuck.setGeometry(QtCore.QRect(20, 20, 20, 20))
                    sqlite_connection = sqlite3.connect("id.db")
                    cursor = sqlite_connection.cursor()
                    users = cursor.execute("""SELECT fio FROM masters""")
                    pickle = users.fetchall()
                    add = []
                    for number, lul in enumerate(pickle):
                        a = fuck.addAction(str(pickle[number][0]))
                        add.append(a)
                    action = fuck.exec_(self.mapToGlobal(e.pos()))
                    for number, lul in enumerate(pickle):
                        if action == add[number]:
                            it.setText(str(pickle[number][0]))
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
                        cursor.execute(f"""DELETE FROM orders WHERE ID='{iter}'""")
                        sqlite_connection.commit()
                        it.tableWidget().setRowCount(0)
                        users = cursor.execute("SELECT * FROM orders")
                        for row_number8, order in enumerate(users):
                            rama.insertRow(row_number8)
                            for column_number, data in enumerate(order):
                                cell = QtWidgets.QTableWidgetItem(str(data))
                                rama.setItem(row_number8, column_number, cell)
                                cell.setTextAlignment(Qt.AlignCenter)
                if it.column() == 1:
                    fuck = QtWidgets.QMenu(self)
                    fuck.setGeometry(QtCore.QRect(20, 20, 20, 20))
                    pow = fuck.addAction("Добавить несколько деталей")
                    low = fuck.addAction("Убрать несколько деталей")
                    detal = fuck.addAction("О детали")
                    action = fuck.exec_(self.mapToGlobal(e.pos()))
                    if action == pow:
                        Form, App = uic.loadUiType("plus.ui")
                        app = QDialog()
                        form = Form()
                        form.setupUi(app)
                        app.show()

                        def like():
                            let = form.lineEdit.text()
                            iter = it.text()
                            sqlite_connection = sqlite3.connect("id.db")
                            cursor = sqlite_connection.cursor()
                            cursor.execute(f"""UPDATE orders SET kol=(kol +'{let}') WHERE orderid='{iter}'""")
                            sqlite_connection.commit()
                            cursor.execute(f"""UPDATE orders SET userid=(SELECT (kol))""")
                            pup = cursor.execute("""SELECT userid FROM TO1""")
                            nice = pup.fetchall()
                            fuxx = []
                            loop = []
                            for number, lul in enumerate(nice):
                                a = str(nice[number][0])
                                fuxx.append(a)
                            for numbers, lul in enumerate((",".join(fuxx)).split(",")):
                                loops = (",".join(fuxx)).split(",")[numbers]
                                loop.append(loops)
                                fux = loop[numbers]
                                cursor.execute(
                                    f"""UPDATE orders SET userid=(SELECT (userid - COUNT('{fux}')) WHERE '{fux}'=orderid)""")
                            pup = cursor.execute("""SELECT userid FROM TO2""")
                            nice = pup.fetchall()
                            fuxx = []
                            loop = []
                            for number, lul in enumerate(nice):
                                a = str(nice[number][0])
                                fuxx.append(a)
                            for numbers, lul in enumerate((",".join(fuxx)).split(",")):
                                loops = (",".join(fuxx)).split(",")[numbers]
                                loop.append(loops)
                                fux = loop[numbers]
                                cursor.execute(
                                    f"""UPDATE orders SET userid=(SELECT (userid - COUNT('{fux}')) WHERE '{fux}'=orderid)""")
                            pup = cursor.execute("""SELECT userid FROM TO3""")
                            nice = pup.fetchall()
                            fuxx = []
                            loop = []
                            for number, lul in enumerate(nice):
                                a = str(nice[number][0])
                                fuxx.append(a)
                            for numbers, lul in enumerate((",".join(fuxx)).split(",")):
                                loops = (",".join(fuxx)).split(",")[numbers]
                                loop.append(loops)
                                fux = loop[numbers]
                                cursor.execute(
                                    f"""UPDATE orders SET userid=(SELECT (userid - COUNT('{fux}')) WHERE '{fux}'=orderid)""")
                            pup = cursor.execute("""SELECT userid FROM TO4""")
                            nice = pup.fetchall()
                            fuxx = []
                            loop = []
                            for number, lul in enumerate(nice):
                                a = str(nice[number][0])
                                fuxx.append(a)
                            for numbers, lul in enumerate((",".join(fuxx)).split(",")):
                                loops = (",".join(fuxx)).split(",")[numbers]
                                loop.append(loops)
                                fux = loop[numbers]
                                cursor.execute(
                                    f"""UPDATE orders SET userid=(SELECT (userid - COUNT('{fux}')) WHERE '{fux}'=orderid)""")
                            pup = cursor.execute("""SELECT userid FROM TO5""")
                            nice = pup.fetchall()
                            fuxx = []
                            loop = []
                            for number, lul in enumerate(nice):
                                a = str(nice[number][0])
                                fuxx.append(a)
                            for numbers, lul in enumerate((",".join(fuxx)).split(",")):
                                loops = (",".join(fuxx)).split(",")[numbers]
                                loop.append(loops)
                                fux = loop[numbers]
                                cursor.execute(
                                    f"""UPDATE orders SET userid=(SELECT (userid - COUNT('{fux}')) WHERE '{fux}'=orderid)""")
                            pup = cursor.execute("""SELECT userid FROM TO6""")
                            nice = pup.fetchall()
                            fuxx = []
                            loop = []
                            for number, lul in enumerate(nice):
                                a = str(nice[number][0])
                                fuxx.append(a)
                            for numbers, lul in enumerate((",".join(fuxx)).split(",")):
                                loops = (",".join(fuxx)).split(",")[numbers]
                                loop.append(loops)
                                fux = loop[numbers]
                                cursor.execute(
                                    f"""UPDATE orders SET userid=(SELECT (userid - COUNT('{fux}')) WHERE '{fux}'=orderid)""")
                            pup = cursor.execute("""SELECT userid FROM TO7""")
                            nice = pup.fetchall()
                            fuxx = []
                            loop = []
                            for number, lul in enumerate(nice):
                                a = str(nice[number][0])
                                fuxx.append(a)
                            for numbers, lul in enumerate((",".join(fuxx)).split(",")):
                                loops = (",".join(fuxx)).split(",")[numbers]
                                loop.append(loops)
                                fux = loop[numbers]
                                cursor.execute(
                                    f"""UPDATE orders SET userid=(SELECT (userid - COUNT('{fux}')) WHERE '{fux}'=orderid)""")
                            pup = cursor.execute("""SELECT userid FROM TO8""")
                            nice = pup.fetchall()
                            fuxx = []
                            loop = []
                            for number, lul in enumerate(nice):
                                a = str(nice[number][0])
                                fuxx.append(a)
                            for numbers, lul in enumerate((",".join(fuxx)).split(",")):
                                loops = (",".join(fuxx)).split(",")[numbers]
                                loop.append(loops)
                                fux = loop[numbers]
                                cursor.execute(
                                    f"""UPDATE orders SET userid=(SELECT (userid - COUNT('{fux}')) WHERE '{fux}'=orderid)""")
                            sqlite_connection.commit()
                            rama = it.tableWidget()
                            it.tableWidget().setRowCount(0)
                            users = cursor.execute("SELECT * FROM orders")
                            for row_number, order in enumerate(users):
                                rama.insertRow(row_number)
                                for column_number, data in enumerate(order):
                                    cell = QtWidgets.QTableWidgetItem(str(data))
                                    rama.setItem(row_number, column_number, cell)
                                    cell.setTextAlignment(Qt.AlignCenter)
                            app.close()

                        def end():
                            app.close()

                        form.pushButton.clicked.connect(like)
                        form.pushButton_2.clicked.connect(end)
                        app.exec()
                    if action == low:
                        Form, App = uic.loadUiType("minus.ui")
                        app = QDialog()
                        form = Form()
                        form.setupUi(app)
                        app.show()

                        def like():
                            let = form.lineEdit.text()
                            iter = it.text()
                            sqlite_connection = sqlite3.connect("id.db")
                            cursor = sqlite_connection.cursor()
                            cursor.execute(f"""UPDATE orders SET kol=(kol -'{let}') WHERE orderid='{iter}'""")
                            sqlite_connection.commit()
                            cursor.execute(f"""UPDATE orders SET userid=(SELECT (kol))""")
                            pup = cursor.execute("""SELECT userid FROM TO1""")
                            nice = pup.fetchall()
                            fuxx = []
                            loop = []
                            for number, lul in enumerate(nice):
                                a = str(nice[number][0])
                                fuxx.append(a)
                            for numbers, lul in enumerate((",".join(fuxx)).split(",")):
                                loops = (",".join(fuxx)).split(",")[numbers]
                                loop.append(loops)
                                fux = loop[numbers]
                                cursor.execute(
                                    f"""UPDATE orders SET userid=(SELECT (userid - COUNT('{fux}')) WHERE '{fux}'=orderid)""")
                            pup = cursor.execute("""SELECT userid FROM TO2""")
                            nice = pup.fetchall()
                            fuxx = []
                            loop = []
                            for number, lul in enumerate(nice):
                                a = str(nice[number][0])
                                fuxx.append(a)
                            for numbers, lul in enumerate((",".join(fuxx)).split(",")):
                                loops = (",".join(fuxx)).split(",")[numbers]
                                loop.append(loops)
                                fux = loop[numbers]
                                cursor.execute(
                                    f"""UPDATE orders SET userid=(SELECT (userid - COUNT('{fux}')) WHERE '{fux}'=orderid)""")
                            pup = cursor.execute("""SELECT userid FROM TO3""")
                            nice = pup.fetchall()
                            fuxx = []
                            loop = []
                            for number, lul in enumerate(nice):
                                a = str(nice[number][0])
                                fuxx.append(a)
                            for numbers, lul in enumerate((",".join(fuxx)).split(",")):
                                loops = (",".join(fuxx)).split(",")[numbers]
                                loop.append(loops)
                                fux = loop[numbers]
                                cursor.execute(
                                    f"""UPDATE orders SET userid=(SELECT (userid - COUNT('{fux}')) WHERE '{fux}'=orderid)""")
                            pup = cursor.execute("""SELECT userid FROM TO4""")
                            nice = pup.fetchall()
                            fuxx = []
                            loop = []
                            for number, lul in enumerate(nice):
                                a = str(nice[number][0])
                                fuxx.append(a)
                            for numbers, lul in enumerate((",".join(fuxx)).split(",")):
                                loops = (",".join(fuxx)).split(",")[numbers]
                                loop.append(loops)
                                fux = loop[numbers]
                                cursor.execute(
                                    f"""UPDATE orders SET userid=(SELECT (userid - COUNT('{fux}')) WHERE '{fux}'=orderid)""")
                            pup = cursor.execute("""SELECT userid FROM TO5""")
                            nice = pup.fetchall()
                            fuxx = []
                            loop = []
                            for number, lul in enumerate(nice):
                                a = str(nice[number][0])
                                fuxx.append(a)
                            for numbers, lul in enumerate((",".join(fuxx)).split(",")):
                                loops = (",".join(fuxx)).split(",")[numbers]
                                loop.append(loops)
                                fux = loop[numbers]
                                cursor.execute(
                                    f"""UPDATE orders SET userid=(SELECT (userid - COUNT('{fux}')) WHERE '{fux}'=orderid)""")
                            pup = cursor.execute("""SELECT userid FROM TO6""")
                            nice = pup.fetchall()
                            fuxx = []
                            loop = []
                            for number, lul in enumerate(nice):
                                a = str(nice[number][0])
                                fuxx.append(a)
                            for numbers, lul in enumerate((",".join(fuxx)).split(",")):
                                loops = (",".join(fuxx)).split(",")[numbers]
                                loop.append(loops)
                                fux = loop[numbers]
                                cursor.execute(
                                    f"""UPDATE orders SET userid=(SELECT (userid - COUNT('{fux}')) WHERE '{fux}'=orderid)""")
                            pup = cursor.execute("""SELECT userid FROM TO7""")
                            nice = pup.fetchall()
                            fuxx = []
                            loop = []
                            for number, lul in enumerate(nice):
                                a = str(nice[number][0])
                                fuxx.append(a)
                            for numbers, lul in enumerate((",".join(fuxx)).split(",")):
                                loops = (",".join(fuxx)).split(",")[numbers]
                                loop.append(loops)
                                fux = loop[numbers]
                                cursor.execute(
                                    f"""UPDATE orders SET userid=(SELECT (userid - COUNT('{fux}')) WHERE '{fux}'=orderid)""")
                            pup = cursor.execute("""SELECT userid FROM TO8""")
                            nice = pup.fetchall()
                            fuxx = []
                            loop = []
                            for number, lul in enumerate(nice):
                                a = str(nice[number][0])
                                fuxx.append(a)
                            for numbers, lul in enumerate((",".join(fuxx)).split(",")):
                                loops = (",".join(fuxx)).split(",")[numbers]
                                loop.append(loops)
                                fux = loop[numbers]
                                cursor.execute(
                                    f"""UPDATE orders SET userid=(SELECT (userid - COUNT('{fux}')) WHERE '{fux}'=orderid)""")
                            sqlite_connection.commit()
                            rama = it.tableWidget()
                            it.tableWidget().setRowCount(0)
                            users = cursor.execute("SELECT * FROM orders")
                            for row_number, order in enumerate(users):
                                rama.insertRow(row_number)
                                for column_number, data in enumerate(order):
                                    cell = QtWidgets.QTableWidgetItem(str(data))
                                    rama.setItem(row_number, column_number, cell)
                                    cell.setTextAlignment(Qt.AlignCenter)
                            app.close()

                        def end():
                            app.close()

                        form.pushButton.clicked.connect(like)
                        form.pushButton_2.clicked.connect(end)
                        app.exec()
                    if action == detal:
                        if it.column() == 1:
                            iter = it.text()
                            Form, App = uic.loadUiType("detali.ui")
                            app = QtWidgets.QDialog()
                            form = Form()
                            form.setupUi(app)
                            app.show()
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
                            n = 0
                            lot = 0
                            for row in enumerate(pow):
                                lot += 1
                            while n != lot:
                                i = 0
                                try:
                                    pux = pow[n][3].split(",")
                                except:
                                    pux = pow[n][3]
                                n += 1
                                try:
                                    for r in range(len(pux)):
                                        trying = pux[r]
                                        if iter in trying:
                                            i += 1
                                    like.append(i)
                                except:
                                    i = 1
                                    like.append(i)
                            cursor.execute("""DELETE FROM poll WHERE ID > -1""")
                            sqlite_connection.commit()
                            for r in range(n):
                                cursor.execute("""INSERT INTO poll VALUES (NULL,'','','','')""")
                            sqlite_connection.commit()
                            for r in range(n):
                                cursor.execute(
                                    f"""UPDATE poll SET one='{str(pow[r][0])}',two='{str(pow[r][1])}',three='{str(pow[r][2])}',foo='{str(like[r])}' WHERE ID='{r + 1}'""")
                            sqlite_connection.commit()

                            def all():
                                form.tableWidget.setRowCount(0)
                                users00 = cursor.execute(
                                    f"""SELECT one,two,three,foo FROM poll ORDER BY one DESC""")
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

                            def plan():
                                form.tableWidget.setRowCount(0)
                                users00 = cursor.execute(
                                    f"""SELECT one,two,three,foo FROM poll WHERE three='План' ORDER BY one DESC""")
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

                            def vneplan():
                                form.tableWidget.setRowCount(0)
                                users00 = cursor.execute(
                                    f"""SELECT one,two,three,foo FROM poll WHERE three='Внеплан' ORDER BY one DESC""")
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

                            def repair():
                                form.tableWidget.setRowCount(0)
                                users00 = cursor.execute(
                                    f"""SELECT one,two,three,foo FROM poll WHERE three='Ремонт' ORDER BY one DESC""")
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
            QtWidgets.QTableWidget.mousePressEvent(self, e)
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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
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
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\User\\PycharmProjects\\SQL_Maket\\train.ico"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
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
        self.pushButton_40.setCheckable(True)
        self.pushButton_40.setChecked(True)
        self.pushButton_40.setObjectName("pushButton_40")
        self.tableWidget_10 = Test(self.tab_13)
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
        self.tableWidget_10.setColumnCount(8)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_10.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_10.setHorizontalHeaderItem(7, item)
        self.tableWidget_10.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)  # МОД
        self.tableWidget_10.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_10.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_10.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_10.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_10.horizontalHeader().setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_10.horizontalHeader().setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_10.horizontalHeader().setSectionResizeMode(7, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_10.horizontalHeader().setHighlightSections(False)
        self.tableWidget_10.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_10.verticalHeader().setVisible(False)
        self.pushButton_41 = QtWidgets.QPushButton(self.tab_13)
        self.pushButton_41.setGeometry(QtCore.QRect(1343, 520, 71, 41))
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
        self.label_10.setGeometry(QtCore.QRect(1210, 170, 241, 20))
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
        self.pushButton_save_3.setCheckable(True)
        self.pushButton_save_3.setChecked(True)
        self.pushButton_save_3.setAutoDefault(False)
        self.pushButton_save_3.setDefault(False)
        self.pushButton_save_3.setFlat(False)
        self.pushButton_save_3.setObjectName("pushButton_save_3")
        self.label_52 = QtWidgets.QLabel(self.tab_13)
        self.label_52.setGeometry(QtCore.QRect(-20, 41, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(39)
        font.setBold(True)
        font.setWeight(75)
        self.label_52.setFont(font)
        self.label_52.setStyleSheet("color: rgb(50, 50, 50);")
        self.label_52.setTextFormat(QtCore.Qt.AutoText)
        self.label_52.setObjectName("label_52")
        self.label_53 = QtWidgets.QLabel(self.tab_13)
        self.label_53.setGeometry(QtCore.QRect(-20, 600, 91, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label_53.setFont(font)
        self.label_53.setStyleSheet("color: rgb(50, 50, 50);")
        self.label_53.setObjectName("label_53")
        self.label_30 = QtWidgets.QLabel(self.tab_13)
        self.label_30.setGeometry(QtCore.QRect(1310, 38, 51, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("color: rgb(50, 50, 50);")
        self.label_30.setObjectName("label_30")
        self.label_37 = QtWidgets.QLabel(self.tab_13)
        self.label_37.setGeometry(QtCore.QRect(1310, 598, 51, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label_37.setFont(font)
        self.label_37.setStyleSheet("color: rgb(50, 50, 50);")
        self.label_37.setObjectName("label_37")
        self.pushButton_42 = QtWidgets.QPushButton(self.tab_13)
        self.pushButton_42.setGeometry(QtCore.QRect(1343, 570, 71, 41))
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
        self.label_52.raise_()
        self.label_53.raise_()
        self.label_30.raise_()
        self.pushButton_41.raise_()
        self.label_37.raise_()
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
        self.pushButton_49.setCheckable(True)
        self.pushButton_49.setChecked(True)
        self.pushButton_49.setObjectName("pushButton_49")
        self.label_11 = QtWidgets.QLabel(self.tab_14)
        self.label_11.setGeometry(QtCore.QRect(1120, 30, 241, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("QLabel {\n"
                                    "    color: rgb(255, 255, 255);}")
        self.label_11.setObjectName("label_11")
        self.pushButton_55 = QtWidgets.QPushButton(self.tab_14)
        self.pushButton_55.setGeometry(QtCore.QRect(1343, 520, 71, 41))
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
        self.pushButton_56.setGeometry(QtCore.QRect(1343, 570, 71, 41))
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
        self.tableWidget_11 = Test1(self.tab_14)
        self.tableWidget_11.setGeometry(QtCore.QRect(20, 70, 1311, 551))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget_11.setFont(font)
        self.tableWidget_11.setStyleSheet("QTableWidget {\n"
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
        self.tableWidget_11.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget_11.setObjectName("tableWidget_11")
        self.tableWidget_11.setColumnCount(8)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_11.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_11.setHorizontalHeaderItem(7, item)
        self.tableWidget_11.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)  # МОД
        self.tableWidget_11.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_11.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_11.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_11.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_11.horizontalHeader().setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_11.horizontalHeader().setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_11.horizontalHeader().setSectionResizeMode(7, QtWidgets.QHeaderView.ResizeToContents)
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
        self.pushButton_save_4.setCheckable(True)
        self.pushButton_save_4.setChecked(True)
        self.pushButton_save_4.setAutoDefault(False)
        self.pushButton_save_4.setDefault(False)
        self.pushButton_save_4.setFlat(False)
        self.pushButton_save_4.setObjectName("pushButton_save_4")
        self.label_8 = QtWidgets.QLabel(self.tab_14)
        self.label_8.setGeometry(QtCore.QRect(1310, 38, 51, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(50, 50, 50);")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab_14)
        self.label_9.setGeometry(QtCore.QRect(-20, 600, 91, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(50, 50, 50);")
        self.label_9.setObjectName("label_9")
        self.label_18 = QtWidgets.QLabel(self.tab_14)
        self.label_18.setGeometry(QtCore.QRect(1310, 598, 51, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color: rgb(50, 50, 50);")
        self.label_18.setObjectName("label_18")
        self.label_7 = QtWidgets.QLabel(self.tab_14)
        self.label_7.setGeometry(QtCore.QRect(-20, 41, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(39)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(50, 50, 50);")
        self.label_7.setTextFormat(QtCore.Qt.AutoText)
        self.label_7.setObjectName("label_7")
        self.frame_3.raise_()
        self.lineEdit_11.raise_()
        self.pushButton_43.raise_()
        self.pushButton_49.raise_()
        self.label_11.raise_()
        self.pushButton_55.raise_()
        self.tableWidget_11.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_18.raise_()
        self.label_7.raise_()
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
        self.pushButton_50.setCheckable(True)
        self.pushButton_50.setChecked(True)
        self.pushButton_50.setObjectName("pushButton_50")
        self.label_12 = QtWidgets.QLabel(self.tab_15)
        self.label_12.setGeometry(QtCore.QRect(1120, 30, 241, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("QLabel {\n"
                                    "    color: rgb(255, 255, 255);}")
        self.label_12.setObjectName("label_12")
        self.pushButton_57 = QtWidgets.QPushButton(self.tab_15)
        self.pushButton_57.setGeometry(QtCore.QRect(1343, 520, 71, 41))
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
        self.pushButton_58.setGeometry(QtCore.QRect(1343, 570, 71, 41))
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
        self.tableWidget_12 = Test2(self.tab_15)
        self.tableWidget_12.setGeometry(QtCore.QRect(20, 70, 1311, 551))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget_12.setFont(font)
        self.tableWidget_12.setStyleSheet("QTableWidget {\n"
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
        self.tableWidget_12.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget_12.setObjectName("tableWidget_12")
        self.tableWidget_12.setColumnCount(8)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_12.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_12.setHorizontalHeaderItem(7, item)
        self.tableWidget_12.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)  # МОД
        self.tableWidget_12.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_12.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_12.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_12.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_12.horizontalHeader().setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_12.horizontalHeader().setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_12.horizontalHeader().setSectionResizeMode(7, QtWidgets.QHeaderView.ResizeToContents)
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
        self.pushButton_save_5.setCheckable(True)
        self.pushButton_save_5.setChecked(True)
        self.pushButton_save_5.setAutoDefault(False)
        self.pushButton_save_5.setDefault(False)
        self.pushButton_save_5.setFlat(False)
        self.pushButton_save_5.setObjectName("pushButton_save_5")
        self.label_54 = QtWidgets.QLabel(self.tab_15)
        self.label_54.setGeometry(QtCore.QRect(-20, 600, 91, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label_54.setFont(font)
        self.label_54.setStyleSheet("color: rgb(50, 50, 50);")
        self.label_54.setObjectName("label_54")
        self.label_24 = QtWidgets.QLabel(self.tab_15)
        self.label_24.setGeometry(QtCore.QRect(-20, 41, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(39)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("color: rgb(50, 50, 50);")
        self.label_24.setTextFormat(QtCore.Qt.AutoText)
        self.label_24.setObjectName("label_24")
        self.label_31 = QtWidgets.QLabel(self.tab_15)
        self.label_31.setGeometry(QtCore.QRect(1310, 38, 51, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet("color: rgb(50, 50, 50);")
        self.label_31.setObjectName("label_31")
        self.label_38 = QtWidgets.QLabel(self.tab_15)
        self.label_38.setGeometry(QtCore.QRect(1310, 598, 51, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label_38.setFont(font)
        self.label_38.setStyleSheet("color: rgb(50, 50, 50);")
        self.label_38.setObjectName("label_38")
        self.frame_16.raise_()
        self.lineEdit_12.raise_()
        self.pushButton_44.raise_()
        self.pushButton_50.raise_()
        self.label_12.raise_()
        self.pushButton_57.raise_()
        self.tableWidget_12.raise_()
        self.label_54.raise_()
        self.label_24.raise_()
        self.label_31.raise_()
        self.label_38.raise_()
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
        self.pushButton_51.setCheckable(True)
        self.pushButton_51.setChecked(True)
        self.pushButton_51.setObjectName("pushButton_51")
        self.label_13 = QtWidgets.QLabel(self.tab_16)
        self.label_13.setGeometry(QtCore.QRect(1120, 30, 241, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("QLabel {\n"
                                    "    color: rgb(255, 255, 255);}")
        self.label_13.setObjectName("label_13")
        self.pushButton_59 = QtWidgets.QPushButton(self.tab_16)
        self.pushButton_59.setGeometry(QtCore.QRect(1343, 520, 71, 41))
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
        self.pushButton_60.setGeometry(QtCore.QRect(1343, 570, 71, 41))
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
        self.tableWidget_13 = Test3(self.tab_16)
        self.tableWidget_13.setGeometry(QtCore.QRect(20, 70, 1311, 551))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget_13.setFont(font)
        self.tableWidget_13.setStyleSheet("QTableWidget {\n"
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
        self.tableWidget_13.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget_13.setObjectName("tableWidget_13")
        self.tableWidget_13.setColumnCount(8)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_13.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_13.setHorizontalHeaderItem(7, item)
        self.tableWidget_13.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)  # МОД
        self.tableWidget_13.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_13.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_13.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_13.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_13.horizontalHeader().setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_13.horizontalHeader().setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_13.horizontalHeader().setSectionResizeMode(7, QtWidgets.QHeaderView.ResizeToContents)
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
        self.pushButton_save_6.setCheckable(True)
        self.pushButton_save_6.setChecked(True)
        self.pushButton_save_6.setAutoDefault(False)
        self.pushButton_save_6.setDefault(False)
        self.pushButton_save_6.setFlat(False)
        self.pushButton_save_6.setObjectName("pushButton_save_6")
        self.label_19 = QtWidgets.QLabel(self.tab_16)
        self.label_19.setGeometry(QtCore.QRect(-20, 600, 91, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color: rgb(50, 50, 50);")
        self.label_19.setObjectName("label_19")
        self.label_25 = QtWidgets.QLabel(self.tab_16)
        self.label_25.setGeometry(QtCore.QRect(-20, 41, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(39)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("color: rgb(50, 50, 50);")
        self.label_25.setTextFormat(QtCore.Qt.AutoText)
        self.label_25.setObjectName("label_25")
        self.label_32 = QtWidgets.QLabel(self.tab_16)
        self.label_32.setGeometry(QtCore.QRect(1310, 38, 51, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label_32.setFont(font)
        self.label_32.setStyleSheet("color: rgb(50, 50, 50);")
        self.label_32.setObjectName("label_32")
        self.label_39 = QtWidgets.QLabel(self.tab_16)
        self.label_39.setGeometry(QtCore.QRect(1310, 598, 51, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label_39.setFont(font)
        self.label_39.setStyleSheet("color: rgb(50, 50, 50);")
        self.label_39.setObjectName("label_39")
        self.frame_18.raise_()
        self.lineEdit_13.raise_()
        self.pushButton_45.raise_()
        self.pushButton_51.raise_()
        self.label_13.raise_()
        self.pushButton_59.raise_()
        self.tableWidget_13.raise_()
        self.label_19.raise_()
        self.label_25.raise_()
        self.label_32.raise_()
        self.label_39.raise_()
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
        self.pushButton_52.setCheckable(True)
        self.pushButton_52.setChecked(True)
        self.pushButton_52.setObjectName("pushButton_52")
        self.label_14 = QtWidgets.QLabel(self.tab_17)
        self.label_14.setGeometry(QtCore.QRect(1120, 30, 241, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("QLabel {\n"
                                    "    color: rgb(255, 255, 255);}")
        self.label_14.setObjectName("label_14")
        self.pushButton_61 = QtWidgets.QPushButton(self.tab_17)
        self.pushButton_61.setGeometry(QtCore.QRect(1343, 520, 71, 41))
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
        self.pushButton_62.setGeometry(QtCore.QRect(1343, 570, 71, 41))
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
        self.tableWidget_14 = Test4(self.tab_17)
        self.tableWidget_14.setGeometry(QtCore.QRect(20, 70, 1311, 551))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget_14.setFont(font)
        self.tableWidget_14.setStyleSheet("QTableWidget {\n"
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
        self.tableWidget_14.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget_14.setObjectName("tableWidget_14")
        self.tableWidget_14.setColumnCount(8)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_14.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_14.setHorizontalHeaderItem(7, item)
        self.tableWidget_14.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)  # МОД
        self.tableWidget_14.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_14.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_14.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_14.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_14.horizontalHeader().setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_14.horizontalHeader().setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_14.horizontalHeader().setSectionResizeMode(7, QtWidgets.QHeaderView.ResizeToContents)
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
        self.pushButton_save_7.setCheckable(True)
        self.pushButton_save_7.setChecked(True)
        self.pushButton_save_7.setAutoDefault(False)
        self.pushButton_save_7.setDefault(False)
        self.pushButton_save_7.setFlat(False)
        self.pushButton_save_7.setObjectName("pushButton_save_7")
        self.label_20 = QtWidgets.QLabel(self.tab_17)
        self.label_20.setGeometry(QtCore.QRect(-20, 600, 91, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color: rgb(50, 50, 50);")
        self.label_20.setObjectName("label_20")
        self.label_26 = QtWidgets.QLabel(self.tab_17)
        self.label_26.setGeometry(QtCore.QRect(-20, 41, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(39)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("color: rgb(50, 50, 50);")
        self.label_26.setTextFormat(QtCore.Qt.AutoText)
        self.label_26.setObjectName("label_26")
        self.label_33 = QtWidgets.QLabel(self.tab_17)
        self.label_33.setGeometry(QtCore.QRect(1310, 38, 51, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label_33.setFont(font)
        self.label_33.setStyleSheet("color: rgb(50, 50, 50);")
        self.label_33.setObjectName("label_33")
        self.label_40 = QtWidgets.QLabel(self.tab_17)
        self.label_40.setGeometry(QtCore.QRect(1310, 598, 51, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label_40.setFont(font)
        self.label_40.setStyleSheet("color: rgb(50, 50, 50);")
        self.label_40.setObjectName("label_40")
        self.frame_19.raise_()
        self.lineEdit_14.raise_()
        self.pushButton_46.raise_()
        self.pushButton_52.raise_()
        self.label_14.raise_()
        self.pushButton_61.raise_()
        self.tableWidget_14.raise_()
        self.label_20.raise_()
        self.label_26.raise_()
        self.label_33.raise_()
        self.label_40.raise_()
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
        self.pushButton_53.setCheckable(True)
        self.pushButton_53.setChecked(True)
        self.pushButton_53.setObjectName("pushButton_53")
        self.label_15 = QtWidgets.QLabel(self.tab_18)
        self.label_15.setGeometry(QtCore.QRect(1120, 30, 241, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("QLabel {\n"
                                    "    color: rgb(255, 255, 255);}")
        self.label_15.setObjectName("label_15")
        self.pushButton_63 = QtWidgets.QPushButton(self.tab_18)
        self.pushButton_63.setGeometry(QtCore.QRect(1343, 520, 71, 41))
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
        self.pushButton_64.setGeometry(QtCore.QRect(1343, 570, 71, 41))
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
        self.tableWidget_15 = Test5(self.tab_18)
        self.tableWidget_15.setGeometry(QtCore.QRect(20, 70, 1311, 551))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget_15.setFont(font)
        self.tableWidget_15.setStyleSheet("QTableWidget {\n"
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
        self.tableWidget_15.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget_15.setObjectName("tableWidget_15")
        self.tableWidget_15.setColumnCount(8)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_15.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_15.setHorizontalHeaderItem(7, item)
        self.tableWidget_15.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)  # МОД
        self.tableWidget_15.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_15.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_15.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_15.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_15.horizontalHeader().setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_15.horizontalHeader().setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_15.horizontalHeader().setSectionResizeMode(7, QtWidgets.QHeaderView.ResizeToContents)
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
        self.pushButton_save_8.setCheckable(True)
        self.pushButton_save_8.setChecked(True)
        self.pushButton_save_8.setAutoDefault(False)
        self.pushButton_save_8.setDefault(False)
        self.pushButton_save_8.setFlat(False)
        self.pushButton_save_8.setObjectName("pushButton_save_8")
        self.label_21 = QtWidgets.QLabel(self.tab_18)
        self.label_21.setGeometry(QtCore.QRect(-20, 600, 91, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("color: rgb(50, 50, 50);")
        self.label_21.setObjectName("label_21")
        self.label_27 = QtWidgets.QLabel(self.tab_18)
        self.label_27.setGeometry(QtCore.QRect(-20, 41, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(39)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("color: rgb(50, 50, 50);")
        self.label_27.setTextFormat(QtCore.Qt.AutoText)
        self.label_27.setObjectName("label_27")
        self.label_34 = QtWidgets.QLabel(self.tab_18)
        self.label_34.setGeometry(QtCore.QRect(1310, 38, 51, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label_34.setFont(font)
        self.label_34.setStyleSheet("color: rgb(50, 50, 50);")
        self.label_34.setObjectName("label_34")
        self.label_41 = QtWidgets.QLabel(self.tab_18)
        self.label_41.setGeometry(QtCore.QRect(1310, 598, 51, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label_41.setFont(font)
        self.label_41.setStyleSheet("color: rgb(50, 50, 50);")
        self.label_41.setObjectName("label_41")
        self.frame_20.raise_()
        self.lineEdit_15.raise_()
        self.pushButton_47.raise_()
        self.pushButton_53.raise_()
        self.label_15.raise_()
        self.pushButton_63.raise_()
        self.tableWidget_15.raise_()
        self.label_21.raise_()
        self.label_27.raise_()
        self.label_34.raise_()
        self.label_41.raise_()
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
        self.pushButton_54.setCheckable(True)
        self.pushButton_54.setChecked(True)
        self.pushButton_54.setObjectName("pushButton_54")
        self.label_16 = QtWidgets.QLabel(self.tab_19)
        self.label_16.setGeometry(QtCore.QRect(1120, 30, 241, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("QLabel {\n"
                                    "    color: rgb(255, 255, 255);}")
        self.label_16.setObjectName("label_16")
        self.pushButton_65 = QtWidgets.QPushButton(self.tab_19)
        self.pushButton_65.setGeometry(QtCore.QRect(1343, 520, 71, 41))
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
        self.pushButton_66.setGeometry(QtCore.QRect(1343, 570, 71, 41))
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
        self.tableWidget_16 = Test6(self.tab_19)
        self.tableWidget_16.setGeometry(QtCore.QRect(20, 70, 1311, 551))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget_16.setFont(font)
        self.tableWidget_16.setStyleSheet("QTableWidget {\n"
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
        self.tableWidget_16.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget_16.setObjectName("tableWidget_16")
        self.tableWidget_16.setColumnCount(8)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_16.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_16.setHorizontalHeaderItem(7, item)
        self.tableWidget_16.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)  # МОД
        self.tableWidget_16.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_16.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_16.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_16.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_16.horizontalHeader().setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_16.horizontalHeader().setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_16.horizontalHeader().setSectionResizeMode(7, QtWidgets.QHeaderView.ResizeToContents)
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
        self.pushButton_save_9.setCheckable(True)
        self.pushButton_save_9.setChecked(True)
        self.pushButton_save_9.setAutoDefault(False)
        self.pushButton_save_9.setDefault(False)
        self.pushButton_save_9.setFlat(False)
        self.pushButton_save_9.setObjectName("pushButton_save_9")
        self.label_22 = QtWidgets.QLabel(self.tab_19)
        self.label_22.setGeometry(QtCore.QRect(-20, 600, 91, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("color: rgb(50, 50, 50);")
        self.label_22.setObjectName("label_22")
        self.label_28 = QtWidgets.QLabel(self.tab_19)
        self.label_28.setGeometry(QtCore.QRect(-20, 41, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(39)
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("color: rgb(50, 50, 50);")
        self.label_28.setTextFormat(QtCore.Qt.AutoText)
        self.label_28.setObjectName("label_28")
        self.label_35 = QtWidgets.QLabel(self.tab_19)
        self.label_35.setGeometry(QtCore.QRect(1310, 38, 51, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label_35.setFont(font)
        self.label_35.setStyleSheet("color: rgb(50, 50, 50);")
        self.label_35.setObjectName("label_35")
        self.label_42 = QtWidgets.QLabel(self.tab_19)
        self.label_42.setGeometry(QtCore.QRect(1310, 598, 51, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label_42.setFont(font)
        self.label_42.setStyleSheet("color: rgb(50, 50, 50);")
        self.label_42.setObjectName("label_42")
        self.frame_21.raise_()
        self.lineEdit_16.raise_()
        self.pushButton_48.raise_()
        self.pushButton_54.raise_()
        self.label_16.raise_()
        self.pushButton_65.raise_()
        self.tableWidget_16.raise_()
        self.label_22.raise_()
        self.label_28.raise_()
        self.label_35.raise_()
        self.label_42.raise_()
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
        self.pushButton_70.setCheckable(True)
        self.pushButton_70.setChecked(True)
        self.pushButton_70.setObjectName("pushButton_70")
        self.tableWidget_3 = Test7(self.tab_3)
        self.tableWidget_3.setGeometry(QtCore.QRect(20, 70, 1311, 551))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget_3.setFont(font)
        self.tableWidget_3.setStyleSheet("QTableWidget {\n"
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
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(8)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(7, item)
        self.tableWidget_3.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)  # МОД
        self.tableWidget_3.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_3.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_3.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_3.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_3.horizontalHeader().setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_3.horizontalHeader().setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_3.horizontalHeader().setSectionResizeMode(7, QtWidgets.QHeaderView.ResizeToContents)
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
        self.pushButton_71.setGeometry(QtCore.QRect(1343, 530, 71, 41))
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
        self.label_17.setGeometry(QtCore.QRect(1120, 40, 241, 20))
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
        self.pushButton_save_10.setCheckable(True)
        self.pushButton_save_10.setChecked(True)
        self.pushButton_save_10.setAutoDefault(False)
        self.pushButton_save_10.setDefault(False)
        self.pushButton_save_10.setFlat(False)
        self.pushButton_save_10.setObjectName("pushButton_save_10")
        self.label_23 = QtWidgets.QLabel(self.tab_3)
        self.label_23.setGeometry(QtCore.QRect(-20, 600, 91, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("color: rgb(50, 50, 50);")
        self.label_23.setObjectName("label_23")
        self.label_29 = QtWidgets.QLabel(self.tab_3)
        self.label_29.setGeometry(QtCore.QRect(-20, 41, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(39)
        font.setBold(True)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("color: rgb(50, 50, 50);")
        self.label_29.setTextFormat(QtCore.Qt.AutoText)
        self.label_29.setObjectName("label_29")
        self.label_36 = QtWidgets.QLabel(self.tab_3)
        self.label_36.setGeometry(QtCore.QRect(1310, 38, 51, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label_36.setFont(font)
        self.label_36.setStyleSheet("color: rgb(50, 50, 50);")
        self.label_36.setObjectName("label_36")
        self.label_55 = QtWidgets.QLabel(self.tab_3)
        self.label_55.setGeometry(QtCore.QRect(1310, 598, 51, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label_55.setFont(font)
        self.label_55.setStyleSheet("color: rgb(50, 50, 50);")
        self.label_55.setObjectName("label_55")
        self.pushButton_72 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_72.setGeometry(QtCore.QRect(1343, 570, 71, 41))
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
        self.label_23.raise_()
        self.label_29.raise_()
        self.label_36.raise_()
        self.label_55.raise_()
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
        self.pushButton.setGeometry(QtCore.QRect(1310, 620, 71, 41))
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
        self.pushButton_2.setGeometry(QtCore.QRect(1310, 570, 71, 41))
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
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setChecked(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.tableWidget = TestDetalis(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(20, 70, 1272, 601))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(12, 12, 12))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 73, 74))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(12, 12, 12))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(12, 12, 12))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 73, 74))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 73, 74))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(12, 12, 12))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 73, 74))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(12, 12, 12))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(12, 12, 12))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 73, 74))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 73, 74))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(12, 12, 12))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 73, 74))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(12, 12, 12))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(12, 12, 12))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 73, 74))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 73, 74))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.tableWidget.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget.setFont(font)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setStyleSheet("QTableWidget {\n"
                                       "border-radius: 15px;\n"
                                       "background-color: rgb(72, 73, 74)}\n"
                                       "\n"
                                       "QHeaderView::section {\n"
                                       "    background-color: rgb(255, 255, 255);\n"
                                       "    padding: 4px;\n"
                                       "    font-size: 12pt;\n"
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
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
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
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)  # МОД
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)  # first table
        self.tableWidget.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setVisible(False)
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
        self.label.setGeometry(QtCore.QRect(1080, 30, 241, 20))
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
        self.pushButton_11.setCheckable(True)
        self.pushButton_11.setChecked(True)
        self.pushButton_11.setObjectName("pushButton_11")
        self.label_56 = QtWidgets.QLabel(self.tab)
        self.label_56.setGeometry(QtCore.QRect(-20, 41, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(39)
        font.setBold(True)
        font.setWeight(75)
        self.label_56.setFont(font)
        self.label_56.setStyleSheet("color: rgb(50, 50, 50);")
        self.label_56.setTextFormat(QtCore.Qt.AutoText)
        self.label_56.setObjectName("label_56")
        self.label_43 = QtWidgets.QLabel(self.tab)
        self.label_43.setGeometry(QtCore.QRect(1270, 37, 51, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label_43.setFont(font)
        self.label_43.setStyleSheet("color: rgb(50, 50, 50);")
        self.label_43.setObjectName("label_43")
        self.label_44 = QtWidgets.QLabel(self.tab)
        self.label_44.setGeometry(QtCore.QRect(1268, 650, 51, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label_44.setFont(font)
        self.label_44.setStyleSheet("color: rgb(50, 50, 50);")
        self.label_44.setObjectName("label_44")
        self.label_57 = QtWidgets.QLabel(self.tab)
        self.label_57.setGeometry(QtCore.QRect(-20, 650, 91, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label_57.setFont(font)
        self.label_57.setStyleSheet("color: rgb(50, 50, 50);")
        self.label_57.setObjectName("label_57")
        self.frame_2.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.lineEdit.raise_()
        self.pushButton_3.raise_()
        self.tableWidget.raise_()
        self.pushButton_9.raise_()
        self.pushButton_save.raise_()
        self.label_56.raise_()
        self.label_43.raise_()
        self.label_44.raise_()
        self.label_57.raise_()
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
        self.pushButton_4.setCheckable(True)
        self.pushButton_4.setChecked(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.tableWidget_2 = TestMasters(self.tab_2)
        self.tableWidget_2.setGeometry(QtCore.QRect(20, 70, 1029, 521))
        self.tableWidget_2.setStyleSheet("QTableWidget {\n"
                                         "border-radius: 15px;\n"
                                         "background-color: rgb(72, 73, 74)}\n"
                                         "\n"
                                         "QHeaderView::section {\n"
                                         "    background-color: rgb(255, 255, 255);\n"
                                         "    padding: 4px;\n"
                                         "    font-size: 12pt;\n"
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
        self.tableWidget_2.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)  # МОД
        self.tableWidget_2.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_2.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
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
        self.pushButton_10.setCheckable(True)
        self.pushButton_10.setChecked(True)
        self.pushButton_10.setObjectName("pushButton_10")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(840, 30, 241, 20))
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
        self.pushButton_save_2.setCheckable(True)
        self.pushButton_save_2.setChecked(True)
        self.pushButton_save_2.setObjectName("pushButton_save_2")
        self.pushButton_67 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_67.setGeometry(QtCore.QRect(1060, 490, 71, 41))
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
        self.pushButton_68.setGeometry(QtCore.QRect(1060, 540, 71, 41))
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
        self.label_58 = QtWidgets.QLabel(self.tab_2)
        self.label_58.setGeometry(QtCore.QRect(-18, 40, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(39)
        font.setBold(True)
        font.setWeight(75)
        self.label_58.setFont(font)
        self.label_58.setStyleSheet("color: rgb(50, 50, 50);")
        self.label_58.setTextFormat(QtCore.Qt.AutoText)
        self.label_58.setObjectName("label_58")
        self.label_45 = QtWidgets.QLabel(self.tab_2)
        self.label_45.setGeometry(QtCore.QRect(1025, 37, 51, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label_45.setFont(font)
        self.label_45.setStyleSheet("color: rgb(50, 50, 50);")
        self.label_45.setObjectName("label_45")
        self.label_59 = QtWidgets.QLabel(self.tab_2)
        self.label_59.setGeometry(QtCore.QRect(-20, 569, 91, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label_59.setFont(font)
        self.label_59.setStyleSheet("color: rgb(50, 50, 50);")
        self.label_59.setObjectName("label_59")
        self.label_46 = QtWidgets.QLabel(self.tab_2)
        self.label_46.setGeometry(QtCore.QRect(1026, 570, 51, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label_46.setFont(font)
        self.label_46.setStyleSheet("color: rgb(50, 50, 50);")
        self.label_46.setObjectName("label_46")
        self.frame_6.raise_()
        self.lineEdit_2.raise_()
        self.pushButton_4.raise_()
        self.tableWidget_2.raise_()
        self.pushButton_10.raise_()
        self.label_2.raise_()
        self.label_58.raise_()
        self.label_45.raise_()
        self.label_59.raise_()
        self.label_46.raise_()
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_5.setGeometry(QtCore.QRect(40, 40, 481, 61))
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:\\Users\\User\\PycharmProjects\\SQL_Maket\\../../Desktop/png/zapros.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon1)
        self.pushButton_5.setIconSize(QtCore.QSize(100, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_6.setGeometry(QtCore.QRect(590, 40, 481, 61))
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:\\Users\\User\\PycharmProjects\\SQL_Maket\\../../Desktop/png/period.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon2)
        self.pushButton_6.setIconSize(QtCore.QSize(100, 35))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_7.setGeometry(QtCore.QRect(590, 130, 481, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_7.setAutoFillBackground(False)
        self.pushButton_7.setStyleSheet("QPushButton{\n"
                                        "    background-color: rgb(255, 255, 255);\n"
                                        "    border-radius: 5px;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: rgb(229, 229, 229);\n"
                                        "    color:rgb(0, 0, 0)}\n"
                                        "QPushButton:pressed {\n"
                                        "    background-color: rgb(255, 255, 255);}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("C:\\Users\\User\\PycharmProjects\\SQL_Maket\\../../Desktop/png/invent.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon3)
        self.pushButton_7.setIconSize(QtCore.QSize(110, 40))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_8.setGeometry(QtCore.QRect(40, 130, 481, 61))
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
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("C:\\Users\\User\\PycharmProjects\\SQL_Maket\\../../Desktop/png/tool.jpg"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_8.setIcon(icon4)
        self.pushButton_8.setIconSize(QtCore.QSize(50, 40))
        self.pushButton_8.setObjectName("pushButton_8")
        self.frame_22 = QtWidgets.QFrame(self.tab_5)
        self.frame_22.setGeometry(QtCore.QRect(-10, -70, 1461, 1021))
        self.frame_22.setStyleSheet("\n"
                                    "background-color: rgb(50, 50, 50);")
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.frame_22.raise_()
        self.pushButton_5.raise_()
        self.pushButton_6.raise_()
        self.pushButton_7.raise_()
        self.pushButton_8.raise_()
        self.tabWidget.addTab(self.tab_5, "")
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
        self.pushButton_74 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_74.setGeometry(QtCore.QRect(1370, 0, 36, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
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
        self.pushButton_74.raise_()
        self.pushButton_73.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "База данных ЖД"))
        self.pushButton_39.setText(_translate("MainWindow", "🔍"))
        self.pushButton_40.setText(_translate("MainWindow", "🗑"))
        self.tableWidget_10.setSortingEnabled(False)
        item = self.tableWidget_10.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "№"))
        item = self.tableWidget_10.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "№ локо"))
        item = self.tableWidget_10.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Вид ремонта"))
        item = self.tableWidget_10.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Редуктор"))
        item = self.tableWidget_10.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Мастер"))
        item = self.tableWidget_10.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Артикул"))
        item = self.tableWidget_10.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Часов наката"))
        item = self.tableWidget_10.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Дата"))
        self.pushButton_41.setText(_translate("MainWindow", "-"))
        self.label_10.setText(_translate("MainWindow", "Количество записей:"))
        self.pushButton_save_3.setText(_translate("MainWindow", "💾"))
        self.label_52.setText(_translate("MainWindow", "╭"))
        self.label_53.setText(_translate("MainWindow", "╰"))
        self.label_30.setText(_translate("MainWindow", "╮"))
        self.label_37.setText(_translate("MainWindow", "╯"))
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
        item.setText(_translate("MainWindow", "№ локо"))
        item = self.tableWidget_11.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Вид ремонта"))
        item = self.tableWidget_11.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Редуктор"))
        item = self.tableWidget_11.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Мастер"))
        item = self.tableWidget_11.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Артикул"))
        item = self.tableWidget_11.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Часов наката"))
        item = self.tableWidget_11.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Дата"))
        self.pushButton_save_4.setText(_translate("MainWindow", "💾"))
        self.label_8.setText(_translate("MainWindow", "╮"))
        self.label_9.setText(_translate("MainWindow", "╰"))
        self.label_18.setText(_translate("MainWindow", "╯"))
        self.label_7.setText(_translate("MainWindow", "╭"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_14), _translate("MainWindow", "Система 2"))
        self.pushButton_44.setText(_translate("MainWindow", "🔍"))
        self.pushButton_50.setText(_translate("MainWindow", "🗑"))
        self.label_12.setText(_translate("MainWindow", "Количество записей:"))
        self.pushButton_57.setText(_translate("MainWindow", "-"))
        self.pushButton_58.setText(_translate("MainWindow", "+"))
        item = self.tableWidget_12.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "№"))
        item = self.tableWidget_12.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "№ локо"))
        item = self.tableWidget_12.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Вид ремонта"))
        item = self.tableWidget_12.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Редуктор"))
        item = self.tableWidget_12.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Мастер"))
        item = self.tableWidget_12.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Артикул"))
        item = self.tableWidget_12.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Часов наката"))
        item = self.tableWidget_12.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Дата"))
        self.pushButton_save_5.setText(_translate("MainWindow", "💾"))
        self.label_54.setText(_translate("MainWindow", "╰"))
        self.label_24.setText(_translate("MainWindow", "╭"))
        self.label_31.setText(_translate("MainWindow", "╮"))
        self.label_38.setText(_translate("MainWindow", "╯"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_15), _translate("MainWindow", "Система 3"))
        self.pushButton_45.setText(_translate("MainWindow", "🔍"))
        self.pushButton_51.setText(_translate("MainWindow", "🗑"))
        self.label_13.setText(_translate("MainWindow", "Количество записей:"))
        self.pushButton_59.setText(_translate("MainWindow", "-"))
        self.pushButton_60.setText(_translate("MainWindow", "+"))
        item = self.tableWidget_13.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "№"))
        item = self.tableWidget_13.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "№ локо"))
        item = self.tableWidget_13.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Вид ремонта"))
        item = self.tableWidget_13.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Редуктор"))
        item = self.tableWidget_13.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Мастер"))
        item = self.tableWidget_13.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Артикул"))
        item = self.tableWidget_13.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Часов наката"))
        item = self.tableWidget_13.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Дата"))
        self.pushButton_save_6.setText(_translate("MainWindow", "💾"))
        self.label_19.setText(_translate("MainWindow", "╰"))
        self.label_25.setText(_translate("MainWindow", "╭"))
        self.label_32.setText(_translate("MainWindow", "╮"))
        self.label_39.setText(_translate("MainWindow", "╯"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_16), _translate("MainWindow", "Система 4"))
        self.pushButton_46.setText(_translate("MainWindow", "🔍"))
        self.pushButton_52.setText(_translate("MainWindow", "🗑"))
        self.label_14.setText(_translate("MainWindow", "Количество записей:"))
        self.pushButton_61.setText(_translate("MainWindow", "-"))
        self.pushButton_62.setText(_translate("MainWindow", "+"))
        item = self.tableWidget_14.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "№"))
        item = self.tableWidget_14.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "№ локо"))
        item = self.tableWidget_14.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Вид ремонта"))
        item = self.tableWidget_14.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Редуктор"))
        item = self.tableWidget_14.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Мастер"))
        item = self.tableWidget_14.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Артикул"))
        item = self.tableWidget_14.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Часов наката"))
        item = self.tableWidget_14.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Дата"))
        self.pushButton_save_7.setText(_translate("MainWindow", "💾"))
        self.label_20.setText(_translate("MainWindow", "╰"))
        self.label_26.setText(_translate("MainWindow", "╭"))
        self.label_33.setText(_translate("MainWindow", "╮"))
        self.label_40.setText(_translate("MainWindow", "╯"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_17), _translate("MainWindow", "Система 5"))
        self.pushButton_47.setText(_translate("MainWindow", "🔍"))
        self.pushButton_53.setText(_translate("MainWindow", "🗑"))
        self.label_15.setText(_translate("MainWindow", "Количество записей:"))
        self.pushButton_63.setText(_translate("MainWindow", "-"))
        self.pushButton_64.setText(_translate("MainWindow", "+"))
        item = self.tableWidget_15.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "№"))
        item = self.tableWidget_15.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "№ локо"))
        item = self.tableWidget_15.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Вид ремонта"))
        item = self.tableWidget_15.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Редуктор"))
        item = self.tableWidget_15.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Мастер"))
        item = self.tableWidget_15.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Артикул"))
        item = self.tableWidget_15.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Часов наката"))
        item = self.tableWidget_15.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Дата"))
        self.pushButton_save_8.setText(_translate("MainWindow", "💾"))
        self.label_21.setText(_translate("MainWindow", "╰"))
        self.label_27.setText(_translate("MainWindow", "╭"))
        self.label_34.setText(_translate("MainWindow", "╮"))
        self.label_41.setText(_translate("MainWindow", "╯"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_18), _translate("MainWindow", "Система 6"))
        self.pushButton_48.setText(_translate("MainWindow", "🔍"))
        self.pushButton_54.setText(_translate("MainWindow", "🗑"))
        self.label_16.setText(_translate("MainWindow", "Количество записей:"))
        self.pushButton_65.setText(_translate("MainWindow", "-"))
        self.pushButton_66.setText(_translate("MainWindow", "+"))
        item = self.tableWidget_16.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "№"))
        item = self.tableWidget_16.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "№ локо"))
        item = self.tableWidget_16.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Вид ремонта"))
        item = self.tableWidget_16.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Редуктор"))
        item = self.tableWidget_16.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Мастер"))
        item = self.tableWidget_16.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Артикул"))
        item = self.tableWidget_16.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Часов наката"))
        item = self.tableWidget_16.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Дата"))
        self.pushButton_save_9.setText(_translate("MainWindow", "💾"))
        self.label_22.setText(_translate("MainWindow", "╰"))
        self.label_28.setText(_translate("MainWindow", "╭"))
        self.label_35.setText(_translate("MainWindow", "╮"))
        self.label_42.setText(_translate("MainWindow", "╯"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_19), _translate("MainWindow", "Система 7"))
        self.pushButton_69.setText(_translate("MainWindow", "🔍"))
        self.pushButton_70.setText(_translate("MainWindow", "🗑"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "№"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "№ локо"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Вид ремонта"))
        item = self.tableWidget_3.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Редуктор"))
        item = self.tableWidget_3.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Мастер"))
        item = self.tableWidget_3.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Артикул"))
        item = self.tableWidget_3.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Часов наката"))
        item = self.tableWidget_3.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Дата"))
        self.pushButton_71.setText(_translate("MainWindow", "-"))
        self.label_17.setText(_translate("MainWindow", "Количество записей:"))
        self.pushButton_save_10.setText(_translate("MainWindow", "💾"))
        self.label_23.setText(_translate("MainWindow", "╰"))
        self.label_29.setText(_translate("MainWindow", "╭"))
        self.label_36.setText(_translate("MainWindow", "╮"))
        self.label_55.setText(_translate("MainWindow", "╯"))
        self.pushButton_72.setText(_translate("MainWindow", "+"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_3), _translate("MainWindow", "Локодром"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "ТО"))
        self.pushButton.setText(_translate("MainWindow", "+"))
        self.pushButton_2.setText(_translate("MainWindow", "-"))
        self.pushButton_3.setText(_translate("MainWindow", "🔍"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "№"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Артикул"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Тип детали"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Локомотив"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Количество"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Ящик"))
        self.pushButton_9.setText(_translate("MainWindow", "🗑"))
        self.pushButton_save.setText(_translate("MainWindow", "💾"))
        self.label.setText(_translate("MainWindow", "Количество записей:"))
        self.pushButton_11.setText(_translate("MainWindow", "↺"))
        self.label_56.setText(_translate("MainWindow", "╭"))
        self.label_43.setText(_translate("MainWindow", "╮"))
        self.label_44.setText(_translate("MainWindow", "╯"))
        self.label_57.setText(_translate("MainWindow", "╰"))
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
        self.label_58.setText(_translate("MainWindow", "╭"))
        self.label_45.setText(_translate("MainWindow", "╮"))
        self.label_59.setText(_translate("MainWindow", "╰"))
        self.label_46.setText(_translate("MainWindow", "╯"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Мастера"))
        self.pushButton_5.setText(_translate("MainWindow", "Запрос на детали"))
        self.pushButton_6.setText(_translate("MainWindow", "Переиод трат деталей"))
        self.pushButton_7.setText(_translate("MainWindow", "Инвентаризация "))
        self.pushButton_8.setText(_translate("MainWindow", "Запрос на оборудование, материалы"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Другое"))
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
