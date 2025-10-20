import sys
from collections import deque

sys.stdin = open('input.txt')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(viruses):
    queue = deque()
    time_map = [[-1] * n for _ in range(n)]

    # 활성 바이러스 초기화
    for x, y in viruses:
        queue.append((x, y))
        time_map[x][y] = 0

    max_time = 0
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and time_map[nx][ny] == -1 and lab[nx][ny] != 1:
                time_map[nx][ny] = time_map[x][y] + 1
                max_time = max(max_time, time_map[nx][ny])
                queue.append((nx, ny))

    # 모든 빈 칸 채워졌는지 확인
    for i in range(n):
        for j in range(n):
            if lab[i][j] == 0 and time_map[i][j] == -1:
                return -1
    return max_time


def dfs(virus_list, selected, start):
    global min_time
    if len(selected) == m:
        temp_time = bfs(selected)
        if temp_time != -1:
            min_time = min(min_time, temp_time)
        return

    for i in range(start, len(virus_list)):
        selected.append(virus_list[i])
        dfs(virus_list, selected, i + 1)
        selected.pop()


n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]

# 비활성 바이러스 위치 수집
virus_list = []
empty_count = 0
for i in range(n):
    for j in range(n):
        if lab[i][j] == 2:
            virus_list.append((i, j))
        elif lab[i][j] == 0:
            empty_count += 1

# 빈 칸이 없으면 0
if empty_count == 0:
    print(0)

else:
    min_time = float('inf')
    # DFS로 조합 생성
    dfs(virus_list, [], 0)

    print(min_time if min_time != float('inf') else -1)

# #############################################################################
#
# N, M = map(int, input().split())
# table = [list(map(int, input().split())) for _ in range(N)]
#
# virus_list = []
# empty_count = 0
# for i in range(N):
#     for j in range(N):
#         if lab[i][j] == 2:
#             virus_list.append((i, j))
#         elif lab[i][j] == 0:
#             empty_count += 1
#
# if empty_count == 0:
#     print(0)
#
# else:
#     min_time = float('inf')
#     # DFS로 조합 생성
#     dfs(virus_list, [], 0, m, lab, n)
#
#     print(min_time if min_time != float('inf') else -1)
#





