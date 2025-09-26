# in演算子　ある要素がリストの中に入っているかをTrue or Falseで返す演算子
# fruits = ['apple', 'peach', 'grapes', 'banana']
# print('apple'in fruits)
# print('lemon'in fruits)
# print('lemon'not in fruits)     # ないものにTrueを返す
# print('apple'in fruits)
# print('h'in 'hello')            # 文字列でもいける


print('↓　challenge')
# challenge: ユーザーに好きなフルーツを入力してもらい、そのフルーツがfruitsリストにあればそのフルーツを削除し、
# なければそのフルーツをリストに追加する。

fruits = ['apple', 'peach', 'grapes', 'banana']
favorite_fruits = input('好きな果物を教えてください')
if favorite_fruits in fruits:                   # 好きなフルーツがある場合、リストからそのフルーツを削除
    fruits.remove(favorite_fruits)
    print(f'リストから{favorite_fruits}を削除しました')
else:                                           # 好きなフルーツがない場合、リストにそのフルーツを追加する。
    fruits.append(favorite_fruits)
    print(f'リストに{favorite_fruits}を追加しました')
print(f'''現在リストには以下が入っています。
{fruits}
''')
