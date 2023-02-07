#9.1

# 보병: 공격 유닛, 군인, 총을 쏠 수 있음
name = "보병" # 이름
hp = 40 # 체력
damage = 5 # 공격력

print("{} 유닛을 생성했습니다.".format(name))
print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# 탱크: 공격 유닛, 포를 쏠 수 있음, 두 가지 모드(일반/시지 모드)
tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print("{} 유닛을 생성했습니다.".format(tank_name))
print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

# 새로 탱크2 추가
tank2_name = "탱크"
tank2_hp = 150
tank2_damage = 35

print("{} 유닛을 생성했습니다.".format(tank2_name))
print("체력 {0}, 공격력 {1}\n".format(tank2_hp, tank2_damage))

# 공격 함수
def attack(name, location, damage):
    print("{0} : {1} 방향 적군을 공격합니다. [공격력 {2}]".format(name, location, damage))

attack(name, "1시", damage) # 보병 공격 명령
attack(tank_name, "1시", tank_damage) # 탱크 공격 명령
attack(tank2_name, "1시", tank2_damage) # 탱크2 공격 명령


#9.2

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name # 인스턴스 변수 name에 전달값 name 저장
        self.hp = hp # 인스턴스 변수 hp에 전달값 hp 저장
        self.damage = damage # 인스턴스 변수 damage에 전달값 damage 저장
        print("{0} 유닛을 생성했습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

soldier1 = Unit("보병", 40, 5) # 보병1 생성, 전달값으로 이름/체력/공격력 전달
soldier2 = Unit("보병", 40, 5) # 보병2 생성, 전달값으로 이름/체력/공격력 전달
tank = Unit("탱크", 150, 35) # 탱크 생성, 전달값으로 이름/체력/공격력 전달


#9.2.1
class Unit:
    def __init__(self, name, hp, damage): # 생성자, self 외 전달값 3개
        self.name = name 
        self.hp = hp 
        self.damage = damage
        print("{0} 유닛을 생성했습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

soldier1 = Unit("보병", 40, 5) # 객체 생성
soldier2 = Unit("보병", 40, 5) # 객체 생성
tank = Unit("탱크", 150, 35) # 객체 생성
#soldier3 = Unit("보병") # 전달값 3개 중 1개만 넘김, TypeError 발생
#soldier3 = Unit("보병", 40) # 전달값 3개 중 2개만 넘김, TypeError 발생


#9.2.2
class Unit:
    def __init__(self, name, hp, damage): # 생성자, 전달값 3개
        self.name = name # 인스턴스 변수 name
        self.hp = hp # 인스턴스 변수 hp
        self.damage = damage # 인스턴스 변수 damage
        print("{0} 유닛을 생성했습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# 전투기: 공중 유닛, 은폐 불가
stealth1 = Unit("전투기", 80, 5) # 객체 생성, 체력 80, 공격력 5
print("유닛 이름 : {0}, 공격력 : {1}".format(stealth1.name, stealth1.damage)) # 인스턴스 변수 접근

# 은폐 가능
stealth2 = Unit("업그레이드한 전투기", 80, 5)
stealth2.cloaking = True # 업그레이드한 전투기만을 위한 특별한 인스턴스 변수 정의, 은폐 상태

if stealth2.cloaking == True: # 은폐 상태라면
    print("{0}는 현재 은폐 상태입니다.".format(stealth2.name))

# 오류 발생
# if stealth1.cloaking == True: # 다른 전투기의 은폐 여부
#     print("{0}는 현재 은폐 상태입니다.".format(stealth1.name)) 


#9.2.3
class AttackUnit: # 공격 유닛
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, location): # 전달받은 방향으로 공격
        print("{0} : {1} 방향 적군을 공격합니다. [공격력 {2}]" \
            .format(self.name, location, self.damage)) # 공간이 좁아서 2줄로 나눔

    def damaged(self, damage): # damage만큼 유닛 피해
        # 피해 정보 출력
        print("{0} : {1}만큼 피해를 입었습니다.".format(self.name, damage))
        self.hp -= damage # 유닛의 체력에서 전달받은 damage만큼 감소
        # 남은 체력 출력
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0: # 남은 체력이 0 이하이면
            print("{0} : 파괴됐습니다.".format(self.name)) # 유닛 파괴 처리

# 화염방사병: 공격 유닛, 화염방사기를 사용함
flamethrower1 = AttackUnit("화염방사병", 50, 16) # 객체 생성, 체력 50, 공격력 16
flamethrower1.attack("5시") # 5시 방향으로 공격 명령

# 25만큼의 공격을 2번 받음
flamethrower1.damaged(25) # 남은 체력 25
flamethrower1.damaged(25) # 남은 체력 0


#9.3

#9.3.1
class Unit:
    def __init__(self, name, hp):
        self.name = name 
        self.hp = hp 

class AttackUnit(Unit): # Unit 클래스 상속
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp) # 부모 클래스의 생성자 호출
        self.damage = damage
    
    def attack(self, location): # 전달받은 방향으로 공격
        print("{0} : {1} 방향 적군을 공격합니다. [공격력 {2}]" \
            .format(self.name, location, self.damage)) # 공간이 좁아서 2줄로 나눔

    def damaged(self, damage): # damage만큼 유닛 피해
        # 피해 정보 출력
        print("{0} : {1}만큼 피해를 입었습니다.".format(self.name, damage))
        self.hp -= damage # 유닛의 체력에서 전달받은 damage만큼 감소
        # 남은 체력 출력
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0: # 남은 체력이 0 이하이면
            print("{0} : 파괴됐습니다.".format(self.name)) # 유닛 파괴 처리

flamethrower1 = AttackUnit("화염방사병", 50, 16)
flamethrower1.attack("5시") # 5시 방향으로 공격 명령

# 25만큼의 공격을 2번 받음
flamethrower1.damaged(25) # 남은 체력 25
flamethrower1.damaged(25) # 남은 체력 0


#9.3.2
class Unit:
    def __init__(self, name, hp):
        self.name = name 
        self.hp = hp 

class AttackUnit(Unit): # Unit 클래스 상속
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp) # 부모 클래스의 생성자 호출
        self.damage = damage
    
    def attack(self, location): # 전달받은 방향으로 공격
        print("{0} : {1} 방향 적군을 공격합니다. [공격력 {2}]" \
            .format(self.name, location, self.damage)) # 공간이 좁아서 2줄로 나눔

    def damaged(self, damage): # damage만큼 유닛 피해
        # 피해 정보 출력
        print("{0} : {1}만큼 피해를 입었습니다.".format(self.name, damage))
        self.hp -= damage # 유닛의 체력에서 전달받은 damage만큼 감소
        # 남은 체력 출력
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0: # 남은 체력이 0 이하이면
            print("{0} : 파괴됐습니다.".format(self.name)) # 유닛 파괴 처리

