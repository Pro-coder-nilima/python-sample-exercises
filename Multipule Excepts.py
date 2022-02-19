
def ex_t():
	a,b=1,0
	try:
		print(a/b)
		print("con't be divisible by zero")
		print('10'+10)
	except TypeError:
		print("You added values of incompatible types")
	except ZeroDivisionError:
		print("You divided by 0")
ex_t()