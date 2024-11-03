# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1005, 727)
        MainWindow.setMinimumSize(QtCore.QSize(1005, 712))
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.FEntS = QtWidgets.QFrame(self.centralwidget)
        self.FEntS.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FEntS.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FEntS.setObjectName("FEntS")
        self.gridLayout = QtWidgets.QGridLayout(self.FEntS)
        self.gridLayout.setObjectName("gridLayout")
        self.BtnSLog = QtWidgets.QPushButton(self.FEntS)
        self.BtnSLog.setMinimumSize(QtCore.QSize(317, 45))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.BtnSLog.setFont(font)
        self.BtnSLog.setStyleSheet("QPushButton{\n"
"border-radius: 7px;\n"
"background-color: rgb(110, 200, 220);\n"
"color: white;\n"
"}")
        self.BtnSLog.setObjectName("BtnSLog")
        self.gridLayout.addWidget(self.BtnSLog, 1, 2, 1, 1)
        self.FCadSe = QtWidgets.QFrame(self.FEntS)
        self.FCadSe.setMinimumSize(QtCore.QSize(0, 50))
        self.FCadSe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FCadSe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FCadSe.setObjectName("FCadSe")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.FCadSe)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout.addWidget(self.FCadSe, 1, 1, 1, 1)
        self.BtnCad = QtWidgets.QPushButton(self.FEntS)
        self.BtnCad.setMinimumSize(QtCore.QSize(287, 45))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.BtnCad.setFont(font)
        self.BtnCad.setStyleSheet("QPushButton{\n"
"border-radius: 7px;\n"
"background-color: rgb(60, 160, 181);\n"
"color: white;\n"
"}")
        self.BtnCad.setObjectName("BtnCad")
        self.gridLayout.addWidget(self.BtnCad, 1, 0, 1, 1)
        self.fBtns = QtWidgets.QFrame(self.FEntS)
        self.fBtns.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fBtns.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fBtns.setObjectName("fBtns")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.fBtns)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.fLogo = QtWidgets.QFrame(self.fBtns)
        self.fLogo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fLogo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fLogo.setObjectName("fLogo")
        self.logo_home = QtWidgets.QLabel(self.fLogo)
        self.logo_home.setGeometry(QtCore.QRect(12, 12, 80, 80))
        self.logo_home.setMinimumSize(QtCore.QSize(80, 80))
        self.logo_home.setMaximumSize(QtCore.QSize(80, 80))
        self.logo_home.setText("")
        self.logo_home.setPixmap(QtGui.QPixmap("UI_Files\Images\Logo.png"))
        self.logo_home.setScaledContents(True)
        self.logo_home.setObjectName("logo_home")
        self.horizontalLayout_2.addWidget(self.fLogo)
        self.fCenter = QtWidgets.QFrame(self.fBtns)
        self.fCenter.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fCenter.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fCenter.setObjectName("fCenter")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.fCenter)
        self.verticalLayout.setObjectName("verticalLayout")
        self.fnothing_3 = QtWidgets.QFrame(self.fCenter)
        self.fnothing_3.setMaximumSize(QtCore.QSize(16777215, 200))
        self.fnothing_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fnothing_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fnothing_3.setObjectName("fnothing_3")
        self.verticalLayout.addWidget(self.fnothing_3)
        self.fCpftext = QtWidgets.QFrame(self.fCenter)
        self.fCpftext.setMinimumSize(QtCore.QSize(300, 70))
        self.fCpftext.setMaximumSize(QtCore.QSize(16777215, 60))
        self.fCpftext.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fCpftext.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fCpftext.setObjectName("fCpftext")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.fCpftext)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.l_CPF = QtWidgets.QLabel(self.fCpftext)
        self.l_CPF.setMinimumSize(QtCore.QSize(350, 50))
        self.l_CPF.setMaximumSize(QtCore.QSize(10000, 10000))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.l_CPF.setFont(font)
        self.l_CPF.setObjectName("l_CPF")
        self.gridLayout_3.addWidget(self.l_CPF, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.fCpftext)
        self.fDispC = QtWidgets.QFrame(self.fCenter)
        self.fDispC.setMinimumSize(QtCore.QSize(300, 290))
        self.fDispC.setMaximumSize(QtCore.QSize(1000, 1000))
        self.fDispC.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fDispC.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fDispC.setObjectName("fDispC")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.fDispC)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.txt_CPF = QtWidgets.QTextBrowser(self.fDispC)
        self.txt_CPF.setMinimumSize(QtCore.QSize(334, 50))
        self.txt_CPF.setMaximumSize(QtCore.QSize(400, 55))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(16)
        self.txt_CPF.setFont(font)
        self.txt_CPF.setStyleSheet("QTextBrowser{\n"
"background-color: rgb(229, 233, 237);\n"
"border-radius: 7px;\n"
"border: 1px solid rgb(196, 205, 208);\n"
"padding-top: 10px;\n"
"}\n"
"")
        self.txt_CPF.setObjectName("txt_CPF")
        self.verticalLayout_2.addWidget(self.txt_CPF)
        self.fBtnsCpf = QtWidgets.QFrame(self.fDispC)
        self.fBtnsCpf.setMinimumSize(QtCore.QSize(325, 320))
        self.fBtnsCpf.setMaximumSize(QtCore.QSize(650, 640))
        self.fBtnsCpf.setStyleSheet("QFrame { \n"
"   background-color: rgb(245, 245, 245);\n"
"   border-radius: 7px;\n"
"   border: 1px solid rgb(196, 205, 208);\n"
"} ")
        self.fBtnsCpf.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fBtnsCpf.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fBtnsCpf.setObjectName("fBtnsCpf")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.fBtnsCpf)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btn_0 = QtWidgets.QPushButton(self.fBtnsCpf)
        self.btn_0.setMinimumSize(QtCore.QSize(91, 51))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(14)
        self.btn_0.setFont(font)
        self.btn_0.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 7px;\n"
