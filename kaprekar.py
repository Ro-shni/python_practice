
def kap(num):
    kaprekar = 6174
    num_str = str(num)
    num_arr1 = list(num_str)
    num_arr2 = list(num_arr1)
    num_arr1.sort()
    num_arr2.sort(reverse=True)
    sorted_num_str1 = ''.join(num_arr1)
    sorted_num_str2 = ''.join(num_arr2)
    sor1 = int(sorted_num_str1)
    sor2 = int(sorted_num_str2)
    diff = sor2-sor1
    print(diff)
    
        
kap(3524)
