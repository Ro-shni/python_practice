#even number
num1 = int(input("enter first limit"))
num2 = int(input("enter end limit"))
for i in range(num1,num2+1):
    if(i%2==0):
        print(i)

#vALID CODE
import random
digit = random.randint(500000,599999)
print(str(digit))  

#armstrong code
num = int(input("Enter a number: "))
siz = len(str(num))
sum =0
temp = num
while temp>0:
    digit = temp%10
    sum = sum + digit**siz
    temp //=10

if num==sum:
    print("is armstrong")
else:
    print("is not armstrong")


#strong num
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

#pattern printing 
alp = str(input("enter a string: "))
siz = len(str(alp))
if alp[0]:
        new = alp[0].upper()
        print(new,end=" ")
for i in range(1,siz+1):
    for j in range(1,i+2):
        print(alp[i],end=" ")

#pattern printing
alp = str(input("enter a string: "))
siz = len(str(alp))
if alp[0]:
        new = alp[0].upper()
        print(new,end=" ")
for i in range(1,siz+1):
    new1=alp[i].upper()
    print(new1,end=" ")
    for j in range(1,i+1):
        print(alp[i],end=" ")

#raising powers
num = int(input("enter the power: "))
num1 = 2**num
ans =0
while num1>0:
    digit = num1%10
    ans=ans+digit
    num1//=10
print(ans)

#largest prime factor

def prime(n):
    i = 2
    while i**i <= n:
        if n%i:
            i +=1
        else:
            n//=i
        return n
print(prime(600851475143))




