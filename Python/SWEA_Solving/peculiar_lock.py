from collections import deque
import sys
sys.stdin = open('input.txt')
# also BOJ 9019

def double(num):        # D 버튼 연산
    result = (2 * num) % 10000
    return result


def subtract(num):        # S 버튼 연산
    if num == 0:
        return 9999
    else:
        result = num - 1
        return result


def left(num):    # L 버튼 연산 (ccw 돌리기)
    A, BCD = divmod(num, 1000)     # divmod -> 몫, 나머지
    result = BCD * 10 + A
    return result


def right(num):    # R 버튼 연산 (cw 돌리기)
    ABC, D = divmod(num, 10)
    result = (D * 1000) + ABC
    return result


def find_password(num, password):    # bfs
    q = deque([(num, '')])
    visited = [0] * 10000       # time out 안하게
    visited[num] = 1
    buttons = [(double, 'D'), (subtract, 'S'), (left, 'L'), (right, 'R')]

    while q:
        now, dslr = q.popleft()

        if now == password:
            return dslr
        
        for func, button in buttons:
            next_num = func(now)
            if visited[next_num] != 0:
                continue

            visited[next_num] = 1
            q.append((next_num, dslr + button))


T = int(input())

for test_case in range(1, T + 1):
    A, B = map(int, input().split())   # A - 지금 번호, B - 정답

    print(f'#{test_case} {find_password(A, B)}')