# 비행 기능
class Flyable:
    def __init__(self, flying_speed): # 비행 속도
        self.flying_speed = flying_speed
    
    def fly(self, name, location): # 유닛 이름, 비행 방향
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]" \
            .format(name, location, self.flying_speed))

# 공중 공격 유닛
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed): # 유닛 이름, 체력, 공격력, 비행 속도
        AttackUnit.__init__(self, name, hp, damage) # 유닛 이름, 체력, 공격력
        Flyable.__init__(self, flying_speed) # 비행 속도

# 요격기: 공중 공격 유닛, 미사일 여러 발을 한 번에 발사
interceptor = FlyableAttackUnit("요격기", 200, 6, 5) # 유닛 이름, 체력, 공격력, 비행 속도
interceptor.fly(interceptor.name, "3시") # 3시 방향으로 이동


#9.3.3
# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed): # speed 추가
        self.name = name
        self.hp = hp
        self.speed = speed # 지상 이동 속도

    def move(self, location): # 이동 동작 정의
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]" \
            .format(self.name, location, self.speed))

# 공격 유닛
class AttackUnit(Unit): # Unit 클래스 상속
    def __init__(self, name, hp, damage, speed): # speed 추가
        Unit.__init__(self, name, hp, speed) # speed 추가
        self.damage = damage

    def attack(self, location): # 전달받은 방향으로 공격
        print("{0} : {1} 방향 적군을 공격합니다. [공격력 {2}]" \
            .format(self.name, location, self.damage)) # 공간이 좁아서 2줄로 나눔

    def damaged(self, damage): # damage만큼 유닛 피해
        # 피해 정보 출력
        print("{0} : {1}만큼 피해를 입었습니다.".format(self.name, damage))
        self.hp -= damage # 유닛의 체력에서 전달받은 damage만큼 감소
        # 남은 체력 출력
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0: # 남은 체력이 0 이하이면
            print("{0} : 파괴됐습니다.".format(self.name)) # 유닛 파괴 처리

