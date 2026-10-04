# app_original.py - Baseline version with intentional bottlenecks
import math 
import time 

def is_prime_slow(n):
    """ 
    Bottleneck 1 : Inefficient algorithm 
    Check divisibility till n-1.Time Complexity 0(n)
    For n= 9999, it will loop 9997 times!
    """
    if n<2:
        return False
    for i in range(2,n): # Should only go till sqrt(n)
        if n % i == 0:
            return False
    return True

def fibonacci_slow(n):
    """
    Bottleneck 2 : Exponential Recursion without caching
    fibonacci(20) calls itself 21891 times repeatedly.
    No memorization used.
    """
    if n <= 1:
        return n
    return fibonacci_slow(n-1)+ fibonacci_slow(n-2)

def process_data_slow(data):
    """
    Bottleneck 3 : Redundant computation + Slow string concatenation 
    - Calls heavy functions inside loop 
    - Using '+' for string in loop creates new string every time (very slow)
    """
    result = [] # Storing results
    final_string = "" # For string concat test 

    for num in data:
        # For every number, we check prime(slow)
        if is_prime_slow(num):
            # If prime,we cakcukate fibonacci (even slower )
            fib = fibonacci_slow(num % 20) # mod 20 to avoid infinite recursion
            result.append(fib)
            # Slow string concatenation - creates new object each time
            final_string = final_string + str(fib)+ ","
    return result 

if __name__ == "__main__":
    # Test data of 10000 numbers 
    test_data = list(range(10000))
    start = time.time()
    process_data_slow(test_data)
    end = time.time()
    print(f"Original took:{end - start:.2f} seconds")        
