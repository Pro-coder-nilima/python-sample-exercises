


def ex(val,list = []):
	list.append(val)
	return list
list1 = ex(10)
list2 = ex(123,[])
list3 = ex('a')

print(ex(list1,list2))

