# Quiz
'''
참석자 중에서 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰
추첨 프로그램을 작성하시오.

조건1 : 편의상 댓글은 20명이 작성하였고, 아이디는 1~20이라고 가정
조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
조건3 : random 모듈의 shuffle과 sample활용할 것

출력 예제:
-- 당첨자 발표 --
치킨 당첨자 : 1
커피 당첨자 : [2, 3, 4]
-- 축하합니다 --
'''

from random import *

users = list(range(1,21))         # 이 경우 type이 range로 저장 되므로, list로 자료 변환 시켜주기

shuffle(users)              # 무작위로 섞어주기
winners = sample(users, 4)  # 중복 허용 안하고 4명 뽑기

print('-- 당첨자 발표 --')
print('치킨 당첨자 : {}'.format(winners[0]))
print('커피 당첨자 : {}'.format(winners[1:]))
print('-- 축하합니다 --')

