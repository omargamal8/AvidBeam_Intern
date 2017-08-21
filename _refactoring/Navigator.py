from PyQt4 import QtCore, QtGui
from computing_modules import ComputingModule
class Navigator:
	def __init__(self):
		self.event_action = {"comp_mod": self.nav_to_comps,
							 "new_mod":ComputingModule.create_module,
							 "insert_comp_mod":self.nav_to_new_comp,
							 "delete_comp":ComputingModule.delete_module}
	def trigger(self, event, *data):
		self.event_action[event](*data)

	def nav_to_comps(self):
		import Computing_Modules
		D = QtGui.QDialog()
		ui = Computing_Modules.Ui_Dialog()
		ui.setupUi(D)
		D.exec_()

	def nav_to_new_comp(self):
		import New_Mod
		D = QtGui.QDialog()
		ui = New_Mod.Ui_Dialog()
		ui.setupUi(D)
		D.exec_()