# lambda
# 간결하고 이름이 없는 한 줄 함수
def add(a,b):
    return a + b

plus = lambda a,b: a+b
result = plus(5,7)
print(result)

minus = lambda a,b: a-b
multi = lambda a,b: a*b

# callback 함수
# something(add)
# 매개변수에 함수를 넣는 것. f(g(x))

# cf. something(add(3,5)) = something(8)

def hello(some):
    print("안녕!")
    some()

def bye():
    print("잘가")

hello(bye)

eggs = ['🥚''🥚''🥚']

# index는 변수, recipe는 함수
def cookEggs(eggs,index,recipe):
    recipe(eggs,index)

def makefry(eggs,index):
    eggs[index] = '🍳'

def makeSandwich(eggs,index):
    eggs[index] = '🥪'

cookEggs(eggs, 0, makefry)
cookEggs(eggs, 1, makeSandwich)
print(eggs)