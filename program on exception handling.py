
class ATM(Exception):
	pass
class validId:
	def __init__(self):
		print("Age is greater tahn 18. you are eligible to Apply")
	def InvalidId(self,age):
		if age >= 18:
			return "valid statement"
		else:
			return "Inavlid statement"
a = validId()
print(a.InvalidId(17))	