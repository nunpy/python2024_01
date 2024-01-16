# 함수: 코드를 모아놓은 묶음.

# f(x) = x + 10
# input => 코드를 모아놓은 묶음 => output
# input 또는 output 이 없을수도 있음

# 파이썬 내장 함수
# ???() 함수
# print()함수
# input() 함수
# int() 함수
# something() 함수
# enumerate() 함수

# 파이썬 커스터마이즈 함수
# def add(x,y):
#     result = x+y
#     return result
#
# a = add(5,10)
# print(a)

#minus 함수
# def minus(x,y):
#     return x - y
# b = minus(12,4)
# print(b)
#multiply 함수
# def multi(x,y):
#     return x * y
# c = multi(3,4)
# print(c)
#
# 홀 짝 함수
# def oddEven(x):
#     if x % 2 == 0:
#         return "짝수입니다."
#     else:
#         return "홀수입니다."
#
# d = oddEven(56)
# print(d)

# 이런 함수를 정의하겠습니다: 어떤 변수 x에 대해서
# 만약 2로 나눈 나머지가 0이라면 "짝수입니다"를 출력해주세요

# 아무것도 없이 콘솔에 찍을수 없음
# 파이썬 변수/ 함수 거쳐서 프린트.


# def makeListDict(xList,yList, xKey, yKey):
#     return [{xKey: x, yKey: y} for x, y in zip(xList, yList)]
#
# breads = ['소금빵', '보름달', '단팥빵', '앙버터','마카롱']
# price = [2500, 1000, 2400, 4500, 3000]
#
# result = makeListDict(breads, price, "빵 종류", "가격")
# print(result)


def makeListDict(xList,yList, xKey = 'item', yKey = 'price'):
    return [{xKey: x, yKey: y} for x, y in zip(xList, yList)]

breads = ['소금빵', '보름달', '단팥빵', '앙버터','마카롱']
price = [2500, 1000, 2400, 4500, 3000]

#xkey값은 item, ykey값 price
result = makeListDict(breads, price)
print(result)


