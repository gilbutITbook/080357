#5.1

#5.1.1
# 지하철 칸별로 10명, 20명, 30명 승차
subway1 = 10
subway2 = 20
subway3 = 30


subway = [10, 20, 30]
print(subway)


#5.1.2
subway = ["푸", "피글렛", "티거"]
print(subway)

# 피글렛이 몇 번째 칸에 탔는가?
print(subway.index("피글렛"))

# 이요르 탑승
subway.append("이요르")
print(subway)

# 루를 푸와 피글렛 사이(인덱스 1 위치)에 삽입
subway.insert(1, "루")
print(subway)

# 지하철 역마다 한 명씩 내림
print(subway.pop()) # 이요르 내림
print(subway)
print(subway.pop()) # 티거 내림
print(subway)
print(subway.pop()) # 피글렛 내림
print(subway)

# 지하철에서 모두 내림
subway.clear()
print(subway)


#5.1.3
# 같은 이름이 몇 명 있는지 확인
subway = ["푸", "피글렛", "티거"]
subway.append("푸") # 푸 추가
print(subway)
print(subway.count("푸"))


#5.1.4
num_list = [5, 2, 4, 3, 1]

num_list.sort() # 오름차순 정렬
print(num_list)

num_list.sort(reverse=True) # 내림차순 정렬
print(num_list)

num_list.reverse() # 순서 뒤집기
print(num_list)


my_list = [1, 3, 2]
my_list.sort() # 리스트 정렬
print(my_list) # my_list 리스트 데이터 변경
your_list = [1, 3, 2]
new_list = sorted(your_list) # 정렬할 리스트를 소괄호 안에 넣음
print(your_list) # your_list 리스트 데이터는 변경되지 않음
print(new_list) # 정렬된 새로운 리스트


#5.1.5
mix_list = ["푸", 20, True, [5, 2, 4, 3, 1]]
print(mix_list)


mix_list = ["푸", 20, True]
num_list = [5, 2, 4, 3, 1]
num_list.extend(mix_list) # 리스트 합치기
print(mix_list)
print(num_list)


#5.2

#5.2.1
cabinet = {3: "푸", 100: "피글렛"}

print(cabinet[3]) # key 3에 해당하는 value
print(cabinet[100]) # key 100에 해당하는 value

print(cabinet.get(3)) # key 3에 해당하는 value

print(cabinet.get(5)) 
print("hi")
#print(cabinet[5]) # KeyError 발생
print("hi")

print(cabinet.get(5, "사용 가능")) # key에 해당하는 값이 없으면 기본값을 사용하게 함

print(3 in cabinet)
print(5 in cabinet)


cabinet = {"A-3": "푸", "B-100": "피글렛"}
print(cabinet["A-3"])
print(cabinet["B-100"])

print("곰" in "곰돌이")
print("돌이" in "곰돌이")
print("푸" in "곰돌이")


#5.2.2
cabinet = {"A-3": "푸", "B-100": "피글렛"}
print(cabinet)
cabinet["A-3"] = "티거" # key에 해당하는 값이 있을 때 -> 값 변경
cabinet["C-20"] = "이요르" # key에 해당하는 값이 없을 때 - > 값 추가
print(cabinet)

del cabinet["A-3"] # key 'A-3'에 해당하는 값 삭제
print(cabinet)


#5.2.3
print(cabinet.keys()) # key만 출력

print(cabinet.values()) # value만 출력

print(cabinet.items()) # key, value 한 쌍으로 출력

cabinet.clear() # 값 전체 삭제
print(cabinet)


#5.3
menu = ("돈가스", "치즈돈가스")
print(menu[0])
print(menu[1])


name = "피글렛"
age = 20
hobby = "코딩"
print(name, age, hobby)


(name, age, hobby) = ("피글렛", 20, "코딩")
print(name, age, hobby)


(departure, arrival) = ("김포", "제주")
print(departure, ">", arrival) # 김포 > 제주
(departure, arrival) = (arrival, departure)
print(departure, ">", arrival) # 제주 > 김포


#5.4
my_set = {1, 2, 3, 3, 3}
print(my_set)

java = {"푸", "피글렛", "티거"} # 자바 개발자 세트
python = set(["푸", "이요르"]) # 파이썬 개발자 세트

# 교집합(자바와 파이썬을 모두 다룰 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# 합집합(자바 또는 파이썬을 다룰 수 있는 개발자)
print(java | python)
print(java.union(python))

# 차집합(자바는 할 수 있지만 파이썬은 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))

# 파이썬 개발자 추가(기존 개발자: 푸, 이요르)
python.add("피글렛")
print(python)

# 자바 개발자 삭제(기존 개발자: 푸, 피글렛, 티거)
java.remove("피글렛")
print(java)


#5.5
menu = {"커피", "우유", "주스"}
print(menu)
print(type(menu))

menu = list(menu) # 리스트로 변환
print(menu, type(menu))

menu = tuple(menu) # 튜플로 변환
print(menu, type(menu))

menu = set(menu) # 세트로 변환
print(menu, type(menu))