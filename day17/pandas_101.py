import pandas as pd

#dataframe

data = {
    'age': [30, 40, 50, 40, 50],
    'name': ['a', 'b', 'c', 'd', 'e'],
    'gender': ['m', 'f', 'f', 'm', 'm']
}

df = pd.DataFrame(data)
print(df)
#class = 변수 + 함수
#dataframe = 변수

#shape 행과 열의 수를 돌려줌
print(df.shape)
#index 행
print(df.index)
#column 열
print(df.columns)
#values 데이터[list]
print(df.values)

# 해당 열 뽑기
print(df['age'])
print(df[['age', 'name']])

#해당 열 뽑기[조건]
print(df[df['age'] > 30])
print(df[df['gender']== 'f'][df['age'] == 40])

#행 뽑기
print(df.loc[0, 'name'])