from collections import deque
import sys
sys.stdin = open('input.txt')


def brick(shots, board):
    global min_bricks
    que = deque()
    matrix = board[:]
    if shots == N:
        cnt = 0
        for i in range(H):
            for j in range(W):
                if matrix[i][j] == 0:
                    continue
                cnt += 1
        if min_bricks > cnt:
            min_bricks = cnt
        return

    for width in range(W):
        height = 0
        while H > height and not matrix[height][width]:
            height += 1
        if height == H:
            continue

        que.append((height, width))

        while que:
            now_i, now_j = que.popleft()

            radius = matrix[now_i][now_j]
            matrix[now_i][now_j] = 0
            for q in range(radius - 1):
                for p in range(4):
                    ni = now_i + di[p] * q
                    nj = now_j + dj[p] * q

                    if 0 <= ni < H and 0 <= nj < W:
                        if matrix[ni][nj] <= 1:
                            matrix[ni][nj] = 0
                            continue
# #########################     내리기 구현 해야함.....  ################################

                        que.append((ni, nj))

    brick(shots + 1, matrix)


T = int(input())
for test_case in range(1, T + 1):
    N, W, H = map(int, input().split())   # n - number of shots, W * H wide board
    board = [list(map(int, input().split())) for _ in range(H)]
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    min_bricks = 21e8

    brick(0, board)
    print(min_bricks)