"border-styles: outset;\n"
"border: 1px solid rgb(196, 205, 208);\n"
"}")
        self.btn_0.setObjectName("btn_0")
        self.gridLayout_2.addWidget(self.btn_0, 3, 2, 1, 1)
        self.btn_3 = QtWidgets.QPushButton(self.fBtnsCpf)
        self.btn_3.setMinimumSize(QtCore.QSize(91, 51))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.btn_3.setFont(font)
        self.btn_3.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 7px;\n"
"border-styles: outset;\n"
"border: 1px solid rgb(196, 205, 208);\n"
"}")
        self.btn_3.setObjectName("btn_3")
        self.gridLayout_2.addWidget(self.btn_3, 0, 3, 1, 1)
        self.btn_back = QtWidgets.QPushButton(self.fBtnsCpf)
        self.btn_back.setMinimumSize(QtCore.QSize(91, 51))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(14)
        self.btn_back.setFont(font)
        self.btn_back.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 7px;\n"
"border-styles: outset;\n"
"border: 1px solid rgb(196, 205, 208);\n"
"}")
        self.btn_back.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/backspace.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_back.setIcon(icon)
        self.btn_back.setIconSize(QtCore.QSize(25, 25))
        self.btn_back.setObjectName("btn_back")
        self.gridLayout_2.addWidget(self.btn_back, 3, 3, 1, 1)
        self.btn_7 = QtWidgets.QPushButton(self.fBtnsCpf)
        self.btn_7.setMinimumSize(QtCore.QSize(91, 51))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(14)
        self.btn_7.setFont(font)
        self.btn_7.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 7px;\n"
"border-styles: outset;\n"
"border: 1px solid rgb(196, 205, 208);\n"
"}")
        self.btn_7.setObjectName("btn_7")
        self.gridLayout_2.addWidget(self.btn_7, 2, 0, 1, 1)
        self.btn_8 = QtWidgets.QPushButton(self.fBtnsCpf)
        self.btn_8.setMinimumSize(QtCore.QSize(91, 51))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(14)
        self.btn_8.setFont(font)
        self.btn_8.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 7px;\n"
"border-styles: outset;\n"
"border: 1px solid rgb(196, 205, 208);\n"
"}")
        self.btn_8.setObjectName("btn_8")
        self.gridLayout_2.addWidget(self.btn_8, 2, 2, 1, 1)
        self.btn_6 = QtWidgets.QPushButton(self.fBtnsCpf)
        self.btn_6.setMinimumSize(QtCore.QSize(91, 51))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(14)
        self.btn_6.setFont(font)
        self.btn_6.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 7px;\n"
"border-styles: outset;\n"
"border: 1px solid rgb(196, 205, 208);\n"
"}")
        self.btn_6.setObjectName("btn_6")
        self.gridLayout_2.addWidget(self.btn_6, 1, 3, 1, 1)
        self.btn_9 = QtWidgets.QPushButton(self.fBtnsCpf)
        self.btn_9.setMinimumSize(QtCore.QSize(91, 51))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(14)
        self.btn_9.setFont(font)
        self.btn_9.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 7px;\n"
