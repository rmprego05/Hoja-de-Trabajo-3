def combinar():
    list1 = [1, 5, 6, 9, 11]
    list2 = [3, 4, 7, 8, 10]
    
     
    print ("The original list 1 is : " + str(list1))
    print ("The original list 2 is : " + str(list2))
    
    
    size_1 = len(list1)
    size_2 = len(list2)
    
    res = []
    i, j = 0, 0
    
    while i < size_1 and j < size_2:
        if list1[i] < list2[j]:
            res.append(list1[i])
            i += 1
    
        else:
            res.append(list2[j])
            j += 1
    
    res = res + list1[i:] + list2[j:]
    
    print ("The combined sorted list is : " + str(res))