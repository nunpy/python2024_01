# # dict_type
# # key-value
# # key: 중복 안됨, 숫자 or 문자 type 가능
# #value: 중복 가능, any type

# zodiac = {
#     1: '쥐',
#     2: '소',
#     3: '호랑이',
#     4: '토끼',
#     5: '용',
#
# } # dict type
# print(zodiac[2])

user = input("mbti 입력:")
user.split()
mbti = {
    'e': '외향적',
    'i': '내향적',
    's': '감각적',
    'n': '직관적',
    'f': '감성적',
    't': '이성적',
    'j': '계획적',
    'p': '즉흥적',
}
print(f"당신은 {mbti[user[0]]}, {mbti[user[1]]}, {mbti[user[2]]}, {mbti[user[3]]}이군요!")

# 아니면 그냥
# user = input("mbti 입력하세요:")
# print(f"당신의 성향은 {mbti[user[0]]}, {mbti[user[1]]}, {mbti[user[2]]}, {mbti[user[3]]}이군요!")
# 문자열[0]: 그 문자열의 첫 번째 글자

instagram = {
    "신촌맛집":['싸다김밥', '신촌순댓국', '서브웨이'],
    "서강대맛집":{
        "서강대학식":['한식정식', '오늘의치돈', '육회덮밥']
    }
}
print(instagram["신촌맛집"][2])
print(instagram["서강대맛집"]["서강대학식"][1])
