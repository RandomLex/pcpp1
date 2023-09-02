class SimpleDecorator:
    def __init__(self, decorated_function):
        self.function = decorated_function

    def __call__(self, *args, **kwargs):
        print(f'{self.function.__name__} was called with the following arguments')
        print(f'\t{args}\n\t{kwargs}\n')
        self.function(*args, **kwargs)
        print('Decorator is still working')

@SimpleDecorator
def combiner(*args, **kwargs):
    print(f'\tHello from the decorated function; received arguments: {args}, {kwargs}')


combiner('a', 'b', exec='yes')