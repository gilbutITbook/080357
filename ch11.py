#11.1

#11.1.2
import theater_module # 모듈 가져오기

theater_module.price(3) # 3명이 영화를 보러 갔을 때 가격
theater_module.price_morning(4) # 4명이 조조 영화를 보러 갔을 때 가격
theater_module.price_soldier(5) # 군인 5명이 영화를 보러 갔을 때 가격


import theater_module as mv # theater_module을 별명인 mv로 사용한다는 의미
mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)


from theater_module import * # theater_module에서 모든 기능을 가져와 사용함

price(3) # theater_module.을 작성할 필요 없음
price_morning(4)
price_soldier(5)


from theater_module import price, price_morning # 모듈에서 일부 함수만 가져와 사용함

price(5) # 5명
price_morning(6) # 6명
price_soldier(7) # import하지 않아서 사용 불가


# price_soldier를 별명인 price로 대체 사용
from theater_module import price_soldier as price

price(5) # price_soldier() 함수 호출


#11.2

#11.2.2
import travel.thailand # travel 패키지의 thailand 모듈 가져오기

trip_to = travel.thailand.ThailandPackage()
trip_to.detail()


"""
import travel.thailand.ThailandPackage # 클래스 import 불가

trip_to = travel.thailand.ThailandPackage()
trip_to.detail()
"""


# travel.thailand 모듈에서 ThailandPackage 클래스 가져오기
from travel.thailand import ThailandPackage 

trip_to = ThailandPackage() # from~import 문에서는 travel.thailand. 제외
trip_to.detail()


#11.3

from travel import *

trip_to = vietnam.VietnamPackage() # 베트남
#trip_to = thailand.ThailandPackage() # 태국
trip_to.detail()


#11.4

from travel import *

trip_to = thailand.ThailandPackage()
trip_to.detail()


#11.5

import inspect
import random

print(inspect.getfile(random)) # random 모듈 위치(경로)


import inspect
from travel import *

print(inspect.getfile(thailand)) # thailand 모듈 위치


#11.6

from bs4 import BeautifulSoup

soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())


# 11.7

language = input("어떤 언어를 좋아하세요? ")
print("{0}은 아주 좋은 언어입니다!".format(language))


print(dir())
import random # random 모듈 가져다 쓰기
print(dir())
import pickle # pickle 모듈 가져다 쓰기
print(dir())


import random
print(dir(random))


lst = [1, 2, 3]
print(dir(lst))


name = "Jim"
print(dir(name))


#11.8

#11.8.1
import glob

print(glob.glob("*.py")) # 확장자가 py인 모든 파일 출력

#11.8.2
import os

print(os.getcwd()) # 현재 작업 폴더 위치(경로)


folder = "sample_dir"
if os.path.exists(folder): # 같은 이름의 폴더가 존재한다면
    print("이미 존재하는 폴더입니다.")
    os.rmdir(folder) # 폴더 삭제
    print(folder, "폴더를 삭제했습니다.") # 삭제 문구 출력
else: # 폴더가 존재하지 않으면
    os.makedirs(folder) # 폴더 생성
    print(folder, "폴더를 생성했습니다.")


print(os.listdir()) # 현재 작업 폴더 안의 폴더와 파일 목록 출력

#11.8.3

import time

print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S")) # 연-월-일 시:분:초


import datetime

print("오늘 날짜는", datetime.date.today())
today = datetime.date.today() # 오늘 날짜 저장
td = datetime.timedelta(days=100) # 100일째 날짜 저장
print("우리가 만난 지 100일은", today + td) # 오늘부터 100일 후 날짜