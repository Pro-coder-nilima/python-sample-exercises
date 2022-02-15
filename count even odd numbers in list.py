

def EvenOdd(list):
	Even = 0
	Odd = 0
	for i in list:
		if i%2 == 0:
			Even += 1
			
		else:
			Odd += 1
	print(Even)
	print(Odd)
EvenOdd([1,2,3,4,5,6,7,8,9,10,12])