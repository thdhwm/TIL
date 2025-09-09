import sys
sys.stdin = open('input.txt')


def power_set(depth):
    global pSet, min_height
    prev = 0
    tower = sum(pSet)
    if tower >= min_height:
        return

    if depth == N:
        return

    for i in range(N):
        if visited[i] != 0:
            continue
        if prev == heights[i]:
            continue



        visited[i] = 1
        pSet.append(heights[i])
        tower = sum(pSet)
        if tower >= B:
            min_height = min(min_height, tower)
        power_set(depth + 1)
        pSet.pop()
        visited[i] = 0
        prev = heights[i]
    return


T = int(input())

for test_case in range(1, T + 1):
    N, B = map(int, input().split())    # n - 사람 수, b - 탑 높이
    heights = sorted(list(map(int, input().split())))
    visited = [0] * N
    pSet = []
    min_height = 21e8
    power_set(0)
    result = min_height - B
    print(result)

# # #############################################################################################################

# def dfs(depth):
#     global result
#     prev = 0
#
#     if depth == M:   # M 개 뽑으면 출력
#         print(*result)
#         return
#
#     for i in range(N):
#         if visited[i] == 0 and prev != arr[i]:
#             result.append(arr[i])
#             visited[i] = 1
#             dfs(depth + 1)
#             visited[i] = 0
#             result.pop()
#             prev = arr[i]
#
#
# N, M = map(int, input().split())
# arr = sorted(list(map(int, input().split())))
# visited = [0] * N
# result = []
#
# dfs(0)