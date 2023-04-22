import datetime

import sqlite3
import sys
import time


from PyQt5 import uic, QtWidgets, QtCore
from PyQt5.QtCore import Qt, QThread, QByteArray
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QApplication, QAbstractItemView, QLabel, QFileDialog


from sql_main import Ui_MainWindow, ExampleApp


lvl = 0
sqlite_connection1 = sqlite3.connect("loko_and_poezd.db")
sqlite_connection = sqlite3.connect("id.db")
cursor = sqlite_connection.cursor()
cursor1 = sqlite_connection1.cursor()
today = datetime.datetime.today()


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
        global login, password, lvl
        login = form.lineEdit.text()
        password = form.lineEdit_2.text()
        try:
            log=cursor.execute(f"""SELECT login FROM autorization WHERE login='{login}'""").fetchone()
            pas=cursor.execute(f"""SELECT password FROM autorization WHERE password='{password}'""").fetchone()
            if login == log[0] and password == pas[0]:
                lvl = int(cursor.execute(f"""SELECT levels FROM autorization WHERE login='{login}' and password='{password}'""").fetchone()[0])
                cursor.execute(f"""INSERT INTO logout VALUES (NULL,'{login}','{today.strftime("%d.%m.%Y-%Hh %Mm")}')""")
                window.close()
        except:
            form.label_5.setText("Ошибка авторизации!")
            return auto

    def close():
        window.close()

    form.pushButton_auto.clicked.connect(point)
    form.pushButton.clicked.connect(close)
    app.exec()


auto()  # авторизация

if lvl == 0:
    sys.exit()  # если авторизация не пройдена
start_time = time.time()
app = QtWidgets.QApplication(sys.argv)
MainWindow = ExampleApp()
form = Ui_MainWindow()
form.setupUi(MainWindow)
MainWindow.show()



#cursor.execute("""CREATE TABLE IF NOT EXISTS autorization(
#   ID INTEGER PRIMARY KEY,
#   login TEXT,
#   password TEXT,
#   levels TEXT);""")

def load_data():
    global row_number00
    users = cursor.execute("SELECT ID,NULL,orderid,tip,datem,userid,total FROM orders")
    for row_number00, order in enumerate(users):
        form.tableWidget.insertRow(row_number00)
        for column_number, data in enumerate(order):
            item = QtWidgets.QTableWidgetItem(str(data))
            item.setTextAlignment(Qt.AlignCenter)
            if column_number==1:
                pass
            else:
                form.tableWidget.setItem(row_number00, column_number, item)
    users = cursor.execute("SELECT foto FROM orders")
    a = users.fetchall()
    for i in range(len(a)):
        if str(a[i][0]) != "None":
            label = QLabel()
            label.setText("")
            label.setScaledContents(True)
            pix = QPixmap(f"{a[i][0]}")
            label.setPixmap(pix)
            form.tableWidget.setCellWidget(i, 1, label)
        else:
            pass
    pool = int(row_number00 + 1)
    form.label.setText(f"Количество записей: {str(pool)}")
    form.tableWidget.horizontalHeader().setDefaultSectionSize(100)
    form.tableWidget.verticalHeader().setDefaultSectionSize(100)
    form.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)  # МОД
    form.tableWidget.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Fixed)
    form.tableWidget.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
    form.tableWidget.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
    form.tableWidget.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
    form.tableWidget.horizontalHeader().setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
    form.tableWidget.horizontalHeader().setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)
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
        now = cursor.execute(f"SELECT * FROM orders WHERE orderid='{search}' OR tip LIKE '%{search}%' OR datem='{search}'"
                             f"OR userid='{search}' OR total='{search}' OR ID='{search}'")
        for row_number00, order in enumerate(now):
            form.tableWidget.insertRow(row_number00)
            for column_number, data in enumerate(order):
                item = QtWidgets.QTableWidgetItem(str(data))
                item.setTextAlignment(Qt.AlignCenter)
                if column_number == 1:
                    pass
                else:
                    form.tableWidget.setItem(row_number00, column_number, item)
        users = cursor.execute(f"SELECT foto FROM orders WHERE orderid='{search}' OR tip LIKE '%{search}%' OR datem='{search}'"
                             f"OR userid='{search}' OR total='{search}' OR ID='{search}'")
        a = users.fetchall()
        for i in range(len(a)):
            if str(a[i][0]) != "None":
                label = QLabel()
                label.setText("")
                label.setScaledContents(True)
                pix = QPixmap(f"{a[i][0]}")
                label.setPixmap(pix)
                form.tableWidget.setCellWidget(i, 1, label)
            else:
                pass
        pool = int(row_number00 + 1)
        form.label.setText(f"Количество записей: {str(pool)}")


def boom():
    form.tableWidget.setRowCount(0)
    form.lineEdit.setText("")
    load_data()


def plus():
    apps = QtWidgets.QDialog()
    wb_patch = \
        QtWidgets.QFileDialog.getOpenFileName(MainWindow, "Выбор фотки детали", None, "Image (*.png *.jpg *.jpeg)")[0]
    apps.close()
    if wb_patch:
        foto = wb_patch.split('База данных ЖД/')[1]
        form.tableWidget.setRowCount(0)
        cursor.execute(f"""INSERT INTO orders VALUES (?,?,?,?,?,?,?,?)""",
                        [None, foto, '', '', '', '', '', ''])
        sqlite_connection.commit()
        load_data()



def minus():
    form.tableWidget.setRowCount(0)
    cursor.execute("""DELETE FROM orders WHERE orderid='' AND tip ='' AND datem=''""")
    sqlite_connection.commit()
    load_data()


