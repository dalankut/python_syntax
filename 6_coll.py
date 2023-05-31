# Коржет (tuple)

# упорядоченная неизменяемая (иммутабельная) коллекция

# нельзя добавлять, заменять, удалять элементы

# создание предварительно заполненного кортежа

tuple_1 = (10, 20, 30, 0, 5, 3)
tuple_2 = tuple([1, 50, 3.14, "python"])
tuple_3 = tuple("hello, tuple!")

# print(tuple_3)

# чтение значений элементов кортежа
val_1 = tuple_2[-1]

# срез кортежа
slice_1 = tuple_3[2:7]
slice_1 = tuple_3[:7]
slice_1 = tuple_3[7:]
slice_1 = tuple_3[::2]
slice_1 = tuple_3[3::2]
slice_1 = tuple_3[-1:-3:-1]
slice_1 = tuple_3[-3:-1]
slice_1 = tuple_3[::-1]
# print(slice_1)

# методы кортежа
tuple_4 = (1,2,1,1,2,3)

res = tuple_4.count(1)

# print(res)

# print(tuple_4.index(2))

# Словать (dict, dictionary)

# Неупорядоченная изменяемая (мутабельная) коллекция - нету индексов

# элементы словаря - пара "ключ-значение"

# создание пустого словаря
dict_1 = {}
dict_1 = dict()

# создание предварительно заполненного словаря
dict_2 = {5:1000, 0:3.14, 'A':20, "abc":"python", "кортеж":(1,2,3)}
dict_3 = dict([(10, 20), ("key", "value"), (2, dict_2)])
dict_4 = dict(a=100, b=200)

# print(dict_4)

# чтение значение
val_2 = dict_2['A']
val_2 = dict_2[0]

# print(val_2)

# замена значений
dict_2["A"] = 777

# добавление значений
dict_2['B'] = 888

# удаление значений
del dict_2["A"]
# print(dict_2)

# методы
# print(dict_3)

res = list(dict_3.items())
res = list(dict_3.values())
res = list(dict_3.keys())

# print(res)
# остальные методы самостоятельно
# множество (set)