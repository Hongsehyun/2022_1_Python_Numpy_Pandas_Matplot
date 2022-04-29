# pop	= 뒤에서부터 꺼내기 (꺼낸 값은 해당 리스트에서 삭제됨)
li = [10, 20, 30, 40, 50, 60, 70]
print(li)
print()

print(li.pop())         # 가장 뒤의 값 70을 꺼내오고 출력
print(li)               # 가장 뒤의 값 70을 꺼낸 뒤, 남은 list 값 출력
print()


# clear	= 전체를 모두 삭제하기
li.clear()
print(li)
print()


# extend = 리스트끼리 연결하기
li1 = ["홍세현",25,True]
li2 = ["한동대",1995,True]

li1.extend(li2)
print(li1)