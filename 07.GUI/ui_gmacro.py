# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\A_Firstproject\study\k-digital4\07.GUI\gmacro.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(958, 809)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(320, 170, 331, 171))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(220, 370, 151, 81))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(36)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(220, 470, 161, 81))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(36)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.xpoint = QtWidgets.QLineEdit(Dialog)
        self.xpoint.setGeometry(QtCore.QRect(410, 380, 271, 71))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(36)
        self.xpoint.setFont(font)
        self.xpoint.setText("")
        self.xpoint.setObjectName("xpoint")
        self.ypoint = QtWidgets.QLineEdit(Dialog)
        self.ypoint.setGeometry(QtCore.QRect(410, 470, 271, 71))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(36)
        self.ypoint.setFont(font)
        self.ypoint.setText("")
        self.ypoint.setObjectName("ypoint")
        self.StartButton = QtWidgets.QPushButton(Dialog)
        self.StartButton.setGeometry(QtCore.QRect(320, 590, 321, 81))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(48)
        self.StartButton.setFont(font)
        self.StartButton.setObjectName("StartButton")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(730, 370, 171, 81))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(36)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(730, 460, 161, 81))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(36)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(-100, 530, 681, 291))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(":/newPrefix/109285971.1.jpg"))
        self.label_6.setObjectName("label_6")
        self.label_6.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.xpoint.raise_()
        self.ypoint.raise_()
        self.StartButton.raise_()
        self.label_4.raise_()
        self.label_5.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Gmacro"))
        self.label_2.setText(_translate("Dialog", "X 좌표"))
        self.label_3.setText(_translate("Dialog", "Y 좌표"))
        self.StartButton.setText(_translate("Dialog", "Move Mouse"))
        self.label_4.setText(_translate("Dialog", "0~2560"))
        self.label_5.setText(_translate("Dialog", "0~1600"))
import pic_rc