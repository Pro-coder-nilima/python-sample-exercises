# 15. print the vowels word in a string

def vowel(alphabets):
	string = 'aeiou'
	for i in alphabets:
		if i in string:
			return i
vowel('abcdefgh')