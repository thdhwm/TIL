import sys
sys.stdin = open('input.txt')
#
# N = int(input())
# table = [list(map(int, input().split())) for _ in range(N)]
#
# dp = [[[21e8, 0] for _ in range(N)] for _ in range(N)]    # min, max
# for k in range(N):
#     dp[0][k] = [table[0][k], table[0][k]]
#
# for i in range(1, N):
#     for j in range(N):
#         if j - 1 < 0:
#             dp[i][j][0] = table[i][j] + min(dp[i - 1][j][0], dp[i - 1][j + 1][0])  # min
#             dp[i][j][1] = table[i][j] + max(dp[i - 1][j][1], dp[i - 1][j + 1][1])  # max
#
#         elif j + 1 >= N:
#             dp[i][j][0] = table[i][j] + min(dp[i - 1][j - 1][0], dp[i - 1][j][0])  # min
#             dp[i][j][1] = table[i][j] + max(dp[i - 1][j - 1][1], dp[i - 1][j][1])  # max
#
#         else:
#             dp[i][j][0] = table[i][j] + min(dp[i - 1][j - 1][0], dp[i - 1][j][0], dp[i - 1][j + 1][0])    # min
#             dp[i][j][1] = table[i][j] + max(dp[i - 1][j - 1][1], dp[i - 1][j][1], dp[i - 1][j + 1][1])    # max
#
# print(max(dp[N - 1][x][1] for x in range(N)), min(dp[N - 1][x][0] for x in range(N)))

# ################################################################################################################
N = int(input())

prev_dp = [[0, 0] for _ in range(3)]  # [min, max]
curr_dp = [[0, 0] for _ in range(3)]

first_row = list(map(int, input().split()))
for j in range(3):
    prev_dp[j] = [first_row[j], first_row[j]]

for i in range(1, N):
    row = list(map(int, input().split()))
    for j in range(3):

        if j == 0:
            curr_dp[j][0] = row[j] + min(prev_dp[j][0], prev_dp[j + 1][0])
            curr_dp[j][1] = row[j] + max(prev_dp[j][1], prev_dp[j + 1][1])
        elif j == 2:
            curr_dp[j][0] = row[j] + min(prev_dp[j - 1][0], prev_dp[j][0])
            curr_dp[j][1] = row[j] + max(prev_dp[j - 1][1], prev_dp[j][1])
        else:
            curr_dp[j][0] = row[j] + min(prev_dp[j - 1][0], prev_dp[j][0], prev_dp[j + 1][0])
            curr_dp[j][1] = row[j] + max(prev_dp[j - 1][1], prev_dp[j][1], prev_dp[j + 1][1])

    prev_dp = [row[:] for row in curr_dp]

max_value = max(prev_dp[j][1] for j in range(3))
min_value = min(prev_dp[j][0] for j in range(3))
print(max_value, min_value)
