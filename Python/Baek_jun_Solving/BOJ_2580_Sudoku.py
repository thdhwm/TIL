import sys
sys.stdin = open('input.txt')
def cavity():
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return -1, -1


def validate(r, c, num):
    for i in range(9):
        if board[r][i] == num:
            return False
        if board[i][c] == num:
            return False
    column_location = c//3
    row_location = r//3
    for kr in range(3):
        for kc in range(3):
            if board[row_location * 3 + kr][column_location * 3 + kc] == num:
                return False
    return True


def fill():
    row, column = cavity()
    if row == -1:
        return True

    for i in range(1, 10):
        if validate(row, column, i):
            board[row][column] = i
            if fill():
                return True
            board[row][column] = 0

    return False


board = [list(map(int, input().split())) for _ in range(9)]
fill()
for rw in range(9):
    print(*board[rw])
