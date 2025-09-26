# built in function
# type() ()に入れたデータの形式(int, stringなど)を返すもの
hello_type = type('Hello')
print(hello_type)
print(type('Hello'))

number = type(1)
print(number)

#id() そのデータのIDを表示する
hello_id = id('hello')
print(hello_id)
hello = 'hello'
hello2 = 'hello'
print(id(hello))
print(id(hello2))
w = 'world'
print(id(w))
print(id('world')) 
