
# To find the average of the given list.

def sample(L1):
	total = 0
	for i in range(0,len(L1)):
		total = total+L1[i]
	avg = total/len(L1)
	return avg
sample([1,2,3,4,3,5,1])