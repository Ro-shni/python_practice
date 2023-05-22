#febnoic series 
def fibo():
    firstnum = 0
    secondnum = 1
    while(True):
        nextval = firstnum + secondnum
        yield nextval
        firstnum,secondnum = secondnum,nextval
g = fibo()
num = int(input("enter no of series"))
print("0")
for i in range(1,num):
    print(next(g),end=" ")