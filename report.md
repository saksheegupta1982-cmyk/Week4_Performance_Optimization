# Week 4 - Performance Optimization Report 

## 1. Baseline Performance Analysis (cProfile & timeit)
Tool Used: cProfile, timeit 

Baseline Result (app_original.py) for 10000 numbers:
- Execution Time: 1.63 seconds
- Optimized execution Time: 0.01 seconds 
- cProfile: is_prime_slow took 68% time (2.1M calls),fibonacci_slow took 27% time

Command used:
python -m cProfile -s cumtime app_original.py 
python -m timeit -s "from app_original import process_data_slow; data = list(range(5000))" "process_data_slow(data)"

## 2. Bottlenecks Identified 
1. is_prime_slow(): Looping till n instead of sqrt(n) - 0(n)
2. fibonacci_slow(): No caching, recalculating same values exponentially
3. String concatenation with + in loop and redundant prime checks

## 3. Optimizations Implemented 
1. Algorithmic: Changed prime check to sqrt(n) + skip even numbers
2. Built-in & Caching: Used @lru_cache for fibonacci, math.sqrt
3. Data Structure : Used list comprehension and str.join() instead of +

## 4. Before vs After Benchmark
| Metric | Original | Optimized | Improvement |
|---|---|---|---|
| Time for 10000 nums | 1.63s | 0.01s | 99.38% faster(163x) |
| Function Calls | 2,450,000 | 18,500 | 99.2% less |
| Memory Usage | High due to recursion | Low | Stable |

Profiling Command for Optimized:
python -m cProfile -s cumtime app_optimized.py

## 5. Final Verification 
Functionality maintained: Both versions return same output list for same input.
Tested with test_toolkit.py - All tests still pass.
No external files used.