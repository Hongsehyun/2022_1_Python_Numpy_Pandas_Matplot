# random library 호출하여 함수 사용하기
from random import *

print( int (random()*10) )    # 0~9 사이의 무작위 정수 출력
print( int (random()*10) )    # 0~9 사이의 무작위 정수 출력

print( (int (random()*10)) + 1 )    # 1~10 사이의 무작위 정수 출력
print( (int (random()*10)) + 1 )    # 1~10 사이의 무작위 정수 출력
print()

# 로또 번호 추첨
print( randint(1,45) )
print( randint(1,45) )
print( randint(1,45) )
print( randint(1,45) )
print( randint(1,45) )
print( randint(1,45) )