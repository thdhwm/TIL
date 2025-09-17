from heapq import heappush, heappop
import sys
sys.stdin = open('input.txt', 'r')


def supply(i, j):
    INF = float('inf')
    depths = [[INF] * N for _ in range(N)]
    depths[i][j] = 0
    pq = [(0, i, j)]

    while pq:
        depth, now_i, now_j = heappop(pq)

        if depth > depths[now_i][now_j]:
            continue

        for k in range(4):
            ni = now_i + di[k]
            nj = now_j + dj[k]
            if 0 > ni or N <= ni or 0 > nj or N <= nj:
                continue

            new_depth = depth + table[ni][nj]

            if new_depth >= depths[ni][nj]:
                continue

            depths[ni][nj] = new_depth
            heappush(pq, (new_depth, ni, nj))

    return depths[N - 1][N - 1]

T = int(input())
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
for test_case in range(1, T + 1):
    N = int(input())
    table = [list(map(int, input())) for _ in range(N)]

    print(f'#{test_case} {supply(0, 0)}')
