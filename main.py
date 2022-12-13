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


'''FILTER & MAP & LAMBDA'''
'''Тут часть кода из семинарского занятия - реализация моей части'''

# import ui_c
# from calculations import sum_c, sub_c, mult_c, div_c
#
#
# inputed_sign = ui_c.input_c
# converted_to_list_of_complex = list(map(complex, filter(lambda x:
#                                 x not in '+-*/', inputed_sign())))
#
#
# def check_action(inputed_sign):
#     if inputed_sign[1] == '+': return sum_c
#     elif inputed_sign[1] == '-': return sub_c
#     elif inputed_sign[1] == '*': return mult_c
#     elif inputed_sign[1] == '/': return div_c
#
#
# def check_c(list_of_complex):
#     if (type(list_of_complex[0]) == complex) and \
#             list_of_complex[1] in '+-*/' and \
#             (type(list_of_complex[2]) == complex):
#         return True
#     else:
#         print("Некорректный ввод")
#         return False
