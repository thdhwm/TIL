table = [['']*15 for _ in range(5)]
for i in range(5):
    row = list(input())
    for char in range(len(row)):
        table[i][char] = row[char]


for j in range(15):
    for i in range(5):
        print(table[i][j], end = '')     
