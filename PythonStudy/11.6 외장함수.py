#Glob :		경로 내의 폴더 / 파일 목록을 조회하는 함수 (윈도우 dir)
'''
import glob
print(glob.glob("*.py")) # py로 끝나는 모든 파일에 대해 검색하는 코드
'''




#Os :		운영체제에서 제공하는 기본 기능
'''
import os
print(os.getcwd()) # 현대 디렉토리 경로 / 위치에 대해 나타내주는 코드


folder = "sample_dir"

if os.path.exists(folder):  # 해당 경로에 sample_dir이라는 이름의 폴더가 이미 있는지 체크
    print("이미 존재하는 폴더입니다.")
    os.rmdir(folder)        # 폴더 삭제
    print("{} 폴더를 삭제하였습니다.".format(folder))
else:
    os.makedirs(folder)     # 해당 경로에 sample_dir이라는 이름의 폴더가 없으면 생성!
    print("{} 폴더를 생성하였습니다.".format(folder))
'''




# time :        시간 관련 함수
'''
import time
print(time.localtime())     # 현재의 날짜의 시간을 출력해줌
print(time.strftime("%Y-%m-%d %H:%M:%S"))      # local time으로 출력하면 형태가 알아보기 힘드므로 이와같이 깔끔하게 출력하게 할 수 있음.
'''

# datetime :    시간 관련 함수 (2)
import datetime
print("오늘 날짜는 {}".format(datetime.date.today()))

# timedelta :   두 날짜 사이의 간격
today = datetime.date.today() # 오늘 날짜 저장
td = datetime.timedelta(days=100) # 100일 저장
print("우리가 만난지 100일은 {}".format(today+td))


