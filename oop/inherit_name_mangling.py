class Person():
    def __init__(self, name):
        self.name = name
        self.__mymethod()


    def mymethod(self):
        print('Person method is called.')

    __mymethod = mymethod


class Baby(Person):
    def mymethod(self):
        print('Baby method is called.')


taro_baby = Baby("Taro")
print(taro_baby.name)
taro_baby.mymethod()
jiro_person = Person('Jiro')
print(jiro_person.name)
jiro_person.mymethod()
print(dir(taro_baby))