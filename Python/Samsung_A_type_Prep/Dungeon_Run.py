from collections import deque
import sys
sys.stdin = open('input.txt')


def dungeon(n, g):    # now, golds
    q = deque([(n, g)])
    visited = [0] * N
    visited[0] = 1

    while q:
        now, golds = q.popleft()

        if len(adj_list[now]) == 0:
            return

        for next_node, cost in adj_list[now]:
            if golds < cost:
                continue
            can_go.append(next_node)
            visited[next_node] = 1
            q.append((next_node, golds - cost))

    return


T = int(input())
for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())    # n- nodes, m - edges, k -golds
    adj_list = [[] for _ in range(N)]
    can_go = []
    for _ in range(M):
        start, end, fee = map(int, input().split())
        adj_list[start].append((end, fee))

    dungeon(0, K)
    print(f'#{test_case}', *sorted(can_go))
