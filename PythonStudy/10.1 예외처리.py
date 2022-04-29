'''
try:
    print("나누기 전용 계산기입니다.")

    num1 = int(input("첫 번째 숫자를 입력하세요: "))
    num2 = int(input("두 번째 숫자를 입력하세요: "))
    print("{} / {} = {}".format(num1, num2, int(num1/num2)))

except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")

except ZeroDivisionError:
    print("에러! 0으로 나눌 수 없습니다.")

except Exception:
    print("에러! 알 수 없는 에러가 발생하였습니다.")
'''

    

try:
    print("나누기 전용 계산기입니다.")

    num1 = int(input("첫 번째 숫자를 입력하세요: "))
    num2 = int(input("두 번째 숫자를 입력하세요: "))
    print("{} / {} = {}".format(num1, num2, int(num1/num2)))

except ValueError as err:
    print(err)

except ZeroDivisionError as err:
    print(err)

except Exception as err:
    print(err)