def save():
    try:
        global row_number00
        for i in range(int(row_number00) + 1):
            ID = form.tableWidget.item(i, 0).text()
            id = form.tableWidget.item(i, 2).text()
            tips = form.tableWidget.item(i, 3).text()
            loko = form.tableWidget.item(i, 4).text()
            stoim = form.tableWidget.item(i, 6).text()
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
    form.tableWidget_2.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
    form.tableWidget_2.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
    form.tableWidget_2.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
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
    users = cursor1.execute(f"""SELECT * FROM lokotrain1 ORDER BY loko""")
    for row_number1, order in enumerate(users):
        form.tableWidget_10.insertRow(row_number1)
        for column_number, data in enumerate(order):
            item = QtWidgets.QTableWidgetItem(str(data))
            item.setTextAlignment(Qt.AlignCenter)
            if (column_number == 1):
                pix = form.getImageLabel(data)
                form.tableWidget_10.setCellWidget(row_number1, column_number, pix)
            else:
                form.tableWidget_10.setItem(row_number1, column_number, item)
        pool = int(row_number1 + 1)
        form.label_10.setText(f"Количество записей: {str(pool)}")
    form.tableWidget_10.horizontalHeader().setDefaultSectionSize(130)
    form.tableWidget_10.horizontalHeader().setSectionResizeMode(0,
                                                                QtWidgets.QHeaderView.ResizeToContents)
    form.tableWidget_10.horizontalHeader().setSectionResizeMode(1,
                                                                QtWidgets.QHeaderView.Fixed)
    form.tableWidget_10.horizontalHeader().setSectionResizeMode(2,
                                                             QtWidgets.QHeaderView.ResizeToContents)
    form.tableWidget_10.horizontalHeader().setSectionResizeMode(3,
                                                             QtWidgets.QHeaderView.ResizeToContents)
    form.tableWidget_10.horizontalHeader().setSectionResizeMode(4,
                                                             QtWidgets.QHeaderView.ResizeToContents)
    form.tableWidget_10.horizontalHeader().setSectionResizeMode(5,
                                                             QtWidgets.QHeaderView.Stretch)
    try:
        form.tableWidget_10.scrollToItem(form.tableWidget.item(0, 0), QAbstractItemView.PositionAtTop)
        form.tableWidget_10.selectRow(0)
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
        now = cursor1.execute(
            f"SELECT * FROM lokotrain1 WHERE loko='{search}' OR tiploko='{search}' OR ID='{search}' OR model='{search}'"
            f" OR comment LIKE '%{search}%'")
        for row_number1, order in enumerate(now):
            form.tableWidget_10.insertRow(row_number1)
            for column_number, data in enumerate(order):
                item = QtWidgets.QTableWidgetItem(str(data))
                item.setTextAlignment(Qt.AlignCenter)
                if (column_number == 1):
                    pix = form.getImageLabel(data)
                    form.tableWidget_10.setCellWidget(row_number1, column_number, pix)
                else:
                    form.tableWidget_10.setItem(row_number1, column_number, item)
            pool = int(row_number1 + 1)
            form.label_10.setText(f"Количество записей: {str(pool)}")


def boom_to1():
    form.tableWidget_10.setRowCount(0)
    form.lineEdit_10.setText("")
    load_data_to1()


def plus_to1():
    apps = QtWidgets.QDialog()
    wb_patch = \
        QtWidgets.QFileDialog.getOpenFileName(MainWindow, "Выбор картинки", None, "Image (*.png *.jpg *.jpeg)")[0]
    apps.close()
    if wb_patch:
        image = open(f"{wb_patch}", 'rb')
        form.tableWidget_10.setRowCount(0)
        cursor1.execute(f"""INSERT INTO lokotrain1 VALUES (?,?,?,?,?,?)""",
                        [None, sqlite3.Binary(image.read()), '', '', '', ''])
        sqlite_connection1.commit()
        load_data_to1()


def minus_to1():
    form.tableWidget_10.setRowCount(0)
    cursor1.execute("""DELETE FROM lokotrain1 WHERE loko=''""")
    sqlite_connection1.commit()
    load_data_to1()


def save_to1():
    try:
        global row_number1
        for i in range(int(row_number1) + 1):
            ID = form.tableWidget_10.item(i, 0).text()
            loko = form.tableWidget_10.item(i, 2).text()
            tiploko = form.tableWidget_10.item(i, 3).text()
            model = form.tableWidget_10.item(i, 4).text()
            comment = form.tableWidget_10.item(i, 5).text()
            cursor1.execute(
                f"""UPDATE lokotrain1 SET loko='{loko}',tiploko='{tiploko}',model='{model}',comment='{comment}' WHERE ID='{ID}'""")
        sqlite_connection1.commit()
        form.tableWidget_10.setRowCount(0)
        load_data_to1()
    except:
        pass


