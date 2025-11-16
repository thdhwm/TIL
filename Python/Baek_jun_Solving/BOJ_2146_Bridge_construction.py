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
#             for d in range(4):
#                 ni, nj = i + di[d], j + dj[d]
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


N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]

# 섬 라벨링
parent = [[0] * N for _ in range(N)]
island_id = 1
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

def bfs_label(i, j, island_id):
    q = deque([(i, j)])
    parent[i][j] = island_id
    while q:
        ci, cj = q.popleft()
        for d in range(4):
            ni, nj = ci + di[d], cj + dj[d]
            if 0 <= ni < N and 0 <= nj < N and table[ni][nj] == 1 and parent[ni][nj] == 0:
                parent[ni][nj] = island_id
                q.append((ni, nj))

for i in range(N):
    for j in range(N):
        if table[i][j] == 1 and parent[i][j] == 0:
            bfs_label(i, j, island_id)
            island_id += 1

# 섬별 가장자리 시작점 수집 (중복 제거를 위해 set 사용)
starts = [[] for _ in range(island_id)]
for i in range(N):
    for j in range(N):
        if parent[i][j] > 0:
            for d in range(4):
                ni, nj = i + di[d], j + dj[d]
                if 0 <= ni < N and 0 <= nj < N and table[ni][nj] == 0:
                    starts[parent[i][j]].append((i, j))
                    break  # 한 셀당 한 번만 추가 (중복 방지)

# 다리 놓기 BFS (섬별로 한 번씩만)
min_length = 1e9
visited = [[False] * N for _ in range(N)]

def bfs_bridge(starts_list, start_island):
    global min_length
    q = deque()
    for si, sj in starts_list:
        q.append((si, sj, 0))
        visited[si][sj] = True

    while q:
        ci, cj, dist = q.popleft()
        if dist >= min_length:
            continue

        for d in range(4):
            ni, nj = ci + di[d], cj + dj[d]
            if 0 <= ni < N and 0 <= nj < N:
                if not visited[ni][nj]:
                    if parent[ni][nj] == 0:  # 바다
                        visited[ni][nj] = True
                        q.append((ni, nj, dist + 1))
                    elif parent[ni][nj] != start_island:  # 다른 섬
                        min_length = min(min_length, dist)
                        return

# 각 섬에서 BFS 실행
for iid in range(1, island_id):
    # 방문 배열 초기화 (섬별로 새로 시작)
    visited = [[False] * N for _ in range(N)]
    bfs_bridge(starts[iid], iid)

print(min_length if min_length != 1e9 else 0)