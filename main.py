import sqlite3
import sys

from PyQt5 import uic, QtWidgets, QtCore
from PyQt5.QtCore import Qt, QModelIndex
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QTableWidget, QMainWindow, QAbstractItemView
from PyQt5.uic.properties import QtGui
from sql_main import Ui_MainWindow, ExampleApp

bolt = 0


def auto():
    global login, password, re
    Form, Window = uic.loadUiType("login.ui")
    app = QApplication([])
    window = Window()
    form = Form()
    form.setupUi(window)
    window.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    window.setAttribute(QtCore.Qt.WA_TranslucentBackground)
    window.show()

    def point():
        global login, password, bolt
        login = form.lineEdit.text()
        password = form.lineEdit_2.text()
        if login == "" and password == "":
            bolt = 1
            window.close()
        else:
            return auto

    def close():
        window.close()

    form.pushButton_auto.clicked.connect(point)
    form.pushButton.clicked.connect(close)
    app.exec()


auto()  # авторизация

if bolt == 0:
    sys.exit()  # если авторизация не пройдена

app = QtWidgets.QApplication(sys.argv)
MainWindow = ExampleApp()
form = Ui_MainWindow()
form.setupUi(MainWindow)
MainWindow.show()

sqlite_connection = sqlite3.connect("id.db")
cursor = sqlite_connection.cursor()


# cursor.execute("""CREATE TABLE IF NOT EXISTS poll(
#    ID INTEGER PRIMARY KEY,
#    one TEXT,
#    two TEXT,
#    three TEXT,
#    foo TEXT);""")


def load_data():
    global row_number00
    users = cursor.execute("SELECT * FROM orders")
    for row_number00, order in enumerate(users):
        form.tableWidget.insertRow(row_number00)
        for column_number, data in enumerate(order):
            cell = QtWidgets.QTableWidgetItem(str(data))
            form.tableWidget.setItem(row_number00, column_number, cell)
            cell.setTextAlignment(Qt.AlignCenter)
        pool = int(row_number00 + 1)
        form.label.setText(f"Количество записей: {str(pool)}")
    try:
        form.tableWidget.scrollToItem(form.tableWidget.item(row_number00, 0), QAbstractItemView.PositionAtTop)
        form.tableWidget.selectRow(row_number00)
        form.tableWidget.clearSelection()
    except:
        pass


def room():
    global row_number00
    if form.lineEdit.text() == "":
        form.lineEdit.setText("Пустой запрос")
    else:
        form.tableWidget.setRowCount(0)
        search = form.lineEdit.text()
        now = cursor.execute(f"SELECT * FROM orders WHERE orderid='{search}' OR tip='{search}' OR datem='{search}'"
                             f"OR userid='{search}' OR total='{search}' OR ID='{search}'")
        for row_number00, order in enumerate(now):
            form.tableWidget.insertRow(row_number00)
            for column_number, data in enumerate(order):
                cell = QtWidgets.QTableWidgetItem(str(data))
                form.tableWidget.setItem(row_number00, column_number, cell)
                cell.setTextAlignment(Qt.AlignCenter)
            pool = int(row_number00 + 1)
            form.label.setText(f"Количество записей: {str(pool)}")


def boom():
    form.tableWidget.setRowCount(0)
    form.lineEdit.setText("")
    load_data()


def plus():
    form.tableWidget.setRowCount(0)
    cursor.execute("""INSERT INTO orders VALUES (NULL,'','','','','','')""")
    sqlite_connection.commit()
    load_data()


def minus():
    form.tableWidget.setRowCount(0)
    cursor.execute("""DELETE FROM orders WHERE orderid=''""")
    sqlite_connection.commit()
    load_data()


def save():
    try:
        global row_number00
        for i in range(int(row_number00) + 1):
            id = form.tableWidget.item(i, 1).text()
            tips = form.tableWidget.item(i, 2).text()
            loko = form.tableWidget.item(i, 3).text()
            stoim = form.tableWidget.item(i, 5).text()
            ID = form.tableWidget.item(i, 0).text()
            cursor.execute(
                f"""UPDATE orders SET orderid='{id}',tip='{tips}',datem='{loko}',total='{stoim}' WHERE ID='{ID}'""")
        sqlite_connection.commit()
    except:
        pass


##############2#####################
def load_data1():
    global row_number0
    users = cursor.execute("SELECT * FROM masters")
    for row_number0, order in enumerate(users):
        form.tableWidget_2.insertRow(row_number0)
        for column_number, data in enumerate(order):
            cell = QtWidgets.QTableWidgetItem(str(data))
            form.tableWidget_2.setItem(row_number0, column_number, cell)
            cell.setTextAlignment(Qt.AlignCenter)
        pool = int(row_number0 + 1)
        form.label_2.setText(f"Количество записей: {str(pool)}")
    try:
        form.tableWidget_2.scrollToItem(form.tableWidget_2.item(row_number0, 0), QAbstractItemView.PositionAtTop)
        form.tableWidget_2.selectRow(row_number0)
        form.tableWidget_2.clearSelection()
    except:
        pass


