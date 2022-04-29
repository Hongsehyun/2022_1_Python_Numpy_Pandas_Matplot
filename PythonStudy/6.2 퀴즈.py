# Quiz
'''
당신은 택시 기사님입니다.
50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.
조건1 : 승객별 운행 소요 시간은 5~50분 사이의 난수로 정해집니다
조건2 : 당신은 소요 시간 5~15분 사이의 승객만 매칭해야 합니다

(출력문 예제)
[0] 1번째 손님 (소요시간: 15분)
[ ] 2번째 손님 (소요시간: 50분)
...
[ ] 50번째 손님 (소요시간: 16분)
총 탑승 승객 : 2분
'''
from random import *

customer = 0
for i in range(1,51):
    time = randint(5,50)
    if time<=15 and time>=5 :
        cond = 'O'
        customer = customer + 1
    else:
        cond = ''
    print('[{}] {}번째 손님 (소요시간 : {}분)'.format(cond,i,time))
print('총 탑승 승객 : {}분'.format(customer))