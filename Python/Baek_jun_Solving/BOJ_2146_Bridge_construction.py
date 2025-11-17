# from collections import deque
# import sys
# sys.stdin = open('input.txt')
#
#
# def same_island(i, j):
#     que = deque([(i, j)])
#     while que:
#         now_i, now_j = que.popleft()
#         parents[now_i][now_j] = island_id
#
#         for k in range(4):
#             ni = now_i + di[k]
#             nj = now_j + dj[k]
#             if 0 > ni or N <= ni or 0 > nj or N <= nj:
#                 continue
#             if parents[ni][nj] != 0:
#                 continue
#             if table[ni][nj] == 0:
#                 continue
#             que.append((ni, nj))
#
#
# def bridge(i, j):
#     global min_length, vis_stamp
#     vis_stamp += 1
#     visited[i][j] = vis_stamp
#     que = deque([(i, j, 0)])
#     start_island = parents[i][j]
#     while que:
#         now_i, now_j, length = que.popleft()
#         if length >= min_length:
#             continue
#
#         for k in range(4):
#             ni = now_i + di[k]
#             nj = now_j + dj[k]
#             if 0 > ni or N <= ni or 0 > nj or N <= nj:
#                 continue
#
#             if visited[ni][nj] == vis_stamp:
#                 continue
#
#             if parents[ni][nj] != 0 and parents[ni][nj] != start_island:
#                 min_length = min(min_length, length)
#                 return
#
#             if parents[ni][nj] == 0:
#                 visited[ni][nj] = vis_stamp
#                 que.append((ni, nj, length + 1))
#
#
# N = int(input())
# table = [list(map(int, input().split())) for _ in range(N)]
# parents = [[0]*N for _ in range(N)]
# min_length = 21e8
# island_id = 1
# visited = [[0] * N for _ in range(N)]
# vis_stamp = 0
# edges = set()
# di = (1, 0, -1, 0)
# dj = (0, 1, 0, -1)
#
# for i in range(N):
#     for j in range(N):
#         if table[i][j] == 1 and parents[i][j] == 0:
#             same_island(i, j)
#             island_id += 1
#
# for i in range(N):
#     for j in range(N):
#         if table[i][j] == 1:  # 육지
#             for k in range(4):
#                 ni, nj = i + di[k], j + dj[k]
#                 if 0 <= ni < N and 0 <= nj < N and table[ni][nj] == 0:
#                     edges.add((i, j))
#                     break
#
# for place in edges:
#     bridge(place[0], place[1])
#
# print(min_length)
# #####################################################################################
from collections import deque
import sys
sys.stdin = open('input.txt')


def same_island(i, j, island_id):    # 섬 ID 라벨링 작업
    q = deque([(i, j)])
    parent[i][j] = island_id
    while q:
        ci, cj = q.popleft()
        for k in range(4):
            ni, nj = ci + di[k], cj + dj[k]
            if 0 <= ni < N and 0 <= nj < N and table[ni][nj] == 1 and parent[ni][nj] == 0:
                parent[ni][nj] = island_id
                q.append((ni, nj))


def bridge(starts_list, start_island):    # 가장 짧은 다리 찾기 bfs
    global min_length
    q = deque()
    for si, sj in starts_list:
        q.append((si, sj, 0))     # ( i, j, 거리 )
        visited[si][sj] = 1

    while q:
        ci, cj, dist = q.popleft()
        if dist >= min_length:    # 거리 더 길어지면 바로 컨티뉴
            continue

        for k in range(4):
            ni, nj = ci + di[k], cj + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                if not visited[ni][nj]:
                    if parent[ni][nj] == 0:  # 아직 바다
                        visited[ni][nj] = 1
                        q.append((ni, nj, dist + 1))
                    elif parent[ni][nj] != start_island:  # 다른 섬 도착!
                        min_length = min(min_length, dist)
                        return


N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]
parent = [[0] * N for _ in range(N)]    # 각 섬을 구별하기 위한 리스트
island_id = 1    # 각 섬을 구별하기 위한 ID 숫자
min_length = 21e8
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

for i in range(N):       # 섬 ID 라벨링 작업
    for j in range(N):
        if table[i][j] == 1 and parent[i][j] == 0:
            same_island(i, j, island_id)
            island_id += 1

starts = [set() for _ in range(island_id)]    # 섬별 가장자리 시작점 수집 ( set 으로 중복 제거 )
for i in range(N):
    for j in range(N):
        if parent[i][j]:
            for k in range(4):
                ni, nj = i + di[k], j + dj[k]
                if 0 <= ni < N and 0 <= nj < N and table[ni][nj] == 0:
                    starts[parent[i][j]].add((i, j))

for island in range(1, island_id):    # 각 섬에서 BFS
    visited = [[0] * N for _ in range(N)]    # 섬별로 visited
    bridge(starts[island], island)    # bfs 시작!

print(min_length)
