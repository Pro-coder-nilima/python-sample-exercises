#  write a program to accept a string and replace all spaces by "#" symbol.
def st(sample):
    st1 = ""
    for i in sample:
        if i.isspace():
            st1 = st1 +'#'
        else:
            st1 = st1+i
    return st1
r = "string programming of python"
print(st(r)) 