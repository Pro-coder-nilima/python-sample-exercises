 # write a program in python to find gievn number is perferct or not

def per(num):
	sum = 0;
	for x in range(1,num):
		if num%x == 0:
			sum += x
	return sum
per(6)