def room1():
    global row_number0
    if form.lineEdit_2.text() == "":
        form.lineEdit_2.setText("Пустой запрос")
    else:
        form.tableWidget_2.setRowCount(0)
        search = form.lineEdit_2.text()
        now = cursor.execute(f"SELECT * FROM masters WHERE fio='{search}' OR oplis='{search}' OR ID='{search}'")
        for row_number0, order in enumerate(now):
            form.tableWidget_2.insertRow(row_number0)
            for column_number, data in enumerate(order):
                cell = QtWidgets.QTableWidgetItem(str(data))
                form.tableWidget_2.setItem(row_number0, column_number, cell)
                cell.setTextAlignment(Qt.AlignCenter)
            pool = int(row_number0 + 1)
            form.label_2.setText(f"Количество записей: {str(pool)}")


def boom1():
    form.tableWidget_2.setRowCount(0)
    form.lineEdit_2.setText("")
    load_data1()


def plus1():
    form.tableWidget_2.setRowCount(0)
    cursor.execute("""INSERT INTO masters VALUES (NULL,'','')""")
    sqlite_connection.commit()
    load_data1()


def minus1():
    form.tableWidget_2.setRowCount(0)
    cursor.execute("""DELETE FROM masters WHERE fio=''""")
    sqlite_connection.commit()
    load_data1()


def save1():
    try:
        global row_number0
        for i in range(int(row_number0) + 1):
            ID = form.tableWidget_2.item(i, 0).text()
            fio = form.tableWidget_2.item(i, 1).text()
            oplis = form.tableWidget_2.item(i, 2).text()
            cursor.execute(f"""UPDATE masters SET fio='{fio}',oplis='{oplis}' WHERE ID='{ID}'""")
        sqlite_connection.commit()
    except:
        pass


###############TO1########################
def load_data_to1():
    global row_number1
    users = cursor.execute("SELECT * FROM TO1")
    for row_number1, order in enumerate(users):
        form.tableWidget_10.insertRow(row_number1)
        for column_number, data in enumerate(order):
            cell = QtWidgets.QTableWidgetItem(str(data))
            form.tableWidget_10.setItem(row_number1, column_number, cell)
            cell.setTextAlignment(Qt.AlignCenter)
        pool = int(row_number1 + 1)
        form.label_10.setText(f"Количество записей: {str(pool)}")
    try:
        form.tableWidget_10.scrollToItem(form.tableWidget_10.item(row_number1, 0), QAbstractItemView.PositionAtTop)
        form.tableWidget_10.selectRow(row_number1)
        form.tableWidget_10.clearSelection()
    except:
        pass


def room_to1():
    global row_number1
    if form.lineEdit_10.text() == "":
        form.lineEdit_10.setText("Пустой запрос")
    else:
        form.tableWidget_10.setRowCount(0)
        search = form.lineEdit_10.text()
        now = cursor.execute(
            f"SELECT * FROM TO1 WHERE loko='{search}' OR repair='{search}' OR ID='{search}' OR master='{search}'"
            f" OR userid='{search}' OR hours='{search}' OR datas='{search}' OR redukt='{search}'")
        for row_number1, order in enumerate(now):
            form.tableWidget_10.insertRow(row_number1)
            for column_number, data in enumerate(order):
                cell = QtWidgets.QTableWidgetItem(str(data))
                form.tableWidget_10.setItem(row_number1, column_number, cell)
                cell.setTextAlignment(Qt.AlignCenter)
            pool = int(row_number1 + 1)
            form.label_10.setText(f"Количество записей: {str(pool)}")


def boom_to1():
    form.tableWidget_10.setRowCount(0)
    form.lineEdit_10.setText("")
    load_data_to1()


def plus_to1():
    form.tableWidget_10.setRowCount(0)
    cursor.execute("""INSERT INTO TO1 VALUES (NULL,'','','','','','','')""")
    sqlite_connection.commit()
    load_data_to1()


def minus_to1():
    form.tableWidget_10.setRowCount(0)
    cursor.execute("""DELETE FROM TO1 WHERE loko=''""")
    sqlite_connection.commit()
    load_data_to1()


