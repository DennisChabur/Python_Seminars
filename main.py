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


'''3 Создайте программу для игры в "Крестики-нолики".

Вариант интерфейса:

 1  |  2 | 3
--------------
 4  |  5 | 6
--------------
 7  |  8 | 9
'''




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