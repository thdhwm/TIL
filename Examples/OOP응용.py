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
    # 복습문제1. Character 에 이름(name) 속성을 추가하기
    def __init__(self, hp, mp, power, name):
        self.hp = hp
        self.mp = mp
        self.power = power
        self.name = name

        # 인스턴스 메서드에서 클래스 변수에 접근
        # - 상속을 이해해야, 이게 왜 권장사항이 아닌지, 언제 아래와 같이 써야하는 지 알 수 있다.
        # Character.total_players += 1

        Character.increment_player_count()  # 클래스 메서드 인 걸 알 수 있다.
        # Character.걷기() # 인스턴스 정보가 없다 == self 가 없다
        # self.increment_player_count()  # 인스턴스 메서드인지, 클래스 메서드 인 지 모름

    @classmethod
    def increment_player_count(cls):
        cls.total_players += 1

    # 인스턴스 메서드
    def attack(self):
        print(f"{self.power}의 데미지로 공격!")

    # 복습문제2. 걷기, 상태확인 메서드 만들기
    def 걷기(self):
        print(f'{self.name}이(가) 앞으로 걸어감')

    def 상태확인(self):
        print("====== 상태창 ======")
        print(f"이름: {self.name}")
        print(f"HP: {self.hp}")
        print(f"MP: {self.mp}")
        print(f"공격력: {self.power}")
        print("===================")

    # 클래스 변수와도 관계없고, 인스턴스와도 관계는 없지만
    # Character 클래스안에 있으면 좋을 것 같은 메서드
    # 예) 20% 확률로 강하게 공격한다(공격력의 2배로 공격한다)
    # - 20% 확률로 공격력이 2배로 증가하는 기능
    @staticmethod
    def 치명타계산(기본공격력):
        import random
        if random.random() < 0.2:
            print("치명타 발생!")
            return 기본공격력 * 2
        return 기본공격력


# 클래스명() => 클래스의 생성자를 호출해라고 정해놓음
character1 = Character(100, 50, 10, "기륜") # 1번 캐릭터 (인스턴스)
character2 = Character(500, 200, 100, "범석")  # 2번 캐릭터 (인스턴스)

character1.attack()
character2.attack()

character1.걷기()
character2.걷기()

character1.상태확인()
character2.상태확인()

# character1.increment_player_count() # 인스턴스가 클래스 메서드를 호출 - 가능!!!
#                                 # 파이썬에서 막아놓지는 않았다.
#                                 # 근데 하지마라

# 인스턴스를 통해서도 클래스 변수에 접근 가능!
# --> 하지마라!
# print(f'전체 캐릭터 수 = {character1.total_players}')
print(f'전체 캐릭터 수 = {Character.total_players}')

# 전사, 궁수, 마법사 클래스
# - Character class 속성, 메서드는 모두 포함
# - + 본인 직업만의 기능들을 추가로 가짐

# [조건]
# 1. Warrior(전사)는 체력(hp)에 +100 보너스를 받는다.
# 2. Archer(궁수)는 공격력(power)에 +50 보너스를 받는다.
# 3. Wizard(마법사)는 마나(mp)에 +100 보너스를 받는다.
#
# 예시)
# 전사 = Warrior(150, 30, 20, "기륜")  → 체력은 150 + 100 = 250
# 궁수 = Archer(100, 50, 15, "예지")   → 공격력은 15 + 50 = 65
# 마법사 = Wizard(80, 100, 10, "민준")  → 마나는 100 + 100 = 200

class Warrior(Character):
    total_players = 0  # 전사 유저 수

    # 생성자 오버라이딩
    def __init__(self, hp, mp, power, name):
        # 중복된 코드 발생!
        # self.hp = hp + 100
        # self.mp = mp
        # self.power = power
        # self.name = name
        
        # Character 에 정의된 생성자를 가져다 활용하자
        super().__init__(hp + 100, mp, power, name)
        Warrior.increment_player_count()

    # @classmethod
    # def increment_player_count(cls):
    #     cls.total_players += 1
        

    def 칼로때리기(self):
        print(f"{self.name}이(가) 칼로 때림")

    def 강하게소리지르기(self):
        print(f"{self.name}이(가) 소리지름")

    # 기본공격(attack) 검으로 공격하기로 변경되었다.
    # 같은 함수 이름으로 다시 재정의한다 == 메서드 오버라이딩(overrding)
    def attack(self):
        print(f"이제는 검으로 때린다! {self.power}데미지로 공격함")

warrior = Warrior(100, 50, 10, "기륜")
warrior.상태확인()
warrior.강하게소리지르기()
warrior.attack()

print(f'전체 캐릭터 수 = {Character.total_players}')
print(f'전사 캐릭터 수 = {Warrior.total_players}')

class Archer:
    pass

class Wizard:
    pass

# ------------------------------ 다중 상속

# 시나리오 - 운영자 캐릭터를 만들고 싶다.

class Operator:
    def __init__(self):
        self.permission_level = "운영자"

    def 강퇴(self, target):
        print(f"{target}을 강퇴한다.")

# Operator class 기능과 Warrior class 기능이 모두 포함된 클래스
class OperatorWarrior(Warrior, Operator):
    def __init__(self, hp, mp, power, name):
        # MRO 순서에 따라 자동 호출 -> 다중 상속 시에는 예기치 않은 클래스 호출 가능
        # super().__init__(hp, mp, power, name)

        # 다중 상속일 때는 super 보다 명시적으로 클래스 호출을 권장
        Warrior.__init__(self, hp, mp, power, name)
        Operator.__init__(self)

print(OperatorWarrior.__mro__)
oper1 = OperatorWarrior(100, 100, 100, "기륜")
print(oper1.hp)
