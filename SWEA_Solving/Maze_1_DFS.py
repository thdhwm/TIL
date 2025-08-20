import sys
sys.stdin = open('input.txt')


def maze_run(y, x):
    global is_possible

    if maze[y][x] == '3':
        is_possible = True
        return

    if maze[y][x] == '1':
        return

    for k in range(4):
        if 0 <= y + di[k] < 16 and 0 <= x + dj[k] < 16:    # 상하좌우
            ni = y + di[k]
            nj = x + dj[k]
            maze[y][x] = '1'
            maze_run(ni, nj)
            maze[y][x] = '0'


di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

for _ in range(10):
    test_case = int(input())
    maze = [list(input()) for _ in range(16)]

    is_possible = False
    for i in range(16):
        for j in range(16):
            if maze[i][j] == '2':
                start_i = i
                start_j = j

    maze_run(int(start_i), int(start_j))

    if is_possible:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')

# BFS 로 한번 다시 해보기
