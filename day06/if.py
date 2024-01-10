#if

# 2 + 3
# 컴퓨터 = 기억[RAM] + 연산[CPU]
# RAM: 변수, 데이터 타입
# CPU: 연산자, 명령어() ex. print, 제어문

#print, input, len, 연산자, 변수, 데이터타입[int, float, str, list, set, dict]

#제어문[조건문, 반복문]
#코드의 일부를 실행하거나 반복해서 실행하고 싶을 때

#조건문 - if
# num = int(input("정수 입력:"))
# if num > 0:
#     print('양의 정수 입니다.')
# print('프로그램 끝')

num = int(input("정수 입력:"))
if num > 0:
    print("양의 정수 입니다.")
else:
    print("0 또는 음의 정수 입니다.")

num = int(input("정수 입력:"))
if num > 0:
    print("양의 정수 입니다.")
elif num == 0:
    print("0입니다.")
else:
    print("음의 정수 입니다.")

#유저에게 영어점수를 입력받고
# 100~90 - 'A입니다.'
# 90~80 - 'B입니다.'
# 80~70 - 'C입니다.'
# 70 - '재수강입니다.'

# english = int(input("영어점수:"))
# if 90 <= english <= 100:
#     print("A입니다.")
# elif 80 <= english < 90:
#     print("B입니다.")
# elif 70 <= english < 80:
#     print("C입니다.")
# elif english < 70:
#     print("재수강입니다.")

english = int(input("영어점수:"))
if 90 <= english <= 100:
    print("A입니다.")
elif 80 <= english < 90:
    print("B입니다.")
elif 70 <= english < 80:
    print("C입니다.")
else:
    print("재수강입니다.")

a = 10
if a > 0:
    if a < 20:
        print('a는 20보다 작은 양의 정수 입니다.')
    else:
        print('a는 20보다 큰 양의 정수입니다.')
else:
    if a == 0:
        print('a는 0입니다.')
    else:
        print('음수입니다.')

#유저에게 정수를 입력받고
#양의 홀수, 양의 짝수, 0, 음의 홀수, 음의 짝수

num = int(input("정수 입력:"))
if num > 0:
    if num % 2 == 0:
        print("양의 짝수입니다.")
    else:
        print("양의 홀수입니다.")
elif num == 0:
        print("0입니다.")

#유저에게 비밀번호 설정을 입력받고
#만약에 8글자보다 작으면 비밀번호 재설정!
#크면 비밀번호 완료!

password = input("비밀번호:")
if len(password) < 8:
    print('비밀번호 재설정')
else:
    print('비밀번호 완료')


pw = input("비밀번호 입력:")
if len(pw) < 8:
    print('비밀번호가 8글자 이하입니다.')
# elif pw.count('!') != 1:
elif '!' not in pw:
    print("특수문자가 없습니다.")
else:
    print('비밀번호 통과!')











