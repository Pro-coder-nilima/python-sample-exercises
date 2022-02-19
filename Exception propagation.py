
def sample():
	a,b = 4,0
	try:
		print('1'+1)
		print(sum)
		print(1/0)
	except NameError:                # specific exception
		print("sum does not exist")
	except ZeroDivisionError:
		print("Cannot divide by 0")
	except Exception:                #broder exception
		print("Something went wrong")
sample()