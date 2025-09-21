from heapq import heappop, heappush
from collections import defaultdict
import sys
sys.stdin = open('input.txt')


def dijkstra(start):
    dists = [INF] * (N + 1)
    dists[start] = 0
    pq = [(0, start)]

    while pq:
        now_dist, now_node = heappop(pq)

        if now_dist > dists[now_node]:
            continue

        for next_dist, next_node in graph[now_node]:
            new_dist = now_dist + next_dist
            if new_dist >= dists[next_node]:
                continue

            dists[next_node] = new_dist
            heappush(pq, (new_dist, next_node))

    return dists


N, E = map(int, input().split())    # n - nodes, e - edges
graph = defaultdict(list)
INF = float('inf')
for _ in range(E):
    a, b, c = map(int, input().split())  # both ways a to b, cost c
    graph[a].append((c, b))
    graph[b].append((c, a))

stb1, stb2 = list(map(int, input().split()))    # stop_by 1,2

# dijkstra 3 times
dijk_1 = dijkstra(1)
dijk_st1 = dijkstra(stb1)
dijk_st2 = dijkstra(stb2)

# possible routes
possible_1 = dijk_1[stb1] + dijk_st1[stb2] + dijk_st2[N]
possible_2 = dijk_1[stb2] + dijk_st2[stb1] + dijk_st1[N]

result = min(possible_1, possible_2)

print(result if result != INF else -1)
