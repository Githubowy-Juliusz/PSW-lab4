from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Registration import Registration
from LogIn import LogIn
from DB import DB
from User import User
import sys

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(600, 600)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.log_in_frame = QtWidgets.QFrame(self.centralwidget)
		self.log_in_frame.setGeometry(QtCore.QRect(180, 320, 390, 190))
		font = QtGui.QFont()
		font.setBold(False)
		font.setItalic(False)
		font.setWeight(50)
		self.log_in_frame.setFont(font)
		self.log_in_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.log_in_frame.setFrameShadow(QtWidgets.QFrame.Raised)
		self.log_in_frame.setLineWidth(0)
		self.log_in_frame.setObjectName("log_in_frame")
		self.log_in_login_input = QtWidgets.QLineEdit(self.log_in_frame)
		self.log_in_login_input.setGeometry(QtCore.QRect(0, 0, 240, 35))
		self.log_in_login_input.setInputMask("")
		self.log_in_login_input.setText("")
		self.log_in_login_input.setMaxLength(100)
		self.log_in_login_input.setObjectName("log_in_login_input")
		self.log_in_password_input = QtWidgets.QLineEdit(self.log_in_frame)
		self.log_in_password_input.setGeometry(QtCore.QRect(0, 50, 240, 35))
		self.log_in_password_input.setInputMask("")
		self.log_in_password_input.setText("")
		self.log_in_password_input.setMaxLength(1000)
		self.log_in_password_input.setEchoMode(QtWidgets.QLineEdit.Password)
		self.log_in_password_input.setCursorPosition(0)
		self.log_in_password_input.setObjectName("log_in_password_input")
		self.log_in_log_in_button = QtWidgets.QPushButton(self.log_in_frame)
		self.log_in_log_in_button.setGeometry(QtCore.QRect(30, 100, 180, 35))
		self.log_in_log_in_button.setObjectName("log_in_log_in_button")
		self.log_in_to_registration_button = QtWidgets.QPushButton(self.log_in_frame)
		self.log_in_to_registration_button.setGeometry(QtCore.QRect(30, 150, 180, 35))
		self.log_in_to_registration_button.setObjectName("log_in_to_registration_button")
		self.log_in_show_password_checkbox = QtWidgets.QCheckBox(self.log_in_frame)
		self.log_in_show_password_checkbox.setGeometry(QtCore.QRect(250, 60, 140, 25))
		font = QtGui.QFont()
		font.setBold(True)
		font.setItalic(False)
		font.setWeight(75)
		self.log_in_show_password_checkbox.setFont(font)
		self.log_in_show_password_checkbox.setObjectName("log_in_show_password_checkbox")
		self.log_in_password_input.raise_()
		self.log_in_show_password_checkbox.raise_()
		self.log_in_to_registration_button.raise_()
		self.log_in_log_in_button.raise_()
		self.log_in_login_input.raise_()
		self.registration_frame = QtWidgets.QFrame(self.centralwidget)
		self.registration_frame.setEnabled(True)
		self.registration_frame.setGeometry(QtCore.QRect(10, 20, 580, 535))
		self.registration_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.registration_frame.setFrameShadow(QtWidgets.QFrame.Raised)
		self.registration_frame.setLineWidth(1)
		self.registration_frame.setObjectName("registration_frame")
		self.registration_login_input = QtWidgets.QLineEdit(self.registration_frame)
		self.registration_login_input.setGeometry(QtCore.QRect(20, 250, 240, 35))
		self.registration_login_input.setInputMask("")
		self.registration_login_input.setText("")
		self.registration_login_input.setMaxLength(100)
		self.registration_login_input.setObjectName("registration_login_input")
		self.registration_password_input = QtWidgets.QLineEdit(self.registration_frame)
		self.registration_password_input.setGeometry(QtCore.QRect(20, 300, 240, 35))
		self.registration_password_input.setInputMask("")
		self.registration_password_input.setText("")
		self.registration_password_input.setMaxLength(1000)
		self.registration_password_input.setEchoMode(QtWidgets.QLineEdit.Password)
		self.registration_password_input.setCursorPosition(0)
		self.registration_password_input.setObjectName("registration_password_input")
		self.registration_password_validation_input = QtWidgets.QLineEdit(self.registration_frame)
		self.registration_password_validation_input.setGeometry(QtCore.QRect(20, 350, 240, 35))
		self.registration_password_validation_input.setInputMask("")
		self.registration_password_validation_input.setText("")
		self.registration_password_validation_input.setMaxLength(1000)
		self.registration_password_validation_input.setEchoMode(QtWidgets.QLineEdit.Password)
		self.registration_password_validation_input.setCursorPosition(0)
		self.registration_password_validation_input.setObjectName("registration_password_validation_input")
		self.registration_name_input = QtWidgets.QLineEdit(self.registration_frame)
		self.registration_name_input.setGeometry(QtCore.QRect(320, 250, 240, 35))
		self.registration_name_input.setMaxLength(100)
		self.registration_name_input.setObjectName("registration_name_input")
		self.registration_last_name_input = QtWidgets.QLineEdit(self.registration_frame)
		self.registration_last_name_input.setGeometry(QtCore.QRect(320, 300, 240, 35))
		self.registration_last_name_input.setMaxLength(100)
		self.registration_last_name_input.setObjectName("registration_last_name_input")
		self.registration_email_input = QtWidgets.QLineEdit(self.registration_frame)
		self.registration_email_input.setGeometry(QtCore.QRect(320, 350, 240, 35))
		self.registration_email_input.setMaxLength(255)
		self.registration_email_input.setObjectName("registration_email_input")
		self.registration_register_button = QtWidgets.QPushButton(self.registration_frame)
		self.registration_register_button.setGeometry(QtCore.QRect(200, 400, 180, 35))
		self.registration_register_button.setObjectName("registration_register_button")
		self.registration_to_log_in_button = QtWidgets.QPushButton(self.registration_frame)
		self.registration_to_log_in_button.setGeometry(QtCore.QRect(200, 450, 180, 35))
		self.registration_to_log_in_button.setAutoFillBackground(True)
		self.registration_to_log_in_button.setObjectName("registration_to_log_in_button")
		self.user_frame = QtWidgets.QFrame(self.centralwidget)
		self.user_frame.setGeometry(QtCore.QRect(10, 20, 580, 535))
		self.user_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.user_frame.setFrameShadow(QtWidgets.QFrame.Plain)
		self.user_frame.setObjectName("user_frame")
		self.user_log_out_button = QtWidgets.QPushButton(self.user_frame)
		self.user_log_out_button.setGeometry(QtCore.QRect(200, 400, 180, 35))
		self.user_log_out_button.setObjectName("user_log_out_button")
		self.user_text = QtWidgets.QLabel(self.user_frame)
		self.user_text.setGeometry(QtCore.QRect(10, 10, 560, 100))
		font = QtGui.QFont()
		font.setPointSize(20)
		font.setBold(True)
		font.setWeight(75)
		self.user_text.setFont(font)
		self.user_text.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.user_text.setFrameShadow(QtWidgets.QFrame.Plain)
		self.user_text.setLineWidth(1)
		self.user_text.setScaledContents(False)
		self.user_text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
		self.user_text.setObjectName("user_text")
		self.admin_frame = QtWidgets.QFrame(self.centralwidget)
		self.admin_frame.setGeometry(QtCore.QRect(10, 20, 580, 535))
		self.admin_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.admin_frame.setFrameShadow(QtWidgets.QFrame.Raised)
		self.admin_frame.setObjectName("admin_frame")
		self.admin_log_out_button = QtWidgets.QPushButton(self.admin_frame)
		self.admin_log_out_button.setGeometry(QtCore.QRect(200, 400, 180, 35))
		self.admin_log_out_button.setObjectName("admin_log_out_button")
		self.admin_table = QtWidgets.QTreeWidget(self.admin_frame)
		self.admin_table.setGeometry(QtCore.QRect(10, 10, 560, 350))
		self.admin_table.setColumnCount(8)
		self.admin_table.setObjectName("admin_table")
		MainWindow.setCentralWidget(self.centralwidget)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)

		self.retranslateUi(MainWindow)

		#
		try:
			self.db = DB()
		except:
			print("Can't connect to database:")
			self.create_popup_window("Error!", "Can't connect to database!")
			exit()
		
		self.log_in_to_registration_button.clicked.connect(self.registration_menu)
		self.registration_to_log_in_button.clicked.connect(self.log_in_menu)
		self.log_in_log_in_button.clicked.connect(self.log_in)
		self.registration_register_button.clicked.connect(self.register)
		self.log_in_show_password_checkbox.stateChanged.connect(self.show_or_hide_password)
		self.user_log_out_button.clicked.connect(self.log_out)
		self.admin_log_out_button.clicked.connect(self.log_out)

		self.registration_frame.hide()
		self.admin_frame.hide()
		self.user_frame.hide()

		self.registration = Registration(self.db)
		self.log_in_object = LogIn(self.db)
		self.user = None
		#
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.log_in_password_input.setPlaceholderText(_translate("MainWindow", "Password"))
		self.log_in_show_password_checkbox.setText(_translate("MainWindow", "Show password"))
		self.log_in_log_in_button.setText(_translate("MainWindow", "Log in"))
		self.log_in_to_registration_button.setText(_translate("MainWindow", "I don\'t have an account"))
		self.log_in_login_input.setPlaceholderText(_translate("MainWindow", "Login"))
		self.registration_password_input.setPlaceholderText(_translate("MainWindow", "Password"))
		self.registration_login_input.setPlaceholderText(_translate("MainWindow", "Login"))
		self.registration_password_validation_input.setPlaceholderText(_translate("MainWindow", "Password"))
		self.registration_name_input.setPlaceholderText(_translate("MainWindow", "Name"))
		self.registration_last_name_input.setPlaceholderText(_translate("MainWindow", "Last name"))
		self.registration_email_input.setPlaceholderText(_translate("MainWindow", "E-mail"))
		self.registration_register_button.setText(_translate("MainWindow", "Register"))
		self.registration_to_log_in_button.setText(_translate("MainWindow", "I already have an account"))
		self.user_log_out_button.setText(_translate("MainWindow", "Log out"))
		self.user_text.setText(_translate("MainWindow", "Hello name last_name"))
		self.admin_log_out_button.setText(_translate("MainWindow", "Log out"))
		self.admin_table.headerItem().setText(0, _translate("MainWindow", "id"))
		self.admin_table.headerItem().setText(1, _translate("MainWindow", "name"))
		self.admin_table.headerItem().setText(2, _translate("MainWindow", "last_name"))
		self.admin_table.headerItem().setText(3, _translate("MainWindow", "login"))
		self.admin_table.headerItem().setText(4, _translate("MainWindow", "password"))
		self.admin_table.headerItem().setText(5, _translate("MainWindow", "e-mail"))
		self.admin_table.headerItem().setText(6, _translate("MainWindow", "permission"))
		self.admin_table.headerItem().setText(7, _translate("MainWindow", "registration_date"))

	def create_popup_window(self, title, message):
		popup_window = QMessageBox()
		popup_window.setWindowTitle(title)
		popup_window.setText(message)
		popup_window.exec_()
	
	def clear_inputs(self):
		inputs = self.log_in_frame.findChildren(QtWidgets.QLineEdit)
		inputs += self.registration_frame.findChildren(QtWidgets.QLineEdit)
		for input in inputs:
			input.clear()
		self.log_in_show_password_checkbox.setChecked(False)
	
	def fill_table(self):
		self.admin_table.clear()
		table = self.db.get_table()
		for item in range(len(table)):
			QtWidgets.QTreeWidgetItem(self.admin_table)
			for value in range(len(table[item])):
				self.admin_table.topLevelItem(item).setText(value, str(table[item][value]))

	def registration_menu(self):
		self.log_in_frame.hide()
		self.user_frame.hide()
		self.admin_frame.hide()
		self.registration_frame.show()
		self.clear_inputs()

	def log_in_menu(self):
		self.registration_frame.hide()
		self.user_frame.hide()
		self.admin_frame.hide()
		self.log_in_frame.show()
		self.clear_inputs()

	def user_menu(self):
		self.registration_frame.hide()
		self.log_in_frame.hide()
		self.admin_frame.hide()
		self.user_frame.show()
		self.user_text.setText(f"You are logged in as {self.user.name} {self.user.last_name}")
		self.clear_inputs()

	def admin_menu(self):
		self.registration_frame.hide()
		self.log_in_frame.hide()
		self.user_frame.hide()
		self.admin_frame.show()
		self.fill_table()
		self.clear_inputs()
	
	def log_out(self):
		self.user = None
		self.log_in_menu()

	def log_in(self):
		login = self.log_in_login_input.text()
		password = self.log_in_password_input.text()
		try:
			self.user = self.log_in_object.log_in(login, password)
			if self.user.is_admin():
				self.admin_menu()
			else:
				self.user_menu()
		except Exception as e:
			self.create_popup_window("Error", str(e))

	def register(self):
		name = self.registration_name_input.text()
		last_name = self.registration_last_name_input.text()
		email = self.registration_email_input.text()
		login = self.registration_login_input.text()
		password = self.registration_password_input.text()
		password_validation = self.registration_password_validation_input.text()

		try:
			message = self.registration.register(login, password, password_validation, name, last_name, email)
			self.clear_inputs()
			self.create_popup_window(message[0], message[1])
		except Exception as e:
			self.create_popup_window("Error", str(e))

	def show_or_hide_password(self):
		if self.log_in_show_password_checkbox.isChecked():
			self.log_in_password_input.setEchoMode(QtWidgets.QLineEdit.Normal)
		else:
			self.log_in_password_input.setEchoMode(QtWidgets.QLineEdit.Password)


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())