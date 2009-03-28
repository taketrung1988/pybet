# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/positive/work/python/pybet/LogParser.ui'
#
# Created: Sat Mar 28 13:24:41 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(731, 522)
        MainWindow.setMinimumSize(QtCore.QSize(731, 522))
        MainWindow.setMaximumSize(QtCore.QSize(731, 16777215))
        self.verticalLayout = QtGui.QVBoxLayout(MainWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblPath = QtGui.QLabel(MainWindow)
        self.lblPath.setMinimumSize(QtCore.QSize(711, 21))
        self.lblPath.setObjectName("lblPath")
        self.verticalLayout.addWidget(self.lblPath)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.txtReToMatch = QtGui.QLineEdit(MainWindow)
        self.txtReToMatch.setObjectName("txtReToMatch")
        self.horizontalLayout.addWidget(self.txtReToMatch)
        self.btnParse = QtGui.QPushButton(MainWindow)
        self.btnParse.setObjectName("btnParse")
        self.horizontalLayout.addWidget(self.btnParse)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tvResult = QtGui.QTreeView(MainWindow)
        self.tvResult.setObjectName("tvResult")
        self.verticalLayout.addWidget(self.tvResult)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "LogParser", None, QtGui.QApplication.UnicodeUTF8))
        self.lblPath.setText(QtGui.QApplication.translate("MainWindow", "Please load a log file", None, QtGui.QApplication.UnicodeUTF8))
        self.btnParse.setText(QtGui.QApplication.translate("MainWindow", "Parse", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QDialog()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

