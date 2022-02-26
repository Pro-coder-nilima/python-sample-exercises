

def alpha(a):
	if a.isalpha():
		print("alpha")
	elif a.isdigit():
		print('digit')
	elif a.isalnum():
		print('alphanumeric')
	else:
		print('special charcter')
alpha('hi14')