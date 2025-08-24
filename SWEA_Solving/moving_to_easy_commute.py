from collections import deque
import sys
sys.stdin = open('input.txt')


def commute(start):
    q = deque([start])
    visited = [0] * 11    # node up to 10, for idx usage 11 elements
    visited[start] = 1
    cnt_nodes = 0    # cnt available nodes
    while q:
        now = q.popleft()

        if len(adj_list[now]) == 0:
            return

        for next_node in adj_list[now]:
            if visited[next_node] != 0:
                continue

            visited[next_node] += visited[now] + 1


T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())    # n - nodes, m -edges
    adj_list = [[] for _ in range(M)]

    for _ in range(M):
        A, B = map(int, input().split())    # a - edge_start, b - edge_end
        adj_list[A].append(B)

    R, K = map(int, input().split())    # R - start, K - max cost

    commute(R)

