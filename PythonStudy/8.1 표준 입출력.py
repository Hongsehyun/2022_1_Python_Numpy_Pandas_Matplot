'''
# sep, end 활용하기

print('Python','C','Java script')

print('Python', 'C', 'Java script', sep = " vs ")

print('Python','C','Java script', sep = ",", end="?")
print('무엇이 더 재미있을까요?')
'''



'''
# 표준 출력과 표준 에러
import sys

print('Python','Java', file=sys.stdout)
print('Python','Java', file=sys.stderr)
   # 출력상에서는 똑같아 보이지만
   # 표준 에러로 이렇게 해놓으면,
   # 다음에 에러만 처리해야 하는 일이 있을 때 용이하다.
'''



'''
# 문자 정렬 예시
scores = {'수학':0, '영어':50, '코딩':100}

for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=":")
    # ljust(8) = 왼쪽 정렬을 하고, 문자가 들어갈 수 있는 8칸의 공백 확보
    # rjust(4) = 오른쪽 정렬을 하고, 문자가 들어갈 수 있는  4칸의 공백 확보
'''