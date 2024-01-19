#reduce_test
# map 치환
# filter 필터링
# reduce 누적

from functools import reduce

numbers = [1,2,3,4,5]
#reduce(어떻게, 무엇을)
result = reduce(lambda x,y: x + y,numbers)
print(result)

multi = reduce(lambda x,y: x*y, numbers)
print(multi)