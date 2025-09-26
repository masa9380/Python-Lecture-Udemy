casino_age = 18
age = int(input("あなたは何歳ですか"))
game_dict = {'1': 'ルーレット', '2': 'ブラックジャック', '3': 'ポーカー', '4': 'スロット', '5': 'バカロ'}
# count = len(game_dict)

# 自分の回答
# if age >= casino_age:
#     print("お入りください")
#
#     while True:
#         print(game_dict)
#         game = input("""どのゲームで遊びますか？数字でお答えください。""")
#         i = int(game)
#         if 1 <= i <= count:
#                 print(f"{game}:{game_dict[i]}をお楽しみください")
#                 break
#         else:
#             game =input("1~3の整数を入力してください")
#
# else:
#     print("18歳未満の方は入場できません")
#

# 模範回答
if age >= casino_age:
    print("お入りください")

    while True:
        print('プレイするゲームを選択してください。')
        for num, game_name in game_dict.items():
            print(f'{num}: {game_name}')
        game = input(':')
        if game in game_dict:
                print(f"{game}:{game_dict[game]}をお楽しみください")
                break
        else:
            game =input(f"1~{len(game_dict)}の整数を入力してください")

else:
    print(f"{casino_age}歳の方は入場できません")
