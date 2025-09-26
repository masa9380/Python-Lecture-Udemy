# docstring:その関数をどのように使うか、引数はなにかといった情報を記述できる


# reStructuredTextのdocstring
def multiply(num1, num2):
    """
    multiply num1 with num2 and return the result
    :param num1: first number that you want to multiply
    :param num2: second number that you want to multiply
    :return: num1 * num2
    """
    return num1 * num2

# docstringの内容を確認する場合は↓のコードを記述すれば良い。（どちらでも良い）
# print(multiply.__doc__)
# help(multiply)


# Google styleのdocstring
def dividend(num1, num2):
    """
    num1 is divided by num2 and return the result
    Args:
        num1:number that you want to divide
        num2:number that you want to divided by

    Returns:
        num1 / num2

    """
    return num1 / num2

# dividend(1,1)
