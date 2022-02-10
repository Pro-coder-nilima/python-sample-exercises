
#  Iterate through two lists in parallel

def list1(sample1,sample2):
 	for i,j in zip(sample1,sample2):
 		print(i,j)
list1(['numpy','asyncio','cmath'],['c','c++','java'])
