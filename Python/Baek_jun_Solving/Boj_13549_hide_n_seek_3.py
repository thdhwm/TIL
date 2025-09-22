# from collections import deque
# import sys
# sys.stdin = open('input.txt')
# # boj 13549

# def teleport(num):     # 2x 로 이동    ( 범위 안에 있는 )
#     return 2 * num if 2 * num <= 100000 else -1


# def left(num):     # x - 1 로 이동    ( 범위 안에 있는 )
#     return num - 1 if num > 0 else -1


# def right(num):    # x + 1 로 이동    ( 범위 안에 있는 )
#     return num + 1 if num + 1 <= 100000 else -1


# def hide_n_seek(start, end):     # bfs
#     visited = [300000] * 100001
#     visited[start] = 0
#     funcs = [(teleport, 0), (right, 1), (left, 1)]

#     q = deque([(start, 0)])

#     if start == end:       # 이미 도착한 경우
#         return 0

#     while q:
#         now, moves = q.popleft()

#         for func, time in funcs:
#             next = func(now)
#             if next == -1:  # 범위 초과
#                 continue
#             new_time = moves + time

#             if visited[next] > new_time:
#                 visited[next] = new_time

#                 # if next == end:
#                 #     return new_time

#                 if time == 0:  # teleport 우선 처리
#                     q.appendleft((next, new_time))

#                 else:  # 걸음 이동: 큐 뒤에 추가
#                     q.append((next, new_time))
#     return visited[end]

# N, M = map(int, input().split())

# print(hide_n_seek(N, M))

# #######################################################################################
from heapq import heappop, heappush
import sys
sys.stdin = open('input.txt')
# # boj 13549


def teleport(num):  # 2x 로 이동    ( 범위 안에 있는 )
    return 2 * num if 2 * num <= 100000 else -1


def left(num):  # x - 1 로 이동    ( 범위 안에 있는 )
    return num - 1 if num > 0 else -1


def right(num):  # x + 1 로 이동    ( 범위 안에 있는 )
    return num + 1 if num + 1 <= 100000 else -1


def hide_n_seek(start, end):  # bfs
    visited = [300000] * 100001   # 범위 밖 임의의 큰 수 1 based indexing
    visited[start] = 0
    funcs = [(0, teleport), (1, right), (1, left)]   # priority queue 하기 위해 cost( time )을 앞으로

    pq = [(0, start)]

    if start == end:  # 이미 도착한 경우
        return 0

    while pq:
        moves, now = heappop(pq)

        if now == M:    # visited 숫자로 시간 관리
            return visited[now]

        for time, func in funcs:
            next = func(now)
            if next == -1:  # 범위 초과
                continue

            new_time = moves + time

            if visited[next] > new_time:     # 더 빨리 도착하는 경우만 갱신
                visited[next] = new_time
                heappush(pq, (new_time, next))

    return visited[end]


N, M = map(int, input().split())

print(hide_n_seek(N, M))
