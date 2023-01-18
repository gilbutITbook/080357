#3.1

#3.1.1
print(1 + 1)
print(3 - 2)
print(5 * 2)
print(6 / 3)


print(2 ** 3)
print(10 % 3)
print(10 // 3)

#3.1.2
print(10 > 3)
print(4 >= 7)
print(10 < 3)
print(5 <= 5)


print(3 == 3)
print(4 == 2)
print(3 + 4 == 7)
print(1 != 3)

print((3 > 0) and (3 > 5))
print((3 > 0) or (3 > 5))
print(not(1 != 3))

print(5 > 4 > 3)
print(4 > 5 > 3)


#3.2

print(2 + 3 * 4)
print((2 + 3) * 4)


#3.3

number = 2 + 3 * 4
print(number)
number = number + 2 # 2 + 3 * 4 + 2
print(number)


number = 2 + 3 * 4
print(number)
# number = number + 2
# print(number)
number += 2 # number = number + 2와 동일
print(number)
number -= 2 # number = number - 2와 동일
print(number)
number *= 2 # number = number * 2와 동일
print(number)
number /= 2 # number = number / 2와 동일
print(number)
number **= 2 # number = number ** 2와 동일
print(number)
number //= 2 # number = number // 2와 동일
print(number)
number %= 2 # number = number % 2와 동일
print(number)


#3.4

#3.4.1
print(abs(-5)) # -5의 절대값
print(pow(4, 2)) # 4를 제곱한 값
print(max(5, 12)) # 5와 12 중 큰 값
print(min(5, 12)) # 5와 12 중 작은 값
print(round(3.14)) # 3.14를 소수점 이하 첫째 자리에서 반올림한 정수
print(round(4.678, 2)) # 4.678을 소수점 이하 셋째 자리에서 반올림한 값


#3.4.2
from math import * # math 모듈의 모든 기능을 가져다 쓰겠다는 의미

result = floor(4.99)
print(result) # 4.99의 내림
result = ceil(3.14)
print(result) # 3.14의 올림
result = sqrt(16)
print(result) # 16의 제곱근


#3.4.3
from random import * # random 모듈의 모든 기능을 가져다 쓰겠다는 의미

print(random())
print(random())
print(random())

print(random() * 10)
print(int(random() * 10))
print(int(random() * 10) + 1)

print(int(random() * 45) + 1)

print(randrange(1, 46)) # 1 이상 46 미만에서 난수 생성
print(randint(1, 45)) # 1 이상 45 이하에서 난수 생성

print(randint(1, 45))
print(randint(1, 45))
print(randint(1, 45))
print(randint(1, 45))
print(randint(1, 45))
print(randint(1, 45))