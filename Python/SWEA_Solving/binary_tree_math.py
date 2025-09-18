import sys
sys.stdin = open('input.txt')


def calc(start):
    now = heap[start]

    if isinstance(now, str) and now.isdecimal():
        return int(now)

    operator, left_child, right_child = now
    left_value = calc(int(left_child))
    right_value = calc(int(right_child))

    if operator == '+':
        return left_value + right_value

    elif operator == '-':
        return left_value - right_value

    elif operator == '*':
        return left_value * right_value

    elif operator == '/':
        return left_value / right_value


for test_case in range(1, 11):
    N = int(input())
    heap = [''] * (N + 1)

    # 입력 처리
    for _ in range(N):
        info = input().split()
        node = int(info[0])
        if len(info) == 2:                  # number
            heap[node] = info[1]
        else:                             # operator
            heap[node] = (info[1], info[2], info[3])

    result = int(calc(1))
    print(f'#{test_case} {result}')
