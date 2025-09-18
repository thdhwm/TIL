import sys
sys.stdin = open('input.txt')

#
# def power_set(depth):
#     global pSet, min_height
#     prev = 0
#     tower = sum(pSet)
#     if tower >= min_height:
#         return
#
#     if depth == N:
#         return
#
#     for i in range(N):
#         if visited[i] != 0:
#             continue
#         if prev == heights[i]:
#             continue
#
#
#
#         visited[i] = 1
#         pSet.append(heights[i])
#         tower = sum(pSet)
#         if tower >= B:
#             min_height = min(min_height, tower)
#         power_set(depth + 1)
#         pSet.pop()
#         visited[i] = 0
#         prev = heights[i]
#     return
#
#
# T = int(input())
#
# for test_case in range(1, T + 1):
#     N, B = map(int, input().split())    # n - 사람 수, b - 탑 높이
#     heights = sorted(list(map(int, input().split())))
#     visited = [0] * N
#     pSet = []
#     min_height = 21e8
#     power_set(0)
#     result = min_height - B
#     print(f'#{test_case} {result}')

# # #############################################################################################################

def tower(n, b, heights):
    min_height = 21e8

    # 비트연산
    for bit in range(1, 1 << n):  # 1 ~ 2^n
        total_height = 0

        for i in range(n):
            if bit & (1 << i):  # ex 4개일 때 => 0001, 0010, 0100, 1000
                total_height += heights[i]

        if total_height >= b:
            min_height = min(min_height, total_height - b)

    return min_height


T = int(input())
for test_case in range(1, T + 1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))

    print(f'#{test_case} {tower(N, B, heights)}')

# #######################################################################
# 문제풀이 강의





























