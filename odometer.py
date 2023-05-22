def digits(num):
    l2=[]
    lower_limit = num*"1"
    upper_limit = num*"9"
    lower = int(lower_limit)
    upper = int(upper_limit)

    for i in range(lower,upper+1):
        if "0" in str(i):
            pass
        else:
            l1=[]
            for j in str(i):
                new1 = int(j)
                l1.append(new1)
            if l1[0]==l1[1] or l1[1]==l1[2] or l1[0]==l1[2]:
                pass
            elif l1[0]<l1[1] and l1[1]<l1[2]:
                l2.append(i)
    return l2

print(digits(3))




