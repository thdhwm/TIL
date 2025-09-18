from collections import deque
import sys
sys.stdin = open('input.txt')


def brick(shots, total, board):
    global min_bricks

    if shots == N or total == 0:
        min_bricks = min(min_bricks, total)
        return

    for width in range(W):
        now_board = [row[:] for row in board]
        is_brick = 0
        for i in range(H):
            if now_board[i][width] > 0:
                radius = now_board[i][width]
                is_brick = 1
                break

        if not is_brick:
            continue

        if is_brick:
            que = deque([(i, width, radius)])
            now_total = total - 1
            now_board[i][width] = 0

            while que:
                i, j, radius = que.popleft()
                for r in range(1, radius):
                    for k in range(4):
                        ni = i + di[k] * r
                        nj = j + dj[k] * r

                        if not(0 <= ni < H and 0 <= nj < W):
                            continue

                        if now_board[ni][nj] == 0:
                            continue

                        que.append((ni, nj, now_board[ni][nj]))
                        now_board[ni][nj] = 0
                        now_total -= 1

            for width in range(W):
                idx = H - 1
                for r in range(H - 1, -1, -1):
                    if now_board[r][width]:
                        now_board[r][width], now_board[idx][width] = now_board[idx][width], now_board[r][width]
                        idx -= 1

            brick(shots + 1, now_total, now_board)

T = int(input())

for test_case in range(1, T + 1):
    N, W, H = map(int, input().split())   # n - number of shots, W * H wide board
    board = [list(map(int, input().split())) for _ in range(H)]
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    total = 0    # 벽돌 수
    min_bricks = 21e8
    for i in range(H):
        for j in range(W):
            if board[i][j] != 0:
                total += 1         # total bricks

    brick(0, total, board)
    print(f'#{test_case} {min_bricks}')
