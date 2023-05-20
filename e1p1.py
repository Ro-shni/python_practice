def multi_3_5(num):
    result = 0
    for i in range(num):
        if i % 3 == 0 or i % 5 == 0:
            result += i
    return result

print(multi_3_5(1000)) 