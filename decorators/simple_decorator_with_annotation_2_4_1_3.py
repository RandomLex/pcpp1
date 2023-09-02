def simple_decorator(function):
    print(f'We about to run {function.__name__}')
    return function


@simple_decorator
def simple_function():
    print('Simple function')


simple_function()