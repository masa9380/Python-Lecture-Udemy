# 再帰関数(recursive function):関数の中で自身の関数をcallする
# 階乗(factorial)：3! = 3*2*1 = 6
# n! = n*(n-1)*(n-2)*...*1
# n! = n*(n-1)!

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(4))

# フィボナッチ数列(fibonacci)
# ①再帰関数を使って実装
def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

print(fibonacci_recursive(6))


# ②再帰関数を使わずに実装
def fibonacci2(n):
    fibonacci_list = [0, 1]
    if n == 0:
        return fibonacci_list[0]
    elif n == 1:
        return fibonacci_list[1]
    else:
        for i in range(2,n+1):
            num = fibonacci_list[i-2] + fibonacci_list[i-1]
            fibonacci_list.append(num)
            # print(fibonacci_list)
    return fibonacci_list[n]

print(fibonacci2(7))

#模範解答
def fibonacci(n):
    if n < 2:
        return n
    else:
        n_1 = 1
        n_2 = 0
        for _ in range(n-1):  #iはループ内で使われない変数のため、_で記載すると親切。
            result = n_1 + n_2
            n_2 = n_1
            n_1 = result
        return result


for i in range(50):
    print(i, fibonacci(i))

#再帰バージョンは非常に処理が重い
#再帰バージョンの利点としてはコードが見やすい。処理を軽くする方法もある（数値のキャッシュを利用して再帰計算を行う。）