###############TO2########################
def load_data_to2():
    global row_number2
    users = cursor1.execute("""SELECT * FROM lokotrain2 ORDER BY loko""")
    for row_number2, order in enumerate(users):
        form.tableWidget_11.insertRow(row_number2)
        for column_number, data in enumerate(order):
            item = QtWidgets.QTableWidgetItem(str(data))
            item.setTextAlignment(Qt.AlignCenter)
            if (column_number == 1):
                pix = form.getImageLabel(data)
                form.tableWidget_11.setCellWidget(row_number2, column_number, pix)
            else:
                form.tableWidget_11.setItem(row_number2, column_number, item)
        pool = int(row_number2 + 1)
        form.label_11.setText(f"Количество записей: {str(pool)}")
    form.tableWidget_11.horizontalHeader().setDefaultSectionSize(130)
    form.tableWidget_11.horizontalHeader().setSectionResizeMode(0,
                                                                QtWidgets.QHeaderView.ResizeToContents)
    form.tableWidget_11.horizontalHeader().setSectionResizeMode(1,
                                                                QtWidgets.QHeaderView.Fixed)
    form.tableWidget_11.horizontalHeader().setSectionResizeMode(2,
                                                               QtWidgets.QHeaderView.ResizeToContents)
    form.tableWidget_11.horizontalHeader().setSectionResizeMode(3,
                                                               QtWidgets.QHeaderView.ResizeToContents)
    form.tableWidget_11.horizontalHeader().setSectionResizeMode(4,
                                                               QtWidgets.QHeaderView.ResizeToContents)
    form.tableWidget_11.horizontalHeader().setSectionResizeMode(5,
                                                                QtWidgets.QHeaderView.Stretch)
    try:
        form.tableWidget_11.scrollToItem(form.tableWidget.item(0, 0), QAbstractItemView.PositionAtTop)
        form.tableWidget_11.selectRow(0)
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
        now = cursor1.execute(
            f"SELECT * FROM lokotrain2 WHERE loko='{search}' OR tiploko='{search}' OR ID='{search}' OR model='{search}'"
            f" OR comment LIKE '%{search}%'")
        for row_number2, order in enumerate(now):
            form.tableWidget_11.insertRow(row_number2)
            for column_number, data in enumerate(order):
                item = QtWidgets.QTableWidgetItem(str(data))
                item.setTextAlignment(Qt.AlignCenter)
                if (column_number == 1):
                    pix = form.getImageLabel(data)
                    form.tableWidget_11.setCellWidget(row_number2, column_number, pix)
                else:
                    form.tableWidget_11.setItem(row_number2, column_number, item)
            pool = int(row_number2 + 1)
            form.label_11.setText(f"Количество записей: {str(pool)}")


def boom_to2():
    form.tableWidget_11.setRowCount(0)
    form.lineEdit_11.setText("")
    load_data_to2()


def plus_to2():
    apps = QtWidgets.QDialog()
    wb_patch = \
        QtWidgets.QFileDialog.getOpenFileName(MainWindow, "Выбор картинки", None, "Image (*.png *.jpg *.jpeg)")[0]
    apps.close()
    if wb_patch:
        image = open(f"{wb_patch}", 'rb')
        form.tableWidget_11.setRowCount(0)
        cursor1.execute(f"""INSERT INTO lokotrain2 VALUES (?,?,?,?,?,?)""",
                        [None, sqlite3.Binary(image.read()), '', '', '', ''])
        sqlite_connection1.commit()
        load_data_to2()


def minus_to2():
    form.tableWidget_11.setRowCount(0)
    cursor1.execute("""DELETE FROM lokotrain2 WHERE loko=''""")
    sqlite_connection1.commit()
    load_data_to2()


def save_to2():
    try:
        global row_number2
        for i in range(int(row_number2) + 1):
            ID = form.tableWidget_11.item(i, 0).text()
            loko = form.tableWidget_11.item(i, 2).text()
            tiploko = form.tableWidget_11.item(i, 3).text()
            model = form.tableWidget_11.item(i, 4).text()
            comment = form.tableWidget_11.item(i, 5).text()
            cursor1.execute(
                f"""UPDATE lokotrain2 SET loko='{loko}',tiploko='{tiploko}',model='{model}',comment='{comment}' WHERE ID='{ID}'""")
        sqlite_connection1.commit()
    except:
        pass


###############TO3########################
def load_data_to3():
    global row_number3
    users = cursor1.execute("""SELECT * FROM lokotrain3 ORDER BY loko""")
    for row_number3, order in enumerate(users):
        form.tableWidget_12.insertRow(row_number3)
        for column_number, data in enumerate(order):
            item = QtWidgets.QTableWidgetItem(str(data))
            item.setTextAlignment(Qt.AlignCenter)
            if (column_number == 1):
                pix = form.getImageLabel(data)
                form.tableWidget_12.setCellWidget(row_number3, column_number, pix)
            else:
                form.tableWidget_12.setItem(row_number3, column_number, item)
        pool = int(row_number3 + 1)
        form.label_12.setText(f"Количество записей: {str(pool)}")
    form.tableWidget_12.horizontalHeader().setDefaultSectionSize(130)
    form.tableWidget_12.horizontalHeader().setSectionResizeMode(0,
                                                                QtWidgets.QHeaderView.ResizeToContents)
    form.tableWidget_12.horizontalHeader().setSectionResizeMode(1,
                                                                QtWidgets.QHeaderView.Fixed)
    form.tableWidget_12.horizontalHeader().setSectionResizeMode(2,
                                                                QtWidgets.QHeaderView.ResizeToContents)
    form.tableWidget_12.horizontalHeader().setSectionResizeMode(3,
                                                                QtWidgets.QHeaderView.ResizeToContents)
    form.tableWidget_12.horizontalHeader().setSectionResizeMode(4,
                                                                QtWidgets.QHeaderView.ResizeToContents)
    form.tableWidget_12.horizontalHeader().setSectionResizeMode(5,
                                                                QtWidgets.QHeaderView.Stretch)
    try:
        form.tableWidget_12.scrollToItem(form.tableWidget.item(0, 0), QAbstractItemView.PositionAtTop)
        form.tableWidget_12.selectRow(0)
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
        now = cursor1.execute(
            f"SELECT * FROM lokotrain3 WHERE loko='{search}' OR tiploko='{search}' OR ID='{search}' OR model='{search}'"
            f" OR comment LIKE '%{search}%'")
        for row_number3, order in enumerate(now):
            form.tableWidget_12.insertRow(row_number3)
            for column_number, data in enumerate(order):
                item = QtWidgets.QTableWidgetItem(str(data))
                item.setTextAlignment(Qt.AlignCenter)
                if (column_number == 1):
                    pix = form.getImageLabel(data)
                    form.tableWidget_12.setCellWidget(row_number3, column_number, pix)
                else:
                    form.tableWidget_12.setItem(row_number3, column_number, item)
            pool = int(row_number3 + 1)
            form.label_12.setText(f"Количество записей: {str(pool)}")


