#function_part2

def add(x,y):
    return x + y
#매개변수가 2개일때

# 가변 매개 변수: 변수가 몇 개일지 모를 때. 무한개면?
def makePizza(*toppings):
    print("다음 피자는 아래의 토핑이 들어갑니다.")
    for i in toppings:
        print(i)
makePizza("pineapple")
makePizza("pineapple", "cheese")
makePizza("pineapple", "cheese", "mushroom")


# 돌려주는 게 있으면 return을 쓰고 그냥 나타내는 거면 print
#['닭', '돼지', '소']  = zodiac(1993,1995,1997)

def zodiac(*years):
    sign = ['닭', '개', '돼지', '쥐', '소', '호랑이', '토끼', '용', '뱀', '말', '양', '원숭이', '닭']
    # newList = []
    # for i in years:
    #     newList.append(sign[i - 1993])
    # return newList
    return [sign[i - 1993] for i in years]

a = zodiac(1993, 1994, 1999, 2002)
print(a)

#print와 return의 차이???




movie_name = ['액션 영화','로맨틱 코미디','다큐멘터리']
movie_prices = [12000, 10000, 11000]
popcorn_name = ['팝콘 세트', '스낵 콤보','건강 팩']
popcorn_prices = [6000,8000,7000]
seat_names = ['일반 좌석']

