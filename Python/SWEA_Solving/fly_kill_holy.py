T = int(input())

for t in range(1, T + 1):
    max_kill = 0
    slap = 0

    N, M = map(int, input().split())
    table = [[0] * N for _ in range(N)]

    for i in range(N):
        table[i] = list(map(int, input().split()))

    for i in range(N):
        for j in range(N):
            slap = 0

            for di in range(M):
                for dj in range(M):
                    if 0 <= (i+di) < N and 0 <= (j+dj) < N:
                        slap += table[i+di][j+dj]

            if max_kill < slap:
                max_kill = slap

    print(f'#{t} {max_kill}')


