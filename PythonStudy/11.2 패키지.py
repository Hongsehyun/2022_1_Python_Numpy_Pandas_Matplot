'''
# import 뒤에 패키지와 모듈만 위치한 경우
import travel.thailand
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()
'''


'''
# import 뒤에 패키지와 모듈 뿐만 아니라 클래스, 함수까지 호출한 경우
import travel.thailand.ThailandPackage
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()
'''


'''
# from ~ import 구문을 활용한 경우
#   travel 패키지 안에 있는 thailand라는 모듈을 불러와서
#   ThailandPackage라는 Class를 불러온 문법이므로 옳은 문법!
from travel.thailand import ThailandPackage
trip_to = ThailandPackage()
trip_to.detail()
'''


from travel import *
trip_to = thailand.ThailandPackage()
trip_to.detail()
