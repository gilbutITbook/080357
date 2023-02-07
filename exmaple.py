#ch2

station = "사당"
# station = "신도림"
# station = "인천공항"
print(station + "행 열차가 들어오고 있습니다.")


#ch3

from random import *

date = randint(4, 28) # 4~28일 중에서 무작위 날짜 뽑기
print("오프라인 스터디 모임 날짜는 매월 " + str(date) + "일로 선정됐습니다.")


#ch4

#url = "http://naver.com"
url = "http://daum.net" # dau40!
# url = "http://google.com" # goo61!
# url = "http://youtube.com" # you71!
my_str = url.replace("http://", "") 
# naver.com일 때 my_str.index(".")의 결과는 5이므로 다음 문장은 my_str = mystr[0:5]와 같음
my_str = my_str[:my_str.index(".")] 
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0}의 비밀번호는 {1}입니다.".format(url, password))


#ch5

#방법1
from random import * 

users = range(1, 21) # 리스트 생성, 1부터 21 직전(20)까지 연속한 숫자 모음
users = list(users) # users를 리스트 자료구조로 변환
shuffle(users) # 리스트 섞기
winners = sample(users, 4) # users 리스트에서 중복 없이 4명 추첨

print("-- 당첨자 발표 -- ") # 당첨자 출력
print("치킨 당첨자 : {0}".format(winners[0])) # 0번째 인덱스(1명)
print("커피 당첨자 : {0}".format(winners[1:])) # 1번째부터 마지막까지 슬라이싱(3명)
print("-- 축하합니다! --")


#방법2
from random import *

users = list(range(1, 21)) # range()를 list()로 바로 감싸서 한 줄 줄이기
shuffle(users)
chicken_winner = sample(users, 1) # 치킨 당첨자 1명 추첨
remain_users = set(users) - set(chicken_winner) # 전체 집합에서 치킨 당첨자 집합 제외
coffee_winners = sample(remain_users, 3) # 남은 19명 중에서 3명 추첨

print("-- 당첨자 발표 --") 
print("치킨 당첨자 : {0}".format(chicken_winner))
print("커피 당첨자 : {0}".format(coffee_winners))
print("-- 축하합니다! --")

#파이썬 버전 3.11 이상일 때
from random import *

lst = [1, 2, 3, 4, 5]
# shuffle(lst)
print(sample(lst, len(lst)))


#ch6

from random import * 

cnt = 0 # 총 탑승객 수

for i in range(1, 51): # 손님 총 50명
    time = randrange(5, 51) # 변수 정의 소요시간 5~50분
    if 5 <= time <= 15: # 소요시간 5~15분인 손님만 매칭
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time)) # 매칭 성공 출력
        cnt += 1 # 총 탑승객 수 증가 처리
    else: # 매칭 실패 시
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time)) # 매칭 실패 출력

print("총 탑승객 : {0}명".format(cnt)) # 총 탑승객 수 출력


#ch7

def std_weight(height, gender): # 표준 체중 계산 함수 정의
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21

height = 175 # 전달값(키, cm 단위)을 저장한 변수 정의
gender = "남자" # 전달값(성별)을 저장한 변수 정의
# weight = std_weight(height / 100, gender) # 함수 호출(키는 cm 단위에서 m 단위로 변환)
weight = round(std_weight(height / 100, gender), 2) # 반올림해서 소수점 둘째 자리까지 표시
print("키 {0}cm {1}의 표준 체중은 {2}kg입니다.".format(height, gender, weight))


#ch8

for i in range(1, 51): # 숫자 1~50
    with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
        report_file.write("- {0}주차 주간보고 -".format(i))
        report_file.write("\n부서 : ") # 줄 바꿈 처리
        report_file.write("\n이름 : ")
        report_file.write("\n업무 요약 : ")


#ch9

class House:
    # 매물 초기화 : 위치, 건물 종류, 매물 종류, 가격, 준공연도
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    # 매물 정보 표시
    def show_detail(self):
        print(self.location, self.house_type, self.deal_type, \
        self.price, self.completion_year)

houses = []
house1 = House("강남", "아파트", "매매", "10억 원", "2010년")
house2 = House("마포", "오피스텔", "전세", "5억 원", "2007년")
house3 = House("송파", "빌라", "월세", "500/50만 원", "2000년")

houses.append(house1)
houses.append(house2)
houses.append(house3)

print("총 {0}가지 매물이 있습니다.".format(len(houses)))
for house in houses:
    house.show_detail()


#ch10

class SoldOutError(Exception):
    pass

chicken = 10 # 남은 치킨 수
waiting = 1 # 대기 번호, 1부터 시작

while True:
    try:
        print("[남은 치킨 : {0}]".format(chicken))
        order = int(input("치킨을 몇 마리 주문하시겠습니까? "))
        if order > chicken: # 남은 치킨보다 주문량이 많을 때
            print("재료가 부족합니다.")
        elif order <= 0:
            raise ValueError
        else:
            print("[대기 번호 {0}] {1}마리를 주문했습니다.".format(waiting, order))
            waiting += 1 # 대기 번호 증가
            chicken -= order # 주문 수만큼 남은 치킨 감소
        if chicken == 0:
            raise SoldOutError
    except ValueError:
        print("잘못된 값을 입력했습니다.")
    except SoldOutError:
        print("재료가 소진돼 더 이상 주문을 받지 않습니다.")
        break


#ch11

import byme

byme.sign()