def boom_to3():
    form.tableWidget_12.setRowCount(0)
    form.lineEdit_12.setText("")
    load_data_to3()


def plus_to3():
    apps = QtWidgets.QDialog()
    wb_patch = \
        QtWidgets.QFileDialog.getOpenFileName(MainWindow, "Выбор картинки", None, "Image (*.png *.jpg *.jpeg)")[0]
    apps.close()
    if wb_patch:
        image = open(f"{wb_patch}", 'rb')
        form.tableWidget_12.setRowCount(0)
        cursor1.execute(f"""INSERT INTO lokotrain3 VALUES (?,?,?,?,?,?)""",
                        [None, sqlite3.Binary(image.read()), '', '', '', ''])
        sqlite_connection1.commit()
        load_data_to3()


def minus_to3():
    form.tableWidget_12.setRowCount(0)
    cursor1.execute("""DELETE FROM lokotrain3 WHERE loko=''""")
    sqlite_connection1.commit()
    load_data_to3()


def save_to3():
    try:
        global row_number3
        for i in range(int(row_number3) + 1):
            ID = form.tableWidget_12.item(i, 0).text()
            loko = form.tableWidget_12.item(i, 2).text()
            tiploko = form.tableWidget_12.item(i, 3).text()
            model = form.tableWidget_12.item(i, 4).text()
            comment = form.tableWidget_12.item(i, 5).text()
            cursor1.execute(
                f"""UPDATE lokotrain3 SET loko='{loko}',tiploko='{tiploko}',model='{model}',comment='{comment}' WHERE ID='{ID}'""")
        sqlite_connection1.commit()
    except:
        pass


##############TO4#####################
def load_data_to4():
    global row_number4
    users = cursor1.execute("""SELECT * FROM lokotrain4 ORDER BY loko""")
    for row_number4, order in enumerate(users):
        form.tableWidget_13.insertRow(row_number4)
        for column_number, data in enumerate(order):
            item = QtWidgets.QTableWidgetItem(str(data))
            item.setTextAlignment(Qt.AlignCenter)
            if (column_number == 1):
                pix = form.getImageLabel(data)
                form.tableWidget_13.setCellWidget(row_number4, column_number, pix)
            else:
                form.tableWidget_13.setItem(row_number4, column_number, item)
        pool = int(row_number4 + 1)
        form.label_13.setText(f"Количество записей: {str(pool)}")
    form.tableWidget_13.horizontalHeader().setDefaultSectionSize(130)
    form.tableWidget_13.horizontalHeader().setSectionResizeMode(0,
                                                                QtWidgets.QHeaderView.ResizeToContents)
    form.tableWidget_13.horizontalHeader().setSectionResizeMode(1,
                                                                QtWidgets.QHeaderView.Fixed)
    form.tableWidget_13.horizontalHeader().setSectionResizeMode(2,
                                                                QtWidgets.QHeaderView.ResizeToContents)
    form.tableWidget_13.horizontalHeader().setSectionResizeMode(3,
                                                                QtWidgets.QHeaderView.ResizeToContents)
    form.tableWidget_13.horizontalHeader().setSectionResizeMode(4,
                                                                QtWidgets.QHeaderView.ResizeToContents)
    form.tableWidget_13.horizontalHeader().setSectionResizeMode(5,
                                                                QtWidgets.QHeaderView.Stretch)
    try:
        form.tableWidget_13.scrollToItem(form.tableWidget.item(0, 0), QAbstractItemView.PositionAtTop)
        form.tableWidget_13.selectRow(0)
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
        now = cursor1.execute(
            f"SELECT * FROM lokotrain4 WHERE loko='{search}' OR tiploko='{search}' OR ID='{search}' OR model='{search}'"
            f" OR comment LIKE '%{search}%'")
        for row_number4, order in enumerate(now):
            form.tableWidget_13.insertRow(row_number4)
            for column_number, data in enumerate(order):
                item = QtWidgets.QTableWidgetItem(str(data))
                item.setTextAlignment(Qt.AlignCenter)
                if (column_number == 1):
                    pix = form.getImageLabel(data)
                    form.tableWidget_13.setCellWidget(row_number4, column_number, pix)
                else:
                    form.tableWidget_13.setItem(row_number4, column_number, item)
            pool = int(row_number4 + 1)
            form.label_13.setText(f"Количество записей: {str(pool)}")


def boom_to4():
    form.tableWidget_13.setRowCount(0)
    form.lineEdit_13.setText("")
    load_data_to4()


def plus_to4():
    apps = QtWidgets.QDialog()
    wb_patch = \
        QtWidgets.QFileDialog.getOpenFileName(MainWindow, "Выбор картинки", None, "Image (*.png *.jpg *.jpeg)")[0]
    apps.close()
    if wb_patch:
        image = open(f"{wb_patch}", 'rb')
        form.tableWidget_13.setRowCount(0)
        cursor1.execute(f"""INSERT INTO lokotrain4 VALUES (?,?,?,?,?,?)""",
                        [None, sqlite3.Binary(image.read()), '', '', '', ''])
        sqlite_connection1.commit()
        load_data_to4()


def minus_to4():
    form.tableWidget_13.setRowCount(0)
    cursor1.execute("""DELETE FROM lokotrain4 WHERE loko=''""")
    sqlite_connection1.commit()
    load_data_to4()


def save_to4():
    try:
        global row_number4
        for i in range(int(row_number4) + 1):
            ID = form.tableWidget_13.item(i, 0).text()
            loko = form.tableWidget_13.item(i, 2).text()
            tiploko = form.tableWidget_13.item(i, 3).text()
            model = form.tableWidget_13.item(i, 4).text()
            comment = form.tableWidget_13.item(i, 5).text()
            cursor1.execute(
                f"""UPDATE lokotrain4 SET loko='{loko}',tiploko='{tiploko}',model='{model}',comment='{comment}' WHERE ID='{ID}'""")
        sqlite_connection1.commit()
    except:
        pass


