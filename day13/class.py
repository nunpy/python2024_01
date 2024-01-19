# 객체 and class

# price => int/float
# name => str
# height => float
# Coffee => coffeeName = str, coffeePrice = int, hasShot = bool
# (Struct 구조체[변수 모음(명사/상태)] + function 함수(동사/동작)) => class

# Coffee => coffeeName = str, coffeePrice = int, hasShot = bool
# Coffee => addSyrup(), addShot(),...

# 어떤 프로그램인지 미리 기획이 완성이 되어야 클래스를 만들 수 있습니다.
# 예) 펫보험 dog 클래스
# Dog => master, name, age, breed, surgeryList, hasAdopt
# Dog => changeMasterName, addAge, addSurgery,...

# 예2) 강아지 키우기 게임 dog 클래스
# Dog => hp, skill, energy, state
# Dog => takeAwalk,...

class Car:
    # 생성자 함수
    def __init__(self, b, n, c): # 변수/구조체[명사/상태]
        self.brand = b
        self.name = n
        self.color = c

    def introduce(self):
        print(f"차의 이름은 {self.name}, 브랜드는 {self.brand}, 차 색깔은 {self.color}")

    def horning(self):
        print("경적 울립니다")

    def driving(self):
        print("앞으로 갑니다.")

a = Car('현대', 'k5', '검은색')
a.introduce()
b = Car('기아', '모닝', '보라색')
b.introduce()

# 클래스(문법, 설계도)
# 절차 지향 프로그래밍 -> 객체 지향 프로그래밍(OOP)

#절차[연산자 지향] 지향(위에서 아래로)
# 유지 보수 힘듦/결과 예측 불가

#객체 [object 지향] 지향() object[str,int,float,...]
# "123" + "123"
# "123" - "123"
#유지보수 가능/ 결과 예측
