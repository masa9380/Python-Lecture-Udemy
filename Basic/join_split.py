# join:　stringが持ってるメソッド。指定した文字列で、リスト内の要素をくっつける。
name = 'John'
self_introduction = ["Hi,", "My", "name", "is", name, "."]
text = "＊＊".join(self_introduction)                  # ""で挟んだ文字でリスト内の要素をジョイントする
print(text)
# print("Hi, my name is {}".format(name))

#split
print("Hi, my name is {}".format(name).split(" "))    # ""で挟んだ文字の部分で文を区切ってリスト化する。（joinの逆 ）
print("Hi, my name is {}".format(name).split())       # split()の引数を何も入力しなければデフォルトで半角スペースとして扱われる。


# ファイル名の拡張子を除いた部分 or 拡張子のみを取得したい場合
filename = "sample.py"
print(filename.split(".")[0])
print(filename.split(".")[-1]) 
