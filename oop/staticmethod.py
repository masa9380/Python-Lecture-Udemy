class MyClass():

    def mymethod(self):
        print('This is normal method!')

    @staticmethod
    def mystaticmethod(): # インスタンスの情報を使わないので、selfがいらない
        print('This is staticmethod!')

c = MyClass()   # インスタンスを作成
c.mymethod()    # インスタンスからマイメソッドを実行
MyClass.mystaticmethod()    # インスタンスを作らずに、、クラスから直接実行
# c.mystaticmethod()  # インスタンスから実行することもできるがこのように記述する意味がない。