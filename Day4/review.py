#정삼각형의 넓이와 둘레를 계산하는 프로그램 문구
#1. 사용자로부터 밑변과 높이를 입력받아 정삼각형의 넓이와 둘레를 구하는 프로그램

# len = int(input("밑변 입력:"))
# height = int(input("높이 입력:"))
#
# area = len * height * 0.5
# around = len * 3
#
# print(f"정삼각형의 넓이는 {area}, 둘레는 {around}")
#
# #2. 운동 순서 만들기 프로그램
# #사용자로부터 원하는 운동 종류를 3개 입력받아, 이를 바탕으로 효과적인 운동 순서를 생성하는 프로그램을 만들어보세요
# a = input("첫 번째 운동:")
# b = input("두 번째 운동:")
# c = input("세 번째 운동:")
# print(f"운동 순서: {a}->{b}->{c}")

#3 영화 리스트, 팝콘 리스트, 음료 리스트를 보여줘서 선택한 후 조합을 보여주는 프로그램:

movieList = ['서울의 봄', '위시', '노량']
popcornList = ['일반 팝콘', '치즈 팝콘', '캬라멜 팝콘']
drinksList = ['콜라', '제로 콜라', '스프라이트']

movie = int(input("영화 번호 고르세요 [1번: 서울의 봄, 2번: 위시, 3번: 노량]:")) - 1
popcorn = int(input("팝콘 번호 고르세요 [1번: 일반 팝콘, 2번: 치즈 팝콘, 3번: 캬라멜 팝콘]:")) - 1
drinks = int(input("음료 번호 고르세요 [1번: 콜라, 2번: 제로 콜라, 3번: 스프라이트]:")) - 1
# 위 세 변수는 모두 숫자 취급
print(f"고르신 영화는 {movieList[movie]}이며 팝콘은 {popcornList[popcorn]} 그리고 음료는 {drinksList[drinks]} 주문하셨습니다!")
# print(movieList[movie -1])





