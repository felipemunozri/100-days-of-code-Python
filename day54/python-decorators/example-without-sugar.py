import time


def speed_calc_decorator(funct):
    def wrapper():
        start = time.time()
        funct()
        stop = time.time()
        print(stop - start)

    return wrapper


def fast_function():
    for i in range(10000000):
        i * i


def slow_function():
    for i in range(100000000):
        i * i


fast_function = speed_calc_decorator(fast_function)  # Will manually decorate fast_function.
slow_function = speed_calc_decorator(slow_function)  # Will manually decorate slow_function.

fast_function()
slow_function()

