
def d_division(func):
	def division(x,y):
		if y == 0:
			return "we can't divide by zero"
		else:
			return x/y
	return division
@d_division
def divide(a,b):
	return a/b
print(divide(10,5))