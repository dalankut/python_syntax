# *** Типы данных ***

# целочисленные тип данных (intenger, int)
my_int = 123

# тип данных чисел с плавающей точкой (вещественные числа) (float)
my_float = 3.14

# конвертация из float в int
result = int(my_float)
# конвертация из int в float
result = float(my_int)
# print(result)

# строкой тин данных (символы, слова, тексты) (string, str)
my_str_1 = 'python'
my_str_2 = "мой текст"
my_char = 'A'
my_text = '''
многострочный
текст
'''

my_text_2 = "мой 'текст' с кавычками"
# print(my_text_2)

# способы форматирования строк
# 1. Конкатенация строк - старый способ
str_1 = "Hello"
str_2 = "World"
num_1 = 1000
res = str_1 + ' ' + str_2 + ' ' + str(num_1)

# f-string (f-строка) - новый способ
str_3 = "Число = "
num_2 = 100

# res = f"{str_3}{num_2}"
# res = f"Число = {num_2}"

num_3 = 100.2564636

res = f"Number: {num_3:.3f}"
# print(res)

# булевы типы данных (boolean, bool)
# в честь Джорджа Буль (булева алгебра)

bool_1 = True # логическая 1
bool_2 = False # логический 0

# Арифмитические операции

a = 10
b = 3

# сложение
res = a + b

# вычитание
res = a - b

# умножение
res = a * b
# обычное деленеие
res = a / b
# целочисленное деление
res = a // b

# деление по остатку
res = a % b
print(res)