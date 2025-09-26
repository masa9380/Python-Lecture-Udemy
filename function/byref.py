#参照渡し（byref） <-> 値渡し（byvalue）
def add_nums(a,b):
    print(f"第一引数aのID：{id(a)}")
    print(f"第二引数bのID：{id(b)}")
    return a + b

one = 1
two = 2
print(f"oneのID：{id(one)}")
print(f"twoのID：{id(two)}")

print(add_nums(one, two))


#参照渡しの場合、変数へのアドレスが渡される。pythonでは全て参照渡しが行われる。
#プログラミング言語によっては値渡しの場合もある
#参照渡しはIDが同じものになる。全く同じオブジェクト。


def add_one(num):
    print(f"変更前のID:{id(num)}")
    num += 1
    print(f"変更後のID:{id(num)}")
    return num

one = 1
print(f"oneのID:{id(one)}")
print(f"関数呼び出し前のone:{one}")
add_one(one)
print(f"関数呼び出し後のone:{one}")


#関数の中で引数として渡したものは、変更されても実際には変更されていない。
#一見新しいnumが更新されているのでone(元データ)も変更されているように見える。しかし、実際はそうではない。


def add_fruit(fruits, fruit):
    print(f"変更前のID：{id(fruits)}")
    fruits.append(fruit)
    print(f"変更後のID：{id(fruits)}")
    return fruits


myfruits = ['apple', 'banana', 'peach']
myfruit = 'lemon'
print(f"関数呼び出し前のmyfruits:{myfruits}")
add_fruit(myfruits, myfruit)
print(f"関数呼び出し後のmyfruits:{myfruits}")

