# 比較演算子（relational operator）>, <, >=, <=, ==, !=
print(5 > 3)     # True
print(2.0 < 1)  # False
print(2.0 < 2)  # False
print(5 >= 3)   # True
print(5 <= 5)   # True
print(5 == 3)   # False
print(5 != 3)   # True

print(1 == 1.0) # True intとfloatの比較でも値が同じならTrueが返る
print(1 == '1') # False intとstrではFalseが返る
print('1' == '1')# True strどうしならTrueが返る
