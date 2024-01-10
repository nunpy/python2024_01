#1. 뉴스 기사에서 가장 긴 단어 찾기
#주어진 뉴스 기사에서 가장 긴 단어 3개와 그 길이를 출력하는 파이썬 프로그램을 작성하세요

#영어 기사
# wordList = article.split()
# wordList.sort()
# c = list(set(wordList))
# c.sort()
# print(c)
#print(list(set(wordList)))
# len()


#2. 영화 예매 프로그램(dict 활용)
#사용자로부터 영화 종류를 나타내는 정수 1~3과 나이를 입력받습니다. 각 영화의 가격은 다음과 같이 설정합니다:
#1: 액션 영화 - 10000원
#2: 로맨틱 코미디 - 8000원
#3: 공포 영화 - 9000원

#팝콘 종류
#1: 치즈 팝콘: 6000원
#2: 카라멜 팝콘: 5000원
#3: 일반 팝콘: 5000원
#위 종류를 유저에게 입력받고 총 계산을 출력하는 프로그램을 구하세요

#2
#cgv['movie']['movieList']

cgv = {
    'movie' :{
        'movieList': ['액션 영화', '로맨틱 코미디', '공포 영화'],
        'moviePrice': [10000, 8000, 9000]
    },
    'popcorn': {
        'popcornList': ['1.치즈 팝콘', '카라멜 팝콘', '3.일반 팝콘'],
        'popcornPrice': [6000, 5000, 5000]
    }
}
movie_choice = int(input(f"영화를 고르세요[{cgv['movie']['movieList']}:")) - 1
popcorn_choice = int(input(f"팝콘을 고르세요[{cgv['popcorn']['popcornList']}:")) - 1

print(f"선택한 영화:{cgv['movie']['movieList'][movie_choice]}, 선택한 팝콘:{cgv['popcorn']['popcornList'][popcorn_choice]}, 총 금액:{cgv['movie']['moviePrice'][movie_choice] + cgv['popcorn']['popcornPrice'][popcorn_choice]}")

# movie = int(input("영화 종류:"))
# age = int(input("나이:"))
#
# popcorn = in
