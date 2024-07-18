def print_params(a=1, b='строка', c=True):
    return a, b, c


print(print_params())
print(print_params(2, False))
print(print_params(b=25))
print(print_params(c=[1, 2, 3]))

values_list = [69, 'Python', (1, 2, 3)]
values_dict = {'1': True,
               '2': 2,
               '3': 'third'}


def print_params1(*args, **kwargs):
    print(*args, **kwargs)


print_params1(values_list, values_dict)

values_list_2 = [54.32, 'строка']


def print_params2(*args, a=42):
    print(*values_list_2, a)


print_params2()
