# write a program the given number is polindrome or not.
 
def poli(num):
	string = str(num)
	rev_str = string[::-1]
	if string == rev_str:
		print("polindrome")
	else:
		print('not a polindrome')
poli(151)