'''
# 파일 쓰기

score_file = open("score.txt", "w", encoding="utf8")
# score.txt 라는 텍스트 파일을 만들어서 열고, 그 파일에 정보를 "write" 할 것이라는 의미
# utf8 = 한글 정보를 제대로 읽어올 수 있도록 해줌.

print('수학: 0', file=score_file)
print('영어: 50', file=score_file)
score_file.close()
'''



'''
# 파일 덮어쓰기

score_file = open("score.txt", "a", encoding="utf8")
# "a" = append.
# 즉, 이미 만들어진 파일에 덮어 쓴다는 의미

score_file.write("과학: 80")
score_file.write("\n코딩: 100")
score_file.close()
'''



'''
# 파일에 정보를 입력(쓰기)하는 두 가지 방법 - Print / Write

score_textfile = open("score.txt", "w", encoding="utf8")

# print는 줄 바꿈 기능이 함수 자체에 내장되어 있지만
print('수학: 0', file=score_textfile)
print('영어: 50', file=score_textfile)

# write는 줄 바꿈 기능이 없기에, 원하는 위치에 "\n"을 넣어줘야 한다.
score_textfile.write("과학: 80")
score_textfile.write("코딩: 100")
score_textfile.write("\n코딩: 100")

score_textfile.close()
'''



'''
# 파일 읽기
score_textfile = open("score.txt", "r", encoding="utf8")

print(score_textfile.read())        # 모든 내용 다 읽어오기

# print(score_textfile.readline())    # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_textfile.readline())    # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동

# print(score_textfile.readline(), end ='')    # 줄별로 읽되, 줄 바꿈 없이 읽는 방법
# print(score_textfile.readline(), end ='')    # 줄별로 읽되, 줄 바꿈 없이 읽는 방법
score_textfile.close()
'''



# 원하는 위치까지 파일 읽기
# 파일이 총 몇 줄인지 모를때는, 반복문을 활용해서 이렇게 읽어와도 된다!
score_textfile = open("score.txt", "r", encoding="utf8")

while True:
    line = score_textfile.readline()
    if not line: # 읽어온 정보가 아무것도 없을 경우 IF문 실행
        break
    print(line, end='')
score_textfile.close()

