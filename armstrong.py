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