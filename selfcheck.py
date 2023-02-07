#ch2

status = "상품 준비"
# status = "배송 중"
# status = "배송 완료"
print("주문상태 : " + status)


#ch3

celsius = 30
fahrenheit = (celsius * 9 / 5) + 32
print("섭씨 온도 : " + str(celsius))
print("화씨 온도 : " + str(fahrenheit))


#ch4

proverb = "the early bird catches the worm."
# proverb = "Actions Speak Louder Than Words."
# proverb = "PRACTICE MAKES PERFECT."

#방법1
print(proverb[0].upper() + proverb[1:].lower())
#방법2
print(proverb.capitalize()) # 첫 글자는 대문자로, 나머지는 소문자로 변경


#ch5

subject = ["자료구조", "알고리즘", "자료구조", "운영체제"]
subject = set(subject) # 리스트를 세트로 변환해 중복 제거
subject = list(subject) # 세트를 리스트로 변환
print("신청한 과목은 다음과 같습니다.")
print(subject)


#ch6

price = 1000 # 상품 가격
goods = 3 # 구매 상품 수
total = 0 # 총 가격

for i in range(1, goods + 1): # 구매 상품 수가 3인 경우 1~3 반복 수행
    print("2+1 상품입니다.")
    if i % 3 == 0: # 3의 배수인 경우 가격을 더하지 않음
        continue
    total += price

print("총 가격은 " + str(total) + "원입니다.")


#ch7

def get_air_quality(fine_dust):
    if 0 <= fine_dust <= 30:
        return "좋음"
    elif fine_dust <= 80:
        return "보통"
    elif fine_dust <= 150:
        return "나쁨"
    else:
        return "매우 나쁨"

# 테스트 코드
print(get_air_quality(15)) # 좋음
print(get_air_quality(85)) # 나쁨


#ch8

"""
with open("class.txt", "r", encoding="utf8") as f: # "class.txt"에는 실제 파일 경로 입력
    txt = f.read() # 파일 내용 읽어 오기
    words = txt.split() # 내용을 띄어쓰기로 구분해 리스트로 반환
    for word in words:
        print(word, end=" ")
        if word.endswith("명"): # 명으로 끝나면 줄 바꿈
            print()
"""

#ch9

class ParkingManager:
    # 주차 정보 초기화: 총 주차 가능 대수
    def __init__(self, capacity):
        self.capacity = capacity # 총 주차 가능 대수
        self.count = 0 # 현재 등록된 차량 수
        print(f"총 {capacity}대를 등록할 수 있습니다.")

    # 신규 차량 등록
    def register(self):
        if self.count >= self.capacity:
            print("더 이상 등록할 수 없습니다.")
            return
        self.count += 1
        print(f"차량 신규 등록 ({self.count}/{self.capacity})")

# 테스트 코드
manager = ParkingManager(5)
for i in range(6):
    manager.register()



#ch10

def save_battery(level):
    try:
        print(f"배터리 잔량 : {level}%") # 배터리 잔량 표시
        if level > 30:
            print("일반 모드로 사용합니다.")
        elif level > 5:
            print("절전 모드로 사용합니다.")
        else:
            raise Exception("배터리가 부족해 스마트폰을 종료합니다.") # 오류 발생
    except Exception as e:
        print(e)
    print() # 마지막 줄 바꿈

# 테스트 코드
save_battery(75)
save_battery(25)
save_battery(3)