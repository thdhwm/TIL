from collections import deque
import sys
sys.stdin = open('input.txt')


def bfs(node):
    q = deque([node])
    while q:
        now_at = q.popleft()

        if len(connection_list[now_at]) == 0:
            return

        for next_node in connection_list[now_at]:
            if visited[next_node] != 0:
                continue

            visited[next_node] = 1
            q.append(next_node)


def dfs(node):
    for next_node in connection_list[node]:
        if len(connection_list[node]) == 0 or sum(visited) == N_nodes:
            return

        if visited[next_node] == 1:
            continue

        visited[next_node] = 1
        dfs(next_node)


T = int(input())

for test_case in range(1, T + 1):
    N_nodes = int(input())
    N_roads = int(input())
    connection_list = [[] for _ in range(N_nodes + 1)]
    visited = [0] * (N_nodes + 1)
    visited[1] = 1

    for _ in range(N_roads):
        start, end = map(int, input().split())
        connection_list[start].append(end)
        connection_list[end].append(start)

    # bfs(1)
    dfs(1)
    result = sum(visited) - 1
    print(f'#{test_case} {result}')




