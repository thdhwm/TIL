import sys
sys.stdin = open('input.txt')
# sys.setrecursionlimit(10000) # 예시로 10,000으로 설정
# boj 14503


def clean(row, column, facing):
    global cnt_cleaned

    while True:
        if room[row][column] == 0:    # 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
            room[row][column] = 2    # 2 = cleaned
            cnt_cleaned += 1

        is_done = True
        for k in range(4):    # 현재 칸의 주변 4 칸 중
            next_facing = (facing - k - 1) % 4  # 반시계 방향 회전
            ni = row + di[next_facing]
            nj = column + dj[next_facing]
            if room[ni][nj] == 0:
                is_done = False
                break

        if is_done:    # 현재 칸의 주변 4 칸 중 청소되지 않은 빈 칸이 없는 경우,
            # 뒤로 이동
            back_facing = (facing + 2) % 4
            bi = row + di[back_facing]
            bj = column + dj[back_facing]
            if room[bi][bj] != 1:
                row, column = bi, bj  # 뒤로 이동
            else:
                return  # 뒤가 벽이면 종료

# 4. 청소 가능한 칸이 있는 경우
        else:
            if room[ni][nj] == 0:
                row, column, facing = ni, nj, next_facing  # 회전 후 전진


N, M = map(int, input().split())    # N * M size room
r, c, d = map(int, input().split())    # robot at (r,c), d - direction

room = [list(map(int, input().split())) for _ in range(N)]

di = [-1, 0, 1, 0]    # north, east, south, west
dj = [0, 1, 0, -1]
cnt_cleaned = 0

clean(r, c, d)
print(cnt_cleaned)
