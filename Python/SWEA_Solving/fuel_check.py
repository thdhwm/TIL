import sys
sys.stdin = open('input.txt')


def bi_search(target):
    left = 0
    right = len(fuel_tank) - 1

    while left <= right:
        mid = (left + right) // 2

        if fuel_tank[mid] == target:
            left = mid + 1

        else:
            right = mid -1
    return int(left * 100 / len(fuel_tank))

T = int(input())

for test_case in range(1, T + 1):
    fuel_tank = list(input().strip())
    result = bi_search('#')

    print(f'#{test_case} {result}%')


    # b_s 해서 #이면 max # 비교 후 저장
    # (max_# + 1) * 100 / (len(fuel_tank) + 1)
    # 없으면 0 리턴
# ##################################################################
# def bs():
#     left, right = 0, len(arr) - 1  # 시작점, 끝점 초기화
#
#     while left <= right:  # 교차하면 끝
#         mid = (left + right) // 2
#
#         # mid 의 값이 # 일 때 (오른쪽을 봐야한다)
#         if arr[mid] == '#':
#             left = mid + 1
#         # 아닐 때 (왼쪽을 봐야한다)
#         else:  # _ 일 때
#             right = mid - 1
#
#     return int(left * 100 / len(arr))
#
#
#
# T = int(input())
#
# for tc in range(1, T + 1):
#     arr = input().strip()
#     result = bs()
#     print(f'#{tc} {result}%')