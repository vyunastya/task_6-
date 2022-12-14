#4 Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных индексах. Индексы вводятся одной строкой, через пробел
n = int(input("Введите число N, больше 0 "))
#list comprehension
my_list = [i for i in range(-n, n + 1)]
print(my_list)
str = input("Введите номера индексов для перемножения: ") #Ввод корректных индексов
multiplication = 1
#Map использую
my_number=list(map(int, str.split()))
print(my_number)
# enumerate использую
for i, item in enumerate(my_number):
        multiplication *= my_list[item]
print(f'Произведение элементов списка равно {multiplication}')