from collections import deque
import sys
sys.stdin = open('input.txt')
# boj 12851


def teleport(num):  # 2x 로 이동    ( 범위 안에 있는 )
    return 2 * num if 2 * num <= 100000 else -1


def left(num):  # x - 1 로 이동    ( 범위 안에 있는 )
    return num - 1 if num > 0 else -1


def right(num):  # x + 1 로 이동    ( 범위 안에 있는 )
    return num + 1 if num + 1 <= 100000 else -1


def hide_n_seek(start, end):  # bfs
    global cnt
    visited = [300000] * 100001
    visited[start] = 0
    ways = [0] * 100001
    ways[start] = 1
    funcs = [(teleport, 1), (right, 1), (left, 1)]

    q = deque([(start, 0)])

    if start == end:  # 이미 도착한 경우
        return 0, 1

    while q:
        now, moves = q.popleft()

        for func, time in funcs:
            next = func(now)

            if next == -1:  # 범위 초과
                continue
            new_time = moves + time

            if visited[next] > new_time:
                visited[next] = new_time
                ways[next] = ways[now]
                q.append((next, new_time))

            elif new_time == visited[next]:
                ways[next] += ways[now]

    return visited[end], ways[end]


N, K = map(int, input().split())

print(*hide_n_seek(N, K))
