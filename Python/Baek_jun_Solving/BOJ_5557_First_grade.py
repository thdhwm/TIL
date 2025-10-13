import sys
sys.stdin = open('input.txt')


# def calc(now, depth):
#     global cnt
#
#     if depth == len(numbers) - 1:
#         if now == ans:
#             cnt += 1
#         return
#
#     if 0 > now or now > 20:
#         return
#
#     calc(now + numbers[depth + 1], depth + 1)
#     calc(now - numbers[depth + 1], depth + 1)
#
#
#
#
# N = int(input())
#
# *numbers, ans = list(map(int, input().split()))
# cnt = 0
#
# calc(numbers[0], 0)
# print(cnt)
# #######################################################################################
# 40
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 1 1
# 40개.. 넘 많아서 백트레킹 안댄다
# 다른 방법
# dp?

# 11
# 8 3 2 4 8 7 2 4 0 8 = 8

# 8 3 2 4 8 7 2 4 0 = 16

# 8 3 2 4 8 7 2 4 0 = 0
# dp[i][j] -> i 번째 까지 연산한 결과가 j 를 만드는 가지 수, 0 <= j <= 20 -> 21개
# #######################################################################################

N = int(input())
*numbers, ans = list(map(int, input().split()))
dp = [[0]*21 for _ in range(N - 1)]
dp[0][numbers[0]] = 1
for i in range(1, N - 1):
    for j in range(21):
        if j - numbers[i] >= 0:
            dp[i][j - numbers[i]] += dp[i - 1][j]
        if j + numbers[i] <= 20:
            dp[i][j + numbers[i]] += dp[i - 1][j]
print(dp[N - 2][ans])
# 얘는 안되고, 밑에는 됨...?   * 이라 안되는 것인가?
# #################################################
N = int(input())
numbers = list(map(int, input().split()))
ans = numbers[-1]
numbers = numbers[:-1]
dp = [[0] * 21 for _ in range(N - 1)]
dp[0][numbers[0]] = 1

for i in range(1, N - 1):
    for j in range(21):
        if dp[i - 1][j] == 0:
            continue
        if j - numbers[i] >= 0:
            dp[i][j - numbers[i]] += dp[i - 1][j]
        if j + numbers[i] <= 20:
            dp[i][j + numbers[i]] += dp[i - 1][j]

print(dp[N - 2][ans])
