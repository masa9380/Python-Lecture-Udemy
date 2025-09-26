# Decorator: 関数に機能を付属する（デコレートする）

def greeting(func):
    def inner(*args, **kwargs):
        print('Hello!')
        func(*args, **kwargs)
        print('Nice to meet you!')
    return inner


@greeting #@greetingと記載することによって、
# ↓でsay_name = greeting(say_name)と記載する必要がない。
def say_name(name):
    print(f"I'm {name}")

@greeting
def say_name_and_origin(name, origin):
    print(f"I'm {name}, I'm from {origin}")


# say_name = greeting(say_name)
say_name('Jiro')
say_name_and_origin("Taro", "Tokyo")
#greetingのなかにsay_nameを入れることによって、少し機能を追加した。
# say_name('Jiro')


