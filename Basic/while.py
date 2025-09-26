# while ループ
# count = 0
# while count < 10:   # この条件がいつか必ずFalseになるようにする。無限ループになってしまう。
#     print(count)
#     count += 1


# # breakとcontinue
# while True:
#     age = int(input("あなたは何歳ですか？"))
#     if not 0 <= age < 120:
#         print("入力された値は正しくありません")
#         continue
#     else:
#         print(f"あなたは{age}際です")
#         break


print("↓　ここからchallenge")
# challenge1:「ユーザーに年齢を聞き、18歳以上なら入れるカジノを作成する。
# カジノに入ったらゲームを選べるようにする。」
# できるゲームは1：ルーレット、2：ブラックジャック、3：ポーカー
# 洗濯後、ゲーム内容をprint()する。
casino_age = 18
age = int(input("あなたは何歳ですか"))
if age >= casino_age:
    print("お入りください")

    while True:
        game = input("""どのゲームで遊びますか？
                数字でお答えください。
                1:ルーレット
                2:ブラックジャック
                3:ポーカー""")
        if game == "1":
                print(f"{game}:ルーレットをお楽しみください")
                break
        elif game == "2":
                print(f"{game}:ブラックジャックをお楽しみください")
                break
        elif game == "3":
                print(f"{game}:ポーカーをお楽しみください")
                break
        else:
            game =input("1~3の数字を入力してください")

else:
    print("18歳未満の方は入場できません")





