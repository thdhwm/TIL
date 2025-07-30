# class 라는 것을 왜 쓸까?
# - 중복된 코드를 많이 줄일 수 있다

# 전사, 궁수, 마법사
# - 공통: 체력, 마나, 공격력
# - 기능: 공격하기, 걷기, 상태확인
# 전사만 할 수 있는 것: 칼로때리기(), 강하게소리지르기()
# 궁수만 할 수 있는 것: 활쏘기(), 자세히살펴보기()
# 마법사만 할 수 있는 것: 마법쓰기(), 똑똑해지기()

# 상황1. 전체 캐릭터의 수를 관리해야 한다
# - 전역변수로 관리
#  -> Character class 와 관련된 변수인데, 외부에 값을 관리
#  --> 유지보수가 어려워진다.

class Character:
    total_players = 0  # 클래스 변수
                       # 모든 인스턴스가 공유하는 값
    double_event = True  # ex) 경험치 2배 이벤트

    # self : 인스턴스 자기자신을 가리킨다
    # 생성자에 전달되는 값 : 인스턴스의 초기값
    def __init__(self, hp, mp, power):
        self.hp = hp
        self.mp = mp
        self.power = power
        # 인스턴스 메서드에서 클래스 변수에 접근
        Character.total_players += 1

    # 인스턴스 메서드
    def attack(self):
        print(f"{self.power}의 데미지로 공격!")

# 클래스명() => 클래스의 생성자를 호출해라고 정해놓음
character1 = Character(100, 50, 10) # 1번 캐릭터 (인스턴스)
character2 = Character(500, 200, 100)  # 2번 캐릭터 (인스턴스)

character1.attack()
character2.attack()

# 인스턴스를 통해서도 클래스 변수에 접근 가능!
# --> 하지마라!
# print(f'전체 캐릭터 수 = {character1.total_players}')
print(f'전체 캐릭터 수 = {Character.total_players}')

# 내일 배울 것: 상속
class Warrior(Character):
    def 강하게때리기(self):
        pass

    def 소리지르기(self):
        pass

warrior1 = Warrior(200, 300, 50)
print(warrior1.hp, warrior1.mp)

class Archer:
    pass

class Wizard:
    pass

# 내일 실습 할 것 : 인스턴스 메서드 추가해보기, 클래스 메서드, 스태틱 메서드
# - 상속 실습