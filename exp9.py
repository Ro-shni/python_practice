str1 = str(input("enter 1st string: "))
str2 = str(input("enter 2nd string: "))
len1 = len(str1)
len2 = len(str2)
if len1 != len2:
    print("Invalid")
else:
    for i in range(0,len1):
        print(str2[i], end=" ")
        print(str1[i], end=" ")
        i=i+1

