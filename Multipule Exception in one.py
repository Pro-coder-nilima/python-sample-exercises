
def ex():
	x,y = 1,0
try:
      print('10'+10)
      print(1/0)
except (TypeError,ZeroDivisionError):
      print("Invalid input")
ex()