# 문자열 길이 카운트, 각 길이가 배열 내에서 몇 번 나타나는지를 계산하는 함수

# words = input("영어 단어 열을 입력하세요:")
# lengthList = []
#
# def solution(words):
#     for i in words:
#         length = len(i)
#         lengthList += length

words = ["apple", "banana", "cherry", "date"]

def solution(arr):
    result = {}
    for i in arr:
        length = len(i)
        if length in result:
            result[length] += 1
        else:
            result[length] += 1
    return result





