def addition_simple(a, b):
    return a + b



def addition_args(*args):
    result = 0
    for n in args:
        result += n
    return result



def example_kwargs(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


example_kwargs(test=2, shit=True)