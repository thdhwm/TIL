# 1859. 백만 장자 프로젝트 문제 

import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    prices = list(map(int, input().split()))
    total = 0


    now_max = prices[-1]
    for i in range(len(prices) - 1, -1, -1):
        if prices[i] <= now_max:
            total += (now_max - prices[i])
        else:
            now_max = prices[i]

    print(f'#{test_case} {total}')

# ##################################################################
#
# from collections import deque
# import sys
# sys.stdin = open('input.txt')
#
# T = int(input())
#
# for test_case in range(1, T + 1):
#     N = int(input())
#     prices = deque(list(map(int, input().split())))
#     total = 0
#
#     now_max = prices.pop()
#     while prices:
#         now_price = prices.pop()
#         if now_price <= now_max:
#             total += (now_max - now_price)
#         else:
#             now_max = now_price
#
#     print(f'#{test_case} {total}')