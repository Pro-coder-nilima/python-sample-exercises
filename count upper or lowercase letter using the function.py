

def sample(string):
	upper = 0
	lower = 0
	for i in string:
		if(i.isupper()):
			upper =upper+1
		elif(i.islower()):
			lower =lower+1
	print(" the uppercase length is:",upper)
	print("the lowercase length is:",lower)
sample("PTHON with DataScience")

	