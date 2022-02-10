#  Multiply every element in  a list by 5 with map function.

def multiply(sample):
	s = list(map(lambda x: x*5, sample))
	for i in sample:
		return s
multiply([10,20,30,40,50])