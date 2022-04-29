def open_account():
    print('새로운 계좌가 생성되었습니다')

def deposit(balance, money): #입금
    print('입금이 완료되었습니다. 잔액은 {}원 입니다.'.format(balance+money))
    return balance+money
    #balance = 현재 잔고
    #money = 입금 금액

def withdraw_night(balance, money):
    commission = 100 #수수료 100원
    return commission, balance-money-commission

balance = 0

open_account() #계좌 생성

balance = deposit(balance, 10000) #10000원 입금

commission, balance = withdraw_night(balance,5000) #5000원 출금

print('수수료는 {}원 이며, 잔액은 {}원 입니다.'.format(commission, balance))