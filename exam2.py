#2
matriza = []
for i in range(3):
    matriza.append(tuple(map(int, input().split())))
result = tuple([min(i) for i in matriza])
print(result)