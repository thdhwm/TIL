import sys
sys.stdin = open('input.txt')


T = int(input())

def sDigit(i, j, depth):

    num_list.append(matrix[i][j])
    if depth == 7:
        num_str = ''.join(num_list)
        result.add(num_str)
        return

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < 4 and 0 <= nj < 4:
            sDigit(ni, nj, depth + 1)
            num_list.pop()

    return

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
for test_case in range(1, T + 1):
    matrix = [input().split() for _ in range(4)]
    result = set()

    for i in range(4):
        for j in range(4):
            num_list = []
            sDigit(i, j, 1)

    print(f'#{test_case}', len(result))