import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())    # ex. n - 3, k - 10

INF = float('inf')
coins = []             # [1, 2, 5]
dp = [INF] * (K + 1)
dp[0] = 0

for _ in range(N):
    coins.append(int(input()))

coins = list(set(coins))    # 중복 제거
coins.sort()                # 값이 작은 코인 먼저

for coin in coins:
    for i in range(coin, K + 1):
        dp[i] = min(dp[i - coin] + 1, dp[i])

if dp[K] == INF:
    print(-1)
else:
    print(dp[K])
