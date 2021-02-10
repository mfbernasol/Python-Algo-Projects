# def divide_arr(arr):
#     if len(arr) < 2:
#         return arr[:]
#     else:
#         middle = len(arr) // 2
#         l1 = divide_arr(arr[:middle])
#         l2 = divide_arr(arr[middle:])
#         return merge_sorted(l1,l2)

# l = [8,6,2,5]
# divide_arr(l)