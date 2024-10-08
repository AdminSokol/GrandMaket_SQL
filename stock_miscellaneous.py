import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets


sqlite_connection_02 = sqlite3.connect("setting.db")
cursor_02 = sqlite_connection_02.cursor()
sqlite_connection_01 = sqlite3.connect("id.db")
cursor_01 = sqlite_connection_01.cursor()

try:
    username = cursor_01.execute(f"""SELECT login FROM autorization WHERE online='True'""").fetchone()
    value = cursor_02.execute(
            f"""SELECT font,title_font,color_table,color_table_selection,width_loko,width_detal,width_masters,image_size, rgb, rgb_selection, width_stok FROM setting WHERE user='{username[0]}'""").fetchone()
except:
    pass
class Stock(object):
    def __init__(self):
        self.Forms = QtWidgets.QDialog()

    def setupUi(self, Forms):
        Forms.setObjectName("Forms")
        Forms.resize(749, 696)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("sql_maket/train.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Forms.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Forms)
        self.label.setGeometry(QtCore.QRect(518, 20, 201, 91))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("sql_maket/1loko.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Forms)
        self.label_2.setGeometry(QtCore.QRect(519, 120, 211, 91))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("sql_maket/2loko.png"))
        self.label_2.setObjectName("label_2")
        self.tableWidget_20 = QtWidgets.QTableWidget(Forms)
        self.tableWidget_20.setGeometry(QtCore.QRect(529, 127, 181, 71))
        self.tableWidget_20.setStyleSheet("QTableWidget {\n"
"background-color: rgb(255, 157, 0)}\n"
"\n"
"QHeaderView::section {\n"
"    background-color:  rgb(255, 255, 255);\n"
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
        self.tableWidget_20.setRowCount(0)
        self.tableWidget_20.setObjectName("tableWidget_20")
        self.tableWidget_20.setColumnCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_20.setHorizontalHeaderItem(0, item)
        self.tableWidget_20.horizontalHeader().setVisible(True)
        self.tableWidget_20.horizontalHeader().setDefaultSectionSize(180)
        self.tableWidget_20.horizontalHeader().setHighlightSections(False)
        self.tableWidget_20.verticalHeader().setVisible(False)
        self.tableWidget_20.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_20.verticalHeader().setHighlightSections(True)
        self.tableWidget_30 = QtWidgets.QTableWidget(Forms)
        self.tableWidget_30.setGeometry(QtCore.QRect(529, 27, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tableWidget_30.setFont(font)
        self.tableWidget_30.setStyleSheet("QTableWidget {\n"
"background-color: rgb(16, 0, 255)}\n"
"\n"
"QHeaderView::section {\n"
"    background-color:  rgb(255, 255, 255);\n"
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
        self.tableWidget_30.setRowCount(0)
        self.tableWidget_30.setObjectName("tableWidget_30")
        self.tableWidget_30.setColumnCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_30.setHorizontalHeaderItem(0, item)
        self.tableWidget_30.horizontalHeader().setVisible(True)
        self.tableWidget_30.horizontalHeader().setDefaultSectionSize(180)
        self.tableWidget_30.horizontalHeader().setHighlightSections(False)
        self.tableWidget_30.verticalHeader().setVisible(False)
        self.label_3 = QtWidgets.QLabel(Forms)
        self.label_3.setGeometry(QtCore.QRect(-10, 0, 811, 711))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("sql_maket/lokos.png"))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Forms)
        self.label_4.setGeometry(QtCore.QRect(19, 12, 55, 41))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("sql_maket/4.png"))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Forms)
        self.label_5.setGeometry(QtCore.QRect(460, 8, 41, 41))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("sql_maket/3.png"))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Forms)
        self.label_6.setGeometry(QtCore.QRect(22, 650, 31, 21))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("sql_maket/1.png"))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Forms)
        self.label_7.setGeometry(QtCore.QRect(463, 630, 55, 41))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("sql_maket/2.png"))
        self.label_7.setObjectName("label_7")
        self.lineEdit = QtWidgets.QLineEdit(Forms)
        self.lineEdit.setGeometry(QtCore.QRect(529, 67, 181, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Forms)
        self.lineEdit_2.setGeometry(QtCore.QRect(529, 166, 180, 33))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_minus = QtWidgets.QPushButton(Forms)
        self.pushButton_minus.setGeometry(QtCore.QRect(510, 620, 111, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_minus.sizePolicy().hasHeightForWidth())
        self.pushButton_minus.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
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
        self.label_kol = QtWidgets.QLabel(Forms)
        self.label_kol.setGeometry(QtCore.QRect(520, 230, 321, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_kol.setFont(font)
        self.label_kol.setStyleSheet("QLabel {\n"
"    color: rgb(255, 255, 255);}")
        self.label_kol.setObjectName("label_kol")
        self.tableWidget = QtWidgets.QTableWidget(Forms)
        self.tableWidget.setGeometry(QtCore.QRect(30, 20, 461, 641))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
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
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(140)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.label_3.raise_()
        self.tableWidget_30.raise_()
        self.lineEdit.raise_()
        self.label.raise_()
        self.tableWidget_20.raise_()
        self.lineEdit_2.raise_()
        self.label_2.raise_()
        self.pushButton_minus.raise_()
        self.label_kol.raise_()
        self.tableWidget.raise_()
        self.label_5.raise_()
        self.label_7.raise_()
        self.label_6.raise_()
        self.label_4.raise_()

        self.retranslateUi(Forms)
        QtCore.QMetaObject.connectSlotsByName(Forms)

    def retranslateUi(self, Forms):
        _translate = QtCore.QCoreApplication.translate
        Forms.setWindowTitle(_translate("Forms", "Локо"))
        item = self.tableWidget_20.horizontalHeaderItem(0)
        item.setText(_translate("Forms", "Наименование"))
        item = self.tableWidget_30.horizontalHeaderItem(0)
        item.setText(_translate("Forms", "Артикул"))
        self.pushButton_minus.setText(_translate("Forms", "-"))
        self.label_kol.setText(_translate("Forms", "Количество записей:"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Forms", "Мастер"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Forms", "Добавил/убрал"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Forms", "Дата и время"))
