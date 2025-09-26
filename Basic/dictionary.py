# dictionary: キーと値の組み合わせを複数保持するデータ型
fruits_colors = {'apple': 'red', 'lemon': 'yellow', 'grapes': 'purple'}
print(fruits_colors)
print(fruits_colors['apple'])

# dictionaryはインデックス（0,1,2...）を持たない。順番で管理していない。
# その代わりにキーを使って値を紐づけてる

fruits_colors['peach'] = 'pink'
print(fruits_colors)

dict_sample = {1: 'one', 'two': 2, 'three': [1, 2, 3], 'four': {'inner': 'dict'}}
print(dict_sample)
print(dict_sample['four']['inner'])
# print(dict_sample['four']　この部分でprint(dict_sample['four']が返ってくる

colors = {}     # ディクショナリーは順番を保持しない。キーと値の組み合わせを袋に入れて補完してるイメージ
colors[1] = 'blue'
colors[0] = 'red'
colors[2] = 'green'
print(colors)


# .keys() values()
for fruit in fruits_colors.keys():          # keyを順番に入れてそれに対応するフルーツが出力される
    print(fruit)

for color in fruits_colors.values():        # fruitを順番に回し、それに対応するキーが出力される
    print(color)

for x in fruits_colors:                     # キーが順番い出力される
    print(x)

# .items()
for fruit, color in fruits_colors.items():  # 各要素のキーと値に対してループさせる。
    print(f'{fruit} is {color}')