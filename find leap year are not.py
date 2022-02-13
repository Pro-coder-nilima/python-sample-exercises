
def leap(year):
	if(year % 400 == 0):
		print(year,"is leap year")
	elif(year % 4 == 0 and year % 100 != 0):
		print(year,"is leap year")
	else:
		print(year,"is not leap year")
year = int(input("enter the year:"))
leap(year)
