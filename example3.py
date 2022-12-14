#3 Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
n = int(input("Введите число n, больше 0 "))
#list comprehension
my_list = [(1 + 1/i) ** i for i in range(1, n + 1)]
result = sum(my_list)
print(f'Список: {my_list} \nСумма элементов списка равна {result:.{2}f}')