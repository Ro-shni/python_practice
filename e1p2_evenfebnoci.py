#even febnoci series

def fibo():
    firstnum = 1
    secondnum = 2
    while(True):
        nextval = firstnum + secondnum
        yield nextval
        firstnum,secondnum = secondnum,nextval
g = fibo()
num = int(input("enter no of series: "))
print("1 2",end=" ")
for i in range(1,num):
        print(next(g),end=" ")
        if next(g)%2 == 0:
            print(next(g),end=" ")