# 비행 기능
class Flyable:
    def __init__(self, flying_speed): # 비행 속도
        self.flying_speed = flying_speed
    
    def fly(self, name, location): # 유닛 이름, 비행 방향
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]" \
            .format(name, location, self.flying_speed))

# 공중 공격 유닛
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage, 0) # 지상 이동 속도 0
        Flyable.__init__(self, flying_speed) # 비행 속도

    def move(self, location): # Unit 클래스의 move() 메서드를 오버라이딩
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# 호버 바이크: 지상 유닛, 기동성 좋음
hoverbike = AttackUnit("호버 바이크", 80, 20, 10) # 지상 이동 속도 10

# 우주 순양함: 공중 유닛, 체력도 굉장히 좋음, 공격력도 좋음
spacecruiser = FlyableAttackUnit("우주 순양함", 500, 25, 3) # 비행 속도 3

hoverbike.move("11시")
#spacecruiser.fly(spacecruiser.name, "9시")
spacecruiser.move("9시") # 오버라이딩한 move() 메서드 호출


#9.4

# 건물 유닛
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass

# 보급고: 건물 유닛, 1개 건물 유닛 = 8유닛
supply_depot = BuildingUnit("보급고", 500, "7시") # 체력 500, 생성 위치 7시

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    pass

game_start()
game_over()


#9.5

# 건물 유닛
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        #Unit.__init__(self, name, hp, 0) # 지상 이동 속도 0, 건물은 지상 이동 불가
        super().__init__(name, hp, 0) # 부모 클래스 접근, self 없이 사용
        self.location = location


#9.6

#9.6.1
# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛을 생성했습니다.".format(name)) # 안내 문구 출력
    
    def move(self, location):
        # print("[지상 유닛 이동]") # 출력문 삭제
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]" \
            .format(self.name, location, self.speed))

    def damaged(self, damage): # AttackUnit 클래스에서 Unit 클래스로 이동
        print("{0} : {1}만큼 피해를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴됐습니다.".format(self.name))
    
# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, damage, speed):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
    
    def attack(self, location):
        print("{0} : {1} 방향 적군을 공격합니다. [공격력 {2}]" \
            .format(self.name, location, self.damage))
    
    """
    def damaged(self, damage): # Unit 클래스로 이동
        print("{0} : {1}만큼 피해를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴됐습니다.".format(self.name))
    """

# 보병 유닛
class Soldier(AttackUnit): # AttackUnit 클래스 상속
    def __init__(self):
        AttackUnit.__init__(self, "보병", 40, 5, 1) # 이름, 체력, 공격력, 이동 속도

    # 강화제: 일정 시간 동안 이동 속도와 공격 속도 증가, 체력 10 감소
    def booster(self): # 강화제 기능 메서드로 정의
        if self.hp > 10:
            self.hp -= 10 # 체력 10 소모
            print("{0} : 강화제를 사용합니다. (HP 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족해 기술을 사용할 수 없습니다".format(self.name))

