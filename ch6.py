#6.1

#6.1.1
weather = "비"

if weather == "비": # 대입 연산자(=)가 아닌 비교 연산자(==) 사용
    print("우산을 챙기세요.")


#6.1.2
weather = "맑음"

if weather == "비":
    print("우산을 챙기세요.")


weather = "미세먼지"

if weather == "비":
    print("우산을 챙기세요.") # 1번
elif weather == "미세먼지":
    print("마스크를 챙기세요.") # 2번


#6.1.3
weather = "맑음"

if weather == "비":
    print("우산을 챙기세요.")
elif weather == "미세먼지":
    print("마스크를 챙기세요.")
else:
    print("준비물이 필요 없어요.")


#6.1.4
weather = input("오늘 날씨는 어때요? ")
#print(weather)

if weather == "비":
    print("우산을 챙기세요.")
elif weather == "미세먼지":
    print("마스크를 챙기세요.")
else:
    print("준비물이 필요 없어요.")


weather = input("오늘 날씨는 어때요? ")

if weather == "비" or weather == "눈": # 조건 변경
    print("우산을 챙기세요.")
elif weather == "미세먼지":
    print("마스크를 챙기세요.")
else:
    print("준비물이 필요 없어요.")


temp = int(input("오늘 기온은 어때요? ")) # 입력값을 정수형으로 형변환

if 30 <= temp: # 30도 이상이면
    print("너무 더워요. 외출을 자제하세요.")
elif 10 <= temp and temp < 30: # 10도 이상 30도 미만이면
    print("활동하기 좋은 날씨예요.")
elif 0 <= temp and temp < 10: # 0도 이상 10도 미만이면
    print("외투를 챙기세요.")
else: # 그 외의 모든 경우(0도 미만이면)
    print("너무 추워요. 나가지 마세요.")


temp = int(input("오늘 기온은 어때요? "))

if 30 <= temp:
    print("너무 더워요. 외출을 자제하세요.")
elif 10 <= temp < 30:
    print("활동하기 좋은 날씨예요.")
elif 0 <= temp < 10:
    print("외투를 챙기세요.")
else:
    print("너무 추워요. 나가지 마세요.")


temp = int(input("오늘 기온은 어때요? "))

if temp >= 30:
    print("너무 더워요. 외출을 자제하세요.")
elif temp >= 10:
    print("활동하기 좋은 날씨예요.")
elif temp >= 0:
    print("외투를 챙기세요.")
else:
    print("너무 추워요. 나가지 마세요.")


#6.2

#6.2.1
for waiting_no in [1, 2, 3, 4, 5]:
    print("대기번호 : {0}".format(waiting_no)) # {0} 위치에 waiting_no의 값이 들어감


for waiting_no in range(5): # 0부터 5 직전까지(0~4)
    print("대기번호 : {0}".format(waiting_no))


for waiting_no in range(1, 6): # 1부터 6 직전까지(1~5)
    print("대기번호 : {0}".format(waiting_no))


for waiting_no in range(1, 6, 2): # 1부터 6 직전까지(1~5)에서 2씩 간격 주기
    print("대기번호 : {0}".format(waiting_no))


orders = ["아이언맨", "토르", "스파이더맨"] # 손님 닉네임 리스트
for customer in orders:
    print("{0} 님, 커피가 준비됐습니다. 픽업대로 와 주세요.".format(customer))


#6.2.2
customer = "토르" # 손님 닉네임
index = 5 # 초깃값, 부르는 횟수 최대 5번

while index >= 1: # 부르는 횟수가 1 이상일 때만 실행
    print("{}님, 커피가 준비됐습니다.".format(customer))
    index -= 1 # 횟수 1회 차감
    print("{}번 남았어요.".format(index))
    if index == 0: # 5번 모두 불렀다면
        print("커피를 폐기 처분합니다.")

"""
customer = "아이언맨"
index = 1

while True:
    print("{0} 님, 커피가 준비됐습니다. 호출 {1}회".format(customer, index))
    index += 1
"""


customer = "토르"
person = None

while person != customer:
    print("{0} 님, 커피가 준비됐습니다.".format(customer))
    person = input("이름이 어떻게 되세요? ")


#6.2.3
absent = [2, 5] # 결석한 학생 출석번호
no_book = [7] # 책을 가져오지 않은 학생 출석번호

for student in range(1, 11): # 출석번호 1~10번
    if student in absent: # 결석한 학생이면
        continue # 다음 학생으로 넘어가기
    elif student in no_book: # 책을 가져오지 않으면 바로 수업 종료
        print("오늘 수업은 여기까지. {0}번 학생은 교무실로 따라와요.".format(student))
        break # 반복문 탈출
    print("{0}번 학생, 책을 읽어 보세요.".format(student))


#6.2.4
students = [1, 2, 3, 4, 5]
print(students)

# 한 줄 for 문으로 각 항목에 100 더하기
students = [i + 100 for i in students]
#students = [students[0] + 100, students[1] + 100, students[2] + 100, students[3] + 100, students[4] + 100]
#students = [1 + 100, 2 + 100, 3 + 100, 4 + 100, 5 + 100]
print(students)


students = ["Iron man", "Thor", "Spider Man"]
print(students)

# 한 줄 for 문으로 각 이름을 이름의 길이 정보로 변환
students = [len(i) for i in students]
#students = [len(students[0]), len(students[1]), len(students[2])]
#students = [len("Iron man"), len("Thor"), len("Spider Man")]
print(students)


students = ["Iron man", "Thor", "Spider Man"]
print(students)

# 한 줄 for 문으로 각 이름을 모두 대문자로 변경
students = [i.upper() for i in students]
print(students)