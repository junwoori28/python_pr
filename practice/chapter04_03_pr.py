n=5

while n>0:
    print(n)
    n -= 1

a = ['foo', 'bar', 'baz']

while a :
    print(a.pop())

n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('Looped Ended.')
print()

m = 5
while m > 0:
    m -= 1
    if m == 2:
        continue
    print(m)
print('Loop Ended.')

i = 1

while i <= 10:
    print('i:', i)
    if i == 6:
        break
    i += 1

n = 10
while n > 0:
    n -= 1
    print(n)
    if n == 5:
        print('Found 511')
else:
    print('else out.')

a = ['fpp', 'bar', 'baz', 'qux']
s = 'qux'

i = 0

while i < len(a):
    if a[i] == s:
        print('I found', s, 'in list!')
        break
    i += 1
else:
    print(s, 'not found in list.')

a = ['foo', 'bar', 'baz']
while True:
    if not a:
        break
    print(a.pop())