H, W = map(int, input().split())

cloud_map = [input() for _ in range(H)]
table = [[-1] * W for _ in range(H)]

for i in range(H):
    for j in range(W):
        if cloud_map[i][j] == 'c':
            table[i][j] = 0
            forecast = 1
            for k in range(1, W - j):
                table[i][j + k] = forecast
                forecast += 1

for i in range(H):
    print(*table[i])
