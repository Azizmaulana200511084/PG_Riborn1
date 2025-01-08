from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from forms.frmMahasiswa import MahasiswaWindow

def mahasiswa_panel(self):
        dock = QtWidgets.QDockWidget(self)
        mahasiswa_widget = MahasiswaWindow()
        mahasiswa_widget.select_data()
        self.centralwidget = mahasiswa_widget
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)

        dock.setWidget(self.centralwidget)
        self.addDockWidget(Qt.LeftDockWidgetArea, dock)
        self.centralWidget()
        