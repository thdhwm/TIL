from collections import deque
import sys
sys.stdin = open('input.txt')


def teleport(num):     # 2x 로 이동    ( 범위 안에 있는 )
    return 2 * num if 2 * num <= 100000 else -1


def left(num):     # x - 1 로 이동    ( 범위 안에 있는 )
    return num - 1 if num - 1 >= 0 else -1


def right(num):    # x + 1 로 이동    ( 범위 안에 있는 )
    return num + 1 if num + 1 <= 100000 else -1


def go_to_school(start, end):     # bfs
    visited = [0] * 100001
    visited[start] = 1
    funcs = [teleport, right, left]

    q = deque([(start, 0)])

    if start == end:       # 이미 도착한 경우
        return 0
    
    while q:
        now, moves = q.popleft()

        for func in funcs:
            next = func(now)

            if next != -1 and visited[next] == 0:
                if next == end:
                    return moves + 1
            
                visited[next] = 1
                q.append((next, moves + 1))

            else:
                continue


T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    
    print(f'#{test_case} {go_to_school(N, M)}')
