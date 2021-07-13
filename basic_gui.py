from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def b1_OnClick():
    print("Hello World")

def window():
    app = QApplication(sys.argv)             #configuration setup
    win = QMainWindow()                      #specify a gui window
    win.setGeometry(200,200,300,300)         #coordinates of the window 
    win.setWindowTitle("HEllo World")        

    #your GUI Program starts from here
    
    #creating a label
    label = QtWidgets.QLabel(win)
    label.setText("My first Label")
    label.move(50,20)

    #creating a button
    b1 = QtWidgets.QPushButton(win)
    b1.setText("Click Me")
    b1.move(50,50)
    b1.clicked.connect(b1_OnClick)
    
    win.show()
    sys.exit(app.exec_())

window()
