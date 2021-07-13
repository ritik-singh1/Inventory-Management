from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox
from PyQt5.uic import loadUi
import pyodbc
import sys
from window_2 import Ui_StoreMainPage

conn = pyodbc.connect('DRIVER={SQL SERVER};SERVER=LAPTOP-F8010458\SQLEXPRESS;DATABASE=warehouse;Trusted_connection=yes')
class Login(QMainWindow):
    def __init__(self):
        super(Login, self).__init__()
        loadUi("login.ui",self)
        self.label_4.adjustSize()
        self.label_3.adjustSize()
        self.CreateAccountButton.adjustSize()
        self.LoginButton.clicked.connect(self.loginfunction)
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.CreateAccountButton.clicked.connect(self.goto_create)

    def loginfunction(self):
        email = self.Email.text()
        password = self.Password.text()
        cursor = conn.cursor()
        cursor.execute('select Name, Email, Password, PhoneNo from login_details')
        connection = 0
        name = ''
        phone = ''
        count = 0
        for i in cursor:
            if i[1] == email and i[2] == password:
                connection = 1
                name = i[0]
                phone = i[3]
                break
        if connection == 0:
            QMessageBox.warning(self, "Alert", "Account does not exisit!")
        else:
            self.window = QtWidgets.QMainWindow()
            self.message1 = name
            self.message2 = phone
            self.ui = Ui_StoreMainPage(self.message1, self.message2)
            self.ui.setupUi(self.window)
            self.window.show()
            widget.close()
            
    def goto_create(self):
        create = CreateAccount()
        widget.addWidget(create)
        widget.setCurrentIndex(widget.currentIndex() + 1)
            

class CreateAccount(QMainWindow):
    def __init__(self):
        super(CreateAccount, self).__init__()
        loadUi("createaccount.ui", self)
        self.label_6.adjustSize()
        self.CreateButton.adjustSize()  
        self.CreateButton.clicked.connect(self.acc)
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ConfirmPassword.setEchoMode(QtWidgets.QLineEdit.Password)

    def acc(self):
        name = self.Name.text()
        email = self.Email.text()
        P_no = self.Phone.text()
        if self.Password.text() == self.ConfirmPassword.text():
            password = self.Password.text()
            cursor = conn.cursor()
            cursor.execute('insert into login_details values(?,?,?,?)',(name, email, password, P_no))
            conn.commit()
            QMessageBox.about(self, "Confirm", "Account Successfully Created.")
            login = Login()
            widget.addWidget(login)
            widget.setCurrentIndex(widget.currentIndex() + 1)
            
            


    
app = QApplication(sys.argv)
win = Login()
widget = QtWidgets.QStackedWidget()
widget.addWidget(win)
widget.setGeometry(500,250,700,700)
widget.setWindowTitle("WareHouse")
widget.show()
sys.exit(app.exec_())
                
