class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name                   
        self.hp = hp
        self.damage = damage

    def attack(self, location):
        print("{} : {} 방향으로 적군을 공격합니다. [공격력{}]". format(self.name,location,self.damage))
    
    def damaged(self, damaged):
        print("{} : {} 데미지를 입었습니다.".format(self.name, damaged))
        self.hp -= damaged
        print("{} : 현재 체력은 {} 입니다".format(self.name, self.hp))
        if self.hp <= 0:
            print("{} : 파괴되었습니다.".format(self.name))

firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

firebat1.damaged(25)
firebat1.damaged(25)