def save_to1():
    try:
        global row_number1
        for i in range(int(row_number1) + 1):
            ID = form.tableWidget_10.item(i, 0).text()
            loko = form.tableWidget_10.item(i, 1).text()
            repair = form.tableWidget_10.item(i, 2).text()
            redukt = form.tableWidget_10.item(i, 3).text()
            master = form.tableWidget_10.item(i, 4).text()
            userid = form.tableWidget_10.item(i, 5).text()
            hours = form.tableWidget_10.item(i, 6).text()
            datas = form.tableWidget_10.item(i, 7).text()
            cursor.execute(
                f"""UPDATE TO1 SET loko='{loko}',repair='{repair}',redukt='{redukt}',master='{master}',userid='{userid}',hours='{hours}',datas='{datas}' WHERE ID='{ID}'""")
        sqlite_connection.commit()
    except:
        pass


###############TO2########################
def load_data_to2():
    global row_number2
    users = cursor.execute("SELECT * FROM TO2")
    for row_number2, order in enumerate(users):
        form.tableWidget_11.insertRow(row_number2)
        for column_number, data in enumerate(order):
            cell = QtWidgets.QTableWidgetItem(str(data))
            form.tableWidget_11.setItem(row_number2, column_number, cell)
            cell.setTextAlignment(Qt.AlignCenter)
        pool = int(row_number2 + 1)
        form.label_11.setText(f"Количество записей: {str(pool)}")
    try:
        form.tableWidget_11.scrollToItem(form.tableWidget_11.item(row_number2, 0), QAbstractItemView.PositionAtTop)
        form.tableWidget_11.selectRow(row_number2)
        form.tableWidget_11.clearSelection()
    except:
        pass


def room_to2():
    global row_number2
    if form.lineEdit_11.text() == "":
        form.lineEdit_11.setText("Пустой запрос")
    else:
        form.tableWidget_11.setRowCount(0)
        search = form.lineEdit_11.text()
        now = cursor.execute(
            f"SELECT * FROM TO2 WHERE loko='{search}' OR repair='{search}' OR ID='{search}' OR master='{search}'"
            f" OR userid='{search}' OR hours='{search}' OR datas='{search}' OR redukt='{search}'")
        for row_number2, order in enumerate(now):
            form.tableWidget_11.insertRow(row_number2)
            for column_number, data in enumerate(order):
                cell = QtWidgets.QTableWidgetItem(str(data))
                form.tableWidget_11.setItem(row_number2, column_number, cell)
                cell.setTextAlignment(Qt.AlignCenter)
            pool = int(row_number2 + 1)
            form.label_11.setText(f"Количество записей: {str(pool)}")


def boom_to2():
    form.tableWidget_11.setRowCount(0)
    form.lineEdit_11.setText("")
    load_data_to2()


def plus_to2():
    form.tableWidget_11.setRowCount(0)
    cursor.execute("""INSERT INTO TO2 VALUES (NULL,'','','','','','','')""")
    sqlite_connection.commit()
    load_data_to2()


def minus_to2():
    form.tableWidget_11.setRowCount(0)
    cursor.execute("""DELETE FROM TO2 WHERE loko=''""")
    sqlite_connection.commit()
    load_data_to2()


def save_to2():
    try:
        global row_number2
        for i in range(int(row_number2) + 1):
            ID = form.tableWidget_11.item(i, 0).text()
            loko = form.tableWidget_11.item(i, 1).text()
            repair = form.tableWidget_11.item(i, 2).text()
            redukt = form.tableWidget_11.item(i, 3).text()
            master = form.tableWidget_11.item(i, 4).text()
            userid = form.tableWidget_11.item(i, 5).text()
            hours = form.tableWidget_11.item(i, 6).text()
            datas = form.tableWidget_11.item(i, 7).text()
            cursor.execute(
                f"""UPDATE TO2 SET loko='{loko}',repair='{repair}',redukt='{redukt}',master='{master}',userid='{userid}',hours='{hours}',datas='{datas}' WHERE ID='{ID}'""")
        sqlite_connection.commit()
    except:
        pass


###############TO3########################
def load_data_to3():
    global row_number3
    users = cursor.execute("SELECT * FROM TO3")
    for row_number3, order in enumerate(users):
        form.tableWidget_12.insertRow(row_number3)
        for column_number, data in enumerate(order):
            cell = QtWidgets.QTableWidgetItem(str(data))
            form.tableWidget_12.setItem(row_number3, column_number, cell)
            cell.setTextAlignment(Qt.AlignCenter)
        pool = int(row_number3 + 1)
        form.label_12.setText(f"Количество записей: {str(pool)}")
    try:
        form.tableWidget_12.scrollToItem(form.tableWidget_12.item(row_number3, 0), QAbstractItemView.PositionAtTop)
        form.tableWidget_12.selectRow(row_number3)
        form.tableWidget_12.clearSelection()
    except:
        pass


