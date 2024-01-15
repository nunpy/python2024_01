#1. 1부터 100까지 사이의 수를 유저가 입력한 정수 n의 배수만 출력하도록
user = int(input("1부터 100 사이의 정수 입력:"))
for x in range(101):
    if x % user == 0: #배수 공식
        print(x)

#2. 정수 n을 입력 받고 구구단을 출력해주세요
num = int(input("정수 n 입력:")) #5
for x in range(1,10):
    print(f"{num} * {x} = {num * x}") # 5*1, 5*2, ...