# Quiz
'''
부동산 프로그램 작성하기

(출력 예제)
총 3대의 매물이 있다.
강남 아파트 매매 10억 2010년(준공연도)
마포 오피스텔 전세 5억 2007년(준공연도)
송파 빌라 월세 500/50 2000년(준공연도)
'''
class House:
    # 매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    # 매물 정보 표시
    def show_detail(self):
        print("{} {} {} {} {}(준공연도)".format(self.location, self.house_type, self.deal_type, self.price, self.completion_year))

house_list = []
house1 = House("강남", "아파트", "매매", "10억", "2010년")
house2 = House("마포", "오피스텔", "전세", "5억", "2007년")
house3 = House("송파", "빌라", "월세", "500/50", "2000년")

house_list.append(house1)
house_list.append(house2)
house_list.append(house3)

print("총 {}대의 매물이 있다.".format(len(house_list)))
for house in house_list :
    house.show_detail()