def room_to3():
    global row_number3
    if form.lineEdit_12.text() == "":
        form.lineEdit_12.setText("Пустой запрос")
    else:
        form.tableWidget_12.setRowCount(0)
        search = form.lineEdit_12.text()
        now = cursor.execute(
            f"SELECT * FROM TO3 WHERE loko='{search}' OR repair='{search}' OR ID='{search}' OR master='{search}'"
            f" OR userid='{search}' OR hours='{search}' OR datas='{search}' OR redukt='{search}'")
        for row_number3, order in enumerate(now):
            form.tableWidget_12.insertRow(row_number3)
            for column_number, data in enumerate(order):
                cell = QtWidgets.QTableWidgetItem(str(data))
                form.tableWidget_12.setItem(row_number3, column_number, cell)
                cell.setTextAlignment(Qt.AlignCenter)
            pool = int(row_number3 + 1)
            form.label_12.setText(f"Количество записей: {str(pool)}")


def boom_to3():
    form.tableWidget_12.setRowCount(0)
    form.lineEdit_12.setText("")
    load_data_to3()


def plus_to3():
    form.tableWidget_12.setRowCount(0)
    cursor.execute("""INSERT INTO TO3 VALUES (NULL,'','','','','','','')""")
    sqlite_connection.commit()
    load_data_to3()


def minus_to3():
    form.tableWidget_12.setRowCount(0)
    cursor.execute("""DELETE FROM TO3 WHERE loko=''""")
    sqlite_connection.commit()
    load_data_to3()


def save_to3():
    try:
        global row_number3
        for i in range(int(row_number3) + 1):
            ID = form.tableWidget_12.item(i, 0).text()
            loko = form.tableWidget_12.item(i, 1).text()
            repair = form.tableWidget_12.item(i, 2).text()
            redukt = form.tableWidget_12.item(i, 3).text()
            master = form.tableWidget_12.item(i, 4).text()
            userid = form.tableWidget_12.item(i, 5).text()
            hours = form.tableWidget_12.item(i, 6).text()
            datas = form.tableWidget_12.item(i, 7).text()
            cursor.execute(
                f"""UPDATE TO3 SET loko='{loko}',repair='{repair}',redukt='{redukt}',master='{master}',userid='{userid}',hours='{hours}',datas='{datas}' WHERE ID='{ID}'""")
        sqlite_connection.commit()
    except:
        pass


##############TO4#####################
def load_data_to4():
    global row_number4
    users = cursor.execute("SELECT * FROM TO4")
    for row_number4, order in enumerate(users):
        form.tableWidget_13.insertRow(row_number4)
        for column_number, data in enumerate(order):
            cell = QtWidgets.QTableWidgetItem(str(data))
            form.tableWidget_13.setItem(row_number4, column_number, cell)
            cell.setTextAlignment(Qt.AlignCenter)
        pool = int(row_number4 + 1)
        form.label_13.setText(f"Количество записей: {str(pool)}")
    try:
        form.tableWidget_13.scrollToItem(form.tableWidget_13.item(row_number4, 0), QAbstractItemView.PositionAtTop)
        form.tableWidget_13.selectRow(row_number4)
        form.tableWidget_13.clearSelection()
    except:
        pass


def room_to4():
    global row_number4
    if form.lineEdit_13.text() == "":
        form.lineEdit_13.setText("Пустой запрос")
    else:
        form.tableWidget_13.setRowCount(0)
        search = form.lineEdit_13.text()
        now = cursor.execute(
            f"SELECT * FROM TO4 WHERE loko='{search}' OR repair='{search}' OR ID='{search}' OR master='{search}'"
            f" OR userid='{search}' OR hours='{search}' OR datas='{search}' OR redukt='{search}'")
        for row_number4, order in enumerate(now):
            form.tableWidget_13.insertRow(row_number4)
            for column_number, data in enumerate(order):
                cell = QtWidgets.QTableWidgetItem(str(data))
                form.tableWidget_13.setItem(row_number4, column_number, cell)
                cell.setTextAlignment(Qt.AlignCenter)
            pool = int(row_number4 + 1)
            form.label_13.setText(f"Количество записей: {str(pool)}")


def boom_to4():
    form.tableWidget_13.setRowCount(0)
    form.lineEdit_13.setText("")
    load_data_to4()


def plus_to4():
    form.tableWidget_13.setRowCount(0)
    cursor.execute("""INSERT INTO TO4 VALUES (NULL,'','','','','','','')""")
    sqlite_connection.commit()
    load_data_to4()


def minus_to4():
    form.tableWidget_13.setRowCount(0)
    cursor.execute("""DELETE FROM TO4 WHERE loko=''""")
    sqlite_connection.commit()
    load_data_to4()


