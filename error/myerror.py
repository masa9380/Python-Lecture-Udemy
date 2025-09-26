class MyError(Exception):

    def __str__(self):
        return 'My error occurred'


class MyError2(Exception):

    def __str__(self):
        return 'My error occurred'



if __name__ == '__main__':
    response = input('y/n?')
    # try:
    if response != 'y' and response != 'n':
        raise MyError('My error occurred')
    # except MyError as e:
    #     print(e)    # e.__str__()を裏で実行している