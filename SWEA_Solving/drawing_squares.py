T = int(input())

for t in range(1, T + 1):
    N = int(input())
    table = [[0] * N for _ in range(N)]
    max_area = 0
    count_max = 0
    for i in range(N):
        table[i] = list(map(int, input().split()))

    for i in range(N):
        for j in range(N):
            start = table[i][j]
            for p in range(i, N):
                for q in range(j, N):
                    if start == table[p][q]:
                        area = (p - i + 1) * (q - j + 1)
                    
                        if max_area < area:
                            max_area = area
                            count_max = 1
                    
                        elif max_area == area:
                            count_max += 1

    print(f'#{t} {count_max}')