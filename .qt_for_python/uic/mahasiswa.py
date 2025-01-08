# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mahasiswa.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(579, 508)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(220, 20, 151, 16))
        font = QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 80, 47, 13))
        self.txtNIM = QLineEdit(self.centralwidget)
        self.txtNIM.setObjectName(u"txtNIM")
        self.txtNIM.setGeometry(QRect(160, 80, 141, 20))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(60, 110, 91, 16))
        self.txtNama = QLineEdit(self.centralwidget)
        self.txtNama.setObjectName(u"txtNama")
        self.txtNama.setGeometry(QRect(160, 110, 291, 20))
        self.optLaki = QRadioButton(self.centralwidget)
        self.optLaki.setObjectName(u"optLaki")
        self.optLaki.setGeometry(QRect(160, 150, 82, 17))
        self.optPerempuan = QRadioButton(self.centralwidget)
        self.optPerempuan.setObjectName(u"optPerempuan")
        self.optPerempuan.setGeometry(QRect(160, 180, 82, 17))
        self.cboProdi = QComboBox(self.centralwidget)
        self.cboProdi.addItem("")
        self.cboProdi.addItem("")
        self.cboProdi.addItem("")
        self.cboProdi.addItem("")
        self.cboProdi.setObjectName(u"cboProdi")
        self.cboProdi.setGeometry(QRect(160, 210, 141, 22))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(60, 150, 81, 16))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(60, 210, 81, 16))
        self.btnSimpan = QPushButton(self.centralwidget)
        self.btnSimpan.setObjectName(u"btnSimpan")
        self.btnSimpan.setGeometry(QRect(160, 250, 75, 23))
        self.btnSimpan.setStyleSheet(u"#btnSimpan{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 255);\n"
"}")
        self.gridMahasiswa = QTableWidget(self.centralwidget)
        if (self.gridMahasiswa.columnCount() < 5):
            self.gridMahasiswa.setColumnCount(5)
        if (self.gridMahasiswa.rowCount() < 10):
            self.gridMahasiswa.setRowCount(10)
        self.gridMahasiswa.setObjectName(u"gridMahasiswa")
        self.gridMahasiswa.setGeometry(QRect(20, 290, 541, 192))
        self.gridMahasiswa.setRowCount(10)
        self.gridMahasiswa.setColumnCount(5)
        self.btnCari = QPushButton(self.centralwidget)
        self.btnCari.setObjectName(u"btnCari")
        self.btnCari.setGeometry(QRect(310, 80, 41, 23))
        self.btnClear = QPushButton(self.centralwidget)
        self.btnClear.setObjectName(u"btnClear")
        self.btnClear.setGeometry(QRect(240, 250, 75, 23))
        self.btnClear.setStyleSheet(u"#btnClear{\n"
"	background-color: rgb(0, 255, 0);\n"
"}")
        self.btnHapus = QPushButton(self.centralwidget)
        self.btnHapus.setObjectName(u"btnHapus")
        self.btnHapus.setGeometry(QRect(320, 250, 75, 23))
        self.btnHapus.setStyleSheet(u"#btnHapus{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(255, 0, 0);\n"
"}\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Data Mahasiswa", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"NIM", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Nama Lengkap", None))
        self.optLaki.setText(QCoreApplication.translate("MainWindow", u"Laki-laki", None))
        self.optPerempuan.setText(QCoreApplication.translate("MainWindow", u"Perempuan", None))
        self.cboProdi.setItemText(0, "")
        self.cboProdi.setItemText(1, QCoreApplication.translate("MainWindow", u"IND", None))
        self.cboProdi.setItemText(2, QCoreApplication.translate("MainWindow", u"TIF", None))
        self.cboProdi.setItemText(3, QCoreApplication.translate("MainWindow", u"PET", None))

        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Jenis Kelamin", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Program Studi", None))
        self.btnSimpan.setText(QCoreApplication.translate("MainWindow", u"Simpan", None))
        self.btnCari.setText(QCoreApplication.translate("MainWindow", u"cari", None))
        self.btnClear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.btnHapus.setText(QCoreApplication.translate("MainWindow", u"Hapus", None))
    # retranslateUi

