class MyClass():

    classmethod_count = 0

    def mymethod(self):
        print('This is normal method!')

    @staticmethod
    def mystaticmethod(): # インスタンスの情報を使わないので、selfがいらない
        print('This is staticmethod!')


    @classmethod
    def myclassmethod(cls): #クラスの情報を引数として受け取る
        cls.classmethod_count += 1
        print(f'This is class method and now the count is {cls.classmethod_count}')




c = MyClass()   # インスタンスを作成
c.mymethod()    # インスタンスからマイメソッドを実行
MyClass.mystaticmethod()    # インスタンスを作らずに、、クラスから直接実行
MyClass.myclassmethod()
MyClass.myclassmethod()
c.myclassmethod()