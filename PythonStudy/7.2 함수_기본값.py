'''
def profile(name, age, main_lang):
    print('이름 : {}\t나이 : {}\t주 사용 언어: {}'\
        .format(name,age,main_lang))
        # \를 입력하여 두 줄이지만 하나의 코드로 실행되게 함.

profile("홍세현",25,"C")
'''


# 기본값 실습
def profile(name, age=25, main_lang='C'):
    print('이름 : {}\t나이 : {}\t주 사용 언어: {}'.format(name,age,main_lang))
        
profile("홍세현")
profile("유재석")
profile("박명수", 30, "python")