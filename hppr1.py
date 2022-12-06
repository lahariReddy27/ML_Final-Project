import sys
import os
from hppr import *
from PyQt5 import QtWidgets, QtGui, QtCore

class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton.clicked.connect(self.view)
     self.ui.pushButton_2.clicked.connect(self.params)
     self.ui.pushButton_3.clicked.connect(self.grade)
     self.ui.pushButton_4.clicked.connect(self.graphs)
     self.ui.pushButton_5.clicked.connect(self.basic)
     self.ui.pushButton_6.clicked.connect(self.gnba)
     self.ui.pushButton_7.clicked.connect(self.dtca)
     self.ui.pushButton_8.clicked.connect(self.logregr)
     self.ui.pushButton_9.clicked.connect(self.bagg)
       

  def basic(self):
    os.system("python basics1.py")

  def view(self):
    os.system("python view1.py")

  def params(self):
    os.system("python oparams1.py")

  def grade(self):
    os.system("python grade1.py")

  def gnba(self):
    os.system("python gnb1.py")

  def graphs(self):
    os.system("python grph1.py")

  def dtca(self):
    os.system("python dtc1.py")

  def logregr(self):
    os.system("python -W ignore logregr1.py")
	
  def bagg(self):
    os.system("python bagregr1.py")
       
if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())

