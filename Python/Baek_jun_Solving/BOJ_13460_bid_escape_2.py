from collections import deque
import sys
sys.stdin = open('input.txt')


def escape(table, red, blue, depth):
    q = deque([(table, red, blue, depth)])

    while q:
        now_board, red_bid, blue_bid, now_depth = q.popleft()
        if now_depth == 11:
            return -1

        nBoard = [row[:] for row in now_board]
        nRi, nRj = red_bid
        nBi, nBj = blue_bid

        for k in range(4):
            newRi = nRi + di[k]
            newRj = nRj + dj[k]
            newBi = nBi + di[k]
            newBj = nBj + dj[k]

            if newRi == ei and newRj == ej:
                return now_depth

            if nBoard[newRi][newRj] == '#' or nBoard[newBi][newBj] == 'O':
                continue

            if nBoard[newRi][newRj] == 'B' and nBoard[newBi][newBj] == '#':
                continue

            nBoard[nRi][nRj], nBoard[newRi][newRj] = nBoard[newRi][newRj], nBoard[nRi][nRj]

            if nBoard[newBi][newBj] == '.':
                nBoard[nBi][nBj], nBoard[newBi][newBj] = nBoard[newBi][newBj], nBoard[nBi][nBj]

            q.append((nBoard, (newRi, newRj), (newBi, newBj), depth + 1))


N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            ri, rj = i, j

        elif board[i][j] == 'B':
            bi, bj = i, j

        elif board[i][j] == 'O':
            ei, ej = i, j

print(escape(board, (ri, rj), (bi, bj), 1))

# ########################################################################################
