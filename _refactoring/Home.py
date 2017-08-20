# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Home_index.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import Navigator

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

class Ui_Form(object):
    def __init__(self):
        self._navigator = Navigator.Navigator()
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(640, 480)
        Form.setAcceptDrops(False)
        Form.setAutoFillBackground(False)
        self.widget = QtGui.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 110, 641, 371))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.pushButton = QtGui.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(40, 0, 99, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 0, 99, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.widget)
        self.pushButton_3.setGeometry(QtCore.QRect(450, 0, 99, 27))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(240, 40, 211, 17))
        self.label.setObjectName(_fromUtf8("label"))
 

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda:self._navigator.trigger("comp_mod"))
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Dimensioning Tool", None))
        self.pushButton.setText(_translate("Form", "Computing", None))
        self.pushButton_2.setText(_translate("Form", "Medias", None))
        self.pushButton_3.setText(_translate("Form", "Deployments", None))
        self.label.setText(_translate("Form", "Dimensioning Tool", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

