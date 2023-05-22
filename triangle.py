#triangle
def tri(a,b,c):
    if(a==b==c):
        print("equalateral")
    elif(a!=b!=c):
        print("scalene")
    elif(a==b!=c|a==c!=b |b==c!=a):
        print("isosceles")
    elif(a+b<c | a+c<b | b+c<a | c+a<b):
        print("invalid")
    else:
        print("invalid")
tri(4,5,7)                                    #output: scalene

