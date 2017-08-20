from PyQt4 import QtCore, QtGui
import Home
import sys


if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	Form = QtGui.QWidget()
	ui = Home.Ui_Form()
	ui.setupUi(Form)
	Form.show()
	sys.exit(app.exec_())
	