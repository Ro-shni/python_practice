#GUESS THE NUM

import random
guessnum = random.randint(1,100)
print(guessnum)
mynum = int(input("guess the num : "))
while guessnum != mynum:
    if guessnum < mynum:
        print("guess low")
    else:
        print("guess high")
    mynum = int(input("guess the num"))
print("correct")

