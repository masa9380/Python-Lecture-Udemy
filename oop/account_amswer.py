import time


class Account(object):

    count = 0

    def __init__(self, balance, name):
        self.balance = balance
        self.name = name
        self.account_num = Account.count
        Account.count += 1
        self.transaction_list = []

    def withdraw(self,price):
        if price <= self.balance:
            self.balance -= price
            self.date = Account.now()
            self.show_balance()
            self.add_transaction(-price)
        else:
            print(f'残高がたりません。残高は{self.balance}です。')


    def deposit(self, price):
        self.balance += price
        self.date = Account.now()
        self.show_balance()
        self.add_transaction(price)


    def show_balance(self):
        print(f'口座名：{self.name} 口座番号：{self.account_num}')
        print(f'残高は{self.balance}円です')


    def add_transaction(self, price):
        transaction = {'withdraw/deposit':price,
                       'now_balance':self.balance,
                       'time':Account.now()
        }
        self.transaction_list.append(transaction)


    @staticmethod
    def input_price():
        price = int(input('引き出す/預ける 金額を入力してください。'))
        return price


    @staticmethod
    def now():
        now = time.localtime()
        return "{0.tm_year}/{0.tm_mon}/{0.tm_mday} {0.tm_hour}:{0.tm_min}:{0.tm_sec}".format(now)


    def show_transaction_list(self):
        for transaction in self.transaction_list:
            transaction_str_list = []
            for k, v in transaction.items():
                transaction_str_list.append(f"{k}:{v}")
            print(", ".join(transaction_str_list))

masa = Account(1000, 'masa')
tama = Account(4000, 'tama')
# print(masa)
# print(masa.balance)
# masa.withdraw()

tama.withdraw(3000)
tama.deposit(800)

print(tama.transaction_list)

tama.show_transaction_list()
