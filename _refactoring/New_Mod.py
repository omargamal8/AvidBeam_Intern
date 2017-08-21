# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'New_Mod.ui'
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

    def __init__(self):
        import Navigator
        self._navigator = Navigator.Navigator()
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(640, 572)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(60, 530, 181, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Save)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayoutWidget = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 147, 381))
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
        self.label_10 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.verticalLayout.addWidget(self.label_10)
        self.label_8 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout.addWidget(self.label_8)
        self.label_9 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout.addWidget(self.label_9)
        self.label_4 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.verticalLayoutWidget_2 = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(170, 20, 221, 381))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.Algorithm_Name_LE = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.Algorithm_Name_LE.setObjectName(_fromUtf8("Algorithm_Name_LE"))
        self.verticalLayout_2.addWidget(self.Algorithm_Name_LE)
        self.Ram_Req_LE = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.Ram_Req_LE.setObjectName(_fromUtf8("Ram_Req_LE"))
        self.verticalLayout_2.addWidget(self.Ram_Req_LE)
        self.Threads_LE = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.Threads_LE.setObjectName(_fromUtf8("Threads_LE"))
        self.verticalLayout_2.addWidget(self.Threads_LE)
        self.Cores_LE = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.Cores_LE.setObjectName(_fromUtf8("Cores_LE"))
        self.verticalLayout_2.addWidget(self.Cores_LE)
        self.Phy_Cores_LE = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.Phy_Cores_LE.setObjectName(_fromUtf8("Phy_Cores_LE"))
        self.verticalLayout_2.addWidget(self.Phy_Cores_LE)
        self.Max_Input_Res_LE = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.Max_Input_Res_LE.setObjectName(_fromUtf8("Max_Input_Res_LE"))
        self.verticalLayout_2.addWidget(self.Max_Input_Res_LE)
        self.Max_Freq_LE = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.Max_Freq_LE.setObjectName(_fromUtf8("Max_Freq_LE"))
        self.verticalLayout_2.addWidget(self.Max_Freq_LE)
        self.Processing_FPS_LE = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.Processing_FPS_LE.setObjectName(_fromUtf8("Processing_FPS_LE"))
        self.verticalLayout_2.addWidget(self.Processing_FPS_LE)
        self.Algorithm_Version_LE = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.Algorithm_Version_LE.setObjectName(_fromUtf8("Algorithm_Version_LE"))
        self.verticalLayout_2.addWidget(self.Algorithm_Version_LE)
        self.Plugin_Path_LE = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.Plugin_Path_LE.setObjectName(_fromUtf8("Plugin_Path_LE"))
        self.verticalLayout_2.addWidget(self.Plugin_Path_LE)
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(400, 370, 99, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), lambda:self.saveCallback(Dialog))
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda:self.Plugin_Path_LE.setText(QtGui.QFileDialog.getOpenFileName()))

        QtCore.QMetaObject.connectSlotsByName(Dialog)
    def saveCallback(self,Dialog):
        
        info = []
        info.append(str(self.Algorithm_Name_LE.text()))
        info.append(str(self.Ram_Req_LE.text()))
        info.append(str(self.Threads_LE.text()))
        info.append(str(self.Cores_LE.text()))
        info.append(str(self.Phy_Cores_LE.text()))
        info.append(str(self.Max_Input_Res_LE.text()))
        info.append(str(self.Max_Freq_LE.text()))
        info.append(str(self.Processing_FPS_LE.text()))
        info.append(str(self.Algorithm_Version_LE.text()))
        info.append(str(self.Plugin_Path_LE.text()))
        self._navigator.trigger("new_mod",info)
        Dialog.accept()

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label_3.setText(_translate("Dialog", "Algorithm Name:", None))
        self.label_2.setText(_translate("Dialog", "Ram Requirments:", None))
        self.label.setText(_translate("Dialog", "Threads:", None))
        self.label_5.setText(_translate("Dialog", "Cores:", None))
        self.label_7.setText(_translate("Dialog", "Physical Cores:", None))
        self.label_6.setText(_translate("Dialog", "Max input resolution:", None))
        self.label_10.setText(_translate("Dialog", "Max Frequency:", None))
        self.label_8.setText(_translate("Dialog", "Processing FPS:", None))
        self.label_9.setText(_translate("Dialog", "Algorithm version:", None))
        self.label_4.setText(_translate("Dialog", "Plugin Path:", None))
        self.pushButton.setText(_translate("Dialog", "Browse", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

