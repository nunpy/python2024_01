import pandas as pd

df = pd.read_csv('dummy_data.csv')
# print(df)
#
# vanillaLover = df[df['coffee'] == '바닐라'][df['age'] > 30]

# 위에서 10개 뽑아오기/뒤에서 10개 뽑아오기
print(df.head(10))
print(df.tail(10))

#데이터의 요약본
print(df.describe())

#데이터 정렬 순서
print(df.sort_values(by='name'))
print(df.sort_values(by='age'))
print(df.sort_values(by='coffee'))

#데이터 변경
df['age'] = df['age'] // 10
print(df)

#groupby 데이터 특정 기준으로 그룹화
# groupedCoffee = df.groupby('coffee')

