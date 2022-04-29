cabinet = {3:'유재석',100:'김태호'}

# # 1. 키를 호출하는 경우
# print(cabinet[3])
# print(cabinet[5])

# 2. get 함수를 사용하는 경우
print(cabinet.get(3))
print(cabinet.get(5))
print(cabinet.get(5,'사용 가능'))