import sys
sys.stdin = open('input.txt')


def dfs(depth):
    if depth == M:   # M개 뽑으면 출력
        print(*result)
        return

    for i in range(N):
        if visited[arr[i]] == 0:
            result.append(arr[i])
            visited[arr[i]] = 1
            dfs(depth + 1)
            visited[arr[i]] = 0
            result.pop()


N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
visited = [0] * 10001
result = []

dfs(0)

#
# def dfs(depth):
#     global rain
#     if depth == M:   # M개 뽑으면 출력
#         print(*result)
#         return
#
#     for i in range(1, N + 1):
#         if len(result) == 0 or rain <= i:
#             result.append(i)
#             rain = i
#             dfs(depth + 1)
#             result.pop()
#             if len(result) != 0:
#                 rain = result[-1]
#             else:
#                 rain = 1
#
#
# N, M = map(int, input().split())
# visited = [False] * (N + 1)
# result = []
# rain = 1
#
# dfs(0)