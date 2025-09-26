class Person(object):   # クラス名の初めの文字は大文字で記述する。（キャメルケースというcf:スネークケース）

    num_legs = 2
    count = 0
    # constructor(__new__)
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        Person.count += 1
# 引数として受けとたったname,age,genderは、selfの中に各属性に格納される
# selfというのはインスタンス自身

    def walk(self):
        print(f'{self.name} is walking... with {Person.num_legs} legs!')

    def run(self):
        print(f'{self.name} is running... with {Person.num_legs} legs!')


john = Person('John', 28, 'male')
print(Person.count)
taro = Person('Taro', 18, 'male')
print(Person.count)
emma = Person('Emma', 40, 'female')
print(Person.count)

# インスタンス変数：インスタンスに紐づく変数
# [インスタンス名.変数名]でアクセス可能
print(john.name)
print(john.age)
john.age = 29   # インスタンス変数を呼び出し、それに新しい数字を代入できる
print(john.age)

# 関数もインスタンス名.関数名で呼び出しできる
john.walk()
emma.walk()
john.run()

print('各インスタンスのnum_legsを表示')
print(john.num_legs)
print(taro.num_legs)
print(emma.num_legs)
print(Person.num_legs)

Person.num_legs = 3
print('Person.num_legs = 3を実行')
print(john.num_legs)
print(taro.num_legs)
print(emma.num_legs)

john.num_legs = 4
print('john.num_legs = 4を実行')
print(john.num_legs)
print(taro.num_legs)
print(emma.num_legs)
