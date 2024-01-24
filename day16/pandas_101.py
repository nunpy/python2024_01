# pandas
# 엑셀을 파이썬화. 엑셀의 상위호환 버전..
# 판다스에서 만든 데이터 타입: series, dataframe
# series: 엑셀에서 하나의 열
# dataframe: 엑셀 그 자체[스프레드시트]
import pandas as pd
#as pd: 별명 부여
# import pandas as pd

#
# numList = [5,12,24,13,17]
# series = pd.Series(numList)
# print(series.mean())

# coffee = ['아메리카노', '카페라떼', '바닐라라떼', '카페모카', '카라멜 마끼야토']
# seriesC = pd.Series(coffee)
# print(seriesC)

#dataframe

# coffeeData = {
#     "menu": ['americano', 'latte', 'mocha', 'vanilla', 'mint'],
#     "price": [2500, 3000, 3500, 3500, 4000],
#     "caffeine": [120, 100, 80, 100, 50]
# }
#
# df = pd.DataFrame(coffeeData)
# df.to_csv('coffee.csv', index=False)

# index = False : 0부터 시작하는 인덱스는 빼주세요(엑셀파일에서)

from faker import Faker

fake = Faker('ko_KR')
# print(fake.name())
# faker generates a fake name for you.
# 직접입력하기귀찮잖아
carData = {
    'carName': ['k5', 'k7', 'avante', 'k3', 'tesla'],
    'owner': [fake.name() for i in range(5)],
}
# print(carData)

df = pd.DataFrame(carData)
df.to_csv('car.csv', index=False)