##############TO5#####################
def load_data_to5():
    global row_number5
    users = cursor1.execute("""SELECT * FROM lokotrain5 ORDER BY loko""")
    for row_number5, order in enumerate(users):
        form.tableWidget_14.insertRow(row_number5)
        for column_number, data in enumerate(order):
            item = QtWidgets.QTableWidgetItem(str(data))
            item.setTextAlignment(Qt.AlignCenter)
            if (column_number == 1):
                pix = form.getImageLabel(data)
                form.tableWidget_14.setCellWidget(row_number5, column_number, pix)
            else:
                form.tableWidget_14.setItem(row_number5, column_number, item)
        pool = int(row_number5 + 1)
        form.label_14.setText(f"Количество записей: {str(pool)}")
    form.tableWidget_14.horizontalHeader().setDefaultSectionSize(130)
    form.tableWidget_14.horizontalHeader().setSectionResizeMode(0,
                                                                QtWidgets.QHeaderView.ResizeToContents)
    form.tableWidget_14.horizontalHeader().setSectionResizeMode(1,
                                                                QtWidgets.QHeaderView.Fixed)
    form.tableWidget_14.horizontalHeader().setSectionResizeMode(2,
                                                                QtWidgets.QHeaderView.ResizeToContents)
    form.tableWidget_14.horizontalHeader().setSectionResizeMode(3,
                                                                QtWidgets.QHeaderView.ResizeToContents)
    form.tableWidget_14.horizontalHeader().setSectionResizeMode(4,
                                                                QtWidgets.QHeaderView.ResizeToContents)
    form.tableWidget_14.horizontalHeader().setSectionResizeMode(5,
                                                                QtWidgets.QHeaderView.Stretch)
    try:
        form.tableWidget_14.scrollToItem(form.tableWidget.item(0, 0), QAbstractItemView.PositionAtTop)
        form.tableWidget_14.selectRow(0)
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
        now = cursor1.execute(
            f"SELECT * FROM lokotrain5 WHERE loko='{search}' OR tiploko='{search}' OR ID='{search}' OR model='{search}'"
            f" OR comment LIKE '%{search}%'")
        for row_number5, order in enumerate(now):
            form.tableWidget_14.insertRow(row_number5)
            for column_number, data in enumerate(order):
                item = QtWidgets.QTableWidgetItem(str(data))
                item.setTextAlignment(Qt.AlignCenter)
                if (column_number == 1):
                    pix = form.getImageLabel(data)
                    form.tableWidget_14.setCellWidget(row_number5, column_number, pix)
                else:
                    form.tableWidget_14.setItem(row_number5, column_number, item)
            pool = int(row_number5 + 1)
            form.label_14.setText(f"Количество записей: {str(pool)}")


def boom_to5():
    form.tableWidget_14.setRowCount(0)
    form.lineEdit_14.setText("")
    load_data_to5()


def plus_to5():
    apps = QtWidgets.QDialog()
    wb_patch = \
        QtWidgets.QFileDialog.getOpenFileName(MainWindow, "Выбор картинки", None, "Image (*.png *.jpg *.jpeg)")[0]
    apps.close()
    if wb_patch:
        image = open(f"{wb_patch}", 'rb')
        form.tableWidget_14.setRowCount(0)
        cursor1.execute(f"""INSERT INTO lokotrain5 VALUES (?,?,?,?,?,?)""",
                        [None, sqlite3.Binary(image.read()), '', '', '', ''])
        sqlite_connection1.commit()
        load_data_to5()


def minus_to5():
    form.tableWidget_14.setRowCount(0)
    cursor1.execute("""DELETE FROM lokotrain5 WHERE loko=''""")
    sqlite_connection1.commit()
    load_data_to5()


def save_to5():
    try:
        global row_number5
        for i in range(int(row_number5) + 1):
            ID = form.tableWidget_14.item(i, 0).text()
            loko = form.tableWidget_14.item(i, 2).text()
            tiploko = form.tableWidget_14.item(i, 3).text()
            model = form.tableWidget_14.item(i, 4).text()
            comment = form.tableWidget_14.item(i, 5).text()
            cursor1.execute(
                f"""UPDATE lokotrain5 SET loko='{loko}',tiploko='{tiploko}',model='{model}',comment='{comment}' WHERE ID='{ID}'""")
        sqlite_connection1.commit()
    except:
        pass


