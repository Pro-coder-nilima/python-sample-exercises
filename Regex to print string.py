
import re

information  = "Sruthi grade is 90. Sushmaja grade is 80, Renuka grade is 100"
names = re.findall('[A-Z][a-z]+', information)
print(names)

grades = re.findall('\d+',information)
print(grades)


dictionary = {}
x = 0
for each in names:
	dictionary[each] = grades[x]
	x = x+1
print(dictionary)