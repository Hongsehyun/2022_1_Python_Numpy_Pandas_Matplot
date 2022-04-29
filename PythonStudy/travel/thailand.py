class ThailandPackage:
    def detail(self):
        print("[태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원")


if __name__ == "__main__":          # 모듈 내부에서 직접 실행하는 경우 이 조건이 참
    print("Thailand 모듈을 직접 실행")
    print("이 문장을 모듈을 직접 실행할 때만 실행돼요")

    trip_to = ThailandPackage()
    trip_to.detail()
else :                              # 다른 파일에서 import를 통해 이 모듈을 받아온 뒤 실행하는 경우 이 조건이 참
    print("Thailand 외부에서 모듈 호출")