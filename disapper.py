def disapper(list1):
    list2 = []
    for i in range(1,len(list1)+1):
        if i in list1:
            continue
        list2.append(i)
    print(list2)
disapper([1,4,6,7,8])
