#set_data
#datatype
#int, float, str, list, dict
#키값에는 문자나 숫자만 들어갈수 있다.

megastudy = {
    'python': [1,2,3],
    'java': [1,3,5],
    'c': [2,4,6]
}

#python의 날짜 가져오기
#1. megastudy['python'] - 연산자
#2. megastudy.get('python') 기능
# - megastudy.get('javascript', '수업 없음')

print(list(megastudy.keys()))
print(list(megastudy.values()))
print(list(megastudy.items()))

#set(집합) 중복 안됨

a = {1,2,3,1,2,3,1,2,3}
print(a)

b = set([1,2,3,4,1,2,3])
# 리스트를 세트화
b.add(1)
b.add(5)
b.discard(3)
print(b)
b.clear()
print(b)








