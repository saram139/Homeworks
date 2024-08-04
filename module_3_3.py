def print_params(a=True, b=20, c='Anton'):
    print(a, b, c)


# 1.
print_params()
print_params(19)
print_params(False, 'Ivan')
print_params(b=25)
print_params(c=[1, 2, 3])
# 2.
values_list = [False, 'Alex', 34]
values_dict = {'a': 11, 'b': True, 'c': 'Egor'}
print_params(*values_list)
print_params(**values_dict)
# 3.
values_list_2 = [54.32, 'Denis']
print_params(*values_list_2, 42)
