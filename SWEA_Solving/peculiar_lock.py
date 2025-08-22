from collections import deque
import sys
sys.stdin = open('input.txt')


def double(num):
    result = (2 * num) % 10000
    return result


def subtract(num):
    if num == 0:
        return 9999
    else:
        result = num - 1
        return result


def left(num):    # ccw
    A, BCD = divmod(num, 1000)
    result = BCD * 10 + A
    return result


def right(num):    # cw
    ABC, D = divmod(num, 10)
    result = (D * 1000) + ABC
    return result


def find_password(num, arr):
    q = deque([(num, '')])

    while q:
        now, dslr = q.popleft()

        if now == B:
            return dslr

        q.append((double(now), dslr + 'D'))

        q.append((subtract(now), dslr + 'S'))

        q.append((left(now), dslr + 'L'))

        q.append((right(now), dslr + 'R'))


T = int(input())

for test_case in range(1, T + 1):
    A, B = map(int, input().split())   # A - 지금 번호, B - 정답

    print(f'#{test_case} {find_password(A, "")}')
