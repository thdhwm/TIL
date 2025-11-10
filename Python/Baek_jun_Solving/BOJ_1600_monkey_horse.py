import sys
sys.stdin = open('input.txt')
from collections import deque


def bfs():
    visited = [[[-1] * (K + 1) for _ in range(W)] for _ in range(H)]  # y 좌표, x 좌표, 말 이동 수
    que = deque([[0, 0, 0]])  # y 좌표, x 좌표, 말 이동 수
    visited[0][0][0] = 0

    while que:
        y, x, z = que.popleft()
        if y == H - 1 and x == W - 1:
            return visited[y][x][z]

        if z < K:    # 말 이동 가능하면
            for i in range(8):    # 말 이동
                ny = y + dy[i]
                nx = x + dx[i]
                if ny < 0 or nx < 0 or ny >= H or nx >= W:
                    continue
                if graph[ny][nx]:    # 벽이면 continue
                    continue
                if visited[ny][nx][z + 1] != -1:    # 왔던 장소면 continue
                    continue
                que.append([ny, nx, z + 1])
                visited[ny][nx][z + 1] = visited[y][x][z] + 1    # visited 숫자로 동작 수 계산

        for i in range(8, 12):    # 상하좌우
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= H or nx >= W:
                continue
            if graph[ny][nx]:    # 벽이면 continue
                continue
            if visited[ny][nx][z] != -1:    # 왔던 장소면 continue 
                continue
            que.append([ny, nx, z])
            visited[ny][nx][z] = visited[y][x][z] + 1    # visited 숫자로 동작 수 계산

    return -1    # 불가능하면 -1


K = int(input())
W, H = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(H)]

dy = (1, 2, 2, 1, -1, -2, -2, -1, -1, 0, 0, 1)    # 말, 상하좌우
dx = (-2, -1, 1, 2, 2, 1, -1, -2, 0, -1, 1, 0)

print(bfs())
