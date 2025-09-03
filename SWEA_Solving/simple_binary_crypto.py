import sys
sys.stdin = open('input.txt')


def validate():
    return


def hex_to_bi():
    return


T = int(input())
crypto = {
    '0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
    '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9
}

for test_case in range(1, T + 1):
    N, M = map(int, input().split())    # N * M size matrix

    for _ in range(N):
        in_row = input()
        if int(in_row) != 0:
            row = in_row

# ex. row = 0000011101101100010111011011000101100010001101001001101110110000000000
    refined = row.strip('0')
    how_long = len(refined)
    for _ in range(56 - how_long):
        refined = '0' + refined

    code = []
    for i in range(8):
        code.append(crypto.get(refined[(7 * i): (7 * i) + 7]))

    result = 0
    for i in range(0, 8, 2):
        result += 3 * code[i] + code[i + 1]

    if result % 10 == 0:
        print(f'#{test_case} {sum(code)}')
    else:
        print(f'#{test_case} 0')


# ##################################################################

hex_to_bin