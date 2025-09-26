# 「:」を使って、複数の要素を取ってくることができる（slicing）
even = [2, 4, 6, 8, 10, 12]
print(even[1:4])            # list[a:b] -> a以上b未満の要素

print(even[0:4])
print(even[:4])             # [0:b] = [:b]  0は省略できる

print(even[3:5])
print(even[3:-1])           # indexに負の値を入力することも可能

print(even[3:])             # 後ろを省略すると、最後の要素まで取ってくる

print(even[:])              # 両方省略すると、最初から最後まで取ってくる

text = ('hello world')      # stringに対しても同様の使い方ができる
print(text[3:])

# [開始：未満：step]
print(text[2:10:2])         # 2以上10未満の要素の中から2つおきに出力

print(text[::-1])           # 逆順に表示する。（最初から最後まで、後ろから1個ずつ表示） 
