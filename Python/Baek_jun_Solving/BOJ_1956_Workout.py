INF = float('inf')
answer = INF

V, E = map(int, input().split())
matrix = [[INF] * V for _ in range(V)]

for _ in range(E):
    a, b, c = map(int, input().split())
    matrix[a-1][b-1] = c

for k in range(V):
    for i in range(V):
        for j in range(V):
            if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                matrix[i][j] = matrix[i][k] + matrix[k][j]

for i in range(V):
    for j in range(V):
        answer = min(answer, matrix[i][j] + matrix[j][i])

if answer == INF:
    print('-1')
else:
    print(answer)
