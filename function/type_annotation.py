#type annotation
#引数の隣にコロン＋型（int, float, str）を記入することで、
# その引数にどの方が推奨されるかが提案される。
# ただし、強制されるものではないため、
# 異なった型のデータが入っても問題なく実行される。
def add_nums(num1: int, num2: int) -> int:
    return num1 + num2

print(add_nums(1,2))
print(add_nums("1","2"))    #型は異なるが実行は問題なくできる。

#python->動的型付け言語:プログラムを実行するまでデータの型がわからない。
one = 1
two = 2
one = "hello"
print(add_nums("1","2"))