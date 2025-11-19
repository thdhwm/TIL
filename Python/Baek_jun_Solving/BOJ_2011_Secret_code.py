import sys
sys.stdin = open('input.txt')

data = list(map(int, input().split()))

length = len(data)

dp = [0] * (length + 1)
dp[0] = 1
dp[1] = 1

for k in range(1, length):
    i = k + 1
    if data[k] > 0:
        dp[i] += dp[i - 1]
    if 10 <= data[k] + data[k - 1]*10 <= 26:
        dp[i] += dp[i - 2]

print(dp[length] % 1000000)


# 1 00 00 0 0 0 0 0 0  이러면 어캄!
#
"""
25114

2 5 1 1 4
2 5 11 4
2 5 1 14

25 1 1 4
25 11 4
25 1 14

[][] -> 뒤에꺼랑 안 붙인 경우, 붙인 경우?

[  [][], [][], [][], [][], [][]  ]

"""
