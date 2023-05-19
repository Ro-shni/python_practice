num1 = float(input("enter 1st greatest number: "))
num2 = float(input("enter 2nd number: "))
diff=num1-num2
if diff<=0.001:
    print("numbers are very close ")
else: 
    print("huge difference")
