def add_everything_up(a, b):
    try:
        result = a + b
    except TypeError:
        result = str(a) + str(b)
    return result


print(add_everything_up(123.45, "строка"))
print(add_everything_up("яблоко", 4215))
print(add_everything_up(123.45, 7))
print(add_everything_up("яблоко", "строка"))
