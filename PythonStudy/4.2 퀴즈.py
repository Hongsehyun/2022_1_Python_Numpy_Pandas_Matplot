# Quiz
'''
사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

예) http://naver.com

규칙1 : http:// 부분은 제외 -> naver.com
규칙2 : 처음 만나는 점(.) 이후 부분은 제외 -> naver
규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성 
'''

site = input('사이트를 입력하세요: ')
li = []

site = site[7:]         # 'http://' 제거
li = site.split('.')    # '.'을 기준으로 하여 구분

pw = li[0]

pw = pw[:3]
len = len(li[0])
enum = li[0].count('e')

print('생성된 비밀번호: {}{}{}{}'.format(pw,len,enum,'!'))
