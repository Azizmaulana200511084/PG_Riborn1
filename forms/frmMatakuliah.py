import sys
from PyQt5 import QtWidgets, uic
import psycopg2 as mc
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox
from classes.Matakuliah import Matakuliah

qtcreator_file  = "ui/matakuliah.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)


class MatakuliahWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Event Setup
        self.btnCari.clicked.connect(self.search_data) # Jika tombol cari diklik
        self.btnSimpan.clicked.connect(self.save_data) # Jika tombol simpan diklik
        self.txtKodeMK.returnPressed.connect(self.search_data) # Jika menekan tombol Enter saat berada di textbox NIM
        self.btnClear.clicked.connect(self.clear_entry)
        self.btnHapus.clicked.connect(self.delete_data)
        self.edit_mode=""   
        self.btnHapus.setEnabled(False) # Matikan tombol hapus
        self.btnHapus.setStyleSheet("color:black;background-color : grey")

    def select_data(self):
        try:
            mk = Matakuliah()

            # Get all 
            result = mk.getAllData()

            self.gridMatakuliah.setHorizontalHeaderLabels(['ID', 'KodeMK', 'NamaMK', 'SKS'])
            self.gridMatakuliah.setRowCount(0)
            

            for row_number, row_data in enumerate(result):
                #print(row_number)
                self.gridMatakuliah.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    #print(column_number)
                    self.gridMatakuliah.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def search_data(self):
        try:           
            kdmk=self.txtKodeMK.text()           
            mk = Matakuliah()

            # search process
            result = mk.getByKODEMK(kdmk)
            a = mk.affected
            if(a>0):
                self.txtNamaMK.setText(result[2])
                self.txtSKS.setText(str(result[3]))
                self.btnSimpan.setText("Update")
                self.edit_mode=True
                self.btnHapus.setEnabled(True) # Aktifkan tombol hapus
                self.btnHapus.setStyleSheet("background-color : red")
            else:
                self.messagebox("INFO", "Data tidak ditemukan")
                self.txtNamaMK.setFocus()
                self.btnSimpan.setText("Simpan")
                self.edit_mode=False
                self.btnHapus.setEnabled(False) # Matikan tombol hapus
                self.btnHapus.setStyleSheet("color:black;background-color : grey")
            
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def save_data(self, MainWindow):
        try:
            mk = Matakuliah()
            kdmk=self.txtKodeMK.text()
            namamk=self.txtNamaMK.text()
            sks=self.txtSKS.text()
            self.messagebox("SUKSES", "Edit Mode is " + str(self.edit_mode))
            if(self.edit_mode==False):   
                mk.kodemk = kdmk
                mk.namamk = namamk
                mk.sks = sks
                
                a = mk.simpan()
                if(a>0):
                    self.messagebox("SUKSES", "Data Matakuliah Tersimpan")
                else:
                    self.messagebox("GAGAL", "Data Matakuliah Gagal Tersimpan")
                
                self.clear_entry(self) # Clear Entry Form
                self.select_data() # Reload Datagrid
            elif(self.edit_mode==True):
                mk.kodemk=kdmk
                mk.namamk=namamk
                mk.sks = sks                
                a = mk.updateByKODEMK(kdmk)
                if(a>0):
                    self.messagebox("SUKSES", "Data Matakuliah Diperbarui")
                else:
                    self.messagebox("GAGAL", "Data Matakuliah Gagal Diperbarui")
                
                self.clear_entry(self) # Clear Entry Form
                self.select_data() # Reload Datagrid
            else:
                self.messagebox("ERROR", "Terjadi kesalahan Mode Edit")
            

        except mc.Error as e:
            self.messagebox("ERROR", str(e))

    def delete_data(self, MainWindow):
        try:
            mk = Matakuliah()
            kodemk=self.txtKodeMK.text()
                       
            if(self.edit_mode==True):
                a = mk.deleteByKODEMK(kodemk)
                if(a>0):
                    self.messagebox("SUKSES", "Data Matakuliah Dihapus")
                else:
                    self.messagebox("GAGAL", "Data Matakuliah Gagal Dihapus")
                
                self.clear_entry(self) # Clear Entry Form
                self.select_data() # Reload Datagrid
            else:
                self.messagebox("ERROR", "Sebelum meghapus data harus ditemukan dulu")
            

        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def clear_entry(self, MainWindow):
        self.txtKodeMK.setText("")
        self.txtNamaMK.setText("")
        self.txtSKS.setText("")
        self.btnHapus.setEnabled(False) # Matikan tombol hapus
        self.btnHapus.setStyleSheet("color:black;background-color : grey")

    def messagebox(self, title, message):
        mess = QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QMessageBox.Ok)
        mess.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MatakuliahWindow()
    window.show()
    window.select_data()
    sys.exit(app.exec_())
else:
    app = QtWidgets.QApplication(sys.argv)
    window = MatakuliahWindow()