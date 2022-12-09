from math import pi, fabs
import random

'''Задача 1. Вычислить число c заданной точностью d'''

# d = float(input("Введите точность"))
# i, m, pi_ = 1, 1, 0
#
# while abs(pi_ - pi) >= d:
#     pi_ += 4/(i * 2 - 1) * m
#     i += 1
#     m *= -1
# print(pi_, pi, sep='\n')

'''Задача 1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N'''

# N = int(30030)
# res = []
#
# while N != 1:
#     if N % 2 == 0:
#         res.append(2)
#         N /= 2
#     if N % 2 != 0:
#         for i in range(3, int(N+1), 2):
#             if N % i == 0:
#                 res.append(i)
#                 N /= i
#                 break
# print(res)

'''Задача 2. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.'''

# lst = [1, 1, 2, 2, 3, 4, 4, 5, 'dog', 6, 6, 7] # [3, 5, 7]
# dct = dict()
#
# for i in lst:
#     if i not in dct:
#         dct[i] = 0
#     dct[i] += 1
#
# print([x for x in dct if dct[x] == 1])

'''Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
многочлена и записать в файл многочлен степени k.'''


# def get_random_funck(k):
#     lst = list()
#     for i in range(k-1, -1, -1):
#         if random.randint(0, 10) > 4:
#             if random.randint(0, 10) % 2 == 0:
#                 lst.append(f'+ {random.randint(0, 100)}*x**{i} ')
#             else:
#                 lst.append(f'- {random.randint(0, 100)}*x**{i} ')
#     return ''.join(lst)[1::]
#
#
# file1 = open('funck1', 'w')
# file1.write(get_random_funck(7))
# file1.close()
#
# file2 = open('funck2', 'w')
# file2.write(get_random_funck(5))
# file2.close()

'''5 Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
Коэффициенты могут быть как положительными, так и отрицательными. Степени многочленов могут отличаться.'''

# funck1 = '94*x**6-26*x**4+55*x**2-81*x**0'
# funck2 = '1*x**4-96*x**2+12*x**1'
#
# def transform_to_dict(funck):
#     list_funck = []
#     new_position = 0
#     for i in range(len(funck)):
#         if (funck[i] == "+" or funck[i] == "-") and i != len(funck) - 1:
#             list_funck.append(funck[new_position:i].split('*x**'))
#             new_position = i
#         elif i == len(funck) - 1:
#             list_funck.append(funck[new_position:i + 1].split('*x**'))
#
#     def list_into_dict(list_):
#         dict_ = {}
#         for x in list_:
#             key = x[1]
#             dict_[key] = int(x[0])
#         return dict_
#
#     return list_into_dict(list_funck)
#
# dict1_ = transform_to_dict(funck1)
# dict2_ = transform_to_dict(funck2)
#
# # print(dict1_, dict2_, sep='\n')
#
#
# for key in dict1_:
#     if key in dict2_.keys():
#         dict1_[key] = int(dict1_[key]) + int(dict2_[key])
# dict2_.update(dict1_)
#
# # print(dict2_)
# result = ''
#
# for key, value in dict2_.items():
#     if value > 0:
#         result += '+' + str(value) + "*x**" + key
#     result += str(value) + "*x**" + key
#
# print(result)