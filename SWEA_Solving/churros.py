# # mid 길이로 K 명이 먹을 수 있는가 ?
# # - 있다면 True return, 없다면 False return
# def test(mid):
#     cnt = 0
#     for churros in arr:
#         cnt += churros // mid
#         if cnt >= K:
#             return True
#     return False
#
#
#
# # 츄러스의 최대 길이를 찾고자 한다
# # --> 츄러스의 길이가 타겟
# def bs():
#     left, right = 0, max(arr)  # 최소, 최대 길이
#
#     while left <= right:
#         mid = (left + right) // 2
#
#         if test(mid):   # 가능하면 길이를 늘린다
#             left = mid + 1
#         else:           # 불가능하면 길이를 줄인다
#             right = mid - 1
#
#     # left: 불가능한 첫 번째 값이 저장됨
#     # right: 가능한 마지막 값(최대값)이 저장됨
#     # print(left, right)  # 헷갈리면 항상 출력해보기
#     return right
#
#
# T = int(input())
#
# for tc in range(1, T + 1):
#     N, K = map(int, input().split())
#     arr = [int(input()) for _ in range(N)]
#     print(f'#{tc} {bs()}')
# ##################################################################
import sys
sys.stdin = open('input.txt')


def validation(length):
    cnt = 0
    for churro in churros:
        cnt += (churro // length)
        if cnt >= K:
            return True
    return False


def bi_search():
    left, right = 0, max(churros)

    while left <= right:
        mid = (right + left) // 2

        if validation(mid):
            left = mid + 1
        else:
            right = mid - 1

    return right


T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    churros = [int(input()) for _ in range(N)]

    print(f'#{test_case} {bi_search()}')




