def val_checker (l_func):
    def _val_checker(func):

        from functools import wraps
        @wraps(func)
        def wrapper(num):
            if l_func(num):
                print(func(num))
            else:
                raise ValueError(f'wrong val {num}')

            return  wrapper

    return _val_checker

@val_checker(lambda x: x >0)
def calc_cube(x):
    return x ** 3

try:
    a = calc_cube(5)
    print(help(calc_cube))
except (ValueError, TypeError) as err:
    print(err)
