#main
# import my_math as mm
#
# result = mm.add(10,10)
# print(result)

from my_math import * # *는 universal. 다가져오겠다
result = add(10,20)
print(result)

from my_math import add
result = add(10,20)
print(result)