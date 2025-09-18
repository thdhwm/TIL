import sys
sys.stdin = open('input.txt')


def dfs(node):
    if node == -1:
        return

    pre_order.append(node)  # VLR ( 전위 순회 )

    dfs(graph[node][0])    # 왼쪽 자식

    in_order.append(node)   # LVR ( 중위 순회 )

    dfs(graph[node][1])    # 오른쪽 자식

    post_order.append(node)   # LRV ( 후위 순회 )


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    graph = [[] for _ in range(N + 1)]

    pre_order = []
    in_order = []
    post_order = []

    for i in range(N):
        s, l, r = map(int, input().split())
        graph[s] = [l, r]

    dfs(1)

    print(f'#{test_case}')
    print(*in_order)
    print(*pre_order)
    print(*post_order)

