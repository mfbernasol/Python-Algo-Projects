#Implementation of bubble sort algorithm

def bubble_sort(arr):
    swap_happened = True
    while swap_happened:
        print("Bubble sort status " + str(arr))
        swap_happened = False
        for num in range(len(arr)-1):
            #check if nth element is greater
            if arr[num] > arr[num+1]:
                    swap_happened = True
                    arr[num],arr[num+1] = arr[num+1], arr[num]


#Driver code
nums = [6,8,1,4,10,7,8,9,3,2,5]
bubble_sort(nums)