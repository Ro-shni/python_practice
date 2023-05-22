def palindrome_num(num):
    for i in range(num+1,2*num):
        now = str(i)
        if now[::-1] == now :
            return now

print(palindrome_num(242))

def pal(num):
    num = num+1
    while(str(num)[::-1] == str(num)):
        return num
    return pal(num)
print(pal())