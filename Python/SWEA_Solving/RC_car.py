import sys
sys.stdin = open('input.txt')

T = int(input())
di = [-1, 0, 1, 0]    # starts facing up
dj = [0, 1, 0, -1]
for test_case in range(1, T + 1):
    N = int(input())
    board = [list(input()) for _ in range(N)]
    Q = int(input())
    ans = [0] * Q    # 1 - possible, 0 - not

    for i in range(N):        # find starting point
        for j in range(N):
            if board[i][j] == 'X':
                si, sj = i, j

    for q in range(Q):
        C, *commands = input().split()
        facing = 0    # up, north
        start_i, start_j = si, sj
        for cmd in commands[0]:
            if cmd == 'A':
                ni = start_i + di[facing % 4]
                nj = start_j + dj[facing % 4]

                if 0 > ni or N <= ni or 0 > nj or N <= nj:
                    continue
                if board[ni][nj] == 'T':
                    continue

                start_i, start_j = ni, nj

            elif cmd == 'L':
                facing += 3

            elif cmd == 'R':
                facing += 1

        if board[start_i][start_j] == 'Y':
            ans[q] = 1

    print(f'#{test_case}', *ans)
