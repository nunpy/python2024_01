#1) 리스트 컴프리헨션을 이용한 짝수 생성
# 1부터 20까지의 숫자 중에서 짝수만 포함하는 리스트를 만드시오
even = [i for i in range(1,21) if i % 2 == 0]
print(even)
#또는 [i for i in range(2,21,2)]

#2) 조건을 포함한 리스트 컴프리헨션
# [1,2,3,4,5,6,7,8,9,10]에서 5보다 큰 순자만을 포함하는 새로운 리스트
a = [1,2,3,4,5,6,7,8,9,10]
num = [i for i in a if i > 5]
print(num)

#3) 문자열 처리를 위한 리스트 컴프리헨션
strList = ["apple", "banana", "cherry", "date"]
first = [i[0] for i in strList]
print(first)

#4) 대문자화
upper = [i.upper() for i in strList]
print(upper)



