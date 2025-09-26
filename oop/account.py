import datetime


class Account(object):

    count = 0

    def __init__(self, balance, name):
        self.balance = balance
        self.name = name
        self.account_num = Account.count
        Account.count += 1
        self.transaction_list = []

    def withdraw(self):
        self.withdraw_money = int(input('引き出す金額を入力してください。'))
        if self.withdraw_money <= self.balance:
            self.balance -= self.withdraw_money
            print(f'{self.withdraw_money}円引き出しました。')
            self.date = Account.now()
            self.show_balance()
            withdraw_dict = {'引き出し額':self.withdraw_money, '口座残高':self.balance, '日時':self.date}
            self.add_transaction(withdraw_dict)
        else:
            print(f'残高がたりません。残高は{self.balance}です。')


    def deposit(self):
        self.deposit_money = int(input('預ける金額を入力してください。'))
        self.balance += self.deposit_money
        self.date = Account.now()
        self.show_balance()
        deposit_dict = {'預け入れ額':self.deposit_money, '口座残高':self.balance, '日時':self.date}
        self.add_transaction(deposit_dict)

    def show_balance(self):
        print(f'口座名：{self.name} 口座番号：{self.account_num}')
        print(f'残高は{self.balance}円です')

    def add_transaction(self, record):
        self.transaction_list.append(record)
        return self.transaction_list


    @staticmethod
    def now():
        now = datetime.datetime.now()
        return now


masa = Account(1000, 'masa')
tama = Account(4000, 'tama')
# print(masa)
# print(masa.balance)
# masa.withdraw()

tama.withdraw()
tama.deposit()

print(tama.transaction_list)

