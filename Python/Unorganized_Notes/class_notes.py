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
    def __init__(self, hp, mp, power, name):
        self.hp = hp
        self.mp = mp
        self.power = power
        self.name = name
        # 인스턴스 메서드에서 클래스 변수에 접근
        Character.total_players += 1

    # 인스턴스 메서드
    def attack(self):
        print(f"{self.power}의 데미지로 공격!")
    
    def walk(self):
        print(f"{self.name}이(가) 걸어감!")


# 클래스명() => 클래스의 생성자를 호출해라고 정해놓음
character1 = Character(100, 50, 10, 'john') # 1번 캐릭터 (인스턴스)
character2 = Character(500, 200, 100, 'sam')  # 2번 캐릭터 (인스턴스)

character1.attack()
character2.attack()

class Warrior(Character):
    
    def __init__(self, hp, mp, power, name):
        super().__init__(hp + 100, mp, power, name)
    
    def slash(self):
        print(f'{self.name} slashed in front of him')
    
    def war_cry(self):
        print(f'{self.name} screamed real loud')



warrior = Warrior(500, 150, 20, 'bob')
warrior.attack()
warrior.war_cry()




class Archer:
    pass


class Wizard:
    pass

class Operator:
    def __init__(self):
        self.permission_level = '운영자'

    def kick_out(self, target):
        print(f'kick out {target}')

class OperatorWarrior(Operator, Warrior):
    def __init__(self, hp, mp, power, name):
        # super().__init__()     -> 다중 상속에서는 권장 X

        Warrior.__init__(self, hp, mp, power, name)
        Operator.__init__(self)    # 다중 상속시에는 명시적으로 클랙스 호출을 권장


oper1 = OperatorWarrior(100, 100, 100, 'bob')
print(oper1.permission_level)
print(oper1.hp)

