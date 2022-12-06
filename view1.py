import sys
from view import *
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
        sftl = str(self.ui.lineEdit_4.text())
        floors = str(self.ui.lineEdit_5.text())
        wfrnt = str(self.ui.lineEdit_6.text())
        views = str(self.ui.lineEdit.text())
        condn = str(self.ui.lineEdit_2.text())	
        cur.execute('INSERT INTO view1 VALUES(?,?,?,?,?,?)',([pid,sftl,floors,wfrnt,views,condn]))
        con.commit()
        
if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
