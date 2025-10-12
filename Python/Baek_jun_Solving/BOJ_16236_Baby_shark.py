# from collections import deque
# import sys
# sys.stdin = open('input.txt')
#
#
# def bfs(start_i, start_j):
#     global eaten, baby_shark
#     q = deque([(start_i, start_j, 0)])
#     visited = [[0] * N for _ in range(N)]
#     visited[start_i][start_j] = 1
#
#     while q:
#         now_i, now_j, time = q.popleft()
#         for k in range(4):
#             ni = now_i + di[k]
#             nj = now_j + dj[k]
#
#             if 0 > ni or N <= ni or 0 > nj or N <= nj:
#                 continue
#
#             if visited[ni][nj]:
#                 continue
#
#             if table[ni][nj] > baby_shark:
#                 continue
#
#             if table[ni][nj] < baby_shark and table[ni][nj] != 0:
#                 eaten += 1
#                 if eaten == baby_shark:
#                     eaten = 0
#                     baby_shark += 1
#                 table[ni][nj] = 0
#                 return ni, nj, time + 1
#
#             else:
#                 visited[ni][nj] = 1
#                 q.append((ni, nj, time + 1))
#     return -1, -1, 0  # if no possible ways, return
#
#
# N = int(input())
# table = [list(map(int, input().split())) for _ in range(N)]
# di = [-1, 0, 0, 1]    # up, left, right, down
# dj = [0, -1, 1, 0]
# baby_shark = 2    # starting size of baby_shark is 2
# eaten = 0    # have to eat same num of fishes to grow, ex. 2 fishes to grow to 3
# ans = 0    # time took before calling for help
# for i in range(N):
#     for j in range(N):
#         if table[i][j] == 9:
#             si, sj = i, j
#
# table[si][sj] = 0
# now_at_i, now_at_j = si, sj
# while now_at_i != -1 and now_at_j != -1:
#     now_at_i, now_at_j, time_took = bfs(now_at_i, now_at_j)
#     ans += time_took
#
# print(ans)

# ######################################################################################################################
from collections import deque
import sys
sys.stdin = open('input.txt')


def bfs(start_i, start_j):
    global eaten, baby_shark

    q = deque([(start_i, start_j, 0)])
    visited = [[0] * N for _ in range(N)]
    visited[start_i][start_j] = 1
    candidates = []  # 먹을 수 있는 물고기 후보 (행, 열, 시간)
    min_time = float('inf')  # 최소 거리

    while q:
        now_i, now_j, time = q.popleft()

        if time > min_time:    # if same time scope done, break
            break

        for k in range(4):
            ni = now_i + di[k]
            nj = now_j + dj[k]

            if 0 > ni or N <= ni or 0 > nj or N <= nj:
                continue

            if visited[ni][nj]:
                continue

            if table[ni][nj] > baby_shark:
                continue

            if table[ni][nj] != 0 and table[ni][nj] < baby_shark:
                candidates.append((ni, nj, time + 1))
                min_time = time + 1

            else:
                visited[ni][nj] = 1
                q.append((ni, nj, time + 1))

    if not candidates:
        return -1, -1, 0

    candidates.sort(key=lambda x: (x[2], x[0], x[1]))  # sort by -> time, upper, left
    ni, nj, time = candidates[0]
    eaten += 1
    if eaten == baby_shark:
        eaten = 0
        baby_shark += 1
    table[ni][nj] = 0
    return ni, nj, time


N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]
di = [-1, 0, 0, 1]  # up, left, right, down
dj = [0, -1, 1, 0]
baby_shark = 2
eaten = 0
ans = 0
for i in range(N):
    for j in range(N):
        if table[i][j] == 9:
            si, sj = i, j

table[si][sj] = 0
now_at_i, now_at_j = si, sj
while now_at_i != -1 and now_at_j != -1:
    now_at_i, now_at_j, time_took = bfs(now_at_i, now_at_j)
    ans += time_took

print(ans)