# 탱크 유닛
class Tank(AttackUnit): # AttackUnit 클래스 상속
    # 시지 모드 : 탱크를 지상에 고정, 이동 불가, 공격력 증가
    siege_developed = False # 시지 모드 개발 여부, 클래스 변수로 정의

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 35, 1) # 이름, 체력, 공격력, 이동 속도
        self.siege_mode = False # 시지 모드(해제 상태), 인스턴스 변수로 정의

    # 시지 모드 설정
    def set_siege_mode(self):
        if Tank.siege_developed == False: # 시지 모드가 개발되지 않았으면 바로 반환
            return
        # 현재 일반 모드일 때
        if self.siege_mode == False: # 시지 모드 여부 확인
            print("{0} : 시지 모드로 전환합니다.".format(self.name)) # 시지 모드 전환
            self.damage *= 2 # 공격력 2배 증가
            self.siege_mode = True # 시지 모드 설정
        # 현재 시지 모드일 때
        else:
            print("{0} : 시지 모드를 해제합니다.".format(self.name)) # 일반 모드 전환
            self.damage //= 2 # 공격력 절반으로 감소
            self.siege_mode = False # 시지 모드 해제

# 나는 기능
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]" \
            .format(name, location, self.flying_speed))

# 공중 공격 유닛
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage, 0)
        Flyable.__init__(self, flying_speed)
    
    def move(self, location):
        # print("[공중 유닛 이동]") # 출력문 삭제
        self.fly(self.name, location)

# 전투기 유닛
class Stealth(FlyableAttackUnit): # FlyableAttackUnit 클래스 상속
    def __init__(self):
        FlyableAttackUnit.__init__(self, "전투기", 80, 20, 5) # 부모 클래스 생성자로 기본 정보 설정
        self.cloaked = False # 은폐 모드(해제 상태), 인스턴스 변수 정의

    def cloaking(self): # 은폐 모드를 메서드로 정의
        # 현재 은폐 모드일 때
        if self.cloaked == True:
            print("{0} : 은폐 모드를 해제합니다.".format(self.name))
            self.cloaked = False # 은폐 모드 해제
        # 현재 은폐 모드가 아닐 때
        else:
            print("{0} : 은폐 모드를 설정합니다.".format(self.name))
            self.cloaked = True # 은폐 모드 설정


#9.6

#9.6.1
# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛을 생성했습니다.".format(name)) # 안내 문구 출력
    
    def move(self, location):
        # print("[지상 유닛 이동]") # 출력문 삭제
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]" \
            .format(self.name, location, self.speed))

    def damaged(self, damage): # AttackUnit 클래스에서 Unit 클래스로 이동
        print("{0} : {1}만큼 피해를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴됐습니다.".format(self.name))
    
# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, damage, speed):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
    
    def attack(self, location):
        print("{0} : {1} 방향 적군을 공격합니다. [공격력 {2}]" \
            .format(self.name, location, self.damage))
    
    """
    def damaged(self, damage): # Unit 클래스로 이동
        print("{0} : {1}만큼 피해를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴됐습니다.".format(self.name))
    """

# 보병 유닛
class Soldier(AttackUnit): # AttackUnit 클래스 상속
    def __init__(self):
        AttackUnit.__init__(self, "보병", 40, 5, 1) # 이름, 체력, 공격력, 이동 속도

    # 강화제 : 일정 시간 동안 이동 속도와 공격 속도 증가, 체력 10 감소
    def booster(self): # 강화제 기능 메서드로 정의
        if self.hp > 10:
            self.hp -= 10 # 체력 10 소모
            print("{0} : 강화제를 사용합니다. (HP 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족해 기술을 사용할 수 없습니다".format(self.name))

