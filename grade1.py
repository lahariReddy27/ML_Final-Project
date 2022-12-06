import sys
from grade import *
from PyQt5 import QtWidgets, QtGui, QtCore

import sqlite3
con = sqlite3.connect('hppr1')

#import MySQLdb as mdb
#con = mdb.connect('localhost', 'team1', 'test623', 'hppr1'); 

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
        grade = str(self.ui.lineEdit_4.text())
        sftb = str(self.ui.lineEdit_5.text())
        sfta = str(self.ui.lineEdit_6.text())
        yrblt = str(self.ui.lineEdit.text())
        yrrmdl = str(self.ui.lineEdit_2.text())	
        cur.execute('INSERT INTO grade VALUES(?,?,?,?,?,?)',([pid,grade,sftb,sfta,yrblt,yrrmdl]))
        con.commit()
        
if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
