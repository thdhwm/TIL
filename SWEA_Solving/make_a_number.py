import sys
sys.stdin = open('input.txt', 'r')

def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def multi(a, b):
    return a * b


def div(a, b):
    return int(a / b)


def find(depth, numbers, nFuncs):
    global max_val, min_val
    nNum = numbers[:]
    nnFuncs = nFuncs[:]

    if depth == N - 1:
        if min_val > nNum[-1]:
            min_val = nNum[-1]
        if max_val < nNum[-1]:
            max_val = nNum[-1]
        return

    for i in range(4):
        if nnFuncs[i] == 0:
            continue

        temp = nNum[depth + 1]
        nNum[depth + 1] = funcs[i](nNum[depth], nNum[depth + 1])
        nnFuncs[i] -= 1
        find(depth + 1, nNum, nnFuncs)
        nnFuncs[i] += 1
        nNum[depth + 1] = temp


T = int(input())
funcs = [add, sub, multi, div]
for test_case in range(1, T + 1):
    N = int(input())
    nFuncs = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    max_val = -21e8
    min_val = 21e8

    find(0, numbers, nFuncs)

    print(f'#{test_case} {max_val - min_val}')
