

list1 = [10,20,30,40,50]
del list1[:]
print(list1)

def values(sample):
	del sample[:]
	return sample
list1 = [10,20,30]
print(values(list1))