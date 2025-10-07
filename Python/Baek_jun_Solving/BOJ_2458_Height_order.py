import sys
sys.stdin = open('input.txt')
# floyd-warshall

N, M = map(int, input().split())    # n - nodes, m - edges, one-way
INF = float('inf')
graph = ([[0] * (N+1)]) + [[0] + [INF] * N for _ in range(N)]   # 1-base idx
cnt = 0

for _ in range(M):    # connection list
    a, b = map(int, input().split())
    graph[a][b] = 1

for i in range(1, N + 1):   # self -> 0
    graph[i][i] = 0

for k in range(1, N + 1):    # add routes visiting k
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i == j:
                continue
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# for this question specifically,
# if (i,j) possible -> (j, i) ok
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j:
            continue
        graph[i][j] = min(graph[i][j], graph[j][i])

for row in graph:    # look for possible ans
    if sum(row) < INF:
        cnt += 1

print(cnt - 1)    # - 1 because row 0

# time out in python, pass in pypy...
