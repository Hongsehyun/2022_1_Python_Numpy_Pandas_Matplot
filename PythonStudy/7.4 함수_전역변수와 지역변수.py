'''
gun = 10

def checkpoint(soldiers): #경계 근무
    gun = 20
    gun = gun - soldiers
    print("남은 총: {} 개".format(gun))

checkpoint(2)
print(gun)
'''



'''
# 전역변수 활용하기

gun = 10

def checkpoint(soldiers): #경계 근무
    global gun            #전역 변수 gun 정의
    gun = gun - soldiers
    print("남은 총: {} 개".format(gun))

checkpoint(2)
print(gun)
'''



# 매개변수 추가 및 리턴 값 활용

gun = 10

def checkpoint(gun, soldiers): #함수 매개변수(인자) 추가
    gun = gun - soldiers
    print("남은 총: {} 개".format(gun))
    return gun

gun = checkpoint(20, 2)
print(gun)  # 이미 전역변수로 gun = 10 으로 정의 되었지만
            # 함수 연산 결과를 gun에 리턴했기에, 20-2 = 18로 출력되는 것이다.

