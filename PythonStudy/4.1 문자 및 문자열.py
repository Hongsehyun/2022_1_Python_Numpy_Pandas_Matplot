# sentence = '''나는 홍세현입니다.
# 대전에서 살고 있습니다.
# 나이는 25살 입니다.'''

# print(sentence)





# sentence = 'Python is Amazing'

# index = sentence.index('n')   # n의 인덱스 검색
# print(index)

# index = sentence.index('n',index+1)   # 인덱스 6부터 검색
# print(index)





# 방법 (1)
# age = 25
# print('나는 {} 살 입니다.'.format(age))
# print()

# print('나는 {}색과 {}색을 좋아해요.'.format('파란', '빨간'))
# print('나는 {0}색과 {1}색을 좋아해요.'.format('파란', '빨간'))
# print('나는 {1}색과 {0}색을 좋아해요.'.format('파란', '빨간'))
# print()

# print('나는 {age}살 이며 {color}색을 좋아해요.'.format(age=25, color='파란'))
# print()





# 방법 (2)
# age = 25
# print('나는 %d 살 입니다.' %age)
# print('나는 %s 을(를) 좋아해요' %"파이썬")
# print('Apple은 %c 로 시작해요' %"A")
# print()

# print('나는 %s색과 %s색을 좋아해요.' %('파란', '빨간'))




# \n : 줄바꿈
print('백문이 불여일견 \n 백문이 불여일타')
print()

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine")    # 커서가 맨 앞으로 이동해서 'Red '가 'Pine'으로 대체됨
print()

# \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple")        # \b 에 의해서 앞에 있는 'd' 한 글자를 삭제
print()

# \t : 탭
print("Red\tApple")         # 키보드에서 tab을 치는 것과 같은 효과
print()

# \'   \"   \\ 
print('저는 \'홍세현\' 입니다')
print('저는 \"홍세현\" 입니다')
print('파일경로 : C:\\Users\\sehye\\source\\repos')
print()