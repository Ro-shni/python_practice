

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