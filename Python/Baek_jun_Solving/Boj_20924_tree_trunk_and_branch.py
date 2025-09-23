from collections import defaultdict
import sys
sys.stdin = open('input.txt', 'r')

#
# def trunk(root, total):
#     global dTrunk, giga
#     start = root
#     visited[start] = 1
#
#     if len(graph[start]) <= 2:
#         for node, dist in graph[start]:
#             if visited[node]:
#                 continue
#             # visited[node] = 1
#             trunk(node, total + dist)
#
#     else:
#         dTrunk = total
#         giga = start
#         return
#
#
# def branch(root, total):
#     global dBranch
#     start = root
#     visited[start] = 1
#
#     if len(graph[start]) == 1:
#         dBranch = max(dBranch, total)
#         return
#
#     for node, dist in graph[start]:
#         if visited[node]:
#             continue
#
#         branch(node, total + dist)
#
#
# N, R = map(int, input().split())    # n - num nodes, R - root node num
# graph = defaultdict(list)
# visited = [0] * (N + 1)
# visited[R] = 1
# dTrunk = 0
# dBranch = 0
# giga = 0
#
# for _ in range(N - 1):
#     a, b, d = map(int, input().split())
#     graph[a].append((b, d))
#     graph[b].append((a, d))
#
# trunk(R, 0)
# # print(dTrunk, giga)    # ex. dTrunk - 6, giga - 4
# branch(giga, 0)
#
# print(dTrunk, dBranch)

# ####################################################################################################
# from collections import defaultdict

#
# def trunk(root):
#     global dTrunk, giga
#     stack = [(root, 0, 0)]  # (node, parent, total_distance)
#     visited[root] = 1
#
#     while stack:
#         node, parent, total = stack.pop()
#         degree = len(graph[node])  # 현재 노드의 차수
#         if node != root:
#             degree -= 1  # 부모 노드 제외
#
#         # 기가 노드 조건: 차수가 0(리프) 또는 2 이상 (루트 기준 3 이상)
#         if degree == 0 or degree >= 2:
#             dTrunk = total
#             giga = node
#             return
#
#         # 차수가 1(루트 기준 2)인 경우, 다음 노드 탐색
#         for next_node, dist in graph[node]:
#             if next_node != parent and not visited[next_node]:
#                 visited[next_node] = 1
#                 stack.append((next_node, node, total + dist))
#
#
# def branch(root):
#     global dBranch
#     stack = [(root, 0, 0)]  # (node, parent, total_distance)
#     visited[root] = 1
#
#     while stack:
#         node, parent, total = stack.pop()
#
#         # 리프 노드: 차수가 1이고 부모가 있는 경우
#         if len(graph[node]) == 1 and parent != -1:
#             dBranch = max(dBranch, total)
#             continue
#
#         # 자식 노드 탐색
#         for next_node, dist in graph[node]:
#             if next_node != parent and not visited[next_node]:
#                 visited[next_node] = 1
#                 stack.append((next_node, node, total + dist))
#
#
# N, R = map(int, input().split())  # n - num nodes, R - root node num
# graph = defaultdict(list)
# visited = [0] * (N + 1)
# dTrunk = 0   # 기둥 길이
# dBranch = 0    # 가지 길이
# giga = R      # giga node == root 로 초기화
#
# for _ in range(N - 1):
#     a, b, d = map(int, input().split())
#     graph[a].append((b, d))
#     graph[b].append((a, d))
#
# trunk(R)
#
# branch(giga)
#
# print(dTrunk, dBranch)

# ###################################################################################################
# from collections import defaultdict


def trunk(root):
    global dTrunk, giga
    stack = [(root, None, 0)]  # (노드, 부모, 누적 거리)
    visited[root] = 1

    while stack:
        node, parent, total = stack.pop()
        # 자식 수 계산 (부모 제외)
        children = [next_node for next_node, _ in graph[node] if next_node != parent]
        degree = len(children)

        if degree >= 2 or degree == 0:  # 기가 노드 조건: 차수가 2 이상이거나 리프 노드
            dTrunk = total
            giga = node
            return

        for next_node, dist in graph[node]:
            if not visited[next_node]:
                visited[next_node] = 1
                stack.append((next_node, node, total + dist))


def branch(root, total):
    global dBranch
    if len([n for n, _ in graph[root] if not visited[n]]) == 0:  # 리프 노드
        dBranch = max(dBranch, total)
        return

    for next_node, dist in graph[root]:
        if not visited[next_node]:
            visited[next_node] = 1
            branch(next_node, total + dist)
            visited[next_node] = 0


N, R = map(int, input().split())
graph = defaultdict(list)
visited = [0] * (N + 1)
dTrunk = 0
dBranch = 0
giga = R

for _ in range(N - 1):
    a, b, d = map(int, input().split())
    graph[a].append((b, d))
    graph[b].append((a, d))  # 양방향 간선 추가

trunk(R)

branch(giga, 0)

print(dTrunk, dBranch)
