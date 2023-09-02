def simple_decorator(universal_function):

    def internal_wrapper(*args, **kwargs):
        print(f'"{universal_function.__name__} was called with the following arguments"')
        print(f'\t{args}\n\t{kwargs}\n')
        universal_function(*args, **kwargs)
        print('Decorator is still operating')

    return internal_wrapper


@simple_decorator
def combiner(*args, **kwargs):
    print('\tHello from decorated function; received arguments:', args, kwargs)


combiner('a', 'b', exec='yes')