def save_to4():
    try:
        global row_number4
        for i in range(int(row_number4) + 1):
            ID = form.tableWidget_13.item(i, 0).text()
            loko = form.tableWidget_13.item(i, 1).text()
            repair = form.tableWidget_13.item(i, 2).text()
            redukt = form.tableWidget_13.item(i, 3).text()
            master = form.tableWidget_13.item(i, 4).text()
            userid = form.tableWidget_13.item(i, 5).text()
            hours = form.tableWidget_13.item(i, 6).text()
            datas = form.tableWidget_13.item(i, 7).text()
            cursor.execute(
                f"""UPDATE TO4 SET loko='{loko}',repair='{repair}',redukt='{redukt}',master='{master}',userid='{userid}',hours='{hours}',datas='{datas}' WHERE ID='{ID}'""")
        sqlite_connection.commit()
    except:
        pass


##############TO5#####################
def load_data_to5():
    global row_number5
    users = cursor.execute("SELECT * FROM TO5")
    for row_number5, order in enumerate(users):
        form.tableWidget_14.insertRow(row_number5)
        for column_number, data in enumerate(order):
            cell = QtWidgets.QTableWidgetItem(str(data))
            form.tableWidget_14.setItem(row_number5, column_number, cell)
            cell.setTextAlignment(Qt.AlignCenter)
        pool = int(row_number5 + 1)
        form.label_14.setText(f"Количество записей: {str(pool)}")
    try:
        form.tableWidget_14.scrollToItem(form.tableWidget_14.item(row_number5, 0), QAbstractItemView.PositionAtTop)
        form.tableWidget_14.selectRow(row_number5)
        form.tableWidget_14.clearSelection()
    except:
        pass


def room_to5():
    global row_number5
    if form.lineEdit_14.text() == "":
        form.lineEdit_14.setText("Пустой запрос")
    else:
        form.tableWidget_14.setRowCount(0)
        search = form.lineEdit_14.text()
        now = cursor.execute(
            f"SELECT * FROM TO5 WHERE loko='{search}' OR repair='{search}' OR ID='{search}' OR master='{search}'"
            f" OR userid='{search}' OR hours='{search}' OR datas='{search}' OR redukt='{search}'")
        for row_number5, order in enumerate(now):
            form.tableWidget_14.insertRow(row_number5)
            for column_number, data in enumerate(order):
                cell = QtWidgets.QTableWidgetItem(str(data))
                form.tableWidget_14.setItem(row_number5, column_number, cell)
                cell.setTextAlignment(Qt.AlignCenter)
            pool = int(row_number5 + 1)
            form.label_14.setText(f"Количество записей: {str(pool)}")


def boom_to5():
    form.tableWidget_14.setRowCount(0)
    form.lineEdit_14.setText("")
    load_data_to5()


def plus_to5():
    form.tableWidget_14.setRowCount(0)
    cursor.execute("""INSERT INTO TO5 VALUES (NULL,'','','','','','','')""")
    sqlite_connection.commit()
    load_data_to5()


def minus_to5():
    form.tableWidget_14.setRowCount(0)
    cursor.execute("""DELETE FROM TO5 WHERE loko=''""")
    sqlite_connection.commit()
    load_data_to5()


def save_to5():
    try:
        global row_number5
        for i in range(int(row_number5) + 1):
            ID = form.tableWidget_14.item(i, 0).text()
            loko = form.tableWidget_14.item(i, 1).text()
            repair = form.tableWidget_14.item(i, 2).text()
            redukt = form.tableWidget_14.item(i, 3).text()
            master = form.tableWidget_14.item(i, 4).text()
            userid = form.tableWidget_14.item(i, 5).text()
            hours = form.tableWidget_14.item(i, 6).text()
            datas = form.tableWidget_14.item(i, 7).text()
            cursor.execute(
                f"""UPDATE TO5 SET loko='{loko}',repair='{repair}',redukt='{redukt}',master='{master}',userid='{userid}',hours='{hours}',datas='{datas}' WHERE ID='{ID}'""")
        sqlite_connection.commit()
    except:
        pass


##############TO6#####################
def load_data_to6():
    global row_number6
    users = cursor.execute("SELECT * FROM TO6")
    for row_number6, order in enumerate(users):
        form.tableWidget_15.insertRow(row_number6)
        for column_number, data in enumerate(order):
            cell = QtWidgets.QTableWidgetItem(str(data))
            form.tableWidget_15.setItem(row_number6, column_number, cell)
            cell.setTextAlignment(Qt.AlignCenter)
        pool = int(row_number6 + 1)
        form.label_15.setText(f"Количество записей: {str(pool)}")
    try:
        form.tableWidget_15.scrollToItem(form.tableWidget_15.item(row_number6, 0), QAbstractItemView.PositionAtTop)
        form.tableWidget_15.selectRow(row_number6)
        form.tableWidget_15.clearSelection()
    except:
        pass


