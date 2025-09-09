from collections import deque
import sys
sys.stdin = open('input.txt')

def runaway(limit):
    global total
    q = deque([start])
    visited = [[0] * M for _ in range(N)]
    visited[R][C] = 1

    while q:
        now_i, now_j, time = q.popleft()
        if time == limit:
            continue

        pipe_kind = pipes[now_i][now_j]    # 현 위치 파이프 종류

        if pipe_kind == 0:     # 파이프 없느 곳이면 continue
            continue

        for i in range(4):    # 다음 위치 정하기
            ni = now_i + delta[i][0] * pipe[pipe_kind - 1][i]
            nj = now_j + delta[i][1] * pipe[pipe_kind - 1][i]

            if 0 <= ni < N and 0 <= nj < M:
                connected_pie_kind = pipes[ni][nj]     # 다음 위치의 파이프 종류
                if visited[ni][nj] != 0 or pipes[ni][nj] ==  0:
                    continue    # 전에 방문 했거나, 파이프 없으면 continue

                if not pipe[connected_pie_kind - 1][(i + 2) % 4] * pipe[pipe_kind - 1][i]:
                    continue     #  현재 파이프와 연결된 파이프 끝이 안 맞으면 continue

                total += 1
                visited[ni][nj] = 1
                q.append((ni, nj, time + 1))



T = int(input())

for test_case in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())  # n*m map, (r,c) enterance, l - time passed
    pipes = [list(map(int, input().split())) for _ in range(N)]    # pipe map
    start = (R, C, 1)    # manhole
    total = 1

    pipe = [(1, 1, 1, 1), (1, 0, 1, 0), (0, 1, 0, 1), (1, 1, 0, 0), (0, 1, 1, 0), (0, 0, 1, 1), (1, 0, 0, 1)]
    delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]    # 상, 우, 하, 좌

    runaway(L)

    print(f'#{test_case} {total}')

# #################################################################################################
# BFS 의 시간 복잡도
# - O(V + E)
#   - V: 정점의 개수 / E: 간선의 개수
#   - 정점의 개수 = 2,500개 (50 * 50)
#   # queue 에 2500개 까지 가능
#       -> 여유롭다
#   간선 갯수 * 4 ( 상하좌우) = 10000 ==>> 가능
