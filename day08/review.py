#1. 각도 프로그램
#여러분으 각도 데이터 입력을 요청합니다. 이 프로그램은 사용자로부터 5개의 각도 입력

angle = int(input("각도 입력:"))
if 0< angle and angle < 90:
    print("예각")
elif angle == 90:
    print("직각")
elif 90 < angle and angle < 180:
    print("둔각")
elif angle == 180:
    print("평각")
else:
    print("오바각")

#2. 테마파크 프로그램
# themepark = {
#     'basic' : {
#         'basicFee' : 50000
#     },
#     'premium' : {
#         'premiumFee' : 75000
#     }
#     'vip' : {
#         'vipFee' : 100000
#     }
# }
#
# tp_choice = int(input("놀이기구 입장권을 고르세요:"))
# age = int(input("나이를 입력하세요:"))
#
# if age < 12:

themepark = {
    1: {
        'ticketName' : '일반 입장권',
        'ticketPrice' : 50000
    },
    2: {
        'ticketName' : '프리미엄 입장권',
        'ticketPrice' : 75000
    },
    3: {
        'ticketName' : 'vip 입장권',
        'ticketPrice' : 100000
    }
}

import random

num = [] #빈 리스트
for i in range (6):
    num.append(random.randint(0,10001))
num.sort()
print(num)




