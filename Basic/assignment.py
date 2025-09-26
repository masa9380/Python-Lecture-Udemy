# 変数へ代入：assignment

hello = 'konnichiwa'
world = 'sekai!!'
print(hello + world)
print('konnnichiwa' + 'sekai')  # ハードコーディング

# 変数の命名規則(naming convention)
# snake_case←Pythonはこれ, CamelCase
# 文字から始まる
# 文字、数字_(アンダースコア)を使う
# Case sensitive (Helloとhelloは別の変数、区別が必要)

# format
print('{} {}'.format(hello, world))

# example
name = 'John'
print('Hey, {}!! How are you doing?'.format(name))

balance = 100
print('balance : {}'.format(balance))

# fstring （カーリーブラケットに直接変数を入れる。その際先頭に「f」を入力する）
print(f"{hello},{world}")

print(f'Hey, {name}!! How are you doing?')
print(f'balance : {balance}')

