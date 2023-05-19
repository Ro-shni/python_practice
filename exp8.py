import random
sen = input("enter the word: ")
length = len(sen)
new1 = [sen.count('a'),sen.count('e'),sen.count('i'),sen.count('o'),sen.count('u')]
if new1.count(0)>1:
    print("contains vowels")
else:
    print("no vomels present")
    
