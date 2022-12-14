#3 урок задание 2
# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16]
# [2, 3, 5, 6] => [12, 15]
import random

size = int(input('Введите размер списка: '))
min = int(input('Введите минимальное значение элемента списка: '))
max = int(input('Введите максимальное значение элемента списка: '))
#list comprehension
my_list = [random.randint(min, max) for i in range(size)]
print(my_list)
#list comprehension
new_list =[my_list[i]*my_list[size-i-1] for i in range(size // 2)]
if size % 2 != 0:
    new_list.append(my_list[size // 2 ] ** 2)
print(new_list)