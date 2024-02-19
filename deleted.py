def find_deleted_number(arr, mixed_arr):
    a = 0
    b = 0
    for i in arr:
        a += i
    
    for i in mixed_arr:
        b += i
    return a-b
    

    
print(find_deleted_number([1,2,3,4,5], [3,4,1,5]))
