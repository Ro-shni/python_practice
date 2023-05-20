num = int(input("enter the power: "))
num1 = 2**num
ans =0
while num1>0:
    digit = num1%10
    ans=ans+digit
    num1//=10
print(ans)
