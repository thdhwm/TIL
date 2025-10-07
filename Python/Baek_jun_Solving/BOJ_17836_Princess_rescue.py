from collections import deque
import sys
sys.stdin = open('input.txt')


def bfs():
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]  # shallow copy, deep copy caution
    visited[0][0][0] = 1
    q = deque([(0, 0, 0, 0)])

    while q:
        now_i, now_j, time, sword = q.popleft()

        if time > T:
            return 'Fail'

        if now_i == N - 1 and now_j == M - 1:
            return time

        for k in range(4):
            ni = now_i + di[k]
            nj = now_j + dj[k]

            if 0 > ni or N <= ni or 0 > nj or M <= nj:
                continue

            if visited[ni][nj][sword]:
                continue

            if table[ni][nj] == 2 and not(visited[ni][nj][0] or visited[ni][nj][1]):    # sword obtained
                visited[ni][nj][0] = 1
                visited[ni][nj][1] = 1
                q.append((ni, nj, time + 1, 1))

            elif table[ni][nj] == 1 and sword and visited[ni][nj][1] == 0:  # wall
                visited[ni][nj][1] = 1
                q.append((ni, nj, time + 1, 1))

            elif table[ni][nj] == 0 and not visited[ni][nj][sword]:
                visited[ni][nj][sword] = 1
                q.append((ni, nj, time + 1, sword))

    return 'Fail'


N, M, T = map(int, input().split())   # N * M size maze, T - time limit
table = [list(map(int, input().split())) for _ in range(N)]
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

print(bfs())

