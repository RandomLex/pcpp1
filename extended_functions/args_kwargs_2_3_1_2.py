def combiner(a, b, *args, c=30, **kwargs):
    print(a, type(a))
    print(b, type(b))
    print(c)
    additional_combiner(*args, **kwargs)


def additional_combiner(*args, **kwargs):
    print(args, type(args))
    print(kwargs, type(kwargs))


combiner(10, '20', 40, 60, 30, argument1=50, argument2='66')
