# if分

age = -10
age_alcohol = 21
if age >= age_alcohol:
    print('You can drink beer!')
else:
    print('You are too young to drink beer')


ege_drive = 18
if age >= age_alcohol:
    print('You can drink beer!')
elif age < ege_drive:
    print('You cannot even drive!')
else:
    print("You are not allowed to drink beer but you can drive only if you have a driver's license")


if not 0 < age < 120:
    print('The value is invalid!')

print('\n')
print('↓ challenge')

# challenge1：もしbalance(残高)がwithdraw(引き出し額)より大きければ、balanceを更新し、そうでなければ引き出せないATMをつくる
balance1 = 2000000
withdrawal1 = 100000
if balance1 > withdrawal1:
    # balance = balance - withdrawal
    balance1 -= withdrawal1
    print('Your new balance is {}.'.format(balance1))
else:
    print("You don't have enough money.")

print('\n↓challenge2')
# challenge2：challenge1に加えて、引き出し額の上限を100万に設定し、上限を肥えて引き出そうとすると引き出せないATMを作る
# ↓My answer
# if not withdrawal <= 1000:
#     print("You cannot withdraw cash more than 1000k¥")

balance2 = 200000
withdrawal2 = 10000
withdrawal_limit = 1000000
if withdrawal2 > withdrawal_limit:
     print("The withdrawal limit is {}.".format(withdrawal_limit))
elif balance2 > withdrawal2:
    balance2 -= withdrawal2
    print('Your new balance is {}.'.format(balance2))
else:
    print("You don't have enough money.")


