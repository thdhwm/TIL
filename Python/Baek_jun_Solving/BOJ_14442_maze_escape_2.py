from collections import deque
import sys
sys.stdin = open('input.txt')


def bfs(N, M, K, board):
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    visited = [[[0] * (K + 1) for _ in range(M)] for _ in range(N)]
    q = deque([(0, 0, 1, K)])  # (i, j, moves, wall breaks)
    visited[0][0][K] = 1

    while q:
        i, j, moves, breaks = q.popleft()

        if i == N - 1 and j == M - 1:
            return moves

        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < N and 0 <= nj < M:
                if board[ni][nj] == '1' and breaks > 0 and not visited[ni][nj][breaks - 1]:
                    visited[ni][nj][breaks - 1] = 1
                    q.append((ni, nj, moves + 1, breaks - 1))

                elif board[ni][nj] == '0' and not visited[ni][nj][breaks]:
                    visited[ni][nj][breaks] = 1
                    q.append((ni, nj, moves + 1, breaks))
    return -1


N, M, K = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]
print(bfs(N, M, K, board))
