from collections import deque


def commute(start):
    q = deque([start])
    visited = [0] * 11    # node up to 10, for idx usage 11 elements
    visited[start] = 1
    cnt_nodes = 1    # cnt available nodes, 1 cuz already visited start
    while q:
        now = q.popleft()

        if len(adj_list[now]) == 0:
            return cnt_nodes

        for next_node in adj_list[now]:
            if visited[next_node] != 0:
                continue

            visited[next_node] += visited[now] + 1
            if visited[next_node] - 1 <= K:
                cnt_nodes += 1

            q.append(next_node)
    return cnt_nodes

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())    # n - nodes, m -edges
    adj_list = [[] for _ in range(N + 1)]

    for _ in range(M):
        A, B = map(int, input().split())    # a - edge_start, b - edge_end
        adj_list[A].append(B)
        adj_list[B].append(A)

    R, K = map(int, input().split())    # R - start, K - max cost

    print(f'#{test_case} {commute(R)}')

