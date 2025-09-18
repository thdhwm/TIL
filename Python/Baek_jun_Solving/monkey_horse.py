# from collections import deque
# import sys
# sys.stdin = open('input.txt')
#
#
# def bfs(i, j, nHorses, nMoves):
#     global min_moves
#     visited = [[0] * W for _ in range(H)]
#     visited[0][0] = 1
#     q = deque([(i, j, nHorses, nMoves)])
#
#     while q:
#
#         now_i, now_j, nHorse, moves = q.popleft()
#         if moves > min_moves:
#             continue
#
#         if now_i == H - 1 and now_j == W - 1:
#             min_moves = min(min_moves, moves)
#             continue
#
#         for k in range(5):
#             if k == 4:
#                 if nHorse == 0:
#                     continue
#                 for m in range(8):
#                     ni = now_i + di_h[m]
#                     nj = now_j + di_h[m]
#                     if ni < 0 or ni >= H or nj < 0 or nj >= W:
#                         continue
#
#                     if visited[ni][nj]:
#                         continue
#
#                     if table[ni][nj]:
#                         continue
#
#                     visited[ni][nj] = 1
#                     q.append((ni, nj, nHorse - 1, moves + 1))
#
#
#             else:
#                 ni = now_i + di_m[k]
#                 nj = now_j + dj_m[k]
#                 if ni < 0 or ni >= H or nj < 0 or nj >= W:
#                     continue
#
#                 if visited[ni][nj]:
#                     continue
#
#                 if table[ni][nj]:
#                     continue
#
#                 visited[ni][nj] = 1
#                 q.append((ni, nj, nHorse, moves + 1))
#
#
#
#
#
# K = int(input())  # can move horse_way, K times
# W, H = map(int, input().split())
# table = [list(map(int, input().split())) for _ in range(H)]   # 1 = wall
# # start - (0, 0)     end - (H -1, W -1)
# di_m = [-1, 0, 1, 0]    # monkey style
# dj_m = [0, 1, 0, -1]
# di_h = [-2, -1, 1, 2, 2, 1, -1, -2]    # horse style
# dj_h = [1, 2, 2, 1, -1, -2, -2, -1]
# min_moves = 21e8
#
# bfs(0, 0, K, 1)
#
# print(min_moves if min_moves != 21e8 else -1)
# ##############################################################################################################
from collections import deque
import sys
sys.stdin = open('input.txt')

def bfs(i, j, nHorses, nMoves):
    global min_moves
    # 3차원 방문 배열: (i, j, 남은 말 이동 횟수)
    visited = [[[0] * (K + 1) for _ in range(W)] for _ in range(H)]
    visited[0][0][nHorses] = 1
    q = deque([(i, j, nHorses, nMoves)])

    while q:
        now_i, now_j, nHorse, moves = q.popleft()
        if moves > min_moves:
            continue

        # 목표 지점 도달
        if now_i == H - 1 and now_j == W - 1:
            min_moves = min(min_moves, moves)
            continue

        # 일반 이동 (원숭이 이동)
        for k in range(4):
            ni = now_i + di_m[k]
            nj = now_j + dj_m[k]
            if ni < 0 or ni >= H or nj < 0 or nj >= W:
                continue
            if visited[ni][nj][nHorse]:
                continue
            if table[ni][nj]:
                continue
            visited[ni][nj][nHorse] = 1
            q.append((ni, nj, nHorse, moves + 1))

        # 말 이동 (K번 제한)
        if nHorse > 0:
            for m in range(8):
                ni = now_i + di_h[m]
                nj = now_j + dj_h[m]
                if ni < 0 or ni >= H or nj < 0 or nj >= W:
                    continue
                if visited[ni][nj][nHorse - 1]:
                    continue
                if table[ni][nj]:
                    continue
                visited[ni][nj][nHorse - 1] = 1
                q.append((ni, nj, nHorse - 1, moves + 1))

K = int(input())  # can move horse_way K times
W, H = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(H)]  # 1 = Wall
di_m = [-1, 0, 1, 0]    # monkey
dj_m = [0, 1, 0, -1]
di_h = [-2, -1, 1, 2, 2, 1, -1, -2]  # horse
dj_h = [1, 2, 2, 1, -1, -2, -2, -1]
min_moves = float('inf')

bfs(0, 0, K, 0)  # 초기 이동 횟수는 0

print(min_moves if min_moves != float('inf') else -1)