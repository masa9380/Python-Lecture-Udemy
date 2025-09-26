# リスト（lists）: 複数のオブジェクトを順序づけて保存するデータ型
# []で括って、,(カンマ)で各オブジェクトを区切る

fruits = ['apple', 'peach', 'melon', 'grapes']

hetro_list = ['string', 1, 3.4, True, fruits]       # listも入れられる

# print(hetro_list)
# print(fruits[0])            # indexは0始まりであることに注意する
# print(fruits[-3])           # -をつけることで後ろから選べる
# print(hetro_list[-1][-1])   # hetro_list[-1] = fruits
# print("hello world"[4])     # 文字列のなかの文字も取ってこれる


# listを使う上で便利なメソッド
# .append: 新しいオブジェクトを追加する（リストの1番最後に要素を追加する）
print('fruits list')
print(fruits)
print('\nappend:リストの最後にbananaを追加')
fruits.append('banana')
print(fruits)

# .insert: 指定したindexに指定したオブジェクトを追加する
print('\ninsert：index3の位置にlemonを追加')
fruits.insert(3, 'lemon')                       # indexで入力した数字の要素の前にオブジェクトを追加。
print(fruits)

# .remove: マッチした最初のオブジェクトを除く
print('\nremove: リストからpeachを取り除く')
fruits.remove('peach')
print(fruits)

# .sort: 昇順または降順に並び替える
print('\nsort: リスト内のオブジェクトを昇順（アルファベット順）に並び替える')
fruits.sort()
print(fruits)
print('sort(reverse = True): リストないのオブジェクトを降順に並べ替える')
fruits.sort(reverse = True)
print(fruits)


# len(): リストの要素数を取得する
print('\nリスト内の要素数を出力する')
print(len(fruits))
print('文字列（hello world）の数を出力する')
print(len('hello world'))       #文字列に対しても使える。

