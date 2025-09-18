T = int(input())    # test 케이스 수

for t in range(1, T + 1):
    N = int(input())
    table = [[0] * N for _ in range(N)]    # N*N 행렬 생성
    numbers = 1
    layers = 0                                 # 1 껍질 씩

    while N - (2 * layers) >= 1:
        # → 방향 N 칸
        for i in range(N - (2 * layers)):
            table[0 + layers][i + layers] = numbers
            numbers += 1

        # ↓ 방향 N - 1 칸
        for i in range(N - 1 - (2 * layers)):
            table[i + 1 + layers][N - 1 - layers] = numbers
            numbers += 1

        # ← 방향 N - 1 칸
        for i in range(N - 1 - (2 * layers)):
            table[N - 1 - layers][N - 2 - i - layers] = numbers
            numbers += 1

        # ↑ 방향 N - 2 칸
        for i in range(N - 2 - (2 * layers)):
            table[N - 2 - i - layers][0 + layers] = numbers
            numbers += 1

        layers += 1                   # 안으로 1 껍데기 들어감

    print(f'#{t}')
    for i in range(N):
        print(' '.join(map(str, table[i])))
