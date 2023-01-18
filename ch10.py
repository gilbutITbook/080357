#10.1

#10.1.2
print("나누기 전용 계산기입니다.")
num1 = int(input("첫 번째 숫자를 입력하세요 : "))
num2 = int(input("두 번째 숫자를 입력하세요 : "))
print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))


try:
    print("나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))

except ValueError:
    print("오류 발생! 잘못된 값을 입력했습니다.")


#10.1.3
try:
    print("나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("오류 발생! 잘못된 값을 입력했습니다.")
except ZeroDivisionError as err:
    print(err)


try:
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
    #nums.append(int(nums[0] / nums[1])) # 연산 결과를 리스트에 추가
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("오류 발생! 잘못된 값을 입력했습니다.")
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print("알 수 없는 오류가 발생했습니다.")
    print(err)


#10.2

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10: # 입력받은 수가 한 자리인지 확인
        raise ValueError
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("값을 잘못 입력했습니다. 한 자리 숫자만 입력하세요.")


#10.3

class BigNumberError(Exception): # 사용자 정의 예외 처리, Exception 클래스 상속
    #pass
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg
        #return "[오류 코드 001] " + self.msg # 오류 메시지 가공

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10: # 입력받은 수가 한 자리인지 확인
        # raise ValueError
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2)) # 자세한 오류 메시지
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("값을 잘못 입력했습니다. 한 자리 숫자만 입력하세요.")
except BigNumberError as err: # 사용자 정의 예외 처리
    print("오류가 발생했습니다. 한 자리 숫자만 입력하세요.")
    print(err) # 오류 메시지 출력


class SpecialClass():
    def __init__(self):
        print("특별한 생성자")

    def __str__(self):
        return "특별한 메서드"

s = SpecialClass() # 특별한 생성자 출력
print(s) # 특별한 메서드 출력


#10.4

class BigNumberError(Exception): 
    #pass
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10: 
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2)) 
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("값을 잘못 입력했습니다. 한 자리 숫자만 입력하세요.")
except BigNumberError as err: 
    print("오류가 발생했습니다. 한 자리 숫자만 입력하세요.")
    print(err) 
finally: # 오류 발생 여부와 상관없이 항상 실행
    print("계산기를 이용해 주셔서 감사합니다.")
