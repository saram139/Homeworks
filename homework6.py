my_dict = {'Антон': 1996, 'Егор': 2000, 'Роман': 1992}
print('Dict:', my_dict)
print('Existing value:', my_dict['Антон'])
print('Not existing value:', my_dict.get('Елена'))
my_dict.update({'Елена': 2001, 'Ольга': 1990})
print('Deleted value:', my_dict.pop('Егор'))
print('Modified dictionary:', my_dict, '\n')

my_set = {1, 2, 1, 3, (1, 2), '7', '7'}
print('Set:', my_set)
my_set.add('Банан')
my_set.add(7)
my_set.discard(3)
print('Modified set:', my_set)