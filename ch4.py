#4.1

sentence1 = '나는 소년입니다.'
print(sentence1)


sentence2 = "파이썬은 쉬워요."
print(sentence2)


sentence1 = '나는 소년입니다.'
print(sentence1, type(sentence1))
sentence2 = "파이썬은 쉬워요."
print(sentence2, type(sentence2))


sentence3 = """
나는 소년이고,
파이썬은 쉬워요.
"""
print(sentence3)


#4.2

jumin = "990229-1234567"
print("성별 식별번호 : " + jumin[7])


jumin = "990229-1234567"
print("연 : " + jumin[0:2]) # 0부터 2 직전까지(0, 1)
print("월 : " + jumin[2:4]) # 2부터 4 직전까지(2, 3)
print("일 : " + jumin[4:6]) # 4부터 6 직전까지(4, 5)
print("생년월일 : " + jumin[:6]) # 처음부터 6 직전까지 -> jumin[0:6]과 같음
print("주민등록번호 뒷자리 : " + jumin[7:]) # 7부터 끝까지 -> jumin[7:14]와 같음
print("주민등록번호 뒷자리(뒤에서부터) : " + jumin[-7:]) # 뒤에서 7번째 위치부터 끝까지


#4.3

python = "Python is Amazing"

print(python.lower()) # 전체 소문자로 변환
print(python.upper()) # 전체 대문자로 변환
print(python[0].isupper()) # 인덱스 0에 있는 값이 대문자인지 확인
print(python[1:3].islower()) # 인덱스 1부터 2에 있는 값이 소문자인지 확인
print(python.replace("Python", "Java")) # Python을 Java로 바꾸기


python = "Python is Amazing"

find = python.find("n") # 처음 발견한 n의 인덱스
print(find) # 'Python'에서 n(인덱스 5)
find = python.find("n", find + 1) # 인덱스 6 이후부터 찾아 처음 발견한 n의 인덱스
print(find) # ' is Amazing'에서 n(인덱스15)
find = python.find("Java") # Java가 없으면 -1을 반환(출력)한 후 프로그램 계속 수행
print(find)
index = python.index("n") # 처음 발견한 n의 인덱스
print(index) # 'Python'에서 n
index = python.index("n", index + 1) # 인덱스 6 이후부터 찾아 처음 발견한 n의 인덱스
print(index) # ' is Amazing'에서 n
index = python.index("n", 2, 6) # 인덱스 2부터 6 직전까지 찾아 처음 발견한 n의 인덱스
print(index) # 'thon'에서 n(인덱스 5)
#index = python.index("Java") # Java가 없으면 오류가 발생하며 프로그램 종료
print(index)


python = "Python is Amazing"

print(python.count("n"))
print(python.count("v"))


python = "Python is Amazing"

print(len(python))


#4.4

print("ab" + "ab")
print("ab", "ab")


#4.4.1
print("나는 %d살입니다." % 20)
print("나는 %s을 좋아합니다." % "파이썬")
print("Apple은 %c로 시작해요." % "A")
print("나는 %s살입니다." % 20) # %s로도 정숫값 표현 가능


print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간")) # 값이 여럿일 때


#4.4.2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))


print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color="빨간"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(color="빨간", age=20))


#4.4.3
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")


#4.5

#4.5.1
print("백문이 불여일견 백견이 불여일타")
#print("백문이 불여일견 # SyntaxError 발생
#백견이 불여일타")
print("백문이 불여일견\n백견이 불여일타")


#4.5.2
#print("저는 "나도코딩"입니다.")
print("저는 '나도코딩'입니다.")
# 또는
print('저는 "나도코딩"입니다.')


print("저는 \"나도코딩\"입니다.")
print("저는 \'나도코딩\'입니다.")


#4.5.3
#print("C:\Users\Nadocoding\Desktop\PythonWorkspace") # SyntaxError 발생
print("C:\\Users\\Nadocoding\\Desktop\\PythonWorkspace")
print(r"C:\Users\Nadocoding\Desktop\PythonWorkspace")


#4.5.4
print("Red Apple\rPine")


#4.5.5
print("Redd\bApple")


#4.5.6
print("Red\tApple")