# 関数の中で関数を定義(nested function)
def outer(outer_param):
    def inner():
        print("This is inner function")
        print(outer_param)
    inner()

#こちらのように記述しても同様に実行できる
# def outer():
#     outer_param = "outer arg"
#     def inner():
#         print("This is inner function")
#         print(outer_param)
#     inner()


outer("outer arg")
# inner function は outer functionの変数にアクセスすることができる
#逆にouter functionはinner functionの変数にアクセスすることはできない。

# inner() #innerファンクションを直接呼び出すことはできない。


msg = "I am global"

def outer2():
    # global msg #これを有効にすると変数が更新されるようになる。
    msg = "I am outer"

    def inner2():
        # nonlocal msg  #これを有効にすると、変数が更新されるようになる。
        msg = "I am inner"
        print("This is inner function")
        print(msg)
    inner2()
    print(msg)

outer2()
print(msg)
#どの変数も更新されない。関数内でglobal msgやnonlocal msgをつかえば、グローバル変数が更新される。