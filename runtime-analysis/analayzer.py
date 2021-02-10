import time 
import random
from demos import quicksort, merge_sort,bubble_sort

def create_random_list(size, max_val):
    ran_list = []
    for num in range(size):
        ran_list.append(random.randint(1,max_val))
    return ran_list

def analyze_func(func_name, arr):
    start = time.time()
    func_name(arr)
    end = time.time()
    seconds = end - start
    print(f"{func_name.__name__.capitalize()}\t->Elapsed time {seconds}")

size = int(input("Enter size of list you want to create: "))
max_val = int(input("Enter the max value of the range: "))

l = create_random_list(size,max_val)

analyze_func(quicksort,l)
analyze_func(merge_sort,l)
analyze_func(bubble_sort,l.copy())



