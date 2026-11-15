import time 
 
def measure_time(func, arg, repeats=5, calls=1): 
    """Time of one call to func(arg), in milliseconds.""" 
    func(arg)                     # warm-up call, result thrown away 
    best = None 
    for _ in range(repeats): 
        start = time.perf_counter() 
        for _ in range(calls): 
            func(arg) 
        taken = (time.perf_counter() - start) * 1000 / calls 
        if best is None or taken < best: 
            best = taken 
    return best 
 
def time_once(func, arg): 
    """A single timing of func(arg), in milliseconds.""" 
    start = time.perf_counter() 
    func(arg) 
    return (time.perf_counter() - start) * 1000


def sum_loop(n):
    total = 0
    for i in range(1,n+1):
        total += i
    return total

print(measure_time(sum_loop,800000))