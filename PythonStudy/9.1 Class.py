# class 정의
class unit:                                 #unit라는 Class 자료형 생성
    def __init__(self, name, hp, damage):   #def __init__	= ‘초기 설정을 다음과 같이 하겠다.’는 의미
        self.name = name                    #self		= ‘자기 자신 Class에 대해 정의하겠다.’는 의미	
        self.hp = hp
        self.damage = damage
        print('{} 유닛이 생성되었습니다.'.format(self.name))
        print('체력 {}, 공격력 {}\n'.format(self.hp, self.damage))

# 객체와 인스턴스
marine1 = unit("마린", 40, 5) # unit이라는 클래스의 인스턴스(1)
marine2 = unit("마린", 40, 5) # unit이라는 클래스의 인스턴스(2)
tank = unit("탱크", 150, 35)

# 멤버 변수
wraith1 = unit('레이스', 80, 5)
print("유닛이름 : {}, 공격력 : {}\n".format(wraith1.name, wraith1.damage))    # '.'으로 멤버변수에 접근하여 출력까지 함

# 멤버 변수의 외부 선언 및 호출
wraith2 = unit('레이스', 80, 5)
wraith2.clocking = True       # clocking 이라는 멤버 변수를 새롭게 만들어 줌

if wraith2.clocking == True :
    print("{}는 현재 클로킹 상태입니다.".format(wraith2.name))







'''
# Class 개념 이해를 위한 스타크래프트 예제

# 마린 : 공격 유닛, 군인, 총을 쏠 수 있음
marine_name = "마린"   # 유닛의 이름
marine_hp = 40         # 유닛의 체력
marine_damage = 5      # 유닛의 공격력

print('{} 유닛이 생성되었습니다.'.format(marine_name))
print('체력 {}, 공격력 {}\n'.format(marine_hp, marine_damage))


# 마린 : 공격 유닛, 군인, 총을 쏠 수 있음
tank_name = "탱크"   # 유닛의 이름
tank_hp = 150         # 유닛의 체력
tank_damage = 35      # 유닛의 공격력

print('{} 유닛이 생성되었습니다.'.format(tank_name))
print('체력 {}, 공격력 {}\n'.format(tank_hp, tank_damage))



def attack(name, location, damage):
    print("{} : {} 방향으로 적군을 공격합니다. [공격력{}]". format(name,location,damage))
'''