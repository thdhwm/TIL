# List Comprehension
# - 리스트와 관련된 여러 줄의 코드를 한 줄로 줄이자
# - 남용하면 가독성이 매우 떨어진다.
#   - 간단한 반복 + 조건문만 활용하는 게 좋다
# - 알고리즘 -> 사용자 입력 구현 시 엄청 많이 활용

# 구조
# li = [표현식 for 변수 in 반복객체]
# li = [표현식 for 변수 in 반복객체 if 조건문]

# 1부터 10까지 숫자 리스트
result1 = [num for num in range(1, 11)] # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(result1)

# 1부터 10까지 숫자 리스트를 2배씩 해서 저장
# - 반복하고 싶은 숫자 : 1~10
# - 최종 저장하고 싶은 값 : num * 2
result2 = [num * 2 for num in range(1, 11)] # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print(result2)

# 1~10까지의 숫자 중 짝수만 저장
# - 반복하고 싶은 숫자: 1~10
# - 조건: 짝수
# - 최종 저장하고 싶은 값: 조건이 만족하는 num 그대로
result3 = [num for num in range(1, 11) if num % 2 == 0]
print(result3)  # [2, 4, 6, 8, 10]

# 두 리스트의 모든 조합 만들 때
colors = ["red", "blue"]
sizes = ["S", "M", "L", "XL"]

# 모든 조합을 만들 수 있다 (2 * 4)
# for color in colors:
#     for size in sizes:
result4 = [(color, size) for color in colors for size in sizes]
print(result4)

# 사용자 입력 활용 예시
# '''
# 1 2 3
# 4 5 6
# 7 8 9
# '''
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# 한 줄 마다 수행할 것 : '1 2 3' -> [1, 2, 3]
# _ : 반복을 돌면서 변수에 저장하고 싶은 값이 없을 때
result5 = [list(map(int, input().split())) for _ in range(3)]
print(result5)
