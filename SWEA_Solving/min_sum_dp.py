import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0] * N for _ in range(N)]

    dp[0][0] = table[0][0]
    for i in range(1, N):
        dp[0][i] = table[0][i] + dp[0][i - 1]
        dp[i][0] = table[i][0] + dp[i - 1][0]

    for i in range(1, N):
        for j in range(1, N):
            dp[i][j] = table[i][j] + min(dp[i - 1][j], dp[i][j - 1])

    print(f'#{test_case} {dp[N -1][N -1]}')
