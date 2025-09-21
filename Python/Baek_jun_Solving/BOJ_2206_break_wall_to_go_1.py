from collections import deque
import sys
sys.stdin = open('input.txt')


def bfs(i, j, moves, isBreak):
    global min_moves
    q = deque([(i, j, moves, isBreak)])
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]    # [0, 0]-[벽을 부수고 방문한 경우, 벽을 부수기 전 방문한 경우]
    visited[i][j][isBreak] = 1

    while q:
        now_i, now_j, now_move, isBreak = q.popleft()

        if now_i == eI and now_j == eJ:
            min_moves = min(min_moves, now_move)
            continue

        for k in range(4):
            ni = now_i + di[k]
            nj = now_j + dj[k]
            if 0 > ni or N <= ni or 0 > nj or M <= nj:
                continue

            if board[ni][nj] == '1' and isBreak == 1:  # 벽이지만 부술 수 있음
                visited[ni][nj][0] = 1
                q.append((ni, nj, now_move + 1, 0))  # 벽 부수고 이동

            elif board[ni][nj] == '0' and visited[ni][nj][isBreak] == 0:  # 벽이 아니고 방문하지 않음
                visited[ni][nj][isBreak] = 1
                q.append((ni, nj, now_move + 1, isBreak))  # 기존 상태 유지


N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
min_moves = 2000000

sI, sJ = 0, 0
eI, eJ = N - 1, M - 1
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

bfs(sI, sJ, 1, 1)

if min_moves == 2000000:
    print(-1)
else:
    print(min_moves)
