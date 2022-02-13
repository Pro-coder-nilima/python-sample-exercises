

class Error(Exception):
	def __init__(self):
		print("error")

class ATM:
	def __init__(self,value,string):
		self.value = value
		self.string = string
		print("define Exception")
class Card(ATM):
	def __init__(self):
		self.value = 20
		super().__init__(100,'custom')
	def Account(self,pin):
		self.pin = 9010
		return "show the pin number"
	def divide(self,x):
		if x/0:
			return " not an error"
		else:
			raise Error()


a = Card()
print(a.value,a.string)
print(a.divide(4))