import sys
sys.stdin = open('input.txt')


def quad_tree(arr):
    # 가로, 세로 각각 나누기 2 해서 4 영역 분할
    # 2사분면, 1사분면, 3사분면, 4사분면 순서
    # 각 영역에 대해서 is_zeros, is_ones
    # zeros, ones 맞으면 str에 더하고
    # 아니면 아닌 영역에 대해서 quad_tree
    # dfs
    if len(arr) == 1 and arr[0][0] == '1':
        return '1'
    elif len(arr) == 1 and arr[0][0] == '0':
        return '0'
    else:
        half = len(arr) // 2     # 슬라이싱 문제 있음 나중에 수정
        quadrant_2 = [[arr[i][j] for j in range(half)] for i in range(half)]
        quadrant_1 = [[arr[i][j] for j in range(half, len(arr))] for i in range(half)]
        quadrant_3 = [[arr[i][j] for j in range(half)] for i in range(half, len(arr))]
        quadrant_4 = [[arr[i][j] for j in range(half, len(arr))] for i in range(half, len(arr))]
        return '(' + is_zeros_ones(quadrant_2) + is_zeros_ones(quadrant_1) + is_zeros_ones(quadrant_3) + is_zeros_ones(quadrant_4) + ')'


def is_zeros_ones(arr):
    if len(arr) == 1 and arr[0][0] == '1':
        return '1'
    elif len(arr) == 1 and arr[0][0] == '0':
        return '0'
    else:
        is_what = arr[0][0]
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[i][j] != is_what:
                    return quad_tree(arr)
        return is_what


N = int(input())    # 2의 제곱수 1 ~ 64
screen = [list(input()) for _ in range(N)]
result = quad_tree(screen)

if result == '(0000)':
    print('0')
elif result == '(1111)':
    print('1')
else:
    print(result)
