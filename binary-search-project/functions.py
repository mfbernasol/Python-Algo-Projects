import time
from random import choice
from string import ascii_lowercase as letters

def binary_search(n, arr):
  start = 0
  stop = len(arr)-1
  while start <= stop:
    mid = (start+stop)//2
    if n == arr[mid]:
      return f"{n} found at index: {mid}"
    elif n > arr[mid]:
      start = mid + 1
    else: 
      stop = mid - 1
  return f"{n} not found in list"

def analyze_func(func_name, *args):
    start = time.time()
    func_name(*args) 
    end = time.time()
    seconds = end - start
    print(f'{func_name.__name__.capitalize()}\t-> Elasped Time: {seconds: .5f}')


def generate_name(length_of_name):
    return ''.join(choice(letters) for i in range(length_of_name))

def get_domain(list_of_domains):
    return choice(list_of_domains)

def generate_emails(length_of_name, list_of_domains, total_emails):
    emails = []
    for num in range(total_emails):
        emails.append(generate_name(length_of_name) + "@" + get_domain(list_of_domains))
    return emails