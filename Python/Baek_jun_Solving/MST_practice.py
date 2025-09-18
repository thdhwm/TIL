from heapq import heappush, heappop, heapify
from collections import defaultdict
import sys
sys.stdin = open('input.txt')

#
# def prim(graph, start, n):   # connection_list, start, num of nodes
#     visited = [False] * (n + 1)
#     pq = [(0, start)]
#     mst_cost = 0
#
#     while pq:
#         cost, node = heappop(pq)
#         if visited[node]:
#             continue
#
#         visited[node] = True
#         mst_cost += cost
#         for next_cost, next_node in costs[node]:
#             if not visited[next_node]:
#                 heappush(pq, (next_cost, next_node))
#
#     return mst_cost
#
#
# V, E = map(int, input().split())    # 정점 V(1 ≤ V ≤ 10,000) 간선 E(1 ≤ E ≤ 100,000)
# costs = defaultdict(list)
#
# for _ in range(E):
#     A, B, C = map(int, input().split())    # A -> B cost C, C under abs(1,000,000)
#     costs[A].append((C, B))
#
# print(prim(costs, 1, V))

# ####################################################


def find(parent, a):
    root = a
    # find root node for a
    while parent[root] != root:    # root - temp to chg a
        root = parent[root]
    # compress path (flatten)
    while parent[a] != a:
        next_node = parent[a]
        parent[a] = root
        a = next_node

    return root


def union_by_rank(parent, rank, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)
    if root_a != root_b:
        if rank[root_a] < rank[root_b]:    # lower under higher
            parent[root_a] = root_b
        elif rank[root_a] > rank[root_b]:
            parent[root_b] = root_a
        else:    # same rank
            parent[root_b] = root_a
            rank[root_a] += 1


def kruskal(edges, n):
    edges.sort(key=lambda x: x[2])
    parent = [i for i in range(n + 1)]
    rank = [0] * (n + 1)
    mst_cost = 0

    for s, e, c in edges:
        if find(parent, s) != find(parent, e):
            union_by_rank(parent, rank, s, e)
            mst_cost += c

    return mst_cost


V, E = map(int, input().split())    # 정점 V(1 ≤ V ≤ 10,000) 간선 E(1 ≤ E ≤ 100,000)
edges = []

for _ in range(E):
    edge = tuple(map(int, input().split()))
    edges.append(edge)

print(kruskal(edges, V))









