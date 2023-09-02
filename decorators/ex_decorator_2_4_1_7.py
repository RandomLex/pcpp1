# Create a function decorator that prints a timestamp
# (in a form like year-month-day hour:minute:seconds, e.g. 2019-11-05 08:33:22)
# Create a few ordinary functions that do some simple tasks, like adding or multiplying two numbers.
# Apply your decorator to those functions to ensure that the time of the function executions can be monitored.
from datetime import datetime


def time_stamp(function):
    def __current_time_stamp():
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def internal_wrapper(*args):
        print(__current_time_stamp())
        res = function(*args)
        return res

    return internal_wrapper


@time_stamp
def add(a, b):
    return a + b


@time_stamp
def mul(a, b):
    return a * b


print(add(2, 3))
print(mul(2, 3))
