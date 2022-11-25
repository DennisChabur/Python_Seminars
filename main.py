import random

'''1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.'''

s = input("Введите что угодно, программа посчитает цифры")
count = 0

for i in s:
    if i in "1234567890":
        count += int(i)
print(count)

'''2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)'''

N = int(input("Введите число. Выйдет список фактериалов"))


def factorial(n):
    if n == 1: return 1
    return n * factorial(n - 1)


list_ = []

for i in range(1, N + 1):
    list_.append(factorial(i))
print(list_)

'''3. Задайте список из n чисел последовательности (1 + 1/n)**n и выведите на экран их сумму.
- Для n = 6: [2.0, 2.25, 2.37, 2.44, 2.488, 2.52]     ->       14.072'''

n = int(input("Input number to get odd list"))
list_ = []

for i in range(1, n + 1):
    func = (1 + 1 / i) ** i
    list_.append(round(func, 2))

print(list_)

'''4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
  Найдите произведение элементов на указанных позициях. 
  Позиции вводятся с клавиатуры. 5 2 6'''

N = int(input("Input number to get a list [-N,N]"))
list_ = []

for i in range(-N, N + 1):
    list_.append(i)
print(f'You\'ve got the list {list_}')
print("Now input two indexes to product this in the list")

num1, num2 = int(input()), int(input())

print(list_[num1] * list_[num2])

'''5. Реализуйте алгоритм перемешивания списка.'''
print('\n\n')
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_2 = []
list_j = ''
i = 0

while i <= len(list_1):
    j = random.randint(0, len(list_1)-1)
    list_j += str(j)
    print(j, list_j)
    if str(j) not in list_j:
        print(j)
        list_2[i] = list_1[j]
        list_2.append(list_2[i])
        i += 1
print(list_2)
