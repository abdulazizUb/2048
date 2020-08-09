# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Abdulaziz\Desktop\Projects\file.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setStyleSheet("background-color:#3a3e4a; ")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(100, 100, 201, 51))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    font: 12pt \"Century Gothic\";\n"
"color: #fcfcfc ;\n"
"background-color: #4700ba;\n"
"border: none;\n"
"}\n"
"\n"
"QPushButtonchover{\n"
"color: #f8c7fc ;\n"
"background-color: #6e3cbd;\n"
"border: #0385ff;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color: #00ff84;\n"
"border: #0385ff;\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(60, 30, 291, 51))
        self.lineEdit.setStyleSheet("color: #2f4f3f;\n"
"font: 12pt \"Times New Roman\";\n"
"background-color: #09de90;\n"
"border: #037f3d;")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(26, 162, 341, 121))
        self.label.setStyleSheet("color: #ccc;\n"
"font: 75 12pt \"Gadugi\";\n"
"")
        self.label.setText("")
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Получить "))