java = {'유재석','김태호','양세형'}
python = {'유재석','박명수'}

# 교집합 (Java와 Python을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# 합집합 (Java를 할 수 있거나 Python을 할 수 있는 개발자)
print(java | python)
print(java.union(python))

# 차집합 (Java를 할 수 있지만 Python은 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))