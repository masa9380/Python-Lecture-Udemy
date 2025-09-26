# tuple(タプル)：変更できないリスト　[]ではなく()をつかう
# 変更の必要がないものに対してタプルを使うことが多い
date_of_birth = (1990,2,3)
print(date_of_birth[0])

# 比較タプルではなくリストだった場合
# date_of_birth = [1990,2,3]
# date_of_birth[0] = 1999
# print(date_of_birth[0])     # 1990という値が更新されている

year, month, date = date_of_birth
print(year)
print(month)
print(date)

