data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])]
sum = 0


def calculate_structure_sum(args):
    global sum
    for i in args:
        if isinstance(i, list) or isinstance(i, tuple) or isinstance(i, set):
            calculate_structure_sum(i)
        elif isinstance(i, dict):
            calculate_structure_sum(i.items())
        elif isinstance(i, int):
            sum += i
        elif isinstance(i, str):
            sum += len(i)
    return sum

result = calculate_structure_sum(data_structure)
print(result)
