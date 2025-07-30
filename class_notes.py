# 전사, 궁수, 마법사
# 공통: 체력 마나 공격력
# 기능: 공격하기, 걷기, 상태확인
# 전사만: ...
# 궁수만: ....
# 마법사만: ...

class Character:
    # self : 인스턴스 자기자신을 가리킨다
    def __init__(self, hp, mp, power):
        self.hp = hp
        self.mp = mp
        self.power = power
    
    def attack(self):
        print(f'attacked with {self.power} amount of damage')

character1 = Character(100, 50, 10)    # 1번 캐릭터 (인스턴스)
character2 = Character(500, 20, 100)   # 2번 캐릭터 (인스턴스)

character1.attack()
character2.attack()

class Warrior:
    pass

class Archer:
    pass

class Mage:
    pass