# union find esque...
from collections import deque
import sys
sys.stdin = open('input.txt')


def outer():   # max 10000 calc

    q = deque()
    q.append((0, 0))

    while q:
        i, j = q.popleft()
        parents[i][j] = 0
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]

            if 0 > ni or H <= ni or 0 > nj or W <= nj:
                continue

            if table[ni][nj] == 1:
                temp_1.add((ni, nj))

            if visited[ni][nj]:
                continue
            
            visited[ni][nj] = 1
            q.append((ni, nj))

def decay():
    
    while temp_1:
        now_i, now_j = temp_1.pop()

        for k in range(4):
            ni = now_i + di[k]
            nj = now_j + dj[k]

            if 0 > ni or H <= ni or 0 > nj or W <= nj:
                continue

            if parents[ni][nj] == 0:
                temp_0.add((now_i, now_j))
                break
            
    return len(temp_0)


# def connect():

#     while temp_0:
#         now_i, now_j = temp_0.pop()
#         parents[now_i][now_j] = 0
#         visited[now_i][now_j] = 1

#         for k in range(4):
#             ni = now_i + di[k]
#             nj = now_j + dj[k]

#             if 0 > ni or H <= ni or 0 > nj or W <= nj:
#                 continue

#             if table[ni][nj] == 1:
#                 temp_1.add((ni, nj))

#             if visited[ni][nj]:
#                 continue
            
#             visited[ni][nj] = 1
#             q.append((ni, nj))

#     pass


H, W = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(H)]

parents = [[1] * W for _ in range(H)]
visited = [[0] * W for _ in range(H)]
parents[0][0] = 0
visited[0][0] = 1
temp_1 = set()
temp_0 = set()

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

outer()
prev = decay()
connect()

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
