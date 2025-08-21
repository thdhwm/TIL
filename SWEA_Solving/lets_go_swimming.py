from collections import deque
import time
import sys
sys.stdin = open('input.txt')

#
# def find_water(r, c):
#     que = deque([(r, c)])
#     while que:
#         y, x = que.popleft()
#
#         for k in range(4):
#             if 0 <= y + di[k] < N and 0 <= x + dj[k] < M:
#                 if matrix[y][x] == 'W':
#                     return visited[y][x] - 1
#
#                 ni = y + di[k]
#                 nj = x + dj[k]
#                 if visited[ni][nj] != 0:
#                     continue
#
#                 visited[ni][nj] = visited[y][x] + 1
#                 que.append((ni, nj))
#
#
# T = int(input())
# di = [-1, 0, 1, 0]
# dj = [0, 1, 0, -1]
#
# for test_case in range(1, T + 1):
#     start = time.time()
#     N, M = map(int, input().split())     # r, c
#     matrix = [list(input()) for _ in range(N)]
#     cnt_grids = 0
#
#     for i in range(N):
#         for j in range(M):
#             if matrix[i][j] == 'L':
#                 visited = [[0] * M for _ in range(N)]
#                 visited[i][j] = 1
#                 cnt_grids += find_water(i, j)
#
#     end = time.time()
#     print(f'#{test_case} {cnt_grids} {end - start}')
# ###################################################################################################

# def find_land():
#     global sum_grids
#     while que:
#         y, x = que.popleft()
#
#         for k in range(4):
#             ni = y + di[k]
#             nj = x + dj[k]
#             if 0 <= ni < N and 0 <= nj < M:
#
#                 if visited[ni][nj] == 0:
#                     distance = visited[y][x] + 1
#                     visited[ni][nj] = distance
#                     sum_grids += distance - 1
#                     que.append((ni, nj))


T = int(input())
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

for test_case in range(1, T + 1):
    # start = time.time()
    N, M = map(int, input().split())     # r, c
    matrix = [list(input()) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    sum_grids = 0
    que = deque()

    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 'W':
                que.append((i, j))
                visited[i][j] = 1

    while que:
        y, x = que.popleft()

        for k in range(4):
            ni = y + di[k]
            nj = x + dj[k]
            if 0 <= ni < N and 0 <= nj < M:

                if visited[ni][nj] == 0:
                    distance = visited[y][x] + 1
                    visited[ni][nj] = distance
                    sum_grids += distance - 1
                    que.append((ni, nj))

    # end = time.time()
    print(f'#{test_case} {sum_grids}')
# ###################################################################################
# from collections import deque
#
# T = int(input())
# delta = [[-1, 0], [0, 1], [1, 0], [0, -1]]
#
# for case_num in range(1, T + 1):
#     N, M = map(int, input().split())
#     glen = [list(input().strip()) for _ in range(N)]
#     visited = [[0] * M for _ in range(N)]
#     route = deque()
#
#     for y in range(N):
#         for x in range(M):
#             if glen[y][x] == 'W':
#                 route.append((y, x))
#                 visited[y][x] = 1
#     result = 0
#     while route:
#         y, x = route.popleft()
#         for d in delta:
#             dy = y + d[0]
#             dx = x + d[1]
#             if 0 <= dy < N and 0 <= dx < M:
#                 if visited[dy][dx] == 0:
#                     distance = visited[y][x] + 1
#                     visited[dy][dx] = distance
#                     result += distance - 1
#                     route.append((dy, dx))
#
#     print(f'#{case_num} {result}')
