# 프로그래밍 페러다임(방법론)
# - 어떻게하면 프로그램을 조금 더 쉽게 설계하고 구현할 수 있을까 ?
#   - 절차지향
#     - 절차에 따라 순서대로 구현하자 (C언어)
#     - A -> B -> C -> D
#   - 객체지향
#     - 객체 단위로 분리하여 개발을 하자 (Java, Python)
#     - 각 팀이 하나의 파트를 맡아서 개발 (A, B, C, D)
#       - 다른 팀의 결과가 있다고 가정하고, 가짜 데이터로 개발을 진행


# 스마트폰 -> 객체
# - 변수
    # - 기종: wide5     /   갤럭시 21
    # - 가격: 0원       /   100만원
    # - 사용기간: 4년    /   4년
    # - 저장공간: 128GB  /   256GB
# - 함수(기능)
    # - 전화하기
    # - 카톡하기
    # - 구글링하기
    # - 네이버웹툰 보기

# 전체 구조를 저장할 무엇인가 (설계도) -> class
# 실제 데이터를 저장한 무엇인가 -> 객체

class Smartphone:
    # 초기화하는 함수
    # 매직 메서드: 언더바 2개로 감싸져 있는 메서드
    # - 파이썬 내부에서 특별한 상황에 자동으로 호출됨
    # - __init__: 생성자. 객체를 만들 때 자동으로 호출됨
    # - self: 객체 자기자신을 가리킨다.
    def __init__(self, model, price):
        self.model = model  # 기종
        self.price = price  # 가격

    # 메서드: 객체가 가지고 있는 함수
    def call(self):
        print(f'{self.model}에서 전화함')

giryunPhone = Smartphone("wide5", "0원")
beomseokPhone = Smartphone("갤럭시21", "100만원")

print(giryunPhone.model, giryunPhone.price) # wide5 0원
print(beomseokPhone.model, beomseokPhone.price) # 갤럭시21 100만원

giryunPhone.call() # giryunPhone이 가지고 있는 call 기능 호출



# 쉽지 않은 내용입니다
# class 와 객체
# 일반 함수와 메서드 차이
# 오늘은 이 정도만 이해하셔도 됩니다!
# 객체 내부 데이터 저장이나 매직 메서드 등의 내용은 수~목요일에 이해하셔도 괜찮습니다 :smile: