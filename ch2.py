#2.1 

print(5) 


print(-10) 
print(3.14) 
print(1000) 


print(5 + 3) 
print(2 * 8) 
print(6 / 3)
print(3 * (3 + 1)) 


#2.2

print('풍선')
print("나비")
print("abcdefg")
print("10")
print("파이썬" * 3)


#print('작은따옴표") 
#print("큰따옴표') 


print("I don't want to go to school") # 정상 출력
#print('I don't want to go to school') # 오류 발생


#2.3

print(5 > 10) 
print(5 < 10) 


print(True) 
print(False) 


print(not True) 
print(not False) 


print(not (5 > 10)) 


#2.4

#2.4.1
print("반려동물을 소개해 주세요.")
print("우리 집 반려동물은 개인데, 이름이 연탄이예요.")
print("연탄이는 4살이고, 산책을 아주 좋아해요.")
print("연탄이는 수컷인가요?")
print("네.")


print("반려동물을 소개해 주세요.")
print("우리 집 반려동물은 개인데, 이름이 해피예요.")
print("해피는 4살이고, 산책을 아주 좋아해요.")
print("해피는 수컷인가요?")
print("네.")


name = "연탄이"
animal = "개"
age = 4
hobby = "산책"
is_male =True


#2.4.2
name = "연탄이"
animal = "개"
age = 4
hobby = "산책"

print("반려동물을 소개해 주세요.")
print("우리 집 반려동물은 개인데, 이름이 연탄이예요.")
#print("우리 집 반려동물은 " + animal + "인데, 이름이 " + name + "예요.")
print("연탄이는 4살이고, 산책을 아주 좋아해요.")
#print(name + "는 " + age + "살이고, " + hobby + "을 아주 좋아해요.") # 오류 발생
#print(name + "는 " + str(age) + "살이고, " + hobby + "을 아주 좋아해요.")


name = "해피"
animal = "고양이"
age = 4
hobby = "낮잠"

print("반려동물을 소개해 주세요.")
print("우리 집 반려동물은 " + animal + "인데, 이름이 " + name + "예요.")
print(name + "는 " + str(age) + "살이고, " + hobby + "을 아주 좋아해요.")


name = "연탄이"
animal = "개"
age = 4
hobby = "산책"

print(name + "는 " + str(age) + "살이고, " + hobby + "을 아주 좋아해요.") # + 연산자 사용 시
print(name, "는", age, "살이고,", hobby, "을 아주 좋아해요.") # 쉼표 사용 시

#2.4.3
print(int("3")) 
#print(int("3") + "입니다.") # TypeError 발생
print(int(3.5)) 
#print(int("삼")) # ValueError 발생

print(float("3.5")) 
print(float(3))

#print(float("오")) # ValueError 발생 
print(str(3) + "입니다.")
print(str(3.5) + "입니다.")


print(type(3)) # 정수(int)
print(type("3")) # 문자열(str) 
print(type(3.5)) # 실수(float)
print(type(str(3))) # 정수(int)를 문자열(str)로 형변환


#2.4.4
animal = "개"
age = 4
hobby = "산책"

print("반려동물을 소개해 주세요.")
#print("우리 집 반려동물은 " + animal + "인데, 이름이 " + name + "예요.") # NameError 발생
name = "연탄이"
print(name + "는 " + str(age) + "살이고, " + hobby + "을 아주 좋아해요.")


name = "연탄이"
animal = "개"
age = 4
hobby = "산책"

print("반려동물을 소개해 주세요.")
print("우리 집 반려동물은 " + animal + "인데, 이름이 " + name + "예요.")
hobby = "수영"
print(name + "는 " + str(age) + "살이고, " + hobby + "을 아주 좋아해요.")

#2.5

name = "연탄이" # 이름
animal = "개" # 종류
age = 4 # 나이
hobby = "산책" # 취미

# print("반려동물을 소개해 주세요.")
print("우리 집 반려동물은 " + animal + "인데, 이름이 " + name + "예요.") # 종류, 이름
print(name + "는 " + str(age) + "살이고, " + hobby + "을 아주 좋아해요.") # 나이, 취미


name = "연탄이" # 이름
animal = "개" # 종류
age = 4 # 나이
hobby = "산책" # 취미

"""
# print("반려동물을 소개해 주세요.")
print("우리 집 반려동물은 " + animal + "인데, 이름이 " + name + "예요.") # 종류, 이름
print(name + "는 " + str(age) + "살이고, " + hobby + "을 아주 좋아해요.") # 나이, 취미
"""