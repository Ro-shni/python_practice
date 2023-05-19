import random
num = random.randint(0,11)
ans = num
ele = int(input("enter the number:"))
while(num!=ele):
    if num > ele:
        print("guess heigher")
    else:
        print("guess lower")
    ele = int(input("enter the number: "))
print("you are correct")
            
