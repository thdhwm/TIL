T = int(input())
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for t in range(1, T + 1):
    N, P = map(int, input().split())
    table = [[0] * N for _ in range(N)]
    max_kill = 0

    for i in range(N):
        table[i] = list(map(int, input().split()))

    for i in range(N):
        for j in range(N):
            bomb = table[i][j]
            for direction in range(4):
                for rad in range(1, P + 1):
                    if (0 <= i + rad * dy[direction] < N) and (0 <= j + rad * dx[direction] < N):
                        bomb += table[i + rad * dy[direction]][j + rad * dx[direction]]

            if max_kill < bomb:
                max_kill = bomb

    print(f'#{t} {max_kill}')

# around 16 min.
# pass in 1 go
