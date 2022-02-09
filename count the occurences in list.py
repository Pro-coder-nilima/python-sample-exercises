# 31. count the occurences of an element ina list

def sample(sample1):
    count = 0
    for i in sample1:
        if i == 10:
            count = count+1
    return count
print(sample([10,23,10,45,10,5,10]))            
