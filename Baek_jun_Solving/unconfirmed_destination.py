from collections import defaultdict
from heapq import heappush, heappop
import sys
sys.stdin = open('input.txt', 'r')


def dijkstra(start):
    pass


T = int(input())
for test_case in range(1, T + 1):
    n, m, t = map(int, input().split())    # n - nodes, m - edges, t - candidates
    s, g, h = map(int, input().split())    # s - start, g,h - must use edge between g,h
    graph = defaultdict(list)
    candidates = []

    for _ in range(m):
        a, b, d = map(int, input().split())   # s, e, distance
        graph[a].append((d, b))
        graph[b].append((d, a))

    for _ in range(t):
        candidates.append(int(input()))
