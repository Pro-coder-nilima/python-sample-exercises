
class demo:
	def __init__(self):
		self.x = 120
		self.y = 130
class stu(demo):
	def __init__(self):
		self.x = 140
		self.y = 150
		super().__init__()
class employee(stu):
	def __init__(self):
		self.x = 100
		super().__init__()

a = employee()
print(a.x)
print(a.y)
