class User:
	def __init__(self, name, last_name, login, password, email, permission):
		self.name = name
		self.last_name = last_name
		self.login = login
		self.password = password
		self.email = email
		self.permission = permission
	
	def is_admin(self):
		if self.permission == "admin":
			return True
		return False