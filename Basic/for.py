# forループ
# fruits = ['apple', 'peach', 'grapes', 'banana']

# for fruits in fruits:
#     print(f"I love {fruits}!!")
# 
# for char in 'hello world!!':
#     print(f'char:{char}')


# iteration：ループで回すこと, iterable：ループで回すことができるオブジェクトの事

print('↓　チャレンジ1')
# challenge1: ユーザーに好きなフルーツを入力してもらい、fruitsリストの各フルーツに対して「好き/好きじゃない」をprint()する
# fruits = ['apple', 'peach', 'grapes', 'banana']
# user_favorite = input('好きなフルーツはなんですか？')
# for fruit in fruits:
#     if user_favorite == fruit:                  # 好きなフルーツがそれぞれの要素と一致するかをループさせる
#         print(f'あなたは{fruit}が好きです')
#     else:
#         print(f'あなたは{fruit}が好きではないです')

print('↓　チャレンジ2')
# challenge2: ユーザーに好きなフルーツを入力してもらい、fruitsリストの各フルーツに対して「好き/好きじゃない」をprintする
fruits = ['apple', 'peach', 'grapes', 'banana']
like_fruits = []
notlike_fruits = []

for fruit in fruits:
    favorite = input(f'{fruit}は好きですか？（y/n）')

    if favorite == 'y':
        like_fruits.append(fruit)
    elif favorite == 'n':
        notlike_fruits.append(fruit)
    else:
        print('y または n で回答ください')

print(f'''あなたの好きなフルーツとそうでないものを分けました。
好きなフルーツ：{like_fruits}
そうじゃないフルーツ：{notlike_fruits}
''')


