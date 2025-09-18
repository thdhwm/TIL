# crypto
# 1. 8 digit
# 2. first 7 digit - code, last - validation
# validation - sum(odd_digit) + sum(even_digit) + validation = times 10
# ex. for 8801234
# “( ( 8 + 0 + 2 + 4 ) x 3 ) + ( 8 + 1 + 3 ) + 검증 코드”
# = “42 + 12 + 검증 코드”
# “54 + 검증 코드” 가 10 의 배수가 되어야 하므로, 검증코드는 6이 되어야 한다
# if validation != 6   --->> phony
# therefore 88012346 is valid

# 2000 * 500 table
# hexadecimal to binary, given table
# at least 1 valid code inside table
# if valid -> print.sum(digits)

# all crypto code is 8 digit
# each digit takes at least 7 grid (7 bit minimum) -> 56 is min.len for code
#
# 00 01110110110001011101101100010110001000110100100110111011 00
import sys
sys.stdin = open('input.txt')

hex_to_bin = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
    '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
}


def validate(cyphered):
    return


def hex_to_bi(hex_str):
    result = ''
    for i in range(len(hex_str)):
        result += hex_to_bin[hex_str[i]]

    return result


# row =
T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())    # N * M size matrix

    for _ in range(N):
        row = input()
        if int(row) | 0 != 0:  # 0 이 아닌 무언가가 있으면
            pass

