from collections import defaultdict
import sys
sys.stdin = open('input.txt')

N, E = map(int, input().split())    # n - nodes, e - edges
graph = defaultdict(list)
for _ in range(E):
    a, b, c = map(int, input().split())  # both ways a to b, cost c
    graph[a].append((c, b))
    graph[b].append((c, a))