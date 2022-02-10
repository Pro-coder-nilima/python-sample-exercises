#  write a python program to swap the list of two any elements.

def swap_two(sample):
	sample[3],sample[1] = sample[1],sample[3]
	return sample
swap_two([45,98,20,10,50])
