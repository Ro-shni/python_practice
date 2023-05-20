#BINARY SEARCH - efficiant search
def binary(l,key):
    if len(l)==0:
        return False
    mid = len(l)//2
    if l[mid]==key:
        return True
    elif key<l[mid]:
        return binary(l[:mid],key)
    else:
        return binary(l[mid+1:],key)

l=[100,200,300,400,500,600,700,800,900]
key = 900     #True 



result = binary(l,key)
print(result)
