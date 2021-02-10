def merge_sorted(arr1,arr2):
    sorted_arr = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):  
        if arr1[i] < arr2[j]:
            sorted_arr.append(arr1[i])
            i += 1
        else:
            sorted_arr.append(arr2[j])
            j += 1
    while i < len(arr1):
        sorted_arr.append(arr1[i])
        i += 1
    while j < len(arr2):
       sorted_arr.append(arr2[j])
       j += 1
    return sorted_arr

def merge_sort(arr):
    if len(arr) < 2:
        return arr[:]
    else:
        middle = len(arr) // 2
        l1 = merge_sort(arr[:middle])
        l2 = merge_sort(arr[middle:])
        return merge_sorted(l1,l2)



#Program Execution
l = [8,6,2,5]
print(divide_arr(l))

#Steps
# 1. Compare first element in each list and append smaller element
# 2. Using indices and an iterator perform same comparison for all elements in both lists
# 3. Move marker up by 1 position after smaller number is found 
# 4. Copy remaining list tonce comparisons are complete and there are items still remaining in one of the lists