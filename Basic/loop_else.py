fruits = ["apple", "peach", "grapes", "banana"]

# for文におけるelseの役割→ループが回りきった時に実行されるもの。
# for fruit in fruits:
#     choice = input(f'あなたが探しているフルーツは{fruit}ですか？　y/n:')
#     if choice == 'y':
#         print('見つかってよかったですね')
#         break
#     else:
#         print('そうですか、、、')
# else:               # ループが回りきった時に実行される
#     print('お探しのフルーツは見つかりませんでした。')


# while文におけるelseの役割→条件文がFalseになると実行される
# count = 0
# while count < 10:
#     print(count)
#     count += 1
# else:
#     print('countは10未満ではなくなりました。')

balance = 1000
game_price = 200
while balance >= game_price:
    choice = input(f'1回{game_price}円のゲームに参加しますか？（残高：{balance}円）(y/n:)')

    if choice == "y":
        balance -= game_price
        print(f'残高が{balance}円になりました')
    elif choice == "n":
        print('また遊びましょう。')
        break
    else:
        print("yかnで答えてください")

else:
    print('お金を貯めてまた遊びましょう')