def room_to6():
    global row_number6
    if form.lineEdit_15.text() == "":
        form.lineEdit_15.setText("Пустой запрос")
    else:
        form.tableWidget_15.setRowCount(0)
        search = form.lineEdit_15.text()
        now = cursor.execute(
            f"SELECT * FROM TO6 WHERE loko='{search}' OR repair='{search}' OR ID='{search}' OR master='{search}'"
            f" OR userid='{search}' OR hours='{search}' OR datas='{search}' OR redukt='{search}'")
        for row_number6, order in enumerate(now):
            form.tableWidget_15.insertRow(row_number6)
            for column_number, data in enumerate(order):
                cell = QtWidgets.QTableWidgetItem(str(data))
                form.tableWidget_15.setItem(row_number6, column_number, cell)
                cell.setTextAlignment(Qt.AlignCenter)
            pool = int(row_number6 + 1)
            form.label_15.setText(f"Количество записей: {str(pool)}")


def boom_to6():
    form.tableWidget_15.setRowCount(0)
    form.lineEdit_15.setText("")
    load_data_to6()


def plus_to6():
    form.tableWidget_15.setRowCount(0)
    cursor.execute("""INSERT INTO TO6 VALUES (NULL,'','','','','','','')""")
    sqlite_connection.commit()
    load_data_to6()


def minus_to6():
    form.tableWidget_15.setRowCount(0)
    cursor.execute("""DELETE FROM TO6 WHERE loko=''""")
    sqlite_connection.commit()
    load_data_to6()


def save_to6():
    try:
        global row_number6
        for i in range(int(row_number6) + 1):
            ID = form.tableWidget_15.item(i, 0).text()
            loko = form.tableWidget_15.item(i, 1).text()
            repair = form.tableWidget_15.item(i, 2).text()
            redukt = form.tableWidget_15.item(i, 3).text()
            master = form.tableWidget_15.item(i, 4).text()
            userid = form.tableWidget_15.item(i, 5).text()
            hours = form.tableWidget_15.item(i, 6).text()
            datas = form.tableWidget_15.item(i, 7).text()
            cursor.execute(
                f"""UPDATE TO6 SET loko='{loko}',repair='{repair}',redukt='{redukt}',master='{master}',userid='{userid}',hours='{hours}',datas='{datas}' WHERE ID='{ID}'""")
        sqlite_connection.commit()
    except:
        pass


##############TO7#####################
def load_data_to7():
    global row_number7
    users = cursor.execute("SELECT * FROM TO7")
    for row_number7, order in enumerate(users):
        form.tableWidget_16.insertRow(row_number7)
        for column_number, data in enumerate(order):
            cell = QtWidgets.QTableWidgetItem(str(data))
            form.tableWidget_16.setItem(row_number7, column_number, cell)
            cell.setTextAlignment(Qt.AlignCenter)
        pool = int(row_number7 + 1)
        form.label_16.setText(f"Количество записей: {str(pool)}")
    try:
        form.tableWidget_16.scrollToItem(form.tableWidget_16.item(row_number7, 0), QAbstractItemView.PositionAtTop)
        form.tableWidget_16.selectRow(row_number7)
        form.tableWidget_16.clearSelection()
    except:
        pass


def room_to7():
    global row_number7
    if form.lineEdit_16.text() == "":
        form.lineEdit_16.setText("Пустой запрос")
    else:
        form.tableWidget_16.setRowCount(0)
        search = form.lineEdit_16.text()
        now = cursor.execute(
            f"SELECT * FROM TO7 WHERE loko='{search}' OR repair='{search}' OR ID='{search}' OR master='{search}'"
            f" OR userid='{search}' OR hours='{search}' OR datas='{search}' OR redukt='{search}'")
        for row_number7, order in enumerate(now):
            form.tableWidget_16.insertRow(row_number7)
            for column_number, data in enumerate(order):
                cell = QtWidgets.QTableWidgetItem(str(data))
                form.tableWidget_16.setItem(row_number7, column_number, cell)
                cell.setTextAlignment(Qt.AlignCenter)
            pool = int(row_number7 + 1)
            form.label_16.setText(f"Количество записей: {str(pool)}")


def boom_to7():
    form.tableWidget_16.setRowCount(0)
    form.lineEdit_16.setText("")
    load_data_to7()


