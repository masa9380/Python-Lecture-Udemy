def print_name_local():
    first_name = "Taro" #関数の中で定義されたこれらの変数は、関数の中だけでしかアクセスできない
    last_name = "Yamada" #ローカル変数という。
    print(f"I'm {first_name} {last_name}")


print_name_local()
# print(first_name)  これはアクセスできない

#グローバル変数orモジュール変数
age = 38


def print_age():
    global age
    age = 20 #ローカル変数  #この行をコメントアウトすると、↓のageはグローバル変数の方のageを参照する
    print(f"I'm {age} year old")
#まずローカル変数を探す。なければグローバル変数の方を探しに行く。
#関数では、できるだけローカル変数を使う方がよい。グローバル変数を使うことはできるだけ避ける。

print_age() #関数のなかでage=20と定義されているので、28が返る
print(age) #関数内での処理では上書きされず、もとの数字が出力される
