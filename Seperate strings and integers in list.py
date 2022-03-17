
names = []
numbers = []
lst = ['python',2020,'java',1729,'datascience',2021]
for i in lst:
	if type(i) == str:
		names.append(i)
	if type(i) == int:
		numbers.append(i)
print(names,numbers)
