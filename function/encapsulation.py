# カプセル化（encapsulation）:データをカプセルの中に入れて、
# 外からアクセスできないようにする。（情報隠蔽）

def casino_entrance(age, min_age=21):
    if age < min_age:
        print(f'{min_age}未満お断り')
        return

    def inner_casino_entrance():
        print('ようこそ、カジノへ')

    inner_casino_entrance()


casino_entrance(18)
# inner casino_entrance(18)　#＜ーこの関数には直接アクセスできない。
# アクセスするためにはcasino_entrance関数を経由する必要がある。



#このような構造にすることによって、
# それぞれの関数がそれぞれの機能に集中できる。
#今回の場合、inner関数はカジノの機能、アウター関数は年齢制限の機能