# Create a decorator which calculates the amount of time that it took to execute a function
import time


def execution_time(func):
    def inner_func(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time is {end-start} seconds")
        return result
    return inner_func


@execution_time
def message(txt):
    for i in range(100000000):
        continue
    return txt


print(message("Hello"))

