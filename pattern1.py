rows = int(input("enter a no of rows:"))
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(j,end=' ')
    for k in range(i-1,0,-1):
        print(k,end=" ")
    print()

rows = int(input("enter a no of rows:"))
for i in range(rows,0,-1):
    for j in range(i,0,-1):
        print('*',end=' ')
    print() 