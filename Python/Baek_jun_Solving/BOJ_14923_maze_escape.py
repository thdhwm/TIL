from collections import deque
import sys
sys.stdin = open('input.txt')


def bfs():
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    q = deque([(Hi - 1, Hj - 1, 1)])
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    visited[Hi - 1][Hj - 1][1] = 1

    while q:
        i, j, wand = q.popleft()

        if i == Ei - 1 and j == Ej - 1:
            return visited[i][j][wand] - 1

        for k in range(4):
            ni, nj = i + di[k], j + dj[k]

            if 0 <= ni < N and 0 <= nj < M:
                if maze[ni][nj] == 1 and wand == 1 and visited[ni][nj][0] == 0:
                    visited[ni][nj][0] = visited[i][j][wand] + 1
                    q.append((ni, nj, 0))

                elif maze[ni][nj] == 0 and visited[ni][nj][wand] == 0:
                    visited[ni][nj][wand] = visited[i][j][wand] + 1
                    q.append((ni, nj, wand))

    return -1


N, M = map(int, input().split())
Hi, Hj = map(int, input().split())
Ei, Ej = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(N)]

print(bfs())

