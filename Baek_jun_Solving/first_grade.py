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
