from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from forms.frmMahasiswa import MahasiswaWindow
from forms.frmMatakuliah import MatakuliahWindow
dock = QtWidgets.QDockWidget()
def child_panels(self):   
    matakuliah_panel(self)
    mahasiswa_panel(self)

def mahasiswa_panel(self):     
    mahasiswa_widget = MahasiswaWindow()
    mahasiswa_widget.select_data()
    self.centralwidget = mahasiswa_widget
    self.centralwidget.setObjectName("centralwidget")
    self.widget = QtWidgets.QWidget(self.centralwidget)
        

def matakuliah_panel(self):
    matakuliah_widget = MatakuliahWindow()
    matakuliah_widget.select_data()
    self.centralwidget = matakuliah_widget
    self.centralwidget.setObjectName("centralwidget")
    self.widget = QtWidgets.QWidget(self.centralwidget)

def mahasiswa_on(self):
    mahasiswa_widget = MahasiswaWindow()
    mahasiswa_widget.select_data()
    self.centralwidget = mahasiswa_widget
    dock.setWidget(self.centralwidget)
    self.addDockWidget(Qt.LeftDockWidgetArea, dock)
    self.centralWidget()

def matakuliah_on(self):
    matakuliah_widget = MatakuliahWindow()
    matakuliah_widget.select_data()
    self.centralwidget = matakuliah_widget
    dock.setWidget(self.centralwidget)
    self.addDockWidget(Qt.LeftDockWidgetArea, dock)
    self.centralWidget()




        
     