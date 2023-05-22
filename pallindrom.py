'''#pallindrome
str1 = list("SVECW")
str2 = str1.copy()
str2.reverse()
if str1 == str2:
    print("pallindrome")
else:
    print("not a pallindrome")
                          #output: not a pallindrome'''

def pal(str1: list)->bool:
    str2 = str1.copy()
    str2.reverse()
    return str1 == str2

print(pal(list("pallindrome")))


def pal(str1: str)->bool:
    return str1[::-1] == str1

print(pal("pallindrome"))

#ctrl text = ""