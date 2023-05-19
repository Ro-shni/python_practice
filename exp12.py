import random 
sum=0
for i in range(1,21):
   num=random.randint(1,101)
   a = []
   a.insert(i,num)
   sum = sum+num
   maxim = max(a)
   minim = min(a)
   print(a,end='')
   print()
print(sum/20)

print(maxim)
print(minim)

