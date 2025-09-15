def find(x):
    if x == parents[x]:
        return x

    parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    parent_x = find(x)
    parent_y = find(y)

    if parent_x == parent_y:  # cycle
        return False

    parents[parent_x] = parent_y
    return True


def check():
    for i in range(N):
        for j in range(i + 1, N):
            if graph[i][j] == 0:
                continue

            if not union(i, j): # cycle
                return False

    return True


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    parents = [i for i in range(N + 1)]

    result = check()

    if result:
        print(f'#{test_case} STABLE')
    else:
        print(f'#{test_case} WARNING')
