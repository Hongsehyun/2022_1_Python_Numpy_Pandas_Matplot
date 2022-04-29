# 가변인자를 사용하지 않을 경우
'''
def profile(name, age, lang1, lang2, lang3):
    print('이름 : {}\t나이 : {}\t'.format(name,age), end="")
    print(lang1, lang2, lang3)
        
profile("홍세현",25,"C","Python","Java")
profile("유재석",30,"C","","")
'''



# 가변인자를 사용할 경우
def profile(name, age, *language):   # *을 찍어주면 가변인자!
    print('이름 : {}\t나이 : {}\t'.format(name,age), end="")
    for lang in language:
        print(lang, end=" ")         # end =" " 의 용도는 줄바꿈 방지 
    print()
    
profile("홍세현",25,"C","Python","Java","R","Hadoop")
profile("유재석",30,"C")