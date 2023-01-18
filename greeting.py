def say_hello(to):
    print(f"안녕, {to}?")

def say_goodbye(to):
    print(f"또 만나, {to}!")

if __name__ == "__main__": # 모듈 직접 실행 시 함수 호출
    say_hello("파이썬")
    say_goodbye("나도코딩")