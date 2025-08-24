from collections import deque
import sys
sys.stdin = open('input.txt')


def div(num):
    return num // 2


def mult(num):
    return num * 2 if num * 2 <= 100000 else -1


def plus(num):
    return num + 1 if num + 1 <= 100000 else -1


def minus(num):
    return num - 1 if num - 1 >= 0 else -1


def remote(start):       # bfs
    q = deque([start])
    channels = [0] * 100001  # list to use as 'visited'
    channels[start] = 1
    funcs = [div, mult, plus, minus]
    while q:
        now = q.popleft()

        if now == D:
            return channels[now] - 1

        for func in funcs:
            next_channel = func(now)
            if next_channel == -1 or channels[next_channel] != 0:
                continue

            channels[next_channel] += channels[now] + 1
            q.append(next_channel)

    return


T = int(input())

for test_case in range(1, T + 1):
    S, D = map(int, input().split())    # S - now, D - target

    print(f'#{test_case} {remote(S)}')
