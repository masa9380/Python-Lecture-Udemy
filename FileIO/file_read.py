# # for文でループで回す
# with open('pep8_introduction.txt') as f:
#     for line in f:
#         print(line, end='')
#
#
# # .read()でファイルの中身の全てを一つのstringとして返す
# # 便利だが、大きなファイルにはやらないようにする
# with open('pep8_introduction.txt') as f:
#     print(f.read())


# # .readline()で1行ずつ取得し、stringで返す
# with open('pep8_introduction.txt') as f:
#     line = f.readline() # 1行目を読み込む
#     # line = f.readline() # 2行目を読み込む
#     while line:
#       print(line, end='')
#       line = f.readline()


# .readlines()で全ての行をリストで返す
with open('pep8_introduction.txt') as f:
    lines = f.readlines()
    print(lines)
