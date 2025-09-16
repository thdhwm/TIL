from heapq import heappush, heappop
import sys
sys.stdin = open('input.txt', 'r')


def jump(start_i, start_j):
    limits = [[21e8] * M for _ in range(N)]
    limits[start_i][start_j] = 0
    pq = [(0, start_i, start_j)]
    # limits[1][7] = 0
    # pq = [(0, 1, 7)]

    while pq:
        limit, now_i, now_j = heappop(pq)

        if limit > limits[now_i][now_j]:
            continue

        for k in range(1, 5):
            ni = now_i + di[k]
            nj = now_j + dj[k]
            if 0 > ni or N <= ni or 0 > nj or M <= nj:
                continue

            if k % 2 == 1:   # 상 하 이동, limit 바뀜
                now_limit = 1
                while table[ni][nj] == '0':
                    ni += di[k]
                    nj += dj[k]
                    if 0 > ni or N <= ni or 0 > nj or M <= nj:
                        break
                    now_limit += 1

                if 0 > ni or N <= ni or 0 > nj or M <= nj:
                    continue

                now_limit = max(limit, now_limit)

                if now_limit >= limits[ni][nj]:
                    continue

                limits[ni][nj] = now_limit
                heappush(pq, (now_limit, ni, nj))

            elif k % 2 == 0:
                if table[ni][nj] == '0':
                    continue

                if limits[ni][nj] == limits[now_i][now_j]:
                    continue

                limits[ni][nj] = limits[now_i][now_j]
                heappush(pq, (limits[ni][nj], ni, nj))

    return limits[ei][ej]


T = int(input())
di = [0, -1, 0, 1, 0]
dj = [0, 0, 1, 0, -1]
for tes_case in range(1, T + 1):
    N, M = map(int, input().split())
    table = [list(input().split()) for _ in range(N)]
    si, sj, ei, ej = 0, 0, 0, 0

    for i in range(N):
        for j in range(M):
            if table[i][j] == '2':
                si, sj = i, j

            if table[i][j] == '3':
                ei, ej = i, j

    print(f'#{tes_case} {jump(si, sj)}')
