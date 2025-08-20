# import sys
# sys.stdin = open('input.txt')

# ---->> 실행하면 input.txt 읽어와서 자동으로 입력되게


# ###### 퀵 소트 (임의의 피벗(pivot)값 설정하고 리스트 순회해서 (피벗보다 작은값) (피벗) (피벗보다 큰 값) 으로 정렬 ###### #

# array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
#
#
# def quick_sort(array, start, end):
#     if start >= end:
#         return
#     pivot = start  # 피벗 초기값은 첫번째 요소
#     left = start + 1
#     right = end
#
#     while left <= right:
#         # 피벗보다 큰 데이터를 찾을 때까지 반복
#         while left <= end and array[left] <= array[pivot]:
#             left += 1
#
#             # 피벗보다 작은 데이터를 찾을 때까지 반복
#         while right > start and array[right] >= array[pivot]:
#             right -= 1
#
#         if left > right:  # 엇갈렸다면 작은 right -=1 데이터와 피벗을 교체
#             array[right], array[pivot] = array[pivot], array[right]
#
#         else:  # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
#             array[left], array[right] = array[right], array[left]
#
#     # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
#     quick_sort(array, start, right - 1)
#     quick_sort(array, right + 1, end)
#
#
# quick_sort(array, 0, len(array) - 1)
# print(array)

# ########################################################################################################### #

# 우선순위 큐
# import heapq 조으다 .heappush, .heappop  조으다

# 유니온 파인드

my_dict = {}

my_dict[0] = [1]
my_dict[0] += [4]

print(list(my_dict.keys()))
