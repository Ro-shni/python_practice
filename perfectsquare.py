list2 = []
for i in range(30):
    list1 = i**2
    list2.append(list1)

def perfect_sqr(num):
    if num in list2:
        return True
    return False

print(perfect_sqr(4))


'''
return num**0.5 in range (1,num)

return num**0.5%1==0
'''