##############TO6#####################
def load_data_to6():
    global row_number6
    users = cursor1.execute("""SELECT * FROM lokotrain6 ORDER BY loko""")
    for row_number6, order in enumerate(users):
        form.tableWidget_15.insertRow(row_number6)
        for column_number, data in enumerate(order):
            item = QtWidgets.QTableWidgetItem(str(data))
            item.setTextAlignment(Qt.AlignCenter)
            if (column_number == 1):
                pix = form.getImageLabel(data)
                form.tableWidget_15.setCellWidget(row_number6, column_number, pix)
            else:
                form.tableWidget_15.setItem(row_number6, column_number, item)
        pool = int(row_number6 + 1)
        form.label_15.setText(f"Количество записей: {str(pool)}")
    form.tableWidget_15.horizontalHeader().setDefaultSectionSize(130)
    form.tableWidget_15.horizontalHeader().setSectionResizeMode(0,
                                                                QtWidgets.QHeaderView.ResizeToContents)
    form.tableWidget_15.horizontalHeader().setSectionResizeMode(1,
                                                                QtWidgets.QHeaderView.Fixed)
    form.tableWidget_15.horizontalHeader().setSectionResizeMode(2,
                                                                QtWidgets.QHeaderView.ResizeToContents)
    form.tableWidget_15.horizontalHeader().setSectionResizeMode(3,
                                                                QtWidgets.QHeaderView.ResizeToContents)
    form.tableWidget_15.horizontalHeader().setSectionResizeMode(4,
                                                                QtWidgets.QHeaderView.ResizeToContents)
    form.tableWidget_15.horizontalHeader().setSectionResizeMode(5,
                                                                QtWidgets.QHeaderView.Stretch)
    try:
        form.tableWidget_15.scrollToItem(form.tableWidget.item(0, 0), QAbstractItemView.PositionAtTop)
        form.tableWidget_15.selectRow(0)
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
        now = cursor1.execute(
            f"SELECT * FROM lokotrain6 WHERE loko='{search}' OR tiploko='{search}' OR ID='{search}' OR model='{search}'"
            f" OR comment LIKE '%{search}%'")
        for row_number6, order in enumerate(now):
            form.tableWidget_15.insertRow(row_number6)
            for column_number, data in enumerate(order):
                item = QtWidgets.QTableWidgetItem(str(data))
                item.setTextAlignment(Qt.AlignCenter)
                if (column_number == 1):
                    pix = form.getImageLabel(data)
                    form.tableWidget_15.setCellWidget(row_number6, column_number, pix)
                else:
                    form.tableWidget_15.setItem(row_number6, column_number, item)
            pool = int(row_number6 + 1)
            form.label_15.setText(f"Количество записей: {str(pool)}")


def boom_to6():
    form.tableWidget_15.setRowCount(0)
    form.lineEdit_15.setText("")
    load_data_to6()


def plus_to6():
    apps = QtWidgets.QDialog()
    wb_patch = \
        QtWidgets.QFileDialog.getOpenFileName(MainWindow, "Выбор картинки", None, "Image (*.png *.jpg *.jpeg)")[0]
    apps.close()
    if wb_patch:
        image = open(f"{wb_patch}", 'rb')
        form.tableWidget_15.setRowCount(0)
        cursor1.execute(f"""INSERT INTO lokotrain6 VALUES (?,?,?,?,?,?)""",
                        [None, sqlite3.Binary(image.read()), '', '', '', ''])
        sqlite_connection1.commit()
        load_data_to6()


def minus_to6():
    form.tableWidget_15.setRowCount(0)
    cursor1.execute("""DELETE FROM lokotrain6 WHERE loko=''""")
    sqlite_connection1.commit()
    load_data_to6()


def save_to6():
    try:
        global row_number6
        for i in range(int(row_number6) + 1):
            ID = form.tableWidget_15.item(i, 0).text()
            loko = form.tableWidget_15.item(i, 2).text()
            tiploko = form.tableWidget_15.item(i, 3).text()
            model = form.tableWidget_15.item(i, 4).text()
            comment = form.tableWidget_15.item(i, 5).text()
            cursor1.execute(
                f"""UPDATE lokotrain6 SET loko='{loko}',tiploko='{tiploko}',model='{model}',comment='{comment}' WHERE ID='{ID}'""")
        sqlite_connection1.commit()
    except:
        pass


##############TO7#####################
def load_data_to7():
    global row_number7
    users = cursor1.execute("""SELECT * FROM lokotrain7 ORDER BY loko""")
    for row_number7, order in enumerate(users):
        form.tableWidget_16.insertRow(row_number7)
        for column_number, data in enumerate(order):
            item = QtWidgets.QTableWidgetItem(str(data))
            item.setTextAlignment(Qt.AlignCenter)
            if (column_number == 1):
                pix = form.getImageLabel(data)
                form.tableWidget_16.setCellWidget(row_number7, column_number, pix)
            else:
                form.tableWidget_16.setItem(row_number7, column_number, item)
        pool = int(row_number7 + 1)
        form.label_16.setText(f"Количество записей: {str(pool)}")
    form.tableWidget_16.horizontalHeader().setDefaultSectionSize(130)
    form.tableWidget_16.horizontalHeader().setSectionResizeMode(0,
                                                                QtWidgets.QHeaderView.ResizeToContents)
    form.tableWidget_16.horizontalHeader().setSectionResizeMode(1,
                                                                QtWidgets.QHeaderView.Fixed)
    form.tableWidget_16.horizontalHeader().setSectionResizeMode(2,
                                                                QtWidgets.QHeaderView.ResizeToContents)
    form.tableWidget_16.horizontalHeader().setSectionResizeMode(3,
                                                                QtWidgets.QHeaderView.ResizeToContents)
    form.tableWidget_16.horizontalHeader().setSectionResizeMode(4,
                                                                QtWidgets.QHeaderView.ResizeToContents)
    form.tableWidget_16.horizontalHeader().setSectionResizeMode(5,
                                                                QtWidgets.QHeaderView.Stretch)
    try:
        form.tableWidget_16.scrollToItem(form.tableWidget.item(0, 0), QAbstractItemView.PositionAtTop)
        form.tableWidget_16.selectRow(0)
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
        now = cursor1.execute(
            f"SELECT * FROM lokotrain7 WHERE loko='{search}' OR tiploko='{search}' OR ID='{search}' OR model='{search}'"
            f" OR comment LIKE '%{search}%'")
        for row_number7, order in enumerate(now):
            form.tableWidget_16.insertRow(row_number7)
            for column_number, data in enumerate(order):
                item = QtWidgets.QTableWidgetItem(str(data))
                item.setTextAlignment(Qt.AlignCenter)
                if (column_number == 1):
                    pix = form.getImageLabel(data)
                    form.tableWidget_16.setCellWidget(row_number7, column_number, pix)
                else:
                    form.tableWidget_16.setItem(row_number7, column_number, item)
            pool = int(row_number7 + 1)
            form.label_16.setText(f"Количество записей: {str(pool)}")


