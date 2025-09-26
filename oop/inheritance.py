class Animal(object):
    def __init__(self, name):
        self.name = name
        print('Animal init is called')

    def breath(self):
        print(f'{self.name} is breathing.')


class Dog(Animal):
    def __init__(self, name):         # 継承先にも__init__があると、親クラスの__init__は読まれない
        super().__init__(name=name)
        print('Dog init is called.')


pochi = Dog("Pochi")
