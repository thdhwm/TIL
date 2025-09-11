import sys
sys.stdin = open('input.txt')


def move(i, j, depth):
    now = room[i][j]
    isPossible = 0
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]

        if 0 <= ni < N and 0 <= nj < N:
            if room[ni][nj] == now + 1:
                isPossible = 1
                next_i, next_j = ni, nj

    if isPossible:
        if dp[next_i][next_j] != 0:
            return dp[next_i][next_j] + 1
        else:
            return move(next_i, next_j, depth + 1) + 1

    return 1

T = int(input())
di = [-1, 0, 1, 0]     # delta
dj = [0, 1, 0, -1]
for test_case in range(1, T + 1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0] * N for _ in range(N)]
    max_move = 0
    room_number = 21e8

    for i in range(N):
        for j in range(N):
            connected = move(i, j, 1)
            dp[i][j] = connected
            if max_move <= connected:
                max_move = connected

    for i in range(N):
        for j in range(N):
            if dp[i][j] == max_move:
                if room_number > room[i][j]:
                    room_number = room[i][j]

    print(f'#{test_case} {room_number} {max_move}')