def boom_to7():
    form.tableWidget_16.setRowCount(0)
    form.lineEdit_16.setText("")
    load_data_to7()


def plus_to7():
    apps = QtWidgets.QDialog()
    wb_patch = \
        QtWidgets.QFileDialog.getOpenFileName(MainWindow, "Выбор картинки", None, "Image (*.png *.jpg *.jpeg)")[0]
    apps.close()
    if wb_patch:
        image = open(f"{wb_patch}", 'rb')
        form.tableWidget_16.setRowCount(0)
        cursor1.execute(f"""INSERT INTO lokotrain7 VALUES (?,?,?,?,?,?)""",
                        [None, sqlite3.Binary(image.read()), '', '', '', ''])
        sqlite_connection1.commit()
        load_data_to7()


def minus_to7():
    form.tableWidget_16.setRowCount(0)
    cursor1.execute("""DELETE FROM lokotrain7 WHERE loko=''""")
    sqlite_connection1.commit()
    load_data_to7()


def save_to7():
    try:
        global row_number7
        for i in range(int(row_number7) + 1):
            ID = form.tableWidget_16.item(i, 0).text()
            loko = form.tableWidget_16.item(i, 2).text()
            tiploko = form.tableWidget_16.item(i, 3).text()
            model = form.tableWidget_16.item(i, 4).text()
            comment = form.tableWidget_16.item(i, 5).text()
            cursor1.execute(
                f"""UPDATE lokotrain7 SET loko='{loko}',tiploko='{tiploko}',model='{model}',comment='{comment}' WHERE ID='{ID}'""")
        sqlite_connection1.commit()
    except:
        pass


##############TO8#####################
def load_data_to8():
    global row_number8
    users = cursor1.execute("""SELECT * FROM lokotrain8 ORDER BY loko""")
    for row_number8, order in enumerate(users):
        form.tableWidget_3.insertRow(row_number8)
        for column_number, data in enumerate(order):
            item = QtWidgets.QTableWidgetItem(str(data))
            item.setTextAlignment(Qt.AlignCenter)
            if (column_number == 1):
                pix = form.getImageLabel(data)
                form.tableWidget_3.setCellWidget(row_number8, column_number, pix)
            else:
                form.tableWidget_3.setItem(row_number8, column_number, item)
        pool = int(row_number8 + 1)
        form.label_17.setText(f"Количество записей: {str(pool)}")
    form.tableWidget_3.horizontalHeader().setDefaultSectionSize(130)
    form.tableWidget_3.horizontalHeader().setSectionResizeMode(0,
                                                                QtWidgets.QHeaderView.ResizeToContents)
    form.tableWidget_3.horizontalHeader().setSectionResizeMode(1,
                                                                QtWidgets.QHeaderView.Fixed)
    form.tableWidget_3.horizontalHeader().setSectionResizeMode(2,
                                                                QtWidgets.QHeaderView.ResizeToContents)
    form.tableWidget_3.horizontalHeader().setSectionResizeMode(3,
                                                                QtWidgets.QHeaderView.ResizeToContents)
    form.tableWidget_3.horizontalHeader().setSectionResizeMode(4,
                                                                QtWidgets.QHeaderView.ResizeToContents)
    form.tableWidget_3.horizontalHeader().setSectionResizeMode(5,
                                                                QtWidgets.QHeaderView.Stretch)
    try:
        form.tableWidget_3.scrollToItem(form.tableWidget.item(0, 0), QAbstractItemView.PositionAtTop)
        form.tableWidget_3.selectRow(0)
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
        now = cursor1.execute(
            f"SELECT * FROM lokotrain8 WHERE loko='{search}' OR tiploko='{search}' OR ID='{search}' OR model='{search}'"
            f" OR comment LIKE '%{search}%'")
        for row_number8, order in enumerate(now):
            form.tableWidget_3.insertRow(row_number8)
            for column_number, data in enumerate(order):
                item = QtWidgets.QTableWidgetItem(str(data))
                item.setTextAlignment(Qt.AlignCenter)
                if (column_number == 1):
                    pix = form.getImageLabel(data)
                    form.tableWidget_3.setCellWidget(row_number8, column_number, pix)
                else:
                    form.tableWidget_3.setItem(row_number8, column_number, item)
            pool = int(row_number8 + 1)
            form.label_17.setText(f"Количество записей: {str(pool)}")


def boom_to8():
    form.tableWidget_3.setRowCount(0)
    form.lineEdit_17.setText("")
    load_data_to8()


def plus_to8():
    apps = QtWidgets.QDialog()
    wb_patch = \
        QtWidgets.QFileDialog.getOpenFileName(MainWindow, "Выбор картинки", None, "Image (*.png *.jpg *.jpeg)")[0]
    apps.close()
    if wb_patch:
        image = open(f"{wb_patch}", 'rb')
        form.tableWidget_3.setRowCount(0)
        cursor1.execute(f"""INSERT INTO lokotrain8 VALUES (?,?,?,?,?,?)""",
                        [None, sqlite3.Binary(image.read()), '', '', '', ''])
        sqlite_connection1.commit()
        load_data_to8()


def minus_to8():
    form.tableWidget_3.setRowCount(0)
    cursor1.execute("""DELETE FROM lokotrain8 WHERE loko=''""")
    sqlite_connection1.commit()
    load_data_to8()


def save_to8():
    try:
        global row_number8
        for i in range(int(row_number8) + 1):
            ID = form.tableWidget_3.item(i, 0).text()
            loko = form.tableWidget_3.item(i, 2).text()
            tiploko = form.tableWidget_3.item(i, 3).text()
            model = form.tableWidget_3.item(i, 4).text()
            comment = form.tableWidget_3.item(i, 5).text()
            cursor1.execute(
                f"""UPDATE lokotrain8 SET loko='{loko}',tiploko='{tiploko}',model='{model}',comment='{comment}' WHERE ID='{ID}'""")
        sqlite_connection1.commit()
    except:
        pass


