import datetime
import time
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QAbstractItemView, QDialog
import sqlite3
from plus_del import Plus_del

sqlite_connection_02 = sqlite3.connect("setting.db")
cursor_02 = sqlite_connection_02.cursor()
sqlite_connection_01 = sqlite3.connect("id.db")
cursor_01 = sqlite_connection_01.cursor()
today = datetime.datetime.today()

class LokoDetalis(QtWidgets.QTableWidget):
    def __init__(self, parent=None):
        QtWidgets.QTableWidget.__init__(self, parent)

    def mousePressEvent(self, e):
        it = self.itemAt(e.pos())
        try:
            if e.button() == Qt.RightButton:
                levels = cursor_01.execute(
                    f"""SELECT levels FROM autorization WHERE online='True'""").fetchone()
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
                                inventar = (it.tableWidget().item(it.row(), 4)).text()
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
                                    (it.tableWidget().item(it.row(), 4)).setText(str(int(0) + int(let)))
                                else:
                                    (it.tableWidget().item(it.row(), 4)).setText(str(int(let)))
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
                                plus = (it.tableWidget().item(it.row(), 4)).text()
                                if plus == "":
                                    (it.tableWidget().item(it.row(), 4)).setText(str(int(0) + int(let)))
                                else:
                                    (it.tableWidget().item(it.row(), 4)).setText(str(int(plus) + int(let)))
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
                                minus = (it.tableWidget().item(it.row(), 4)).text()
                                (it.tableWidget().item(it.row(), 4)).setText(str(int(minus) - int(let)))
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
                            QtWidgets.QFileDialog.getOpenFileName(self, "Выбор фотки детали", None,
                                                                  "Image (*.png *.jpg *.jpeg)")[0]
                        apps.close()
                        if wb_patch:
                            foto = wb_patch.split('База данных ЖД/')[1]
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
            QtWidgets.QTableWidget.mousePressEvent(self, e)
        except:
            pass


class Ui_Loko(object):
    def setupUi(self, Loko):
        Loko.setObjectName("Loko")
        Loko.resize(1317, 718)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("train.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Loko.setWindowIcon(icon)
        Loko.setStyleSheet("")
        self.tableWidget = LokoDetalis(Loko)
        self.tableWidget.setGeometry(QtCore.QRect(30, 30, 1251, 651))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("QTableWidget {\n"
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
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(166)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.label = QtWidgets.QLabel(Loko)
        self.label.setGeometry(QtCore.QRect(-6, -5, 1341, 731))
        self.label.setStyleSheet("background-color: rgb(50, 50, 50);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Loko)
        self.label_2.setGeometry(QtCore.QRect(30, 10, 501, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(106, 248, 255);")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(Loko)
        self.label_4.setGeometry(QtCore.QRect(19, 21, 55, 41))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("sql_maket/4.png"))
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(Loko)
        self.label_6.setGeometry(QtCore.QRect(22, 669, 31, 21))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("sql_maket/1.png"))
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(Loko)
        self.label_5.setGeometry(QtCore.QRect(1250, 18, 41, 41))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("sql_maket/3.png"))
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(Loko)
        self.label_7.setGeometry(QtCore.QRect(1253, 649, 55, 41))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("sql_maket/2.png"))
        self.label_7.setObjectName("label_7")
        self.label.raise_()
        self.tableWidget.raise_()
        self.label_4.raise_()
        self.label_6.raise_()
        self.label_5.raise_()
        self.label_7.raise_()
        self.label_2.raise_()
        self.retranslateUi(Loko)
        QtCore.QMetaObject.connectSlotsByName(Loko)

    def retranslateUi(self, Loko):
        _translate = QtCore.QCoreApplication.translate
        Loko.setWindowTitle(_translate("Loko", "Detal_loko"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Loko", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Loko", "Фото"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Loko", "Артикул"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Loko", "Тип детали"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Loko", "Количество"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Loko", "Детали"))
        self.label_2.setText(_translate("Loko", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Loko = QtWidgets.QWidget()
    ui = Ui_Loko()
    ui.setupUi(Loko)
    Loko.show()
    sys.exit(app.exec_())
