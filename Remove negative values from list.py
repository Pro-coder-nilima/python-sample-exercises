# 23. Remove negative values from a list with filter function.

def sample(number):
	 y = list(filter(lambda x: x<0,number))
	 for i in number:
	 	if i%2 == 0:
	 		if i >= 1:
	 			print(i, end=' ')
sample([ 10,20,-30,60,-40,-50])