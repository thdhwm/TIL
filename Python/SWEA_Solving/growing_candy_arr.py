import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):
    A, B, C = list(map(int, input().split()))
    total = 0

    while B >= C:
        B -= 1
        total += 1

    while A >= B:
        A -= 1
        total += 1

    if A <= 0 or B <= 0 or C <= 0:
        print(f'#{test_case} -1')
    else:
        print(f'#{test_case} {total}')

# ######################################################################################################

# 사탕을 담은 상자
# A, B, C 개의 사탕
# 순증가 (A < B < C)
# 각 상자는 1개 이상


# 반복 안해도
# B = C - 1, A = B - 1 로 만드는 로직 짜면 가능