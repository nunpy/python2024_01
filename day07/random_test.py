# random_test
# 내장되어있는 기능은 아님
import random

fruits = ['사과', '망고', '바나나', '멜론']

print(random.randint(0,100))
print(random.random()) #0~1사이의 실수
print(random.choice(fruits))
random.shuffle(fruits)
print(fruits)
