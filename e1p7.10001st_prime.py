def is_prime(num):
    if num<2:
        return False
    if num in [2,3,5,7]:
        return True
    if num%2==0:
        return False
    r=3
    while r<=num**0.5:
        if num%r==0:
            return False
        r=r+2
    return True

def nth_prime(step):
    num,pos=2,1
    while num<=step:
        if is_prime(num):
            pos=pos+1
        num+=1
    return num

print(nth_prime(10001))