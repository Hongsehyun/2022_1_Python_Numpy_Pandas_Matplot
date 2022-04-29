# Quiz
'''
표준 체중을 구하는 프로그램을 작성하시오    (표준 체중 = 각 개인의 키에 적당한 체중)

(성별에 따른 공식)
남자: 키(m) X 키(m) X 22        여자: 키(m) X 키(m) X 21

조건1 : 표준 체중은 별도의 함수 내에서 계산
        * 함수명 : std_weight
        * 전달값 : 키(height), 성별(gender)
조건2 : 표준 체중을 소수 둘째자리까지 표시

(출력 예시)
키 175cm 남자의 표준 체중은 67.38kg 입니다.
'''
def std_weight():
    height = int(input('키를 입력하세요(예: 170): '))
    gender = input('성별을 입력하세요(예: 남자): ')

    if gender =='남자':
        weight = round((height * height * 22)/10000,2)  # 단위변환: cm^2 -> m^2
    elif gender == '여자':
        weight = round((height * height * 21)/10000,2)  # 단위변환: cm^2 -> m^2
    else :
        print('성별은 \'남자\'와 \'여자\'로만 입력해주세요.')
    return height, gender, weight

height, gender, weight = std_weight()
print('키 {}cm {}의 표준 체중은 {}kg 입니다'.format(height,gender,weight))


