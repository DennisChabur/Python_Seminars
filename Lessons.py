res = [1,2,3,4,5,6]
dct = {}
for i in range(1, len(res), 2):
    dct[str(res[i])]=res[i-1]
print(dct)
