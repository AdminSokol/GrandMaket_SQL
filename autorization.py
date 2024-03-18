import base64
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QAbstractItemView

sqlite_connection_02 = sqlite3.connect("setting.db")
cursor_02 = sqlite_connection_02.cursor()
sqlite_connection = sqlite3.connect("id.db")
cursor = sqlite_connection.cursor()

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
                        cursor.execute(f"""DELETE FROM autorization WHERE ID='{iter}'""")
                        sqlite_connection.commit()
                        it.tableWidget().setRowCount(0)
                        users = cursor.execute("SELECT * FROM autorization")
                        for row_number, order in enumerate(users):
                            rama.insertRow(row_number)
                            for column_number, data in enumerate(order):
                                cell = QtWidgets.QTableWidgetItem(str(data))
                                rama.setItem(row_number, column_number, cell)
                                cell.setTextAlignment(Qt.AlignCenter)
                        cursor_02.execute(f"""DELETE FROM setting WHERE ID='{iter}'""")
                        sqlite_connection_02.commit()
        except:
            pass
        QtWidgets.QTableWidget.mousePressEvent(self, e)

class Autorization(object):
    def setupUi(self, Form):
        username = cursor.execute(f"""SELECT login FROM autorization WHERE online='True'""").fetchone()
        value = cursor_02.execute(
            f"""SELECT font,title_font,color_table,color_table_selection,width_loko,width_detal,width_masters,image_size, rgb, rgb_selection, width_stok FROM setting WHERE user='{username[0]}'""").fetchone()
        Form.setObjectName("Form")
        Form.resize(990, 571)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("train.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("")
        self.pushButton_plus = QtWidgets.QPushButton(Form)
        self.pushButton_plus.setGeometry(QtCore.QRect(890, 400, 71, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_plus.sizePolicy().hasHeightForWidth())
        self.pushButton_plus.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton_plus.setFont(font)
        self.pushButton_plus.setStyleSheet("QPushButton {\n"
"    background-color: rgb(134, 140, 140);\n"
"    border-radius: 5px;\n"
"    color: rgb(97, 255, 107);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(122, 122, 122);\n"
"    color: rgb(97, 255, 107)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(134, 140, 140);}")
        self.pushButton_plus.setCheckable(False)
        self.pushButton_plus.setAutoRepeat(False)
        self.pushButton_plus.setAutoExclusive(False)
        self.pushButton_plus.setObjectName("pushButton_plus")
        self.pushButton_minus = QtWidgets.QPushButton(Form)
        self.pushButton_minus.setGeometry(QtCore.QRect(890, 350, 71, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_minus.sizePolicy().hasHeightForWidth())
        self.pushButton_minus.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setUnderline(False)
        font.setStrikeOut(True)
        self.pushButton_minus.setFont(font)
        self.pushButton_minus.setStyleSheet("QPushButton {\n"
"    background-color: rgb(134, 140, 140);\n"
"    border-radius: 5px;\n"
"    color: rgb(222, 6, 10);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(122, 122, 122);\n"
"    color: rgb(222, 6, 10)}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(134, 140, 140);}")
        self.pushButton_minus.setObjectName("pushButton_minus")
        self.pushButton_save = QtWidgets.QPushButton(Form)
        self.pushButton_save.setGeometry(QtCore.QRect(890, 30, 71, 41))
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("sql_maket/save.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_save.setIcon(icon1)
        self.pushButton_save.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_save.setCheckable(True)
        self.pushButton_save.setChecked(True)
        self.pushButton_save.setAutoDefault(False)
        self.pushButton_save.setDefault(False)
        self.pushButton_save.setFlat(False)
        self.pushButton_save.setObjectName("pushButton_save")
        self.tableWidget = Test(Form)
        self.tableWidget.setGeometry(QtCore.QRect(30, 30, 831, 411))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(value[0])
        self.tableWidget.setFont(font)
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
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(166)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(-6, -5, 1001, 601))
        self.label.setStyleSheet("background-color: rgb(50, 50, 50);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(30, 450, 931, 111))
        self.textBrowser.setStyleSheet("background-color: rgb(50, 50, 50);")
        self.textBrowser.setObjectName("textBrowser")
        self.label_19 = QtWidgets.QLabel(Form)
        self.label_19.setGeometry(QtCore.QRect(19, 17, 31, 31))
        self.label_19.setText("")
        self.label_19.setPixmap(QtGui.QPixmap("sql_maket/04.png"))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(Form)
        self.label_20.setGeometry(QtCore.QRect(20, 425, 31, 31))
        self.label_20.setText("")
        self.label_20.setPixmap(QtGui.QPixmap("sql_maket/01.png"))
        self.label_20.setObjectName("label_20")
        self.label_23 = QtWidgets.QLabel(Form)
        self.label_23.setGeometry(QtCore.QRect(847, 17, 31, 31))
        self.label_23.setText("")
        self.label_23.setPixmap(QtGui.QPixmap("sql_maket/03.png"))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(Form)
        self.label_24.setGeometry(QtCore.QRect(851, 426, 21, 31))
        self.label_24.setText("")
        self.label_24.setPixmap(QtGui.QPixmap("sql_maket/02.png"))
        self.label_24.setObjectName("label_24")
        self.label.raise_()
        self.tableWidget.raise_()
        self.pushButton_save.raise_()
        self.pushButton_minus.raise_()
        self.pushButton_plus.raise_()
        self.label_19.raise_()
        self.label_20.raise_()
        self.label_23.raise_()
        self.label_24.raise_()
        self.textBrowser.raise_()
        def load_data():
            global row_number_auto
            users = cursor.execute("SELECT * FROM autorization")
            for row_number_auto, order in enumerate(users):
                self.tableWidget.insertRow(row_number_auto)
                for column_number, data in enumerate(order):
                    if column_number == 2:
                        data = base64.b64decode(str(data))
                        cell = QtWidgets.QTableWidgetItem(data.decode())
                        self.tableWidget.setItem(row_number_auto, column_number, cell)
                        cell.setTextAlignment(Qt.AlignCenter)
                    else:
                        cell = QtWidgets.QTableWidgetItem(str(data))
                        self.tableWidget.setItem(row_number_auto, column_number, cell)
                        cell.setTextAlignment(Qt.AlignCenter)
            self.tableWidget.horizontalHeader().setSectionResizeMode(0,
                                                                     QtWidgets.QHeaderView.ResizeToContents)
            self.tableWidget.horizontalHeader().setSectionResizeMode(1,
                                                                     QtWidgets.QHeaderView.Stretch)
            self.tableWidget.horizontalHeader().setSectionResizeMode(2,
                                                                     QtWidgets.QHeaderView.Stretch)
            self.tableWidget.horizontalHeader().setSectionResizeMode(3,
                                                                     QtWidgets.QHeaderView.ResizeToContents)
            try:
                self.tableWidget.scrollToItem(self.tableWidget.item(row_number_auto, 0),
                                                QAbstractItemView.PositionAtTop)
                self.tableWidget.selectRow(row_number_auto)
                self.tableWidget.clearSelection()
            except:
                pass
        def plus():
            self.tableWidget.setRowCount(0)
            cursor.execute("""INSERT INTO autorization VALUES (NULL,'','','','False')""")
            sqlite_connection.commit()
            load_data()
            cursor_02.execute("""INSERT INTO setting VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                              [None, '', 11, 11, 'Голубой', 'Белый', 1311, 1321, 1030, 75,
                               'rgb(255, 255, 255)', 'rgb(170, 255, 255)', 1030])
            sqlite_connection_02.commit()
        def minus():
            self.tableWidget.setRowCount(0)
            cursor.execute("""DELETE FROM autorization WHERE login=''""")
            sqlite_connection.commit()
            load_data()
            cursor_02.execute(f"""DELETE FROM setting WHERE login=''""")
            sqlite_connection_02.commit()
        def save():
            try:
                global row_number_auto
                for i in range(int(row_number_auto) + 1):
                    ID = self.tableWidget.item(i, 0).text()
                    login = self.tableWidget.item(i, 1).text()
                    password = base64.b64encode((self.tableWidget.item(i, 2).text()).encode('utf-8'))
                    password = password.decode()
                    levels = self.tableWidget.item(i, 3).text()
                    cursor.execute(
                        f"""UPDATE autorization SET login='{login}',password='{password}',levels='{levels}' WHERE ID='{ID}'""")
                    cursor_02.execute(
                        f"""UPDATE setting SET user='{login}' WHERE ID='{ID}'""")
                sqlite_connection.commit()
                sqlite_connection_02.commit()
            except:
                pass
        load_data()
        self.pushButton_save.clicked.connect(save)
        self.pushButton_plus.clicked.connect(plus)
        self.pushButton_minus.clicked.connect(minus)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "autorization"))
        self.pushButton_plus.setText(_translate("Form", "+"))
        self.pushButton_minus.setText(_translate("Form", "-"))
        self.pushButton_save.setText(_translate("Form", "💾"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Login"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Password"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Доступ"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.15094pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#0000ff;\">Уровни доступа:</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">Третий</span><span style=\" font-size:7.8pt;\"> </span><span style=\" font-size:12pt; color:#ffffff;\">-</span><span style=\" font-size:7.8pt; color:#ffffff;\"> </span><span style=\" font-size:12pt; color:#ffffff;\">дает доступ ко всем функциям и вкладкам.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#29b61f;\">Второй</span><span style=\" font-size:12pt;\"> </span><span style=\" font-size:12pt; color:#ffffff;\">- дает доступ ко всем функциям и вкладкам, кроме доступа к вкладке &quot;Авторизации&quot;.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ffbf1d;\">Первый</span><span style=\" font-size:12pt;\"> </span><span style=\" font-size:12pt; color:#ffffff;\">- имеет ограниченный арсенал функций и доступ к вкладкам.</span></p></body></html>"))



