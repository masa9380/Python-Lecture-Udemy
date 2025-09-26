# input(): ユーザーの入力した値（文字列）を取得する

# age = input("何歳ですか？")               # int型ではなくstr型で受け取っている
# print("あなたは{}歳です".format(age))

print('↓ challenge1')
# challenge1:ユーザーに年齢を聞き、18歳以上なら入れるカジノを作成する
age = int(input('How old are you?'))         # int型でデータを取得するために、int()でくくってしまう
age_limit = 18
game_text = '''プレイするゲームを選択してください
1：ルーレット
2：ブラックジャック
3：ポーカー
'''

if age >= age_limit:                               # ここに制限年齢の数字を直接記入するのはハードコーディング。変数にする。
    print('You can enter this casino.')
    # challenge2: カジノに入った後に聞く質問なのでここに入力する。
    game = input(game_text)
    if game == '1':                                     # もし、、、なら
        print('あなたはルーレットを選択しました。')
    elif game == '2':                                   # そうじゃなくてもし、、、
        print('あなたはブラックジャックを選択しました。')
    elif game == '3':                                   # そうじゃなくてもし、、、
        print('あなたはポーカーを選択しました。')
    else:                                               # 上記それ以外なら、、、
        print('1〜3の数字を入力してください。')

else:
    print('You are too young to enter this casino.')

# print('↓　challenge2')
# #challenge2:カジノに入ったらゲームを選べるようにする。選択できるゲームは
# # ・1：ルーレット
# # ・2：ブラックジャック
# # ・3：ポーカー
# # 　選択後、ゲーム内容をprint()する
#
# game = input('Which game do you want to do?')
# print('OK, you can play {}.'.format(game))
