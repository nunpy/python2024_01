#quiz
#전체주석처리 cntrl /
#1) 태어난 연도를 입력받고 현재 만나이 출력하는 프로그램
#ex) 2000 -> 23

#2) 세개의 숫자를 입력받고 총합, 평균(실수) 출력

#birth_year = int(input("출생연도:"))
#current_year = 2024
#print(f"현재 만 나이는 {current_year - birth_year -1}")

#정답
#birth_year = int(input("출생연도:"))
#print(f"현재 만 나이는 {2023 - birth_year}")

#first = int(input("첫 번째 수:"))
#second = int(input("두 번째 수:"))
#third = int(input("세 번째 수:"))
#print(f"총합: {first+second+third}")
#print(f"평균: {(first+second+third)/3}")

#정답
#a = float(input("첫 번째:"))
#b = float(input("두 번째:"))
#c = float(input("세 번째:"))
#sum = a+b+c
#avg = sum/3
#print(f"총합: {sum}, 평균: {avg}")

#3) 섭씨 온도를 입력받아 화씨 온도로 변환을 출력하는 프로그램 만들기
#F=Cx5.9+32
a = float(input("섭씨 온도:"))
print(f"화씨 온도:{a * 5.9 + 32}")

cel = float(input("섭씨 온도:"))
fah = cel * 5.9 + 32
#변수[실수]:.2f 둘째 자리 출력
print(f"화씨 온도:{fah:.2f}")

#4) 사용자의 키와 몸무게를 입력받아 BMI를 출력하는 프로그램 만들기
#bmi = weight / (height **2)
weight = float(input("몸무게:"))
height = float(input("키:"))
print(f"BMI: {weight/(height**2)}")

weight = float(input("몸무게 입력:"))
height = float(input("키 입력:"))
bmi = weight / (height**2)
print(f"BMI: {bmi:.2f}")

#5) 반지름 입력시 원의 넓이와 둘레를 구하는 프로그램
r = float(input("반지름:"))
print(f"원의 넓이: {3.14*(r**2)}, 원의 둘레: {2*3.14*r}")

radius = int(input("반지름:"))
width = 3.14 * radius ** 2
round = 2 * 3.14 * radius
print(f"원의 넓이: {width}, 원의 둘레: {round}")

#복습
# print() -출력
# input() -입력[결과는 문자 타입으로]
# 변수 -   임시저장하는 곳
# int() / float() / str()
# 사칙연산