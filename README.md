# Week 4 - Performance Optimization

This project demonstrates performance optimization in python.

Files:
- app_original.py : Slow version with bottlenecks 
- app_optimized.py : Fast version with improvements
- report.md : Detailed profiling and comparison

How to run profiling:
python -m cProfile -s cumtime app_original.py
python -m cProfile -s cumtime app_optimized.py
Result : Optimized code is 163x faster (99.38% )