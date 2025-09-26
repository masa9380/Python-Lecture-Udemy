class Account:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, price):
        self.__balance += price
        self.show_balance()


    def withdraw(self, price):
        if self.__balance < price:
             print('残高がたりません')
        else:
            self.__balance -= price
            self.show_balance()


    def show_balance(self):
        print(f'残高は{self.__balance}¥です')

myaccount = Account(10000)
print(dir(myaccount))
myaccount.deposit(2000)
myaccount.withdraw(5000)
myaccount.withdraw(10000)
myaccount.__balance = -10000    # あたらしく__balanceという属性が作られており、そこに-10000が代入されている
print(myaccount.__balance)
myaccount.show_balance()    # _Account__balaceの方が処理される。
print(dir(myaccount))
myaccount._Account__balance = -100000   #無理やり代入することはできるが、普通は誰もそんなことはしない。
myaccount.show_balance()