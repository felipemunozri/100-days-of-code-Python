import time


def speed_calc_decorator(funct):
    def wrapper():
        start = time.time()
        funct()
        stop = time.time()
        print(stop - start)

    return wrapper


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


fast_function()  # Will automatically decorate fast_function.
slow_function()  # Will automatically decorate slow_function.
