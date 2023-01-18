# 일반 가격
def price(people):
    print("{0}명, 영화표 가격은 {1}원입니다.".format(people, people * 10000))
# 조조 할인 가격
def price_morning(people):
    print("{0}명, 조조 할인 영화표 가격은 {1}원입니다.".format(people, people * 6000))
# 군인 할인 가격
def price_soldier(people):
    print("{0}명, 군인 할인 영화표 가격은 {1}원입니다. ".format(people, people * 4000))