def plus_to7():
    form.tableWidget_16.setRowCount(0)
    cursor.execute("""INSERT INTO TO7 VALUES (NULL,'','','','','','','')""")
    sqlite_connection.commit()
    load_data_to7()


def minus_to7():
    form.tableWidget_16.setRowCount(0)
    cursor.execute("""DELETE FROM TO7 WHERE loko=''""")
    sqlite_connection.commit()
    load_data_to7()


def save_to7():
    try:
        global row_number7
        for i in range(int(row_number7) + 1):
            ID = form.tableWidget_16.item(i, 0).text()
            loko = form.tableWidget_16.item(i, 1).text()
            repair = form.tableWidget_16.item(i, 2).text()
            redukt = form.tableWidget_16.item(i, 3).text()
            master = form.tableWidget_16.item(i, 4).text()
            userid = form.tableWidget_16.item(i, 5).text()
            hours = form.tableWidget_16.item(i, 6).text()
            datas = form.tableWidget_16.item(i, 7).text()
            cursor.execute(
                f"""UPDATE TO7 SET loko='{loko}',repair='{repair}',redukt='{redukt}',master='{master}',userid='{userid}',hours='{hours}',datas='{datas}' WHERE ID='{ID}'""")
        sqlite_connection.commit()
    except:
        pass


##############TO8#####################
def load_data_to8():
    global row_number8
    users = cursor.execute("SELECT * FROM TO8")
    for row_number8, order in enumerate(users):
        form.tableWidget_3.insertRow(row_number8)
        for column_number, data in enumerate(order):
            cell = QtWidgets.QTableWidgetItem(str(data))
            form.tableWidget_3.setItem(row_number8, column_number, cell)
            cell.setTextAlignment(Qt.AlignCenter)
        pool = int(row_number8 + 1)
        form.label_17.setText(f"Количество записей: {str(pool)}")
    try:
        form.tableWidget_3.scrollToItem(form.tableWidget_3.item(row_number8, 0), QAbstractItemView.PositionAtTop)
        form.tableWidget_3.selectRow(row_number8)
        form.tableWidget_3.clearSelection()
    except:
        pass


def room_to8():
    global row_number8
    if form.lineEdit_17.text() == "":
        form.lineEdit_17.setText("Пустой запрос")
    else:
        form.tableWidget_3.setRowCount(0)
        search = form.lineEdit_17.text()
        now = cursor.execute(
            f"SELECT * FROM TO8 WHERE loko='{search}' OR repair='{search}' OR ID='{search}' OR master='{search}'"
            f" OR userid='{search}' OR hours='{search}' OR datas='{search}' OR redukt='{search}'")
        for row_number8, order in enumerate(now):
            form.tableWidget_3.insertRow(row_number8)
            for column_number, data in enumerate(order):
                cell = QtWidgets.QTableWidgetItem(str(data))
                form.tableWidget_3.setItem(row_number8, column_number, cell)
                cell.setTextAlignment(Qt.AlignCenter)
            pool = int(row_number8 + 1)
            form.label_17.setText(f"Количество записей: {str(pool)}")


def boom_to8():
    form.tableWidget_3.setRowCount(0)
    form.lineEdit_17.setText("")
    load_data_to8()


def plus_to8():
    form.tableWidget_3.setRowCount(0)
    cursor.execute("""INSERT INTO TO8 VALUES (NULL,'','','','','','','')""")
    sqlite_connection.commit()
    load_data_to8()


def minus_to8():
    form.tableWidget_3.setRowCount(0)
    cursor.execute("""DELETE FROM TO8 WHERE loko=''""")
    sqlite_connection.commit()
    load_data_to8()


def save_to8():
    try:
        global row_number8
        for i in range(int(row_number8) + 1):
            ID = form.tableWidget_3.item(i, 0).text()
            loko = form.tableWidget_3.item(i, 1).text()
            repair = form.tableWidget_3.item(i, 2).text()
            redukt = form.tableWidget_3.item(i, 3).text()
            master = form.tableWidget_3.item(i, 4).text()
            userid = form.tableWidget_3.item(i, 5).text()
            hours = form.tableWidget_3.item(i, 6).text()
            datas = form.tableWidget_3.item(i, 7).text()
            cursor.execute(
                f"""UPDATE TO8 SET loko='{loko}',repair='{repair}',redukt='{redukt}',master='{master}',userid='{userid}',hours='{hours}',datas='{datas}' WHERE ID='{ID}'""")
        sqlite_connection.commit()
    except:
        pass


