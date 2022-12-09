import random as r

'''1 Напишите программу, удаляющую из файла все слова, содержащие "абв".'''

# file = open('text.txt', 'r', encoding='utf-8')
# result = file.read().split(' ')
# file.close()
# result1 = ''
# for i in result:
#     if 'абв' in i: continue
#     result1 += i + ' '
# print(result1)

# print(*[x for x in result if 'абв' not in x])

'''2 Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит 2021 конфета.
Играют два игрока делая ход друг после друга.
Первый ход определяется жеребьёвкой.
За один ход можно забрать не более чем 28 конфет.
Все конфеты оппонента достаются сделавшему последний ход.
Сколько конфет нужно взять первому игроку, чтобы забрать все
конфеты у своего конкурента?

a) Добавьте игру против бота
b) Подумайте как наделить бота "интеллектом"'''

# last = 121
# player_num = 1
# while last > 0:
#     if player_num > 0:
#         player = 'player 1'
#     else:
#         player = 'player 2'
#     if last <= 28:
#         num = int(input(f"{player} Input number from 0 to {last} \n"))
#     else:
#         num = int(input(f"{player} Input number from 0 to 28 \n"))
#     if num <= 28 and num <= last:
#         last -= num
#     else: print(f"Hey! {player}! Your number is out of range")
#     print(f'{last} is remain \n')
#     player_num *= -1
#     if last == 0: print(f"{player} You win")

'''a) Добавьте игру против бота'''


# def func(last):
#     if last <= 28:
#         num = r.randint(0, last)
#     else:
#         num = r.randint(0, 28)
#     print(f'The bot took {num}')
#     if last - num == 0:
#         print("The bot win")
#         return 0
#     else: return last - num
#
#
# last = 80
#
# while last > 0:
#     if 0 < last <= 28:
#         num = int(input(f"Input number from 0 to {last} \n"))
#     else:
#         num = int(input(f"Input number from 0 to 28 \n"))
#     if num <= 28 and num <= last:
#         last -= num
#     else: print(f"Your number is out of range")
#     print(f'{last} is remain \n')
#
#     if last == 0:
#         print(f"You win")
#         break
#     last = func(last)

'''b) Подумайте как наделить бота "интеллектом"'''

# def func(last):
#     if last <= 28:
#         num = last
#     elif 29 <= last <= 57:
#         num = last - 29
#     else:
#         num = 28
#     print(f'The bot took {num}')
#     if last - num == 0:
#         print("The bot win")
#         return 0
#     else: return last - num
#
#
# last = 80
#
# while last > 0:
#     if 0 < last <= 28:
#         num = int(input(f"Input number from 0 to {last} \n"))
#     else:
#         num = int(input(f"Input number from 0 to 28 \n"))
#     if num <= 28 and num <= last:
#         last -= num
#     else: print(f"Your number is out of range")
#     print(f'{last} is remain \n')
#
#     if last == 0:
#         print(f"You win")
#         break
#     last = func(last)

'''3 Создайте программу для игры в "Крестики-нолики".

Вариант интерфейса:

 1  |  2 | 3
--------------
 4  |  5 | 6
--------------
 7  |  8 | 9
'''


# def from_input_to_place(point):
#     if point == 1: return x00 = 'x00'
#     elif point == 2: return x01 = 'x01'
#     elif point == 3: return x02 = 'x02'
#     elif point == 4: return x10 = 'x10'
#     elif point == 5: return x11 = 'x11'
#     elif point == 6: return x12 = 'x12'
#     elif point == 7: return x20 = 'x20'
#     elif point == 8: return x21 = 'x21'
#     elif point == 9: return x22 = 'x22'

# x00, x01, x02, x10, x11, x12, x20, x21, x22 = 1, 2, 3, 4, 5, 6, 7, 8, 9
#
# def from_input_to_place(point):
#     if point == 1: return x00
#     elif point == 2: return x01
#     elif point == 3: return x02
#     elif point == 4: return x10
#     elif point == 5: return x11
#     elif point == 6: return x12
#     elif point == 7: return x20
#     elif point == 8: return x21
#     elif point == 9: return x22
#
# def point_to_mark(x):
#     x = 'X'
#
# def paint_grid(x00 = 1, x01 = 2, x02 = 3,
#                x10 = 4, x11 = 5, x12 = 6,
#                x20 = 7, x21 = 8, x22 = 9):
#     print(f' {x00} | {x01} | {x02} ')
#     print('-' * 11)
#     print(f' {x10} | {x11} | {x12} ')
#     print('-' * 11)
#     print(f' {x20} | {x21} | {x22} ')
#
#
# paint_grid()
#
# point = int(input("input number from 1 to 9 if you want to point there your mark\n"))
#
# # while paint_grid().isdigit:
#
# paint_grid(point_to_mark(from_input_to_place(point)))



'''4 Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

Входные и выходные данные хранятся в отдельных текстовых файлах.

aaaasssdddwwwwwwwwwwwweeeffffff -> 4a3s3d9w3w3e6f
4a3s3d9w3w3e6f-> aaaasssdddwwwwwwwwwwwweeeffffff'''

# str = 'aaaasssdddwwwwwwwwwwwweeeffffff'
# lst = []
# syl = str[0]
# num = 1
# for i in range(1, len(str)):
#    if str[i] == syl:
#        num += 1
#        if num == 9:
#            lst.append(f'{num}{syl}')
#            num = 0
#            continue
#        if i == len(str) - 1:
#                lst.append(f'{num}{syl}')
#    else:
#        lst.append(f'{num}{syl}')
#        syl = str[i]
#        num = 1
#
# print(*lst, sep='')



'''5* Дан список чисел. Найдите все возрастающие последовательности. Порядок элементов менять нельзя.

*Пример:*

[1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.'''

list1 = [1, 5, 2, 3, 4, 6, 1, 7]
list_res = []

for i in range(len(list1)):
    list_res.append(list1[i])
    for j in range(i + 1, len(list1)):
        if list1[j] > list_res[i]:
            list_res.append(list1[j])
    print(list_res)