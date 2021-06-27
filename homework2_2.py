el_quantity = int(input('Введите количество элементов:\n'))
my_lists = []
for i in range(el_quantity):
    el_list = (input('Введите слово или цифру:\n'))
    my_lists.append(el_list)
print(my_lists)
j = 0
for i in range(len(my_lists) // 2):
    my_lists[j], my_lists[j + 1] = my_lists[j + 1], my_lists[j]
    j += 2
print(my_lists)