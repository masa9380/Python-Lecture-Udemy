# lambda関数(無名関数)

def square(x):
    return x * x

#ラムダ関数の書き方
s = lambda x: x * x


print(square(3))
print(s(5))

# 元の関数
# def power(exponent):
#     def inner_power(base):
#         return base ** exponent
#     return inner_power

# lambda関数での表記。inner関数部分をラムダ関数で記述
def power(exponent):
    return lambda base: base ** exponent

third_power = power(4)
print(third_power(2))

numbers = [6,2, 5, 43, 5, 36, 67, 2]
# filter()

def filterfunc(num):
    # if num % 2 == 0:
    #     return False
    # else:
    #     return True
    # return not num % 2 == 0  # if文を使わなくても、
    # 直接ブーリアンを返せば良い。（偶数：False,奇数：True）
    return num % 2  # 0,1自体がFalse、Trueの意味を持つので、この表記で良い。

# ↓　これをラムダ関数にする
filtered_num = filter(lambda num: num % 2, numbers)
print(list(filtered_num))

# for num in numbers:
#     print(filterfunc(num))