#######reload######################
def road_to():
    form.tableWidget.setRowCount(0)
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
        cursor.execute(f"""UPDATE orders SET userid=(SELECT (userid - COUNT('{fux}')) WHERE '{fux}'=orderid)""")
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
        cursor.execute(f"""UPDATE orders SET userid=(SELECT (userid - COUNT('{fux}')) WHERE '{fux}'=orderid)""")
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
        cursor.execute(f"""UPDATE orders SET userid=(SELECT (userid - COUNT('{fux}')) WHERE '{fux}'=orderid)""")
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
        cursor.execute(f"""UPDATE orders SET userid=(SELECT (userid - COUNT('{fux}')) WHERE '{fux}'=orderid)""")
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
        cursor.execute(f"""UPDATE orders SET userid=(SELECT (userid - COUNT('{fux}')) WHERE '{fux}'=orderid)""")
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
        cursor.execute(f"""UPDATE orders SET userid=(SELECT (userid - COUNT('{fux}')) WHERE '{fux}'=orderid)""")
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
        cursor.execute(f"""UPDATE orders SET userid=(SELECT (userid - COUNT('{fux}')) WHERE '{fux}'=orderid)""")
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
        cursor.execute(f"""UPDATE orders SET userid=(SELECT (userid - COUNT('{fux}')) WHERE '{fux}'=orderid)""")
    sqlite_connection.commit()
    load_data()


# load_data()
road_to()
load_data1()
load_data_to1()
load_data_to2()
load_data_to3()
load_data_to4()
load_data_to5()
load_data_to6()
load_data_to7()
load_data_to8()
##############1#####################
form.pushButton_3.clicked.connect(room)
form.pushButton_9.clicked.connect(boom)
form.pushButton.clicked.connect(plus)
form.pushButton_2.clicked.connect(minus)
form.pushButton_save.clicked.connect(save)
##############2#####################
form.pushButton_68.clicked.connect(plus1)
form.pushButton_67.clicked.connect(minus1)
form.pushButton_4.clicked.connect(room1)
form.pushButton_10.clicked.connect(boom1)
form.pushButton_save_2.clicked.connect(save1)
##############TO1#####################
form.pushButton_42.clicked.connect(plus_to1)
form.pushButton_41.clicked.connect(minus_to1)
form.pushButton_39.clicked.connect(room_to1)
form.pushButton_40.clicked.connect(boom_to1)
form.pushButton_save_3.clicked.connect(save_to1)
##############TO2#####################
form.pushButton_56.clicked.connect(plus_to2)
form.pushButton_55.clicked.connect(minus_to2)
form.pushButton_43.clicked.connect(room_to2)
form.pushButton_49.clicked.connect(boom_to2)
form.pushButton_save_4.clicked.connect(save_to2)
##############TO3#####################
form.pushButton_58.clicked.connect(plus_to3)
form.pushButton_57.clicked.connect(minus_to3)
form.pushButton_44.clicked.connect(room_to3)
form.pushButton_50.clicked.connect(boom_to3)
form.pushButton_save_5.clicked.connect(save_to3)
##############TO4#####################
form.pushButton_60.clicked.connect(plus_to4)
form.pushButton_59.clicked.connect(minus_to4)
form.pushButton_45.clicked.connect(room_to4)
form.pushButton_51.clicked.connect(boom_to4)
form.pushButton_save_6.clicked.connect(save_to4)
##############TO5#####################
form.pushButton_62.clicked.connect(plus_to5)
form.pushButton_61.clicked.connect(minus_to5)
form.pushButton_46.clicked.connect(room_to5)
form.pushButton_52.clicked.connect(boom_to5)
form.pushButton_save_7.clicked.connect(save_to5)
##############TO6#####################
form.pushButton_64.clicked.connect(plus_to6)
form.pushButton_63.clicked.connect(minus_to6)
form.pushButton_47.clicked.connect(room_to6)
form.pushButton_53.clicked.connect(boom_to6)
form.pushButton_save_8.clicked.connect(save_to6)
##############TO7#####################
form.pushButton_66.clicked.connect(plus_to7)
form.pushButton_65.clicked.connect(minus_to7)
form.pushButton_48.clicked.connect(room_to7)
form.pushButton_54.clicked.connect(boom_to7)
form.pushButton_save_9.clicked.connect(save_to7)
##############TO8#####################
form.pushButton_72.clicked.connect(plus_to8)
form.pushButton_71.clicked.connect(minus_to8)
form.pushButton_69.clicked.connect(room_to8)
form.pushButton_70.clicked.connect(boom_to8)
form.pushButton_save_10.clicked.connect(save_to8)


###############window###################
def myClose():
    MainWindow.close()


def myMinimize():
    MainWindow.showMinimized()


form.pushButton_73.clicked.connect(myClose)
form.pushButton_74.clicked.connect(myMinimize)
##########reload#################
form.pushButton_11.clicked.connect(road_to)

sys.exit(app.exec_())
