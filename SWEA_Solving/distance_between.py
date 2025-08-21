from collections import deque
import sys

sys.stdin = open('input.txt')


def how_far(now):
    if now == G:  # Check if start node is destination
        return 0

    q = deque()
    q.append(now)
    while q:
        now_at = q.popleft()
        for go_to in connection_list[now_at]:
            if go_to == G:
                return visited[now_at]  # Return distance to G

            if visited[go_to] != 0 or len(connection_list[go_to]) == 0:
                continue

            visited[go_to] = visited[now_at] + 1
            q.append(go_to)
    return 0


T = int(input())

for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    connection_list = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)

    for _ in range(E):
        st_nod, ed_nod = map(int, input().split())
        connection_list[st_nod].append(ed_nod)
        connection_list[ed_nod].append(st_nod)

    S, G = map(int, input().split())
    visited[S] = 1
    result = how_far(S)
    print(f'#{test_case} {result}')

# #################################################################
# from collections import deque
# import sys
# sys.stdin = open('input.txt')
#
#
# def how_far(now):
#     q = deque()
#     q.append(now)
#     while q:
#         now_at = q.popleft()
#         if len(connection_list[now_at]) == 0:
#             return 0
#
#         else:
#             for go_to in connection_list[now_at]:
#                 if go_to == G:
#                     distance = visited[now_at]
#                     return distance
#
#                 if visited[go_to] != 0 or len(connection_list[go_to]) == 0:
#                     continue
#
#                 visited[go_to] = visited[now_at] + 1
#                 q.append(go_to)
#     return 0
#
#
# T = int(input())
#
# for test_case in range(1, T + 1):        # V와 E가 주어진다. 5<=V=50, 4<=E<=1000
#     V, E = map(int, input().split())     # V - nod 갯수, E - 간선 갯수
#     connection_list = [[] for _ in range(V + 1)]
#     visited = [0] * V
#
#     for _ in range(E):
#         st_nod, ed_nod = map(int, input().split())
#         connection_list[st_nod].append(ed_nod)
#         connection_list[ed_nod].append(st_nod)
#
#     S, G = map(int, input().split())     # S - 출발 nod, G - 도착 nod
#     visited[S] = 1
#     result = how_far(S)
#     if result == 0 or None:
#         print(f'#{test_case} {0}')
#     else:
#         print(f'#{test_case} {result}')
