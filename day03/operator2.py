# 산술 연산자 [결과:숫자]

# 100이하의 정수를 입력받고 10의 자리와 1의 자리를 출력하는 프로그램
#ex) 89 -> 8,9

# num = int(input("100 이하의 양의 정수 입력:"))
# ten = num // 10
# one = num % 10
# print(f"10의 자리는 {ten}, 1의 자리는 {one}")

# 1000 이하 정수를 입력 받고
# 분과 초로 환산하는 프로그램
num = int(input("1000 이하의 양의 정수 입력:"))
min = num // 60
sec = num % 60
print(f"{min}분 {sec}초")

#정수: 10000~99999 사이를 입력받고
# 100의 자라값을 출력하는 프로그램
#ex) 17300 -> 3
num = int(input("10000~99999 사이의 정수 입력"))
hundred = num // 100
result = hundred % 10
print(result)





# 비교 연산자 [결과:Bool]
# >,<,>=,<=,==(같다),!=(다르다)
#입력값은 숫자만가능, 같다일때는 문자도 가능

a = 3 > 1 #a는 bool type
b = 3 == 1 #b는 bool type [False]
c = 3 != 1 #c는 bool type [True]
print(3<1)

#논리 연산자[결과:bool]
# and: 피연산자가 모두 True이면 True
print(3>1 and 5>1) #True
# or : 피연산자가 하나라도 True이면 True
print(5<1 or 3<1 or 0<1) #True
# not: false -> true, true -> false
print(not(3>1)) #true -> false

# 할당 연산자
a = 1
a = 3 #3으로 바꿔치기하기
# a얼마? 3 (바꿔치기한것)

b = 1
#b = b + 3 #3을 더해주기
b += 3 #3을 더해주기
b -= 3 #3을 빼주기
b *= 3 #3을 곱해주기
b /= 3 #3으로 나누기