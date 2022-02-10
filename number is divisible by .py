# 7. python program to check number is divisible by 5,11 .

def divisible(a,b):
	for i in a,b:
		if(i%5 == 0) & (i%11 == 0):
			print('{} is divisible by 5 and 11'.format(a,b))
		else:
			print('{} is not divisible by 5 and 11'.format(a,b))
divisible(225,55)