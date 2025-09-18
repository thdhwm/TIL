import sys
sys.stdin = open('input.txt')


def dfs(level, num):
    if level == 2:
        print(*route)
        return

    for i in range(N):
        if table[num][i] == 0 or visited[i] == 1:
            continue

        next_num = i
        route.append(next_num)
        visited[next_num] = 1
        dfs(level + 1, next_num)
        route.pop()


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    depth = 0
    start = 0
    visited = [0] * N
    visited[0] = 1
    route = [0]

    print(f'#{test_case}')
    dfs(depth, start)
