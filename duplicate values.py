# 19. print the duplicate values from list in a given list.

def sample(list1):
	new = [ ]
	for i in list1:
		 x = list1.count(i)
		 if x > 1:
		 	if new.count(i)==0:
		 		new.append(i)
	return new	
print(sample([1,3,5,4,8,1,9,4,3,2,3,3])) 		