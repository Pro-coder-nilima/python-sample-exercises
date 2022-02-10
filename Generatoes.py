

''' Generators : Generators are like functions which contain yield keyword.
('multiple statements to return')
'''


def f2():
	for i in range(10):
		yield i
x = f2()

for value in x:
	print(value)
#66

def sample():
	sample1 = [1,3,6,8,9]
	for values in sample1:
		yield values
y = sample()
for i in y:
	print(i)









