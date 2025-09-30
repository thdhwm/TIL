# union find esque...
from collections import deque
import sys
sys.stdin = open('input.txt')


def outer():
    q = deque()
    q.append((0,0))

    while q:
        i, j = q.popleft()
        parents[i][j] = 0
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]

            if 0 > ni or H <= ni or 0 > nj or W <= nj:
                continue

            if table[ni][nj] == 1:
                continue

            if visited[ni][nj]:
                continue
            
            visited[ni][nj] = 1
            q.append((ni, nj))







H, W = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(H)]

parents = [[1] * W for _ in range(H)]
visited = [[0] * W for _ in range(H)]
parents[0][0] = 0
visited[0][0] = 1

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

outer()

for row in parents:
    print(row)
# ######################################################

# 13 12
# 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 1 1 0 0 0
# 0 1 1 1 0 0 0 1 1 0 0 0
# 0 1 1 1 1 1 1 0 0 0 0 0
# 0 1 1 1 1 1 0 1 1 0 0 0
# 0 1 1 1 1 0 0 1 1 0 0 0
# 0 0 1 1 0 0 0 1 1 0 0 0
# 0 0 1 1 1 1 1 1 1 0 0 0
# 0 0 1 1 1 1 1 1 1 0 0 0
# 0 0 1 1 1 1 1 1 1 0 0 0
# 0 0 1 1 1 1 1 1 1 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0
