import sys
sys.stdin = open('input.txt')
# time out in python, pass in pypy
# 문제 예시에서 pypy 로 제한 적어둔거가 pypy 로 풀라는 소리였는듯


def cavity():    # 빈칸 찾는 함수
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j    #
    return -1, -1    # 빈칸 없으면 -1 리턴해서 다 찼음을 알려줌


def validate(r, c, num):    # 칸에 들어갈 수 있는지 확인
    for i in range(9):
        if board[r][i] == num:    # 같은 row 확인
            return False
        if board[i][c] == num:    # 같은 column 확인
            return False

    column_location = c//3    # 3 * 3 영역 나눠서 생각 -> 0~2, 3~5, 6~8
    row_location = r//3       # 3 * 3 영역 나눠서 생각 -> 0~2, 3~5, 6~8
    for kr in range(3):       # 같은 3 * 3 영역 확인
        for kc in range(3):
            if board[row_location * 3 + kr][column_location * 3 + kc] == num:
                return False
    return True               # 위에 조건 다 확인해봤는디 없으면 True


def fill():                   # main dfs 함수
    row, column = cavity()    # 빈칸 찾기
    if row == -1:             # 빈칸 없으면
        return True           # 끝

    for i in range(1, 10):    # 1 ~ 9 숫자
        if validate(row, column, i):    # 들어갈 수 있으면
            board[row][column] = i      # 넣고
            if fill():                  # 다 찼으면
                return True             # 끝
            board[row][column] = 0      # 빼고

    return False              # True False


board = [list(map(int, input().split())) for _ in range(9)]
fill()
for rw in range(9):
    print(*board[rw])

