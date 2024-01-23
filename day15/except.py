# except

try: #try는 에러가 날 것 같은 구문을 적는곳
    num = int(input("숫자 입력:"))
    result = 10 / num
    print(f"결과는 {result}")
except ValueError:
    print("숫자를 입력해야 합니다")
except ZeroDivisionError:
    print("0으로 못나눕니다.")
else:
    print("에러없음")
finally:
    print("에러가 나도 상관없으니 보여줘")


try: #try는 에러가 날 것 같은 구문을 적는곳
    num = int(input("숫자 입력:"))
    result = 10 / num
    print(f"결과는 {result}")
except Exception:
    print("에러남")
