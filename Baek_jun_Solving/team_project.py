# T = int(input())
#
# for test_case in range(1, T + 1):
#     N = int(input())
#     students = [0] + list(map(int, input().split()))    # 1-based idx
#     grouped = [1] * (N + 1)    # 그룹이 되었으면 -> 0으로   result = sum(grouped)
#
#
#     for i in range(1, len(students) + 1):
#         root = i
#         stack = []
#
#         while students[root] != i:
#             root = students[root]
#             stack.append(root)
#
#             if students[root] == root:
#                 grouped[root] = 0
#                 break
#
# 리스트 쭉쭉 가다가,,, idx = value 인 노드 만나면 다시 역순...?
# idx = value 인 노드를 못 만나면 0....?
# ################################################################################################
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    students = [0] + list(map(int, input().split()))
    visited = [0] * (N + 1)
    total = 0

    for i in range(1, N + 1):
        if visited[i] != 0:
            continue

        stack = []
        now = i
        while not visited[now]:
            visited[now] = 1
            stack.append(now)
            now = students[now]

        if now in stack:    # ex. 1 -> 2 -> 4 -> 7 -> 6 -> 4
            sCycle = stack.index(now)         # cycle 시작점 idx 찾아서

            len_cycle = len(stack) - sCycle   # 사이클 길이 = 전체 - 사이클 아닌거

            total += len_cycle                # 사이클 길이 만큼 total 증가

    print(N - total)        # 그룹이 안된 거는 전체 에서 사이클 인 것 뺸만큼
