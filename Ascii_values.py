# 10. print the Ascii_values.

def ascii(Ascii_values):
	alph = ['a','b','c']
	dictionary = dict(zip(Ascii_values,alph))
	return (dictionary)
print(ascii([65,66,67]))