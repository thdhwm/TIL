from heapq import  heappush, heappop
from collections import defaultdict
import sys
sys.stdin = open('input.txt', 'r')


def dijkstra(start):
    INF = float('inf')
    dists = [INF] * N
    dists[start] = 0
    pq = [(0, start)]

    while pq:
        dist, node = heappop(pq)

        if dists[node] < dist:
            continue

        for next_dist, next_node in graph[node]:
            new_dist = dists[node] + next_dist

            if new_dist < dists[next_node]:
                dists[next_node] = new_dist
                heappush(pq, (new_dist, next_node))


    return dists[N - 1] if dists[N - 1] != INF else 'impossible'

T = int(input())

for test_case in range(1, T + 1):
    N, E = map(int, input().split())   # n - nodes (starting from 0), e - edges
    graph = defaultdict(list)
    for _ in range(E):
        a, b, w = map(int, input().split())
        graph[a].append((w, b))

    print(f'#{test_case} {dijkstra(0)}')

# #####################################################################################################################

