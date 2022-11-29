'''Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12'''

lst = [2, 3, 5, 9, 3]

print(f'на нечет. позициях эл-ты {[lst[x] for x in range(1, len(lst), 2)]}, so the result is {sum(lst[i] for i in range(1, len(lst), 2))}')

'''Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример: [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]'''

lst = [2, 3, 4, 5, 6]
lst_prod=[]
for i in range(len(lst)):
    if i < len(lst) - i:
        lst_prod.append(lst[i] * lst[len(lst) - i - 1])
print(lst_prod)

'''Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19'''

lst = [1.1, 1.2, 3.1, 5, 10.01]
max, min  = float('-inf'), float('+inf')

for i in lst:
    curr = i - i//1
    if curr > max: max = curr
    elif curr < min: min = curr
    else: continue
    min_max = [min, max]
print(min_max[1] - min_max[0])


'''Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Пример: 45 -> 101101
- 3 -> 11
- 2 -> 10'''

num = int(input("Input your number to transform dec into bin\n"))
result = ""
while num > 0:
    if num % 2 == 0: result += '0'
    else: result += '1'
    num //= 2
print(result[::-1])

'''Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
Пример: для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]'''

num = int(input("Input numbers of fibonachi numbers\n"))
fib_ok = []
fib_odd = []
f0, f1 = 0, 1

for i in range(num + 1):
    fib_ok.append(f0)
    fib_odd.append(f0 * (-1)**(i+1))
    f0, f1 = f1, f0 + f1
print(fib_odd[::-1] + fib_ok[1:])