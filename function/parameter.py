def func(first, second, third='3'):      # デフォルトではthirdに3が入る
    print(f'first: {first}, second: {second}, third:{third}')


# argument:引数に渡す値自体のこと <-> parameter:値を入れるための箱のこと
func('1', '2', '3')
func('1', third='3', second='2')

#キーワード引数はポジショナル引数の後に持ってくる必要がある。どこに引数を入れるのかわからなくなるから。



