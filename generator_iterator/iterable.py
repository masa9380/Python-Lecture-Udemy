fruits = ['apple', 'lemon', 'peach', 'banana']

# print(next(fruits)) #next関数でう呼べないため、iteratorではない

print(iter(fruits))
fruits_iterator = iter(fruits)
print(next(fruits_iterator))
print(next(fruits_iterator))
print(iter(fruits_iterator))
print(id(fruits_iterator))
print(id(iter(fruits_iterator)))


print('=' * 30)
print(next(fruits_iterator))
print(fruits_iterator.__next__())