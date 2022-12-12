'''1 предложить улучшения кода для четырёх уже решённых задач:
С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
Начиная с 3 семинара.'''

'''LAMBDA'''
'''Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12'''

# lst = [2, 3, 5, 9, 3]
#
# print(f'на нечет. позициях эл-ты {[lst[x] for x in range(1, len(lst), 2)]}, so the result is {sum(lst[i] for i in range(1, len(lst), 2))}')


'''ENUMERATE'''
'''Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19'''

# lst = [1.1, 1.2, 3.1, 5, 10.01]
# max, min  = float('-inf'), float('+inf')
#
# for val, i in enumerate(lst):
#     curr = i - i//1
#     if curr > max: max = curr
#     elif curr < min: min = curr
#     else: continue
#     min_max = [min, max]
#
# print(min_max[1] - min_max[0])

'''1 Напишите программу, удаляющую из файла все слова, содержащие "абв".'''

file = 'абв абввб воа ввабв'
result = file.split(' ')
# file.close()
result1 = ''

# for i in result:
#     if 'абв' in i: continue
#     result1 += i + ' '
result1 = map(result1, result if result, filter("абв" not in result, result))
print(result1)

# print(*[x for x in result if 'абв' not in x])