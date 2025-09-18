import sys
sys.stdin = open('input.txt')


def maze_run(y, x):
    global is_possible

    if maze[y][x] == '3':
        is_possible = 1
        return

    if maze[y][x] == '1':
        return

    for k in range(4):
        if 0 <= y + di[k] < N and 0 <= x + dj[k] < N:
            ni = y + di[k]
            nj = x + dj[k]
            maze[y][x] = '1'
            maze_run(ni, nj)
            maze[y][x] = '0'


T = int(input())
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

for test_case in range(1, T + 1):
    N = int(input())
    maze = [list(input()) for _ in range(N)]
    is_possible = 0

    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                start_i = i
                start_j = j

    maze_run(start_i, start_j)

    print(f'#{test_case} {is_possible}')
