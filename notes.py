# List Comprehension
# 알고리즘 -> 사용자 입력 구현 시 많이 활용

# 구조
# li = [표현식 for 변수 in 반복객체 ]
# li = [표현식 for 변수 in 반복객체 if 조건문]

result1 = [num for num in range(1,11)]      #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result2 = [num * 2 for num in range(1,11)]     #[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# if 예시
# 1~10 중 짝수만

result3 = [num for num in range(1,11) if num % 2 == 0]      #[2, 4, 6, 8, 10]


# 두 리스트의 모든 조합
colors = ['red', 'blue']
sizes = ['s', 'm', 'l', 'xl']

result4 = [(color,sizes) for color in colors for size in sizes]

print(result4)


# 사용자 입력 2차원 행렬
# 1 2 3
# 4 5 6 
# 7 8 9
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# _ : 반복을 돌면서 변수에 저장하고 싶은 값이 없을 때
result5 = [list(map(int, input().split())) for _ in range(3)]
print(result5)





# 함수 vs 메서드 - 왜 다름? 둘다 함수 아님?

#클래스 (class)

# 프로그래밍 페러다임(방법론)
# - 절차지향
# 절차에 따라 순서대로구현하자 (C언어)
# - 객체지향
#  객체 단위로 분리하여 개발을 하자 (JAVA, Python)


# 객체지향
# - 객체지향 프로그래밍( OOP )의 핵심 개념

# 객체?
# 현실 세계의 사물이나 개념을 코드로 표현한 것

class Smartphone:
    def __init__(self, model, price):
        self.model = model
        self.price = price

    def call(self):
        print(f'{self.model}에서 전화함')
# 매직 메서드 : 언더바 2개 ('__')로 감싸져 있는 메서드 -> 파이썬 내부에서 특별한 상황에 자동으로 호출 됨
# self - 객체 자기 자신을 가리킨다

my_Phone = Smartphone('Note10', '10만원')
giryunPhone = Smartphone('wide5', '0원')

giryunPhone.call() # 


