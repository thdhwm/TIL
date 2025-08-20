import sys
sys.stdin = open('input.txt')


def dfs(now_at):
    print(now_at, end=' ')

    for go_to in range(N):
        if Nodes[now_at][go_to] == 0:
            continue

        if visited[go_to]:
            continue

        visited[go_to] = 1
        dfs(go_to)


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    Nodes = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    visited[0] = 1

    print(f'#{test_case}', end=' ')
    dfs(0)
    print('')
