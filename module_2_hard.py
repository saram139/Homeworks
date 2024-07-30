number_from_stone = int(input("Введите число из первой вставки (от 3 до 20): "))
list_by_number = []
result = []
for i in range(number_from_stone):
    list_by_number.append(i + 1)

for i in range(0, number_from_stone):
    for j in range(i, number_from_stone):
        if number_from_stone % (list_by_number[i] + list_by_number[j]) == 0 and list_by_number[i] != list_by_number[j]:
            result.append(list_by_number[i])
            result.append(list_by_number[j])

print('Нужный пароль:', *result)
