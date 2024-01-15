#str_advance

# print(), input()[str], variable
# int(), str(), float(), bool(), list()
# datatype[int,float,str,list,bool, ...]
# operator 산술: +-*/%//**, 논리: and, or, not
# 비교: >,<,!=,==

coffee = "americano" #str
# 내장 함수 [int(), str(), float(), bool(), list(), print(), input()]
# len(): 길이를 알려주는 기능
# print(len(coffee))
# print(coffee.upper()) #AMERICANO
# print(coffee.lower()) #americano
# print(coffee.capitalize()) #Americano
# print(coffee.strip()) # 빈공간 americano 빈공간 [빈공간 없애기]
# print(coffee.find('c'))# 몇변째에 c가 있니? 5번째. 없으면 -1
# print(coffee.replace('cano', 'can')) #왼쪽에서 오른쪽으로 바꾸기
# print(coffee.count('a')) #'a' 가 몇개 있니?

# #퀴즈
# #1. 대소문자 변환 프로그램
# #사용자로부터 소문자로 된 문자열을 입력받은 후, 이를 모두 대문자로 변환하는 프로그램을 만드세여.
# word = input("영단어 입력:")
# print(word.upper())
#
# # 2. 노래 가사에서 단어 카운트
# # 찰리푸스의 노래 "Left and Right"에서 'left'와 'right'라는 단어가 각각 몇 번 나오는지를 세는 프로그램을 만드세요.
# # 대소문자 구분 없이 카운트하세요.
# song = """
# Memories follow me left and right
# I can feel you over here, I can feel you over here
# You take up every corner of my mind (what you gon' do now?)
# Ever since the d-day y-you went away (no, I don't know how)
# How to erase your body from out my brain (what you gon' do now?)
# Maybe I should just focus on me instead (but all I think about)
# Are the nights we were tangled up in your bed
# Oh no (oh no)
# Oh no (oh no)
# You're goin' 'round in circles
# Got you stuck up in my head, yeah
# Memories follow me left and right
# I can feel you over here, I can feel you over here
# You take up every corner of my mind
# Your love stays with me day and night
# I can feel you over here, I can feel you over here
# You take up every corner of my mind (what you gon' do now?)
# Ever since the d-day y-you went away (someone tell me how)
# How much more do I gotta drink for the pain (what you gon' do now?)
# You did things to me that I just can't forget (now all I think about)
# Are the nights we were tangled up in your bed
# Oh no (oh no)
# Oh no (oh no)
# You're going 'round in circles
# Got you stuck up in my head, yeah
# Memories follow me left and right
# I can feel you over here, I can feel you over here
# You take up every corner of my mind (of my mind)
# Your love stays with me day and night
# I can feel you over here, I can feel you over here
# You take up every corner of my mind (what you gon' do now?)
# Did you know you're the one that got away?
# And even now, baby, I'm still not okay
# Did you know that my dreams, they're all the same
# Every time I close my eyes?
# Memories follow me left and right
# I can feel you over here, I can feel you over here
# You take up every corner of my mind (what you gon' do now?)
# Your love stays with me day and night
# I can feel you over here, I can feel you over here
# You take up every corner of my mind (what you gon' do now?)
# (Whoa)
# I can feel you over here, I can feel you over here
# You take up every corner of my mind (what you gon' do now?)
# """
# print(f"가사에서 left는 {song.count('left')}개, right는 {song.count('right')}개")
# print(f"가사의 길이는 {len(song)}")
#
# # a = "mega"
# # b = "study"
# # c = a + b # +는 문자열 연결 연산자 --> 결과: megastudy
# # d = a * 3 # * 문자열 반복 연산자 --> 결과: megamegamega
# # e = a[0] # [] 문자열 인덱싱 --> 결과 :m
# # f = b[0:3] # [start:end] 문자열 슬라이싱(end 제외) --> 결과: stu
# # g = 'g' in a #mega에서 g가 있니? --> 결과: True or False
#
# title = "megastudy python programming"
# print(title.split()) #빈공간 기준으로 찢어줌. str에서 list 만들어주기
#
# title1 = "orange,apple,banana"
# print(title1.split(','))
#
# #퀴즈2
# #유저한테 이메일주소를 입력받고, ['유저아이디','도메인']
# #ex) python@megastudy.com ['python', 'megastudy.com']
email = input("이메일 주소 입력:")
a = email.replace('@','.')
print(a.split('.'))

# #답:
# user = input("이메일 주소 입력:")
# a = user.split("@") # ['python', 'megastudy.com']
# b = a[1].split('.') # ['megastudy','com']
# a[1] = b[0] # ['python', 'megastudy']
# a.append(b[1])# a[2] = b[1] 는 a[2]가 없으므로 안됨.
# print(a)

# join
# word = ' '.join(['ice','cream']) #'ice cream'
#
# id = input("아이디 입력:")
# domain = input("도메인 입력:")
# print('@'.join([id,domain]))

article = """
The unrest was triggered after police and other public servants staged a protest strike outside parliament on Wednesday, after discovering their pay had been reduced by up to 50% in their latest pay-check.

In response, Prime Minister James Marape said the pay cut was an error due to a computer glitch - which had deducted up to $100 (£78) from the pay-checks of public servants. He said the administrative error would be corrected at next month's payments.

But this answer was not accepted by many protesters, some of whom then tried to push into the parliament - with footage showing people torching a car outside the Prime Minister's compound and overrunning a gate.

Many touted theories from social media that the government was raising income taxes- an assertion denied by the government.

"Social media picked up on this wrong information, misinformation," said Mr Marape, according to the New York Times, adding that people had taken advantage of police being off the streets.

Port Moresby local, Maholopa Laveil, told the BBC opportunists ransacked the city, setting many buildings and small shopping centres on fire and stealing cars. The worst of the violence happened during the day.

"We had a lot of fear for people who were working in the shopping centres and offices - there was a lot of glee and excitement from the people who were attacking and entering the shops," he said.

Mr Laveil, who is an economic lecturer at the University of Papua New Guinea, also said most of the people looting appeared to be from the poorer settlements outside the city.

"They had come on when they heard the police had stood down and were not policing the city.

"These are suburbs with really poor people, who don't have jobs and who contribute to a lot of crime and lawlessness in the city. Many have suffered a lot from not being employed- inflation pressures - and they came out in numbers trying to get what they could from the shops nearest to them," he said.

Ambulance officials said they had attended to several shooting injuries, while the US embassy reported shots near its compound.

The Chinese embassy has also lodged a complaint with the PNG government, saying several Chinese businesses were attacked and a number of Chinese nationals injured - though they did not specify how many.

"The Chinese Embassy in Papua New Guinea has lodged solemn representations with the Papua New Guinea side over the attacks on the Chinese shops," the embassy said on WeChat.
"""

newArticle = article.replace('but','however').replace('it','😍').split()
print(newArticle)

