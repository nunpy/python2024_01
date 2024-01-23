# 핸드폰 번호 가리기

def solution(phone_number):
    newNumber = ""
    for index,item in enumerate(phone_number):
        if len(phone_number) - 4 > index:
            newNumber += "*"
        else:
            newNumber += item
    return newNumber

a = solution("01012345678")
print(a)