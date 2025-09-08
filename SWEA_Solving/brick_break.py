from collections import deque
import sys
sys.stdin = open('input.txt')


def stack(board):
    for width in range(W):
            column = [board[i][j] for i in range(H) if board[i][j] > 0]
            for i in range(H - len(column)):
                board[i][j] = 0
            for i in range(len(column)):
                board[H - len(column) + i][j] = column[i]


def shoot(width, now_board):
    is_brick = 0
    for i in range(H):
        if board[i][width] > 0:
            radius = now_board[i][width]
            is_brick = 1
            break

    if is_brick:
        que = deque([(i, width, radius)])
        now_board[i][width] = 0
        while que:
            i, j, radius = que.popleft()
            for k in range(4):
                for r in range(radius - 1):
                    ni = i + di[k] * r
                    nj = j + dj[k] * r
                    if 0 <= ni < H and 0 <= nj < W and now_board[ni][nj] > 0:
                        next_radius = now_board[ni][nj]
                        now_board[ni][nj] = 0
                        if next_radius > 1:
                            que.append((ni, nj, next_radius))
                    else:
                        break

    else:
        return


def brick(shots, board):
    global min_bricks

    if shots == N:
        cnt = 0
        for i in range(H):
            for j in range(W):
                if board[i][j] == 0:
                    continue
                cnt += 1
        if min_bricks > cnt:
            min_bricks = cnt
        return

    for width in range(W):
        now_board = [row[:] for row in board]
        shoot(width, now_board)
        stack(now_board)
        brick(shots + 1, now_board)


T = int(input())

for test_case in range(1, T + 1):
    N, W, H = map(int, input().split())   # n - number of shots, W * H wide board
    board = [list(map(int, input().split())) for _ in range(H)]
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    total = 0
    min_bricks = 21e8
    for i in range(H):
        for j in range(W):
            if board[i][j] != 0:
                total += 1         # total bricks

    brick(0, board)
    print(f'#{test_case} {min_bricks}')
