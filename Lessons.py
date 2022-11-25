import random
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_2, i, list_j = [], 0, []

while i < len(list_1):
    j = random.randint(0, len(list_1)-1)
    list_j.append(j)
    if j not in list_j:
        list_2[i] = list_1[j]
        print(list_2)
        list_2.append(list_2[i])
        print(list_2)
        i += 1
print(list_2)