import mysql.connector as mysql
import datetime
from User import User

class DB:
	def __init__(self):
		self.host = "127.0.0.1"
		self.user = "root"
		self.password = "githubowyjuliusz"
		self.schema = "pswdb"
		self.table = "user"
		self.connection = mysql.connect(user = self.user, password = self.password, host = self.host)
		self.cursor = self.connection.cursor()

	def __del__(self):
		try:
			self.connection.close()
		except:
			print("Couldn't close connection.")
	
	def run_query(self, query):
		try:
			self.cursor.execute(query)
		except Exception as e:
			print(e)
		try:
			table = self.cursor.fetchall()
		except:
			table = self.cursor.fetchone()
		self.connection.commit()
		return table
	
	def insert_user(self, user, date):
		query = f"INSERT INTO {self.schema}.{self.table} VALUES (0, \"{user.name}\", \"{user.last_name}\", \"{user.login}\", \"{user.password}\", \"{user.email}\", \"{user.permission}\", \"{date}\")"
		self.run_query(query)

	def is_login_taken(self, user):
		query = f"SELECT id FROM {self.schema}.{self.table} WHERE login=\"{user.login}\""
		table = self.run_query(query)
		if table == []:
			return False
		return True

	def check_login_and_password(self, login, password):
		query = f"SELECT * FROM {self.schema}.{self.table} WHERE login=\"{login}\" and password=\"{password}\""
		user_data = self.run_query(query)
		return user_data

	def get_table(self):
		query = f"SELECT * FROM {self.schema}.{self.table}"
		table = self.run_query(query)
		return table