#qrcode 만들기
import qrcode
url = 'https://www.instagram.com/riize_official/'
img = qrcode.make(url)
img.save('./riize.png')
#.save(저장하고 싶은 경로)

