
import time 
# recursive countdown timer 
def recur_coundown_timer(n):
    #base case 
    if n == 0: 
        return n
    else: 
        print(n)
        time.sleep(1)
        return recur_coundown_timer(n-1)
#iterative countdown 
def iter_countdown_timer(n):
    while n > 0:
        print(n)
        time.sleep(1)
        n -= 1
    print(n)

z = 5

recur_coundown_timer(5)

print(f"Counting down from {z}: ")

# iter_countdown_timer(z)


