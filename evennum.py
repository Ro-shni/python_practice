#even number
num1 = int(input("enter first limit"))
num2 = int(input("enter end limit"))
for i in range(num1,num2+1):
    if(i%2==0):
        print(i)