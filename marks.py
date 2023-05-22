#FINDING AVG MARKS AND ASSIGNING GRADES 
a = int(input("enter the value of a (a<10): "))
b = int(input("enter the value of b(b<10): "))
avg = a+b/2
sum = a+b
print(avg)
if(sum>15 & sum<=20):
    print("A GRADE")
elif(sum>10& sum<=15):
    print("B GRADE")
else:
    print("FAIL")