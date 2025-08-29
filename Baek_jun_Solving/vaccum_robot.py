import sys
sys.stdin = open('input.txt')
# boj 14503


def clean(row, column, facing):
    global cnt_cleaned
    is_done = True

    if room[row][column] == 0:
        room[row][column] = 2    # 2 = cleaned
        cnt_cleaned += 1

    for k in range(4):
        ni = row + di[(facing + k) % 4]
        nj = column + dj[(facing + k) % 4]
        if room[ni][nj] == 0:
            is_done = False

        if is_done:
            if room[row + di[(facing + 2) % 4]][column + dj[(facing + 2) % 4]] == 1:
                return
            clean(row + di[(facing + 2) % 4], column + dj[(facing + 2) % 4], facing)

        else:
            facing += 1
            if room[row + di[facing % 4]][column + dj[facing % 4]] == 0:
                clean(row + di[facing % 4], column + dj[facing % 4], facing)
            clean(row, column, facing)

    return


N, M = map(int, input().split())    # N * M size room
r, c, d = map(int, input().split())    # robot at (r,c), d - direction

room = [list(map(int, input().split())) for _ in range(N)]

di = [-1, 0, 1, 0]    # north, east, south, west
dj = [0, 1, 0, -1]
cnt_cleaned = 0

clean(r, c, d)
print(cnt_cleaned)
