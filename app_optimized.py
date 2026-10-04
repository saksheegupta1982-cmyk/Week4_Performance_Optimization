# app_optimized.py - Optimized version
from functools import lru_cache  # For caching
import math 
import time

def is_prime_fast(n):
    """
    Optimization 1 : Algorithmic Improvement
    Changed 0(n) to 0(sqrt(n)) + skip even numbers 
    Logic: A larger factor must have a smaller counterpart below sqrt(n)
    """
    if n < 2:
        return False
    if n == 2: # 2 is only even prime
        return True 
    if n % 2 == 0: # Skip all even numbers
        return False 
    # Only check till sqrt(n) and only odd numbers
    # e.g., for 9999, loop only till 100 ,not 9997
    for i in range(3,int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False 
    return True

@lru_cache(maxsize = None) # Optimization 2: Memoization
def fibonacci_fast(n):
    """
    Optimization 2: Using Caching (Memoization)
    @lru_cache stores previous results.
    fibonacci(20) now calculated only once,next time taken from cache.
    Time Complexity reduces from 0(2^n) to  0(n)
    """
    if n <= 1 :
        return n 
    return fibonacci_fast(n - 1) + fibonacci_fast(n -2 )

def process_data_fast(data):
    """
    Optimization 3 : Data Structure & Built- in Libraries 
    - List comprehension: Faster than manual for + append(implemented in c)
    - str.join(): Faster than '+' because it allocates memory only once
    """
    # List comprehension - single line, faster, implemented in C
    primes = [n for n in data if is_prime_fast(n)]

    # Using cached fibonacci 
    fibs = [fibonacci_fast (n % 20 ) for n in primes]

    # Optimized string concatenation using join()
    # join() allocates memory once, '+' allocates every time
    final_string = ",".join(map(str,fibs))

    return fibs
if __name__ == "__main__":
    test_data = list(range(10000))
    start = time.time()
    process_data_fast(test_data)
    end = time.time()
    print(f"Optimized took: {end - start:.2f} second")