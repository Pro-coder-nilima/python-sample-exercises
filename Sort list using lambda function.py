# write a program to sort alist of tuples using lambda


s = [('emloyee',80),('student',90),('id',5)]
s.sort(key = lambda x: x[1])
print(s)