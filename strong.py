
a = int(input("enter range1: "))
b = int(input("enter range2: "))

def strong(j):
    temp = j
    sum = 0
    while temp>0:
        r = temp%10
        fact = 1
        for i in range(1,r+1):
            fact = fact*i
        sum = sum+fact
        temp //=10
    return j ==sum
for j in range(a,b+1):
    if strong(j):
        print(j)



