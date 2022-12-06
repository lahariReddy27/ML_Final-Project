import sys
from oparams import *
from PyQt5 import QtWidgets, QtGui, QtCore

import sqlite3
con = sqlite3.connect('hppr1')

class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton.clicked.connect(self.insertvalues)

  

  def insertvalues(self):
         
     with con:
    
        cur = con.cursor()
        pid = str(self.ui.lineEdit_3.text())
        zip1 = str(self.ui.lineEdit_4.text())
        lat = str(self.ui.lineEdit_5.text())
        long1 = str(self.ui.lineEdit_6.text())
        slivext = str(self.ui.lineEdit.text())
        slotext = str(self.ui.lineEdit_2.text())	
        cur.execute('INSERT INTO opara VALUES(?,?,?,?,?,?)',([pid,zip1,lat,long1,slivext,slotext]))
        con.commit()
        
if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
