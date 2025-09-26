# closure:クロージャ
#pythonはあらゆるデータがオブジェクト（1, "hello", [0,1,2], True, {a:b}）
#関数もオブジェクト

def compute_square(num):
    return num*num

f = compute_square #compute_squareは関数のオブジェクト。
# オブジェクトなので、変数に入れることができる。
print(type(f))
print(f(10))


#関数はオブジェクトなので、リストに入れることもできる。
function_list = ['1', 1, True, f]
print(function_list[-1](10)) #リストから関数を取り出して実行することもできる。

#関数も引数として渡せる
def execute_func(func, param):
    return func(param)

print(execute_func(f,10))


#関数をreturnする
def return_func():

    def inner_func():
        print('This is an inner function')
    return inner_func#()をつけると実行結果がけるが、（）をつけなければ、関数のオブジェクトが返る。

f = return_func()
print(type(f))
f()

#Closure:状態をキープした関数を作ることができる
#状態が静的
def power(exponent):
    def inner_power(base):
        return base ** exponent
    return inner_power #このinnerpowerは、powerが呼ばれた時の状態を保持した関数オブジェクト

power_four = power(4) #exponent=4としたinner_powerが代入される
print(power_four(2)) #inner_powerのbase=2として、関数が実行される
print(power_four(3)) #inner_powerのbase=2として、関数が実行される
#つまり、exponent=4という状態をキープしている

power_five = power(5)
print(power_five(2))

power_five = power(2)
print(power_five(5))

#状態が動的
def average():
    nums = []

    def inner_average(num):
        nums.append(num)
        print(nums)
        return sum(nums) / len(nums)

    return inner_average


average_nums = average()
print(average_nums(5))
print(average_nums(15))
print(average_nums(4))
print(average_nums(10))
print(average_nums(12))
