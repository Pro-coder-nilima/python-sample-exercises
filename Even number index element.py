# python program to get even indexed elements in tuple


def tp(tu_ple):
	for i in tu_ple:
		if i%2 == 0:
			return i
		else:
			pass
tp((1,2,3,4,5,6,7,8))