# from collections import defaultdict
# from heapq import heappush, heappop
# import sys
# sys.stdin = open('input.txt', 'r')
#
#
# def dijkstra(start, skip):
#     INF = float('inf')
#     dists = [INF] * (n + 1)
#     dists[start] = 0
#     pq = [(0, start)]
#
#     while pq:
#         dist, node = heappop(pq)
#
#         if dists[node] < dist:
#             continue
#
#         for next_dist, next_node in graph[node]:
#             new_dist = dists[node] + next_dist
#
#             if next_node in skip:
#                 continue
#
#             if dists[next_node] <= new_dist:
#                 continue
#
#             dists[next_node] = new_dist
#             heappush(pq, (new_dist, next_node))
#
#     return dists
#
#
# def search(start):
#     ans = []
#     initial = dijkstra(start, [])
#
#     if initial[g] > initial[h]:
#         real_start, cross_start = g, h
#
#     else:
#         real_start, cross_start = h, g
#
#     destination = dijkstra(real_start, [cross_start, start])
#
#     for candidate in candidates:
#         if initial[candidate] == destination[candidate] + dGH + initial[cross_start]:
#             ans.append(candidate)
#
#     return ans
#
#
# T = int(input())
#
# for test_case in range(1, T + 1):
#     n, m, t = map(int, input().split())    # n - nodes, m - edges, t - candidates
#     s, g, h = map(int, input().split())    # s - start, g,h - must use edge between g,h
#     graph = defaultdict(list)
#     candidates = []
#     dGH = 0
#
#     for _ in range(m):
#         a, b, d = map(int, input().split())   # s, e, distance
#         if (a == g or a == h) and (b == g or b == h):
#             dGH = d
#         graph[a].append((d, b))
#         graph[b].append((d, a))
#
#     for _ in range(t):
#         candidates.append(int(input()))
#
#     candidates.sort()
#
#     result = search(s)
#
#     print(*result)
# ###############################################################################################################

from collections import defaultdict
from heapq import heappush, heappop
import sys
sys.stdin = open('input.txt', 'r')

def dijkstra(start):
    dists = [INF] * (n + 1)
    dists[start] = 0
    pq = [(0, start)]

    while pq:
        dist, node = heappop(pq)
        if dist > dists[node]: continue
        for next_dist, next_node in graph[node]:
            if dists[next_node] > dists[node] + next_dist:
                dists[next_node] = dists[node] + next_dist
                heappush(pq, (dists[next_node], next_node))
    return dists


T = int(input())

for _ in range(T):
    INF = float('inf')
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = defaultdict(list)
    dGH = 0

    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((d, b))
        graph[b].append((d, a))
        if (a == g and b == h) or (a == h and b == g):
            dGH = d

    candidates = sorted([int(input()) for _ in range(t)])

    dist_s = dijkstra(s)
    dist_g = dijkstra(g)
    dist_h = dijkstra(h)

    result = []

    for cand in candidates:
        path1 = dist_s[g] + dGH + dist_h[cand]
        path2 = dist_s[h] + dGH + dist_g[cand]

        if dist_s[cand] == INF:    # 후보지가 도달 불가능일 수도 있다ㅏㅏㅑㅏㅑㅑㅏ
            continue

        if dist_s[cand] == min(path1, path2):
            result.append(cand)

    print(*result)
