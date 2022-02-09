# 20. write aprogram to print even length word in string.

def word(sample):
	s = sample.split()
	for i in sample:
		if len(i)%2 == 0:
			return i
word('python programming langauge')