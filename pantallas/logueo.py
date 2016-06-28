# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logueo.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setEnabled(True)
        MainWindow.resize(456, 203)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(190, 40, 253, 108))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.logueo_aceptar = QtGui.QPushButton(self.gridLayoutWidget)
        self.logueo_aceptar.setAutoDefault(True)
        self.logueo_aceptar.setObjectName(_fromUtf8("logueo_aceptar"))
        self.gridLayout_2.addWidget(self.logueo_aceptar, 3, 2, 1, 1)
        self.logueo_cancelar = QtGui.QPushButton(self.gridLayoutWidget)
        self.logueo_cancelar.setAutoDefault(True)
        self.logueo_cancelar.setObjectName(_fromUtf8("logueo_cancelar"))
        self.gridLayout_2.addWidget(self.logueo_cancelar, 3, 1, 1, 1)
        self.logueo_password = QtGui.QLineEdit(self.gridLayoutWidget)
        self.logueo_password.setText(_fromUtf8(""))
        self.logueo_password.setEchoMode(QtGui.QLineEdit.Password)
        self.logueo_password.setObjectName(_fromUtf8("logueo_password"))
        self.gridLayout_2.addWidget(self.logueo_password, 2, 1, 1, 2)
        self.logueo_usuario = QtGui.QLineEdit(self.gridLayoutWidget)
        self.logueo_usuario.setText(_fromUtf8(""))
        self.logueo_usuario.setObjectName(_fromUtf8("logueo_usuario"))
        self.gridLayout_2.addWidget(self.logueo_usuario, 1, 1, 1, 2)
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 10, 171, 151))
        self.graphicsView.setStyleSheet(_fromUtf8("border-image: url(:/iconos/cash_register.2.2.png);"))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 456, 19))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.logueo_usuario, self.logueo_password)
        MainWindow.setTabOrder(self.logueo_password, self.logueo_aceptar)
        MainWindow.setTabOrder(self.logueo_aceptar, self.logueo_cancelar)
        MainWindow.setTabOrder(self.logueo_cancelar, self.graphicsView)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Punto de venta", None))
        self.label_2.setText(_translate("MainWindow", "Contraseña", None))
        self.label.setText(_translate("MainWindow", "Usuario", None))
        self.logueo_aceptar.setText(_translate("MainWindow", "Ingresar", None))
        self.logueo_cancelar.setText(_translate("MainWindow", "Salir", None))

import iconos_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