# 탱크 유닛
class Tank(AttackUnit): # AttackUnit 클래스 상속
    # 시지 모드 : 탱크를 지상에 고정, 이동 불가, 공격력 증가
    siege_developed = False # 시지 모드 개발 여부, 클래스 변수로 정의

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 35, 1) # 이름, 체력, 공격력, 이동 속도
        self.siege_mode = False # 시지 모드(해제 상태), 인스턴스 변수로 정의

    # 시지 모드 설정
    def set_siege_mode(self):
        if Tank.siege_developed == False: # 시지 모드가 개발되지 않았으면 바로 반환
            return
        # 현재 일반 모드일 때
        if self.siege_mode == False: # 시지 모드 여부 확인
            print("{0} : 시지 모드로 전환합니다.".format(self.name)) # 시지 모드 전환
            self.damage *= 2 # 공격력 2배 증가
            self.siege_mode = True # 시지 모드 설정
        # 현재 시지 모드일 때
        else:
            print("{0} : 시지 모드를 해제합니다.".format(self.name)) # 일반 모드 전환
            self.damage //= 2 # 공격력 절반으로 감소
            self.siege_mode = False # 시지 모드 해제

# 나는 기능
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]" \
            .format(name, location, self.flying_speed))

# 공중 공격 유닛
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage, 0)
        Flyable.__init__(self, flying_speed)
    
    def move(self, location):
        # print("[공중 유닛 이동]") # 출력문 삭제
        self.fly(self.name, location)

# 전투기 유닛
class Stealth(FlyableAttackUnit): # FlyableAttackUnit 클래스 상속
    def __init__(self):
        FlyableAttackUnit.__init__(self, "전투기", 80, 20, 5) # 부모 클래스 생성자로 기본 정보 설정
        self.cloaked = False # 은폐 모드(해제 상태), 인스턴스 변수 정의

    def cloaking(self): # 은폐 모드를 메서드로 정의
        # 현재 은폐 모드일 때
        if self.cloaked == True:
            print("{0} : 은폐 모드를 해제합니다.".format(self.name))
            self.cloaked = False # 은폐 모드 해제
        # 현재 은폐 모드가 아닐 때
        else:
            print("{0} : 은폐 모드를 설정합니다.".format(self.name))
            self.cloaked = True # 은폐 모드 설정

#9.6.2
# 게임 시작
def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

# 게임 종료
def game_over():
    print("Player : Good Game")
    print("[Player] 님이 게임에서 퇴장했습니다.")

# 게임 시작
game_start()

# 보병 3기 생성
so1 = Soldier()
so2 = Soldier()
so3 = Soldier()

# 탱크 2기 생성
ta1 = Tank()
ta2 = Tank()

# 전투기 1기 생성
st1 = Stealth()

# 유닛 일괄 관리(생성된 모든 유닛 추가)
attack_units = []
attack_units.append(so1)
attack_units.append(so2)
attack_units.append(so3)
attack_units.append(ta1)
attack_units.append(ta2)
attack_units.append(st1)

# 전군 이동
for unit in attack_units:
    unit.move("1시")

# 탱크 시지 모드 개발
Tank.siege_developed = True
print("[알림] 탱크의 시지 모드 개발이 완료됐습니다.")

# 공격 모드 준비(보병: 강화제, 탱크: 시지 모드, 전투기: 은폐 모드)
for unit in attack_units:
    if isinstance(unit, Soldier): # Soldier 클래스의 인스턴스이면 강화제
        unit.booster()
    elif isinstance(unit, Tank): # Tank 클래스의 인스턴스이면 시지 모드
        unit.set_siege_mode()
    elif isinstance(unit, Stealth): # Stealth 클래스의 인스턴스이면 은폐 모드
        unit.cloaking()

# 전군 공격
for unit in attack_units:
    unit.attack("1시")

from random import *

# 전군 피해
for unit in attack_units:
    unit.damaged(randint(5, 20)) # 피해는 무작위로 받음(5~20)

# 게임 종료
game_over()


#9.7

#9.7

from random import *
# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛을 생성했습니다.".format(name))

    def move(self, location):
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]" \
            .format(self.name, location, self.speed))

    def damaged(self, damage):
        print("{0} : {1}만큼 피해를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴됐습니다.".format(self.name))

# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, damage, speed):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향 적군을 공격합니다. [공격력 {2}]" \
            .format(self.name, location, self.damage))

# 보병 유닛
class Soldier(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "보병", 40, 5, 1) # 이름, 체력, 공격력, 이동 속도

    # 강화제: 일정 시간 동안 이동 속도와 공격 속도 증가, 체력 10 감소
    def booster(self):
        if self.hp > 10:
            self.hp -= 10 # 체력 10 소모
            print("{0} : 강화제를 사용합니다. (HP 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족해 기술을 사용할 수 없습니다".format(self.name))

# 탱크 유닛
class Tank(AttackUnit):
    # 시지 모드 : 탱크를 지상에 고정, 이동 불가, 공격력 증가
    siege_developed = False # 시지 모드 개발 여부

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 35, 1) # 이름, 체력, 공격력, 이동 속도
        self.siege_mode = False # 시지 모드(해제 상태)

    # 시지 모드 설정
    def set_siege_mode(self):
        if Tank.siege_developed == False: # 시지 모드가 개발되지 않았으면 바로 반환
            return
        # 현재 일반 모드일 때
        if self.siege_mode == False:
            print("{0} : 시지 모드로 전환합니다.".format(self.name))
            self.damage *= 2 # 공격력 2배 증가
            self.siege_mode = True # 시지 모드 설정
        # 현재 시지 모드일 때
        else:
            print("{0} : 시지 모드를 해제합니다.".format(self.name))
            self.damage //= 2 # 공격력 절반으로 감소
            self.siege_mode = False # 시지 모드 해제

# 비행 기능
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]" \
            .format(name, location, self.flying_speed))

# 공중 공격 유닛
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage, 0)
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        self.fly(self.name, location)

# 전투기 유닛
class Stealth(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "전투기", 80, 20, 5)
        self.cloaked = False # 은폐 모드(해제 상태)

    # 은폐 모드
    def cloaking(self):
    # 현재 은폐 모드일 때
        if self.cloaked == True:
            print("{0} : 은폐 모드를 해제합니다.".format(self.name))
            self.cloaked = False
        # 현재 은폐 모드가 아닐 때
        else:
            print("{0} : 은폐 모드를 설정합니다.".format(self.name))
            self.cloaked = True

# 게임 시작
def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

# 게임 종료
def game_over():
    print("Player : Good Game")
    print("[Player] 님이 게임에서 퇴장했습니다.")

# 실제 게임 진행
game_start() # 게임 시작

# 보병 3기 생성
so1 = Soldier()
so2 = Soldier()
so3 = Soldier()

# 탱크 2기 생성
ta1 = Tank()
ta2 = Tank()

# 전투기 1기 생성
st1 = Stealth()

# 유닛 일괄 관리(생성된 모든 유닛 추가)
attack_units = []
attack_units.append(so1)
attack_units.append(so2)
attack_units.append(so3)
attack_units.append(ta1)
attack_units.append(ta2)
attack_units.append(st1)

# 전군 이동
for unit in attack_units:
    unit.move("1시")

# 탱크 시지 모드 개발
Tank.siege_developed = True
print("[알림] 탱크의 시지 모드 개발이 완료됐습니다.")

# 공격 모드 준비(보병: 강화제, 탱크: 시지 모드, 전투기: 은폐 모드)
for unit in attack_units:
    if isinstance(unit, Soldier): # Soldier 클래스의 인스턴스이면 강화제
        unit.booster()
    elif isinstance(unit, Tank): # Tank 클래스의 인스턴스이면 시지 모드
        unit.set_siege_mode()
    elif isinstance(unit, Stealth): # Stealth 클래스의 인스턴스이면 은폐 모드
        unit.cloaking()

# 전군 공격
for unit in attack_units:
    unit.attack("1시")

# 전군 피해
for unit in attack_units:
    unit.damaged(randint(5, 20)) # 피해는 무작위로 받음(5~20)
    
# 게임 종료
game_over()
