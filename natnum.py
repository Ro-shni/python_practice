#printing natural numbers

def natural(num):
    for j in range(num):
        print(j)
natural(11)

#bigger number
def largest(a,b,c):
    if(a>b & a>c):
        print("a is large")
    elif(b>c):
        print("b is large")
    else:
        print("c is large")
largest(10,11,12) 