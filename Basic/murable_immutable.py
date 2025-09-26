# mutable: 変更可能なオブジェクト　list, dict, set
print('mutableの場合')
fruits = ['apple', 'peach', 'banana']
print(fruits)
print(f'fruitsのIDは{id(fruits)}')
fruits.append('lemon')
print(fruits)
print(f'fruitsのIDは{id(fruits)}')
# 変更可能なオブジェクトなので、同じIDとなる。
# メモリのどこかに格納されたものを変更して同じところに格納するイメージ（使い回す）


# immutable: 変更不可能なオブジェクト　int, float, str, bool, tuple
print('\nimmutableの場合')
fruit = 'apple'
print(fruit)
print(f'fruitのIDは{id(fruit)}')
fruit += ', lemon'
print(fruit)
print(f'fruitのIDは{id(fruit)}')
# 変更不可のオブジェクトなので、IDが異なる。
# 初めに値とは別のメモリに新しく格納されるイメージ

# なぜこのようなことになるのか
# mutableのオブジェクトはたくさんの要素を扱うデータ型。
# もし変更不可能だったら、要素を変更するたびに新しくメモリを使ってしまう
# なので、変更可能にして、メモリの節約をしている


print('')

text = ''  # 1-2-3-4-5-6-7-...
for i in range(1, 11):      # text はimmutableであるから、ループを1回するごとにメモリを使う
    if i == 1:
        text += str(i)
    else:
        text += '-' + str(i)
print(text)

# ではどうすれば効率がよくなるか
text_list = []                  # listを作成し、そこにappendで文字を足していく
for i in range(1, 11):
    text_list.append(str(i))

text = '-'.join(text_list)      # 最後にjoinを使ってリストないの要素を結合する
print(text)