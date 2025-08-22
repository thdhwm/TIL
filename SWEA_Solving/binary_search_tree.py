import sys
sys.stdin = open('input.txt')

#
# def binary_search(depth, num):     # binary_search(1, i)
#     if len(table[depth]) == 0:
#         table[depth].append(num)
#
#     elif table[depth][0] > num:
#         binary_search(2 * depth, num)
#
#     else:
#         binary_search(2 * depth + 1, num)
#
#
# T = int(input())
#
# for test_case in range(1, T + 1):
#     N = int(input())
#     table = [[] for _ in range(N + 1)]
#
#     for i in range(1, N + 1):       # 1, 2, 3, ... N
#         binary_search(1, i)
#     # 루트(1) 에 있는 값, (N // 2) 에 있는 값
#
#     print(f'#{test_case} {table[1]} {table[N // 2]}')
