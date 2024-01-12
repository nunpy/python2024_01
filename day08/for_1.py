#반복문 [for]
# sum = 0
# for x in range(10):
#     if x % 2 == 0:
#         sum += x
#         print(sum)

#유저에게 'InpUT' -> iNPut
# user = input("단어 입력:")
# for x in user:
#     print(x)

#정답:
# user = input("단어 입력:")
# word = ''
# for x in user:
#     if x.isupper():
#         word = word + x.lower() #''+'i' => i
#     else:
#         word = word + x.upper() #i +N => iN
# print(word)

#apple => ppl. a와 e를 제거하는 프로그램

# for x in 'apple':
#     print(x)
# user = input("단어 입력:")
# word = ''
# for x in user:
#     if x == 'a' or x == 'e':
#         pass
#     else:
#         word += x
# print(word)
#
# user = input("단어 입력:")
# word = ''
# for x in user:
#     if x in 'aeiou':
#         pass
#     else:
#         word += x
# print(word)
#
# for x in [1,2,3,4,5]:
#     print(x ** 2)

#연습문제
list = []
for x in ['사과', '바나나', '파인애플']:
    list.append(len(x))
print(list)

#홀수만 담긴 리스트와 짝수의 총합을 구하시오
list = []
sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
    if x % 2 != 0:
        list.append(x)
    else:
        sum += x
print(f"홀수만 담긴 리스트: {list}, 짝수의 총합: {sum}")

# 0~10000사이의 수를 담은 100개의 정수의 리스트
#출력
# 이 리스트에서 홀수면 '🥕' 짝수면 '🐇'

import random
num = []
for x in range(100):
    num.append(random.randint(0,10001))
num.sort()
print(num)

emoji = []
for x in num:
    if x % 2 == 1:
        emoji.append('🥕')
    else:
        emoji.append('🐇')
print(num)
print(emoji)

device = ['아이폰', '갤럭시', '맥북']
for x,y in enumerate(device):
    print(f"{x}. {y}")









