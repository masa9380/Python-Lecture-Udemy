# 論理演算子（logical operators）
# and, or , not

a = 1
b = 1
c = 10
d = 100
print(a == b and c > d) #aとbは等しいが、cはdより大きくないー＞False
print(a == b or c > d)  #aとbが等しいー＞True
print(not a == b)

# Challenge1：年齢10歳以上かつ身長が110cm以上なら乗れるアトラクション
age = 9
height = 120
print(age >= 10 and height >= 110)


# Challenge2：修士号保持もしくは5年以上の実務経験があればVisaの取得が可能
master = True   # True：修士号持ってる、False：修士号持ってない
job_experience = 0
print(master or job_experience >= 5)
