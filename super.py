class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

#class FlyableUnit(Unit, Flyable):
class FlyableUnit(Flyable, Unit): # 상속 순서 변경
    def __init__(self):
        #super().__init__()
        Unit.__init__(self) # Unit 클래스 생성자 호출
        Flyable.__init__(self) # Flyable 클래스 생성자 호출

# 수송선
troopship = FlyableUnit()