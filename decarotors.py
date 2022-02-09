def smart_divide(fun_):
	def inner(x,y):
		if y == 0:
			print("hi")
		else:
		
			return fun_(x,y)
	return inner;
@smart_divide	
def divide(a,b):
	return a/b;
#divide = smart_divide(divide)
print(divide(1,2))	

			
