calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    tuple_ = len(string), string.upper(), string.lower()
    return tuple_


def is_contains(string, list_to_search):
    count_calls()
    new_list_to_search = []
    for i in list_to_search:
        new_list_to_search.append(i.upper())
    return string.upper() in new_list_to_search


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
