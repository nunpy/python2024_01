#1 홀짝
number = int(input("숫자 입력:"))
if number % 2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")

# #2 알파벳 탐지기
# alpha = input("글자 입력:")
# if alpha.isalpha():
#     print("알파벳 입니다.")
# else:
#     print("알파벳이 아닙니다.")
#
# #3 비밀번호 설정 프로그램
# password = input("비밀번호 설정:")
# # !  @
# if len(password) < 10:
#     print("최소 10글자 이상 설정하세요!")
# elif password.isalnum() or not ('!' in password or '@' in password or '#' in password):
#     print("영어와 숫자를 꼭 포함해 주세요!")
# else:
#     if not ('!' in password or '@' in password or '#' in password):
#         print("특수문자를 포함해 주세요")
#     else:
#         print("비밀번호 설정 완료!")
#
# #4. 버스 요금 계산기
# # bus = int(input("버스 노선 번호를 입력하세요 [1: 시내버스, 2: 광역버스, 3: 마을버스]:"))
# # age = int(input("나이를 입력하세요:"))
# # if bus == 1:
# #     if age <= 7:
# #         print("무료입니다.")
# #     elif 7 < age <= 19:
# #         print("840원입니다.")
# #     elif 19 < age < 65
# #         print("1200원입니다.")
# #     else:
# #         print("무료입니다.")
#
# bus = {
#     1: {
#         'name': '시내버스',
#         'price': 1200
#     }
#     2: {
#         'name': '광역버스',
#         'price' : 2000
#     }
#     3: {
#         'name': '마을버스'
#     }
# }
#
# bus_choice = int(input(f'버스를 선택하세요![1.시내버스 - 1200원, 2. 광역버스 - 2000원, 3. 마을버스'))
# age = int(input("나이를 입력하세요:"))
#
# if age <= 7 or 65 <= age:
#     print("무료입니다!")
# elif 8 <= age and age <= 19:
#     print(f"{bus[bus_choice]}")