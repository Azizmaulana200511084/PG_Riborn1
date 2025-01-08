from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from forms.frmMatakuliah import MatakuliahWindow

def matakuliah_panel(self):
        dock = QtWidgets.QDockWidget(self)
        matakuliah_widget = MatakuliahWindow()
        matakuliah_widget.select_data()
        self.centralwidget = matakuliah_widget
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)

        dock.setWidget(self.centralwidget)
        self.addDockWidget(Qt.LeftDockWidgetArea, dock)
        self.centralWidget()
        