import sys
sys.stdin = open('input.txt')

# #######################################################################
# # lower bound, upper bound
# # 2이상 3이하인 숫자들
# # 2가 처음 시작하는 index = 2
# # 3이 끝나는 index = 6
# arr = [-1, 1, 2, 2, 2, 3, 3, 9, 9]
#
#
# # target 이 시작하는 지점을 검색
# def lower_bound(target):
#     left, right = 0, len(arr) - 1
#
#     while left <= right:
#         mid = (left + right) // 2
#
#         # 같은 숫자가 나오면 왼쪽을 검사
#         if target <= arr[mid]:
#             right = mid - 1
#         else:
#             left = mid + 1
#
#     return left
#
#
# def upper_bound(target):
#     left, right = 0, len(arr) - 1
#
#     while left <= right:
#         mid = (left + right) // 2
#
#         # 같은 숫자가 발생하면, 오른쪽을 검사
#         if target >= arr[mid]:
#             left = mid + 1
#         else:
#             right = mid - 1
#
#     # right: 3이 끝나는 인덱스
#     # left: 3 초과인 인덱스
#     return left
#
#
# lower_idx = lower_bound(2)
# upper_idx = upper_bound(8)
# print(f'2~8 사이 숫자 = {upper_idx - lower_idx}개')
# #######################################################################