"border-styles: outset;\n"
"border: 1px solid rgb(196, 205, 208);\n"
"}")
        self.btn_9.setObjectName("btn_9")
        self.gridLayout_2.addWidget(self.btn_9, 2, 3, 1, 1)
        self.btn_1 = QtWidgets.QPushButton(self.fBtnsCpf)
        self.btn_1.setMinimumSize(QtCore.QSize(91, 51))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(14)
        self.btn_1.setFont(font)
        self.btn_1.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 7px;\n"
"border-styles: outset;\n"
"border: 1px solid rgb(196, 205, 208);\n"
"}")
        self.btn_1.setObjectName("btn_1")
        self.gridLayout_2.addWidget(self.btn_1, 0, 0, 1, 1)
        self.btn_5 = QtWidgets.QPushButton(self.fBtnsCpf)
        self.btn_5.setMinimumSize(QtCore.QSize(91, 51))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(14)
        self.btn_5.setFont(font)
        self.btn_5.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 7px;\n"
"border-styles: outset;\n"
"border: 1px solid rgb(196, 205, 208);\n"
"}")
        self.btn_5.setObjectName("btn_5")
        self.gridLayout_2.addWidget(self.btn_5, 1, 2, 1, 1)
        self.btn_ = QtWidgets.QPushButton(self.fBtnsCpf)
        self.btn_.setMinimumSize(QtCore.QSize(91, 51))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(14)
        self.btn_.setFont(font)
        self.btn_.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 7px;\n"
"border-styles: outset;\n"
"border: 1px solid rgb(196, 205, 208);\n"
"}")
        self.btn_.setText("Limpar")
        self.btn_.setObjectName("btn_Clear")
        self.gridLayout_2.addWidget(self.btn_, 3, 0, 1, 1)
        self.btn_4 = QtWidgets.QPushButton(self.fBtnsCpf)
        self.btn_4.setMinimumSize(QtCore.QSize(91, 51))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(14)
        self.btn_4.setFont(font)
        self.btn_4.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 7px;\n"
"border-styles: outset;\n"
"border: 1px solid rgb(196, 205, 208);\n"
"}")
        self.btn_4.setObjectName("btn_4")
        self.gridLayout_2.addWidget(self.btn_4, 1, 0, 1, 1)
        self.btn_2 = QtWidgets.QPushButton(self.fBtnsCpf)
        self.btn_2.setMinimumSize(QtCore.QSize(91, 51))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(14)
        self.btn_2.setFont(font)
        self.btn_2.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 7px;\n"
"border-styles: outset;\n"
"border: 1px solid rgb(196, 205, 208);\n"
"}")
        self.btn_2.setObjectName("btn_2")
        self.gridLayout_2.addWidget(self.btn_2, 0, 2, 1, 1)
        self.verticalLayout_2.addWidget(self.fBtnsCpf)
        self.verticalLayout.addWidget(self.fDispC, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.fnothing_2 = QtWidgets.QFrame(self.fCenter)
        self.fnothing_2.setMaximumSize(QtCore.QSize(16777215, 160))
        self.fnothing_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fnothing_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fnothing_2.setObjectName("fnothing_2")
        self.verticalLayout.addWidget(self.fnothing_2)
        self.horizontalLayout_2.addWidget(self.fCenter)
        self.fnothing = QtWidgets.QFrame(self.fBtns)
        self.fnothing.setMinimumSize(QtCore.QSize(0, 600))
        self.fnothing.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fnothing.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fnothing.setObjectName("fnothing")
        self.horizontalLayout_2.addWidget(self.fnothing)
        self.gridLayout.addWidget(self.fBtns, 0, 0, 1, 4)
        self.btn_entrar = QtWidgets.QPushButton(self.FEntS)
        self.btn_entrar.setMinimumSize(QtCore.QSize(287, 45))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_entrar.setFont(font)
        self.btn_entrar.setStyleSheet("QPushButton{\n"
"border-radius: 7px;\n"
"background-color: rgb(60, 160, 181);\n"
"color: white\n"
"}")
        self.btn_entrar.setObjectName("btn_entrar")
        self.gridLayout.addWidget(self.btn_entrar, 1, 3, 1, 1)
        self.horizontalLayout.addWidget(self.FEntS)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.BtnSLog.setText(_translate("MainWindow", "Entre sem Login"))
        self.BtnCad.setText(_translate("MainWindow", "Cadastre-se"))
        self.l_CPF.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Insira o seu CPF para login</span></p></body></html>"))
        self.txt_CPF.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.txt_CPF.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Poppins\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt;\">XXX.XXX.XXX-XX</span></p></body></html>"))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_entrar.setText(_translate("MainWindow", "Entrar"))


