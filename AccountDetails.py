# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AccountDetails.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_AccountsMainWindow(object):
    def setupUi(self, AccountsMainWindow):
        AccountsMainWindow.setObjectName("AccountsMainWindow")
        AccountsMainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(AccountsMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 50, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(28)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(210, 180, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(430, 180, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(210, 260, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(430, 260, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(210, 350, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(430, 350, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(450, 470, 121, 31))
        self.pushButton.setObjectName("pushButton")
        AccountsMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AccountsMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        AccountsMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AccountsMainWindow)
        self.statusbar.setObjectName("statusbar")
        AccountsMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AccountsMainWindow)
        QtCore.QMetaObject.connectSlotsByName(AccountsMainWindow)

    def retranslateUi(self, AccountsMainWindow):
        _translate = QtCore.QCoreApplication.translate
        AccountsMainWindow.setWindowTitle(_translate("AccountsMainWindow", "Account Details"))
        self.label.setText(_translate("AccountsMainWindow", "Account Details"))
        self.label.adjustSize()
            
        self.label_2.setText(_translate("AccountsMainWindow", "Name"))
        self.label_3.setText(_translate("AccountsMainWindow", "Text1"))
        self.label_3.adjustSize()
        self.label_4.setText(_translate("AccountsMainWindow", "Email"))
        self.label_5.setText(_translate("AccountsMainWindow", "Text2"))
        self.label_5.adjustSize()
        self.label_6.setText(_translate("AccountsMainWindow", "Phone No"))
        self.label_7.setText(_translate("AccountsMainWindow", "Text3"))
        self.label_7.adjustSize()
        self.pushButton.setText(_translate("AccountsMainWindow", "Change Password"))
        self.pushButton.adjustSize()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AccountsMainWindow = QtWidgets.QMainWindow()
    ui = Ui_AccountsMainWindow()
    ui.setupUi(AccountsMainWindow)
    AccountsMainWindow.show()
    sys.exit(app.exec_())
