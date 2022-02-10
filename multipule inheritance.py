# multipule inheritance

class mobile:
	def __init__(self):
		self.a = 10;
		print("motrola @ moto")      #here we printing one string statement
class nokia():
	def __init__(self):
		self.a = 40;
		print("welcome to nokia")
class vivo(mobile):
	def __init__(self):
		self.a = 50;                  #creating instance variable
		print("hello....")
		super().__init__()
class realme(vivo):
	def __init__(self):
		self.a = 60;
		print("hi.....")
		super().__init__()         #we are calling suoer class consrtuctor with this statement
class redme(realme,vivo,nokia):
	def __init__(self):
		self.a = 100;
		super().__init__()
x = redme()                         #creating red me class object that is refered by "b" reference variable
print(x.a)		