#######reload######################
def road_to():
    form.tableWidget.setRowCount(0)
    cursor.execute(f"""UPDATE orders SET userid=(SELECT (kol))""")
    for i in range(8):
        title = f"TO{i+1}"
        pup = cursor.execute(f"""SELECT userid FROM '{title}' WHERE userid != ''""")
        nice = pup.fetchall()
        for o in range(len(nice)):
            a = str(nice[o][0]).split(",")
            for n in range(len(a)):
                c = a[n].split("_")
                try:
                    for i in range(int(c[1])):
                        cursor.execute(
                            f"""UPDATE orders SET userid=(SELECT (userid - COUNT('{c[0]}')) WHERE '{c[0]}'=orderid)""")
                except:
                    pass
    sqlite_connection.commit()
    load_data()

###################################Авторизация######################################
def autorization():
    if lvl==3:
        Form, App = uic.loadUiType("autorization.ui")
        app = QtWidgets.QDialog()
        form = Form()
        form.setupUi(app)
        app.show()
        def load_data():
            global row_number_auto
            users = cursor.execute("SELECT * FROM autorization")
            for row_number_auto, order in enumerate(users):
                form.tableWidget.insertRow(row_number_auto)
                for column_number, data in enumerate(order):
                    cell = QtWidgets.QTableWidgetItem(str(data))
                    form.tableWidget.setItem(row_number_auto, column_number, cell)
                    cell.setTextAlignment(Qt.AlignCenter)
            form.tableWidget.horizontalHeader().setSectionResizeMode(0,
                                                                     QtWidgets.QHeaderView.ResizeToContents)
            form.tableWidget.horizontalHeader().setSectionResizeMode(1,
                                                                     QtWidgets.QHeaderView.Stretch)
            form.tableWidget.horizontalHeader().setSectionResizeMode(2,
                                                                     QtWidgets.QHeaderView.Stretch)
            form.tableWidget.horizontalHeader().setSectionResizeMode(3,
                                                                     QtWidgets.QHeaderView.ResizeToContents)
            try:
                form.tableWidget.scrollToItem(form.tableWidget.item(row_number_auto, 0),
                                                QAbstractItemView.PositionAtTop)
                form.tableWidget.selectRow(row_number_auto)
                form.tableWidget.clearSelection()
            except:
                pass
        def plus():
            form.tableWidget.setRowCount(0)
            cursor.execute("""INSERT INTO autorization VALUES (NULL,'','','')""")
            sqlite_connection.commit()
            load_data()
        def minus():
            form.tableWidget.setRowCount(0)
            cursor.execute("""DELETE FROM autorization WHERE login=''""")
            sqlite_connection.commit()
            load_data()
        def save():
            try:
                global row_number_auto
                for i in range(int(row_number_auto) + 1):
                    ID = form.tableWidget.item(i, 0).text()
                    login = form.tableWidget.item(i, 1).text()
                    password = form.tableWidget.item(i, 2).text()
                    levels = form.tableWidget.item(i, 3).text()
                    cursor.execute(
                        f"""UPDATE autorization SET login='{login}',password='{password}',levels='{levels}'WHERE ID='{ID}'""")
                sqlite_connection.commit()
            except:
                pass
        load_data()
        form.pushButton_save.clicked.connect(save)
        form.pushButton_plus.clicked.connect(plus)
        form.pushButton_minus.clicked.connect(minus)
        app.exec()
    else:
        Form, App = uic.loadUiType("dont.ui")
        app = QtWidgets.QDialog()
        form = Form()
        form.setupUi(app)
        app.show()
        def ok():
            app.close()
        form.pushButton.clicked.connect(ok)
        app.exec()

form.pushButton_5.clicked.connect(autorization)
########################Входы в БД#####################
def log_out():
    if lvl==3 or lvl==2:
        Form, App = uic.loadUiType("bd_log_out.ui")
        app = QtWidgets.QDialog()
        form = Form()
        form.setupUi(app)
        app.show()
        def load_data():
            global row_number_log
            users = cursor.execute("""SELECT * FROM logout ORDER BY ID DESC LIMIT 50""")
            for row_number_log, order in enumerate(users):
                form.tableWidget.insertRow(row_number_log)
                for column_number, data in enumerate(order):
                    cell = QtWidgets.QTableWidgetItem(str(data))
                    form.tableWidget.setItem(row_number_log, column_number, cell)
                    cell.setTextAlignment(Qt.AlignCenter)
            form.tableWidget.horizontalHeader().setSectionResizeMode(0,
                                                                     QtWidgets.QHeaderView.ResizeToContents)
            form.tableWidget.horizontalHeader().setSectionResizeMode(1,
                                                                     QtWidgets.QHeaderView.Stretch)
            form.tableWidget.horizontalHeader().setSectionResizeMode(2,
                                                                     QtWidgets.QHeaderView.Stretch)
        load_data()
        app.exec()
    else:
        Form, App = uic.loadUiType("dont.ui")
        app = QtWidgets.QDialog()
        form = Form()
        form.setupUi(app)
        app.show()
        def ok():
            app.close()
        form.pushButton.clicked.connect(ok)
        app.exec()
form.pushButton_6.clicked.connect(log_out)

######### load_data ##############
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

sqlite_connection.commit()
form.pushButton_73.clicked.connect(myClose)
form.pushButton_74.clicked.connect(myMinimize)
##########reload#################
form.pushButton_11.clicked.connect(road_to)
print("--- %s seconds ---" % (time.time() - start_time))
sys.exit(app.exec_())

####################     start_time = time.time(); print("--- %s seconds ---" % (time.time() - start_time))