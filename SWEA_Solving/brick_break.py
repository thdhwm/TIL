from collections import deque
import sys
sys.stdin = open('input.txt')


def brick(shots):
    que = deque()
    if shots == N:
        return
    
    for i in range(W):
        height = 0
        while not board[height][i]:
            height += 1

        que.append((height, i))
        while que:
            now_i, now_j = que.popleft()
            radius = board[now_i][now_j]
            board[now_i][now_j] = 0
            for q in range(radius - 1):
                for p in range(4):
                    ni = now_i + di[p] * q
                    nj = now_j + dj[p] * q
                    if 0 <= ni < H and 0 <= nj < W:
                        if board[ni][nj] <= 1:
                            board[ni][nj] = 0

                        else:
                            que.append((ni, nj))
        brick(shots + 1)

        # for i in range(H):
        #     print(board[i])


T = int(input())
N, W, H = map(int, input().split())   # n - number of shots, W * H wide board
board = [list(map(int, input().split())) for _ in range(H)]
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
# print(board)

brick(0)