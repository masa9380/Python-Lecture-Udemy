# # 関数（function）
# print()
# len()
# input()
# # これらはビルトイン関数と言われる。
# Pythonの中にもともと入っている

# 華氏から摂氏に変換するプログラムを作成する
fahrenheit = 72

def fahrenheit_to_celsius(fahrenheit):      # この行のfahrenheitは次の行にのみ影響する。
    celsius = (fahrenheit - 32) * 5/9       # 関数の外のfahrenheitとは関係がない
    return celsius

celsius = fahrenheit_to_celsius(fahrenheit)
print(celsius)

