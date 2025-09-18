T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split()) # 세로, 가로 크기   ex 3, 5
    K = int(input())  # 화력   ex 2
    table = [list(input()) for _ in range(N)]
    dy = [0, 1, 0, -1]
    dx = [-1, 0, 1, 0]
    for i in range(N):
        for j in range(M):
            if table[i][j] == '@':
                table[i][j] = '%'
                for p in range(4):
                    for k in range(1, K + 1):
                        if 0 <= i + k * dy[p] < N and 0 <= j + k * dx[p] < M:
                            if table[i + k * dy[p]][j + k * dx[p]] == '#' or table[i + k * dy[p]][j + k * dx[p]] == '@':
                                break

                            table[i + k * dy[p]][j + k * dx[p]] = '%'
    
    print(f'#{t}')
    for i in range(N):
        print(''.join(table[i]))





