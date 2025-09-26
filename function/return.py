def print_dict(input_dict):
    for k, v in input_dict.items():         # .items はkeyとvalueをタプルで受け取ることができる
        print(f'key: {k}, value: {v}')

a = {'one': 1, 'two': 2}       # aはディクショナリー
print(a)
print_dict(a)

return_value = print_dict(a)
print(return_value)


# returnを明示しない関数はNoneを返す


def get_first_last_word(text):
    text = text.replace(',', '')
    words = text.split()
    return words[0], words[-1]

text = 'Hello, my name is Mike'
r = get_first_last_word(text)
print(r)

first, last = get_first_last_word(text)
print(f'first word is {first}, last word is {last} ')



