for v1 in range(10) :
    print('v1 is :', v1)

print ()

for v2 in range(1, 11, 2):
    print('v2 is :', v2)

print()

for v3 in range(1, 11, 2):
    print('v3 is :', v3)

print()

sum1=0

for v in range(1,1001):
    sum1 += v

print('1 ~ 1000 sum : ', sum1)

print('1 ~ 1000 sum : ', sum1)
print('1 ~ 1000 sum : ', sum(range(1, 1001)))
print('1 ~ 1000 sum : ', sum(range(0, 1001, 4)))

sum2=0

for v in range(0,1001,4):
    sum2+=v

print('4의 배수의 합 : ', sum2)

names = ['Kim', 'Park', 'Cho', 'Lee', 'Choi', 'Yoo']

for name in names:
    print('You are : ', name)

lotto_numbers = [11, 19, 21, 28, 36, 37]

for number in lotto_numbers:
    print('Current number : ', number)

word = 'Beautiful'

for s in word:
    print('word : ', s)

my_info = {
    'Name': 'Lee',
    'Age': 33,
    'City': 'Seoul'
}

print(type(my_info))

for key in my_info:
    print('key :', key)

for val in my_info.values():
    print('val :', val)

name = 'FineApplE'
for n in name:
    if n.isupper():
        print(n)

    else:
        print(n.upper())



numbers = [14, 3, 4, 7, 10, 24, 17, 2, 34, 15, 36, 38]

for num in numbers:
    if num == 34:
        print('Found : 34!')
        break
    else:
        print('Not found : ', num)

lt = ['1', 2, 5, True, 4.3, complex(4)]

for v in lt:
    if type(v) is complex:
        continue

    print('current type : ', type(v))
    print('multi by 2 : ', v*3)


numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 36, 38]

for num in numbers:
    if num == 34:
        print('Found : 34!')
        break
else:
        print('Not Found 45...')

for i in range(2, 10):
    for j in range(1, 10):
        print('{:4d}'.format(i*j), end='')
    print()

name = 'Aceman'
print('Reversed : ', reversed(name))
print('List : ', list(reversed(__name__)))

l = ['a', 'b', 'c']
t = ('a', 'b', 'c')
s = 'abc'

l.reverse()
print(l)

print(list(reversed(l)))
print(tuple(reversed(l)))
print(''.join(reversed(l)))
print('List : ', list(reversed(name)))
print('Tuple : ', tuple(reversed(name)))
print('Set : ', set(reversed(name)))