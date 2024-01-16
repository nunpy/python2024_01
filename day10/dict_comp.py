#dict_comp
# normalPopcorn = {
#     'name':'일반 팝콘',
#     'price': 2500,
# }

# coffee = ['아메리카노', '라떼', '바닐라']
# price = [2500, 3000, 3500]
#zipper
# zipped = zip(coffee,price)
# print(list(zipped))

coffee = ['아메리카노', '라떼', '바닐라']
price = [2500, 3000, 3500]
caffeine = [120, 150, 50]
result = [{'이름':name, '가격':price, '카페인':caffeine} for name,price,caffeine in zip(coffee,price,caffeine)]
print(result)

coffee = ['아메리카노', '라떼', '바닐라']
for index, item in enumerate(coffee):
    print(f"{index}.{item}")

coffee = ['아메리카노', '라떼', '바닐라']
price = [2500, 3000, 3500]
a = {index:{'name':coffee, 'price':price} for index,(coffee,price) in enumerate(zip(coffee,price))}
print(a)

