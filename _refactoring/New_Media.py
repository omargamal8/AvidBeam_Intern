# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'New_Media.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(640, 572)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(60, 530, 181, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Save)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayoutWidget = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 30, 147, 371))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.label_5 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout.addWidget(self.label_5)
        self.label_7 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout.addWidget(self.label_7)
        self.label_6 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout.addWidget(self.label_6)
        self.verticalLayoutWidget_2 = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(170, 20, 221, 401))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.X_LE = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.X_LE.setObjectName(_fromUtf8("X_LE"))
        self.verticalLayout_2.addWidget(self.X_LE)
        self.Y_LE = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.Y_LE.setObjectName(_fromUtf8("Y_LE"))
        self.verticalLayout_2.addWidget(self.Y_LE)
        self.Width_LE = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.Width_LE.setObjectName(_fromUtf8("Width_LE"))
        self.verticalLayout_2.addWidget(self.Width_LE)
        self.Height_LE = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.Height_LE.setObjectName(_fromUtf8("Height_LE"))
        self.verticalLayout_2.addWidget(self.Height_LE)
        self.Media_Name_LE = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.Media_Name_LE.setObjectName(_fromUtf8("Media_Name_LE"))
        self.verticalLayout_2.addWidget(self.Media_Name_LE)
        self.Media_Path_LE = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.Media_Path_LE.setObjectName(_fromUtf8("Media_Path_LE"))
        self.verticalLayout_2.addWidget(self.Media_Path_LE)
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(400, 360, 99, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label_3.setText(_translate("Dialog", "X:", None))
        self.label_2.setText(_translate("Dialog", "Y:", None))
        self.label.setText(_translate("Dialog", "Width:", None))
        self.label_5.setText(_translate("Dialog", "Height:", None))
        self.label_7.setText(_translate("Dialog", "Media Name:", None))
        self.label_6.setText(_translate("Dialog", "Media Path:", None))
        self.pushButton.setText(_translate("Dialog", "Browse", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

