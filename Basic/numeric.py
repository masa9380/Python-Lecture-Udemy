# 数値型（Numeric）: integer(整数), float(少数), complex(複素数)

# int (integer, 整数) -3, -2, -1, 0, 1,2,3, 100
print(type(1))

# float(浮動小数点)
print(type(0.1))
print(0.1 + 0.1 + 0.1) #0.3→実際は0.30000004 ちょっと大きい数になる

# Numeric Operator(数値演算子)
# 四則演算
print(1 + 0.4)
print(1 - 0.4)
print(2 * 3)
print(1 / 2)
print(5*6 - 3/6) # 優先度の高い項は演算子の前後にスペースをお置く

result = 1 + 6.0
print(type(result))
print(f'type of result:{result} is {type(result)}')

# その他の演算
# floot division
print(14 // 3)
# modulo, 剰余, 余り
print(14 % 3)
# exponentiation 累乗
print(2 ** 3)

hit_point = 100
attack_point = 40.3
remain = hit_point - attack_point
print(f'remamin hit point is {remain}')

# augmented assignment
a = 1
a = a + 1
a += 1  # a = a + 1と同じ意味
print(a)
