# 움직여서 갈 수 있는 좌표 모두 구하고 별도의 n*n table save
# compare tables afterwards to see if it's 1 (pawn)
import sys
sys.stdin = open('input.txt')

T = int(input())


def move(y, x, depth):    # depth 3 -> return
    if depth == 3:
        return

    for k in range(4):
        for n in range(1, N):
            ni = y + di[k] * n
            nj = x + dj[k] * n

            if 0 > ni or ni >= N or 0 > nj or nj >= N:
                continue

            if table[ni][nj] == 1:
                ni += 1 * di[k]
                nj += 1 * dj[k]
                while 0 <= ni < N and 0 <= nj < N and table[ni][nj] != 1:
                    move(ni, nj, depth + 1)
                    ni += 1 * di[k]
                    nj += 1 * dj[k]

                if 0 <= ni < N and 0 <= nj < N and table[ni][nj] == 1:
                    table_to_compare[ni][nj] = 1
                    table[ni][nj] = 0
                    move(ni, nj, depth + 1)
                    table[ni][nj] = 1
                    break

    return


for test_case in range(1, T + 1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]    # jang-gi board
    table_to_compare = [[0] * N for _ in range(N)]    # possible out-come ( where cannon can go )
    di = [-1, 0, 1, 0]    # cannon movement delta
    dj = [0, 1, 0, -1]
    cnt = 0

    for i in range(N):
        for j in range(N):
            if table[i][j] == 2:
                po_i, po_j = i, j

    move(po_i, po_j, 0)

    for i in range(N):
        for j in range(N):
            if table[i][j] == 1 and table_to_compare[i][j] == 1:
                cnt += 1

    print(f'#{test_case}', cnt)
