import sys
sys.stdin = open('input.txt')


def validation(num):
    if num ** 2 == target:
        return True
    return False


def root_search():
    left, right = 0, target

    while left <= right:
        mid = (right + left) // 2

        if validation(mid):
            return mid
        else:
            if mid ** 2 < target:
                left = mid + 1
            else:
                right = mid - 1

    return right


T = int(input())

for test_case in range(1, T + 1):
    target = int(input())

    print(f'#{test_case} {root_search()}')



