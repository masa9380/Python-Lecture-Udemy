# range(start, stop, step) start=<value<stop

# for _ in range(4, 13, 2):   # (処理を始める数, 処理を終わる数, 何言葉しにやるか)
#     print("hello")               # (スタートを抜くと0から始まる。ステップを抜くと1ずつ処理。)


print("↓　ここからchallenge")
# FizzBuzzゲームを作る
# 1~50の数字をそれぞれprint()して、
# 3の倍数で「Fizz」5の倍数で「Buzz」、
# 3と5の倍数で「FizzBuzz」と表示するコードを作成する
fizzbuzz = None

for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        fizzbuzz = "fizzbuzz"
    elif i % 3 == 0:
        fizzbuzz = "fizz"
    elif i % 5 == 0:
        fizzbuzz = "buzz"
    else:
        fizzbuzz = " "
    print(f"{i} {fizzbuzz}")