# #review
# #영어로 표기되어 있는 숫자를 수로 바꾸기
#
# engNum = input("영어로 숫자를 입력하세요:")
# def solution(engNum):
#     for i in num:
#         if i in engNum:
#             return num[i]
#
# solution(engNum)
#
# num = {
#     "one": 1,
#     "two": 2,
#     "three": 3,
#     "four": 4,
#     "five": 5,
#     "six": 6,
#     "seven": 7,
#     "eight": 8,
#     "nine": 9,
#     "zero": 0
# }


def solution(numbers):
    numList = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for index, item in enumerate(numList):
        numbers = numbers.replace(item, str(index))
    return int(numbers)

print(solution("onefourzero"))

