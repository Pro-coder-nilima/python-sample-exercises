
def sample(list1):
	result = []
	for i in list1:
		if 'd' in i:
			result.append(i)
	return (result)

print(sample(['python', 'datascience', 'django']))