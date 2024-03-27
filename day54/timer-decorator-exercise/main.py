import time
# current_time = time.time()
# print(current_time)

def speed_calc_decorator(f):
    def wrapper():
        start = time.time()
        f()
        total =  time.time() - start
        print(f"{f.__name__} run speed: {total}")

    return wrapper

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i
        
@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i

fast_function()
slow_function()
