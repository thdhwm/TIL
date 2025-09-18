import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())    # ex. n - 3, k - 10

coins = []             # [1, 2, 5]
dp = [0] * (K + 1)
dp[0] = 1

for _ in range(N):
    coins.append(int(input()))

for coin in coins:
    for i in range(coin, K + 1):    # ex. 2, 4, 6, 8, 10
        dp[i] += dp[i - coin]

print(dp[K])
