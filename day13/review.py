# day 13
# 문자열 뒤집기
# 함수가 없으면 타입변환 시도
def reverseStr(my_string):
    strList = list(my_string) # [b,r,e,a,d]
    strList.reverse() #[d,a,e,r,b]
    word = ""
    for i in strList:
        word += i
    return word
print(reverseStr("bread"))


# 2. 미완성된 할일 찾기

todoList = ["problemsolving", "practiceguitar", "swim", "studygraph"]
finished = [True, False, True, False]

def haveto_List(todoList, finishedList):
    newList = []
    for index,item in enumerate(finishedList):
        if not item:
            newList.append(todoList[index])
    return newList

# def haveto_List(todoList, finishedList):
#     return [todoList[index] for index,item in enumerate(finishedList) if not item]

print(haveto_List(todoList, finished))

