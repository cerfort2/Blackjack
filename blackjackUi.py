# Form implementation generated from reading ui file 'blackjack.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(836, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1071, 571))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("table.png"))
        self.label.setObjectName("label")
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 211, 231))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.playercards = QtWidgets.QTextEdit(parent=self.gridLayoutWidget)
        self.playercards.setEnabled(False)
        self.playercards.setObjectName("playercards")
        self.gridLayout.addWidget(self.playercards, 2, 1, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(parent=self.gridLayoutWidget)
        self.textEdit.setEnabled(False)
        self.textEdit.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 1, 0, 1, 1)
        self.textEdit_3 = QtWidgets.QTextEdit(parent=self.gridLayoutWidget)
        self.textEdit_3.setEnabled(False)
        self.textEdit_3.setObjectName("textEdit_3")
        self.gridLayout.addWidget(self.textEdit_3, 2, 0, 1, 1)
        self.dealercards = QtWidgets.QTextEdit(parent=self.gridLayoutWidget)
        self.dealercards.setEnabled(False)
        self.dealercards.setObjectName("dealercards")
        self.gridLayout.addWidget(self.dealercards, 1, 1, 1, 1)
        self.textEdit_2 = QtWidgets.QTextEdit(parent=self.gridLayoutWidget)
        self.textEdit_2.setEnabled(False)
        self.textEdit_2.setObjectName("textEdit_2")
        self.gridLayout.addWidget(self.textEdit_2, 0, 0, 1, 1)
        self.winnings = QtWidgets.QTextEdit(parent=self.gridLayoutWidget)
        self.winnings.setEnabled(False)
        self.winnings.setObjectName("winnings")
        self.gridLayout.addWidget(self.winnings, 0, 1, 1, 1)
        self.dealertext = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.dealertext.setEnabled(False)
        self.dealertext.setGeometry(QtCore.QRect(280, 490, 301, 61))
        self.dealertext.setObjectName("dealertext")
        self.pcard1 = QtWidgets.QLabel(parent=self.centralwidget)
        self.pcard1.setGeometry(QtCore.QRect(340, 340, 71, 111))
        self.pcard1.setText("")
        self.pcard1.setScaledContents(True)
        self.pcard1.setObjectName("pcard1")
        self.pcard2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.pcard2.setGeometry(QtCore.QRect(420, 340, 71, 111))
        self.pcard2.setText("")
        self.pcard2.setScaledContents(True)
        self.pcard2.setObjectName("pcard2")
        self.pcard3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.pcard3.setGeometry(QtCore.QRect(490, 340, 71, 111))
        self.pcard3.setText("")
        self.pcard3.setScaledContents(True)
        self.pcard3.setObjectName("pcard3")
        self.pcard5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.pcard5.setGeometry(QtCore.QRect(570, 330, 71, 111))
        self.pcard5.setText("")
        self.pcard5.setScaledContents(True)
        self.pcard5.setObjectName("pcard5")
        self.pcard4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.pcard4.setGeometry(QtCore.QRect(250, 340, 71, 111))
        self.pcard4.setText("")
        self.pcard4.setScaledContents(True)
        self.pcard4.setObjectName("pcard4")
        self.pcard7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.pcard7.setGeometry(QtCore.QRect(640, 300, 71, 111))
        self.pcard7.setText("")
        self.pcard7.setScaledContents(True)
        self.pcard7.setObjectName("pcard7")
        self.pcard6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.pcard6.setGeometry(QtCore.QRect(140, 300, 71, 111))
        self.pcard6.setText("")
        self.pcard6.setScaledContents(True)
        self.pcard6.setObjectName("pcard6")
        self.dcard1 = QtWidgets.QLabel(parent=self.centralwidget)
        self.dcard1.setGeometry(QtCore.QRect(330, 100, 71, 111))
        self.dcard1.setText("")
        self.dcard1.setScaledContents(True)
        self.dcard1.setObjectName("dcard1")
        self.dcard2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.dcard2.setGeometry(QtCore.QRect(420, 100, 71, 111))
        self.dcard2.setText("")
        self.dcard2.setScaledContents(True)
        self.dcard2.setObjectName("dcard2")
        self.dcard3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.dcard3.setGeometry(QtCore.QRect(510, 100, 71, 111))
        self.dcard3.setText("")
        self.dcard3.setScaledContents(True)
        self.dcard3.setObjectName("dcard3")
        self.dcard5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.dcard5.setGeometry(QtCore.QRect(600, 100, 71, 111))
        self.dcard5.setText("")
        self.dcard5.setScaledContents(True)
        self.dcard5.setObjectName("dcard5")
        self.dcard4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.dcard4.setGeometry(QtCore.QRect(240, 90, 71, 111))
        self.dcard4.setText("")
        self.dcard4.setScaledContents(True)
        self.dcard4.setObjectName("dcard4")
        self.dcard6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.dcard6.setGeometry(QtCore.QRect(670, 100, 71, 111))
        self.dcard6.setText("")
        self.dcard6.setScaledContents(True)
        self.dcard6.setObjectName("dcard6")
        self.dcard7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.dcard7.setGeometry(QtCore.QRect(740, 80, 71, 111))
        self.dcard7.setText("")
        self.dcard7.setScaledContents(True)
        self.dcard7.setObjectName("dcard7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 836, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:700; font-style:italic; color:#000000;\">Dealer Card Count:</span></p></body></html>"))
        self.textEdit_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:700; font-style:italic;\">Your Card Count:</span></p></body></html>"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700; font-style:italic;\">Winnings:</span></p></body></html>"))
        self.dealertext.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700; font-style:italic;\">Dealer:</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:700; font-style:italic;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())