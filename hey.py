def perm_check(word,check_w):
    for i in range(len(word)):
        new = (word[i::]+word[0:i])
        if check_w == new:
            return True
    return False    

print(perm_check("abcde","bcdea"))