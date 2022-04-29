class unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

# 다중 상속
class FlyableUnit(Flyable, unit):
    def __init__(self):
        unit.__init__(self)
        Flyable.__init__(self)

dropship = FlyableUnit()
