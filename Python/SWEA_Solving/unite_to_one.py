from collections import defaultdict
from heapq import heappop, heappush
import sys
sys.stdin = open('input.txt', 'r')


# def find(parents, x):
#     root = x
#
#     while parents[root] != root:
#         root = parents[root]
#
#     while parents[x] != x:
#         next_node = parents[x]
#         parents[x] = root
#         x = next_node
#
#     return root
#
#
# def union(parents, x, y):
#     parent_x = find(parents, x)
#     parent_y = find(parents, y)
#
#     if parent_x < parent_y:
#         parents[parent_y] = parent_x
#
#     else:
#         parents[parent_x] = parent_y
#
#
# def kruskal(edges, n):
#     edges.sort()
#     parents = [i for i in range(n)]
#     total = 0
#
#     for cost, start, end in edges:
#         if find(parents, start) != find(parents, end):
#             union(parents, start, end)
#             total += cost
#
#     return round(total)


def prim(graph, start, n):
    visited = [0] * n
    pq = [(0, start)]
    total = 0

    while pq:
        cost, node = heappop(pq)
        if visited[node]:
            continue

        visited[node] = True
        total += cost
        for next_cost, next_node in graph[node]:
            if not visited[next_node]:
                heappush(pq, (next_cost, next_node))
    return round(total)


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    xCords = list(map(int, input().split()))
    yCords = list(map(int, input().split()))
    cords = []
    # edges = []
    graph = defaultdict(list)
    E = float(input())

    for x in range(N):
        cords.append((xCords[x], yCords[x]))

    for i in range(N):
        for j in range(i + 1, N):
            money = E * ((cords[i][0] - cords[j][0])**2 + (cords[i][1] - cords[j][1])**2)
            # edges.append((money, i, j))
            graph[i].append((money, j))
            graph[j].append((money, i))
    #
    print(f'#{test_case} {prim(graph, 0, N)}')
    # print(f'#{test_case} {kruskal(edges, N)}')

# #####################################################################################################################






















