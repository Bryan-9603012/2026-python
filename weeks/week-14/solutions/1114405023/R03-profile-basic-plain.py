import cProfile
import math
import pstats
import time
import timeit
from functools import wraps

def timed(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - t0
        print(f'[timed] {func.__name__}: {elapsed * 1000:.2f} ms')
        return result
    return wrapper

@timed
def sum_of_squares(n):
    return sum((i * i for i in range(n)))

def bench_timeit():
    n = 10000
    t1 = timeit.timeit('sum(i*i for i in range(n))', globals={'n': n}, number=1000)
    t2 = timeit.timeit('sum(map(lambda i: i*i, range(n)))', globals={'n': n}, number=1000)
    print(f'[timeit] genexp = {t1:.3f}s, map+lambda = {t2:.3f}s')

def workload():
    total = 0
    for i in range(1, 5000):
        total += math.sqrt(i) * math.sin(i)
    return total

def bench_cprofile():
    pr = cProfile.Profile()
    pr.enable()
    workload()
    pr.disable()
    print('[cProfile] 前 5 名：')
    pstats.Stats(pr).sort_stats('cumulative').print_stats(5)
if __name__ == '__main__':
    sum_of_squares(1000000)
    bench_timeit()
    bench_cprofile()
