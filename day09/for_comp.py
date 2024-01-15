#for_comp(심화/축약 버전)

# a = []
# for i in range(1001):
#     a.append(i)
#
# a = [i for i in range(1001)]
# print(a)
# #1. 0~100 comp 짜고
# #2. 1~500
#
# b = [x for x in range(101)]
# print(b)
#
# c = [i for i in range(1,501)]
# print(c)
#
# d = [i for i in "megastudy"]
# print(d)

# e = [i*2 for i in range(1,101)]
#1. 1~10을 각각 제곱한 수의 리스트
#2. 1~10에 각각 5를 더한 수의 리스트

# f = [i**2 for i in range(1,11)]
# print(f)
#
# g = [i + 5 for i in range(1,11)]
# print(g)

#for 컴프리헨션 조건문
# 1. if가 뒤에 있을 때는 filter 역할
# [i for i in range(1,101) if i % 5 == 0]

# fruits = ['apple', 'strawberry', 'mango', 'orange', 'melon']
# a = [i for i in fruits if i.count('a') > 0]
# b = [i for i in fruits if i.count('r') == 1]
# c = [i for i in fruits if len(i) >= 6]
# print(a)
# print(b)
# print(c)
#
# 2. if - else 있을 때는 map 변환/치환 역할
# a = ['😎' if i % 2 == 0 else i for i in range(1,101)]
# print(a)

# 1. 유저에게 n을 입력받고 1~100까지 리스트를 출력하는데, n의 배수만 당근을 표현해주고 나머지는 숫자로 표현
num = int(input("숫자 n 입력:"))
x = ['🥕' if i % num == 0 else i for i in range(1,101)]
print(x)

# 2. fruits에서 5글자 이하이면 대문자로 바꿔서 출력하고 아니면 토끼 이모지를 출력하는 리스트 만들기
fruits = ['apple', 'strawberry', 'mango', 'orange', 'melon']
p = [i.upper() if len(i) <= 5 else '🐇' for i in fruits]
print(p)

# for 컴프리헨션 중첩 루프문
h = [i*j for i in range(1,4) for j in range(1,4)]
g = [i+j for i in ["apple", "banana"] for j in ["pie", "tanghuru"]

# i = 1, j = 1,2,3


