from heapq import heappush, heappop
import sys
sys.stdin = open('input.txt', 'r')


def dijkstra(start_i, start_j):
    INF = float('inf')
    dists = [[INF] * N for _ in range(N)]
    dists[start_i][start_j] = table[start_i][start_j]
    pq = [(dists[start_i][start_j], start_i, start_j)]
    max_dist = 0
    while pq:
        fatigue, now_i, now_j = heappop(pq)

        if dists[now_i][now_j] < fatigue:
            continue

        for k in range(4):
            ni = now_i + di[k]
            nj = now_j + dj[k]
            if 0 > ni or N <= ni or 0 > nj or N <= nj:
                continue

            if table[ni][nj] == -1:
                continue

            new_fatigue = fatigue + table[ni][nj]
            if new_fatigue >= dists[ni][nj]:
                continue
            dists[ni][nj] = new_fatigue
            heappush(pq, (new_fatigue, ni, nj))

    for i in range(N):
        for j in range(N):
            if dists[i][j] == INF:
                continue

            if max_dist < dists[i][j]:
                max_dist = dists[i][j]

    return max_dist


T = int(input())
di = [-1, 0, 1, 0]    # 상, 우 , 하, 좌
dj = [0, 1, 0, -1]
for test_case in range(1, T + 1):
    si, sj = map(int, input().split())
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]

    print(f'#{test_case} {dijkstra(si, sj)}')
