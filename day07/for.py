#print, input, 변수, 데이터타입[int,float,str,bool,list,set,dict]
#if문, random, 연산자,

#컴퓨터 = 기억[RAM] + 연산[CPU]

# #RAM: 변수[데이터타입], random
#
# #CPU: 연산자, print(), input(), len(), ~~() --> 명령문(), 조건문[if], 반복문[for]
# num = int(input("몇번 까지 보실래요?")) + 1
# for x in range(num):
#     print(x)
# print("끝")
#
# num = int(input("몇번 까지 보실래요?")) + 1
# for x in range(num):
#     if x % 2 == 0:
#         print(x)
# print("끝")

#유저에게 어떤 수를 입력받고 그 수의 배수를 1000까지 보여주는 프로그램
num = int(input("공배수 입력:"))
for x in range(1001):
    if x % num == 0:
        print(x)
print("끝")

# 1부터 10까지의 총합을 나타내는 프로그램
sum = 0
for x in range(11):
    sum += x
print(sum)

# n의 정수 입력받고 m의 정수를 받으면
# 0~n까지의 m의 공배수의 총합을 나타내는 프로그램

n = int(input("첫 번째 정수 입력:")) + 1
m = int(input("두 번째 정수 입력:"))
sum = 0
for x in range(n):
    if x % m == 0:
        sum += x
print(f"총합:{sum}")

# for x in range(n) #0 ~ n-1

# random, list, for
#0~10000사이의 랜덤한 숫자를 담고 있는 6개의 정수를 담고있는 리스트 출력

import random
for x in range(10001)
    random.randint(0,10001)


