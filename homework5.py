immutable_var = 1, 2, 'a', False, 'Python'
print('Неизменяемый кортеж:' , immutable_var)
#immutable_var[3] = True
mutable_list = [1, 2, 'a', False, 'Python']
mutable_list.remove(1)
mutable_list[2] = True
mutable_list.append('Urban')
print('Изменяемый список:' , mutable_list)
