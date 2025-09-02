from collections import defaultdict
from heapq import heappush, heappop, heapify
import sys
sys.stdin = open('input.txt')
#
#
# def dijkstra(start, table):
#     INF = float('inf')
#     distance = [INF] * (N + 1)
#     distance[start] = 0
#     q = []
#     heappush(q, (0, start))
#
#     while q:
#         current_dist, current_node = heappop(q)
#
#         if distance[current_node] < current_dist:
#             continue
#
#         for next_distance, next_node in table[current_node]:
#             new_dist = current_dist + next_distance
#             if new_dist < distance[next_node]:
#                 table[next_node] = new_dist
#                 heappush(q, (new_dist, next_node))
#
#     return distance
#
#
# N, M, X = map(int, input().split())  # N - num of people, M - roads, X - destination
# table = defaultdict(list)
# max_distance = 0
#
# for _ in range(M):
#     s, e, t = map(int, input().split())
#     table[s].append((t, e))
#
# for n in range(1, N + 1):
#     total_distance = dijkstra(n, table)[X] + dijkstra(X, table)[n]
#     if max_distance < total_distance:
#         max_distance = total_distance
#
# print(max_distance)
#

# ##########################################################################
# from collections import defaultdict
# from heapq import heappush, heappop


def dijkstra(start, graph, N):
    INF = float('inf')
    distance = [INF] * (N + 1)
    distance[start] = 0
    q = []
    heappush(q, (0, start))

    while q:
        current_dist, current_node = heappop(q)

        if distance[current_node] < current_dist:
            continue

        for next_dist, next_node in graph[current_node]:
            new_dist = current_dist + next_dist
            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                heappush(q, (new_dist, next_node))

    return distance


N, M, X = map(int, input().split())
graph = defaultdict(list)
graph_rev = defaultdict(list)


for _ in range(M):
    s, e, t = map(int, input().split())
    graph[s].append((t, e))
    graph_rev[e].append((t, s))

to_X = dijkstra(X, graph_rev, N)
from_X = dijkstra(X, graph, N)

max_distance = 0
for i in range(1, N + 1):
    if to_X[i] != float('inf') and from_X[i] != float('inf'):
        total_distance = to_X[i] + from_X[i]
        max_distance = max(max_distance, total_distance)

print(max_distance)
