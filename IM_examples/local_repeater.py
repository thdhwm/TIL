T = int(input())

for t in range(1, T + 1):
    N = int(input())
    table = [[0] * N for _ in range(N)]
    y = 0
    x = 0
    power_D = 0
    max_power_D = 0
    R = 0

    for i in range(N):
        table[i] = list(map(int, input().split()))

######################  입력 받기 끝  ######################

    for i in range(N):
        for j in range(N):
            if table[i][j] == 2:
                y, x = i, j

    for i in range(N):
        for j in range(N):
            if table[i][j] == 1:
                hy, hx = i, j
                power_D = (hy - y) ** 2 + (hx - x) ** 2
                if max_power_D < power_D:
                    max_power_D = power_D

    for i in range(1, 20):
        if i**2 >= max_power_D:
            R = i
            break

    print(f'#{t} {R}')

# 24 min.
# pass in 1 go
