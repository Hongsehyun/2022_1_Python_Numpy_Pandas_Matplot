# 반복문의 활용

'''
출석번호가 1 2 3 4 인데,
앞에 100을 붙이기로 함. 즉, 101 102 103 104 ...
'''
students = [1,2,3,4,5]
students = [i+100 for i in students]
# students의 값들을 i에 하나씩 가져오고, 그 i 값에 100을 더해준다는 의미
print(students)


'''
학생 이름을 길이로 변환하여 저장하기
'''
students_name = ['IronMan','Thor','I am groot']
students_name = [len(i) for i in students_name]
print(students_name)

