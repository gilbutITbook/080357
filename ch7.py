#7.1

#7.1.1
def open_account():
    print("새로운 계좌를 개설합니다.")

open_account() # 앞에 정의한 open_account() 함수 호출

#7.2

#7.2.1
def open_account():
    print("새로운 계좌를 개설합니다.")

open_account() # open_account() 함수 호출

def deposit(balance, money): # 입금 처리 함수
    print("{0}원을 입금했습니다. 잔액은 {1}원입니다.".format(money, balance + money))
    return balance + money # 입금 후 잔액 정보 반환

balance = 0 # 초기 잔액, balance 변수에 초깃값으로 0 저장
balance = deposit(balance, 1000) # 1,000원 입금, balance 변수에 deposit() 함수의 반환값을 다시 저장
#deposit(balance, 1000)


#7.2.2
def open_account():
    print("새로운 계좌를 개설합니다.")

open_account() # open_account() 함수 호출

def deposit(balance, money): # 입금 처리 함수
    print("{0}원을 입금했습니다. 잔액은 {1}원입니다.".format(money, balance + money))
    return balance + money # 입금 후 잔액 정보 반환

def withdraw(balance, money): # 출금 처리 함수
    if balance >= money: # 잔액이 출금액보다 많으면
        print("{0}원을 출금했습니다. 잔액은 {1}원입니다.".format(money, balance - money))
        return balance - money # 출금 후 잔액 반환
    else:
        print("잔액이 부족합니다. 잔액은 {0}원입니다.".format(balance))
        return balance # 기존 잔액 반환

balance = 0 # 초기 잔액
balance = deposit(balance, 1000) # 1,000원 입금

# 출금
balance = withdraw(balance, 2000) # 2,000원 출금 시도
balance = withdraw(balance, 500) # 500원 출금 시도


#7.2.3
def open_account():
    print("새로운 계좌를 개설합니다.")

open_account() # open_account() 함수 호출

def deposit(balance, money): # 입금 처리 함수
    print("{0}원을 입금했습니다. 잔액은 {1}원입니다.".format(money, balance + money))
    return balance + money # 입금 후 잔액 정보 반환


def withdraw_night(balance, money): # 업무 시간 외 출금
    commission = 100 # 출금 수수료 100원
    print("업무 시간 외에 {}원을 출금했습니다." .format(money))
    return commission, balance - money - commission

balance = 0 # 초기 잔액
balance = deposit(balance, 1000) # 1,000원 입금

# 업무 시간 외 출금 시도
commission, balance = withdraw_night(balance, 500)
print("수수료 {0}원이며, 잔액은 {1}원입니다.".format(commission, balance))


(name, age, hobby) = ("피글렛", 20, "코딩") # 변수명에 소괄호가 없어도 실행결과는 동일
print(name, age, hobby)

name, age, hobby = ("피글렛", 20, "코딩") # 변수명에 소괄호가 없어도 실행결과는 동일
print(name, age, hobby)

name, age, hobby = "피글렛", 20, "코딩" # 값에 소괄호가 없어도 실행결과는 동일
print(name, age, hobby)


#7.3

#7.3.1
def profile(name, age, main_lang):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))
    
profile("찰리", 20, "파이썬")
profile("루시", 25, "자바")


def profile(name, age=20, main_lang="파이썬"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))

profile("찰리")
profile("루시")


def profile(name, age=20, main_lang="파이썬"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))
    
profile("찰리") # age, main_lang은 기본값 사용
profile("찰리", 22) # main_lang은 기본값 사용
profile("찰리", 24, "자바") # 기본값을 사용하지 않음


# 마트에서 2가지 상품을 구매하는 경우
def buy(item1, item2="음료수"): # 올바른 함수 정의: 일반 전달값을 먼저 작성
    print(item1, item2)

buy("빵") # item1=빵, item2=음료수

"""
# 마트에서 2가지 상품을 구매하는 경우
def buy(item1="음료수", item2): # 잘못된 함수 정의: 기본값을 가지는 전달값을 먼저 작성 
    print(item1, item2)

buy("빵") # item1=빵? item2=빵? 
"""


#7.3.2
def profile(name, age, main_lang): # 키워드 인자 : name, age, main_lang
    print(name, age, main_lang)

profile(name="찰리", main_lang="파이썬", age=20)
profile(main_lang="자바", age=25, name="루시")


def profile(name, age, main_lang): # 키워드 인자 : name, age, main_lang 
    print(name, age, main_lang)

profile("찰리", age=20, main_lang="파이썬") # 올바른 함수 호출: 일반 전달값을 먼저 작성
#profile(name="루시", 25, "파이썬") # 잘못된 함수 호출: 키워드 인자를 먼저 작성 후 일반 전달값 작성


#7.3.3
def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름 : {0}\t나이 : {1}\t".format(name, age))
    print(lang1, lang2, lang3, lang4, lang5)

profile("찰리", 20, "파이썬", "자바", "C", "C++", "C#")
profile("루시", 25, "코틀린", "스위프트", "", "", "")


def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ") # 줄 바꿈 대신 띄어쓰기
    print(lang1, lang2, lang3, lang4, lang5)

profile("찰리", 20, "파이썬", "자바", "C", "C++", "C#")
profile("루시", 25, "코틀린", "스위프트", "", "", "")


def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    print(language, type(language))

profile("찰리", 20, "파이썬", "자바", "C", "C++", "C#", "자바스크립트") # 자바스크립트 추가
profile("루시", 25, "코틀린", "스위프트")


def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    # print(language, type(language))
    for lang in language:
        print(lang, end=" ") # 언어를 모두 한 줄에 표시
    print() # 줄 바꿈 목적

profile("찰리", 20, "파이썬", "자바", "C", "C++", "C#", "자바스크립트")
profile("루시", 25, "코틀린", "스위프트")


def add(item):
    print(item, "붓기")

def americano():
    add("뜨거운 물")
    add("에스프레소")

print("아메리카노 만드는 법")
americano()


#7.4
glasses = 10 # 전체 3D 안경 개수: 10개

def rent(people): # 3D 안경을 대여한 관객 수
    #glasses = 20 # 변수 정의 추가
    #global glasses # 전역 공간에 있는 glasses 변수를 함수 안에서 사용하겠다는 표시
    glasses = glasses - people # 잔여 3D 안경 개수 = 전체 개수 - 대여한 개수 
    print("[함수 내부] 남은 3D 안경 개수: {0}".format(glasses))

print("전체 3D 안경 개수: {0}".format(glasses))
rent(2) # 3D 안경을 대여한 관객이 2명일 때
print("남은 3D 안경 개수: {0}".format(glasses))


glasses = 10

def rent_return(glasses, people): # 전체 3D 안경 수와 대여 관객 수를 전달받음
    glasses = glasses - people # 전달값을 담은 glasses 사용
    print("[함수 내부] 남은 3D 안경 개수: {0}".format(glasses))
    return glasses

print("전체 3D 안경 개수: {0}".format(glasses))
glasses = rent_return(glasses, 2) # 함수 안에서 수정된 glasses 값을 반환받음
print("남은 3D 안경 개수: {0}".format(glasses))
