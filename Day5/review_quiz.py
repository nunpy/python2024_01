# # 복습퀴즈
# # 1. 유저에게 쉼표 기준으로 할 계획을 입력받고, 할일을 나타내는 프로그램 만들기
#
# user = input("일본 여행 계획표를 입력하세요(쉼표 기준):")
# print(f"일본 여행 계획표는 {user.split(',')} 입니다!")
#
# # 2. 뉴스 기사 단어 찾기 프로그램
# # 뉴스 기사를 하나 가져와서 유저에게 찾고 싶은 단어를 물어보고, 해당 단어의 개수를 출력하는 프로그램
# news = """
# In the run-up to the New Year, the southern city of Bengaluru (formerly Bangalore) - often called India's Silicon Valley for being home to global information-technology (IT) majors - hit the headlines after protesters tore down English billboards, demanding that they be written in the city's local language, Kannada.
#
# The Karnataka Rakshana Vedike's (KRV) protest was to coerce the government to implement a law which mandates that 60% of each display sign in the city should have Kannada.
#
# KRV got some support from India's main political parties which condemned the violence but said there was no harm in demanding Kannada signages. A federal minister of the governing Bharatiya Janata Party (BJP) told a local news channel, "What is the harm in writing in Kannada, apart from English? This is not England".
#
# None of this came as a surprise because in India - home to more than 300 languages - assertion of linguistic identities is common. For instance, pro-Tamil language protesters in Karnataka's neighbouring state Tamil Nadu have used the slogan "Tamil Nadu is for Tamils" since the 1930s.
#
# After India won its independence in 1947, several states in the country were formed along linguistic lines by grouping together regions which spoke the same language. Karnataka was one such state formed in 1956.
#
# KRV, which tore down the English billboards last month, has been claiming for decades that Kannada and its speakers have been relegated to the margins in the cosmopolitan city where people from across the country, and the world, work and live. In Bengaluru, four out of 10 people come from outside the city, reports say, although two-thirds of this population come from within the state.
#
# While the influx of migrants has made some local people think that they would soon become a minority in the city, KRV's "Kannada first" demand springs from a linguistic nationalism that has been in the making for decades. Cultural historian Janaki Nair says in a research paper that Kannada speakers first demanded a separate state in the 1920s.
#
# Ms Nair notes that, at first, Kannada nationalists were accommodative of other languages, including English. One of the Kannada nationalists even said that "English is our cultural and political language, Sanskrit our spiritual and classical language and Kannada our native and speaking language", she writes.
# """
#
# word = input("찾고 싶은 단어:")
# countWord = news.count(word)
# print(f"단어 '{word}'의 개수는 {countWord}개 입니다.")
#
# #3. 스타벅스 메뉴 선택 프로그램
# # coffee = input("커피 메뉴 선택 [1. 아메리카노: 4000, 2. 라뗴: 5000, 3. 바닐라라떼: 5500]: ")
# # cake = input("케익 메뉴 선택 [1. 치즈케익: 5000, 2. 딸기케익: 6000, 3. 우유케익: 5500]: ")
#
# coffee = [4000, 5000, 5500]
# cake = [5000, 6000, 5500]
# coffee_choice = int(input("커피 메뉴 선택 (번호 입력) [1.아메리카노, 2.라뗴, 3.바닐라라떼]:")) - 1
# cake_choice = int(input("케익 메뉴 선택 (번호 입력) [1.치즈케익, 2.딸기케익, 3.우유케익]:")) - 1
# print(f"총 가격은 {coffee[coffee_choice] + cake[cake_choice]}원 입니다.")

#4. 좋아하는 커피 브랜드 저장 프로그램
# brand = input("좋아하는 커피 브랜드 입력(소문자로, 쉼표 기준):")
# brandCap = brand.capitalize()
# brandList = brandCap.split(',')
# print(brandList)

#풀이1
# brand = input("좋아하는 커피 브랜드 입력(소문자로, 쉼표 기준):")
# brandList = brand.split(',')
# first = brandList[0].capitalize()
# second = brandList[1].capitalize()
# third = brandList[2].capitalize()
# brandCapList = [first, second, third]
# print(brandCapList)

#풀이2
# brandList = input("좋아하는 커피 브랜드 입력(소문자로, 쉼표 기준):").split(',')
# brandCapList = [brandList[0].capitalize(), brandList[1].capitalize(), brandList[2].capitalize()]
# print(brandCapList)

#답:
# brandsList = input("좋아하는 커피 브랜드 3개 입력(쉼표 기준):").split(',')
# brandsList[0] = brandsList[0].capitalize()
# brandsList[1] = brandsList[1].capitalize()
# brandsList[2] = brandsList[2].capitalize()
# print(brandsList)