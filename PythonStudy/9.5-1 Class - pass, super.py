'''
# PASS 설명

# 일반 유닛
class unit:                                 #unit라는 Class 자료형 생성
    def __init__(self, name, hp, speed):    #def __init__	= ‘초기 설정을 다음과 같이 하겠다.’는 의미
        self.name = name                    #self		= ‘자기 자신 Class에 대해 정의하겠다.’는 의미	
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{} : {} 방향으로 이동합니다. [속도{}]".format(self.name, location, self.speed))


# 건물
class BuildingUnit(unit):
    def __init__(self, name, hp, location):
        pass            # 아무 역할 안하고 그냥 일단 넘어가게 해주는 코드


# 서플라이 디폿 : 건물, 1개 건물 = 8유닛
supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")


def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_stop():
    pass                # 아무 역할 안하고 그냥 일단 넘어가게 해주는 코드
'''




# Super 설명
# 일반 유닛
class unit:                                 #unit라는 Class 자료형 생성
    def __init__(self, name, hp, speed):    #def __init__	= ‘초기 설정을 다음과 같이 하겠다.’는 의미
        self.name = name                    #self		= ‘자기 자신 Class에 대해 정의하겠다.’는 의미	
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{} : {} 방향으로 이동합니다. [속도{}]".format(self.name, location, self.speed))

# 공격 유닛
class AttackUnit(unit):                     #AttackUnit 이라는 Class는 unit이라는 Class를 상속받았다
    def __init__(self, name, hp, speed, damage):   
        unit.__init__(self, name, hp, speed)       #상속해주는 class의 내용을 불러와준다.
        self.damage = damage

    def attack(self, location):
        print("{} : {} 방향으로 적군을 공격합니다. [공격력{}]". format(self.name,location,self.damage))
    
    def damaged(self, damaged):
        print("{} : {} 데미지를 입었습니다.".format(self.name, damaged))
        self.hp -= damaged
        print("{} : 현재 체력은 {} 입니다".format(self.name, self.hp))
        if self.hp <= 0:
            print("{} : 파괴되었습니다.".format(self.name))

# 공중 유닛
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print("{} : {}방향으로 날아갑니다. [속도 {}]".format(name, location, self.flying_speed))

# 공중 공격 유닛 - 다중 상속을 받는 Class
class FlyableAttackUnit(AttackUnit, Flyable): #공격도 할 수 있고, 날 수도 있는 Class를 모두 상속받음
    def __init__(self, name, hp, damage, flying_speed):   
        AttackUnit.__init__(self, name, hp, 0, damage)      #상속해주는 class의 내용을 불러와준다.
                                                            #공중 유닛이므로 지상 speed = 0 이라고 정의함.
        Flyable.__init__(self,flying_speed)                 #상속해주는 class의 내용을 불러와준다.
    
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)    # 메소드 오버라이딩!!  # 메소드 오버라이딩!!  # 메소드 오버라이딩!!


# 건물
class BuildingUnit(unit):
    def __init__(self, name, hp, location):
        unit.__init__(self, name, hp, 0)  # 건물은 speed가 0이다.