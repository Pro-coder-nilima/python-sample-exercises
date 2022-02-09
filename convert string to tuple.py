# 49. write a program convert a given string list to atuple.

def values(sample):
	for i in sample:
		result = tuple(sample)
		return result
print(values(('python')))