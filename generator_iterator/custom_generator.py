# range(10)
def myrange(stop):
    start = 0
    while start < stop:
        yield start
        start += 1


#
mr = myrange(10)
print(type(mr))
print(mr)
print(next(mr))
print(next(mr))
print(next(mr))
print(next(mr))
print(next(mr))
print(next(mr))
print('end of next()')
# print(next(mr))
# print(next(mr))
# print(next(mr))
# print(next(mr))   # 9
# print(next(mr))

print('beginning of for loop')
for i in mr:
    print(i)



# challenge
# def even(num):
#     start = num
#     while start >= 2:
#         yield start
#         start -= 2

def even(num):
    while num != 0:
        if num % 2 == 0:
            yield num
        num -= 1

print('=================')
for i in even(10):
    print(i)

print('=================')
even_gen = even(10)
print(next(even_gen))
print(next(even_gen))
print(id(iter(even_gen)))
print(id(even_gen))
