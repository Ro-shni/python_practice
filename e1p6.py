#problem6 E1
sum1=0
for i in range(1,11):
    sum1=sum1+i**2
print(sum1)

sum2=0
for k in range(1,11):
    sum2=sum2+k
print(sum2**2)

result=sum2**2-sum1
print(result)