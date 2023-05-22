#1.Positional argument 
def linear(l,key):
    for value in l:
        if key == value:
            return True
    else:
            return False
l = [1,2,3,4,5,6]
key=4
result = linear(l,key)
print(result)

