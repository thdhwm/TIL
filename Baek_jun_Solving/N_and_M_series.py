import sys
sys.stdin = open('input.txt')


def dfs(depth):
    global result, rain
    prev = 0

    if depth == M:   # M 개 뽑으면 출력
        # ans.append(result)      # 복사 문제....
        # result = result[:]      # global scope에서 result 받으니까 복사...

        print(*result)
        return

    for i in range(N):
        # if visited[i] != 0:
        #     continue

        if prev == arr[i]:
            continue

        if len(result) == 0 or rain <= arr[i]:
            rain = arr[i]
            result.append(arr[i])
            # visited[i] = 1
            dfs(depth + 1)
            # visited[i] = 0
            result.pop()
            if len(result) != 0:
                rain = result[-1]
            else:
                rain = 1
            prev = arr[i]


N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
# visited = [0] * N   # idx 로 visited 관리
result = []
rain = 1
dfs(0)

# ##################################################################

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
# ################################################

#
# def dfs(depth):
#     global result
#     prev = 0
#
#     if depth == M:   # M 개 뽑으면 출력
#         print(*result)
#         return
#
#     for i in range(N):
#         # if visited[i] == 0 and prev != arr[i]:
#         if prev != arr[i]:
#             result.append(arr[i])
#             # visited[i] = 1
#             dfs(depth + 1)
#             # visited[i] = 0
#             result.pop()
#             prev = arr[i]
#
#
# N, M = map(int, input().split())
# arr = sorted(list(map(int, input().split())))
# # visited = [0] * N
# result = []
#
# dfs(0)
