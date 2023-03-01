a = []
b = list()
c = [70, 75, 80, 85]
d = [1000, 10000, 'ACE', 'BASE', 'Captain']
e = [1000, 10000, ['ACE', 'BASE', 'Captain']]
f = [21.42, 'footer', 3, 4, 'bark', False, 3.14159]

print('>>>>>>>')
print('d -', type(d), d)
print('d -', d[1])
print('d -', d[0] + d[1] + d[1])
print('d -', d[0] + d[1] + len(d[2]))
print('d -', d[-1])
print('e -', e[-1][1]) #리스트 지정 후 요소 선언
print('e -', list(e[-1][1]))
print('e -', e[2][1])

print('>>>>>>>')
print('d -', d[0:3])
print('d -', d[0:-2])
print('d -', d[2:])
print('e -', e[2][1:3])

print('>>>>>>>')
print('c + d', c + d)
print('c * 3', c * 3)
print("'Test' + c[0] - ", 'Test' + str(c[0]))

print(c == c[:4])

temp = c
print(c == temp)
print(id(c))
print(id(temp))


print('>>>>>>>')
c[0] = 4
print(c)
c[1:2] = [[1, 2, 3]]
print(c)
c[1][1] = 100
print(c)
c[1:3] = []
print(c)
c = [70, 75, 80, 85]
c[2:4] = list()
print(c)
c = [70, 75, 80, 85]
print(c)
del c[3]
print(c)

print('>>>>>>>')

#리스트 함수
"""
append : 끝에 무엇을 추가함
sort : 리스트 내용을 오름차순 정렬
reverse : 리스트 내용을 기존 순서에서 반대로 정렬
index : 리스트에 a가 몇번째에 있는지 알려줌 // a=[1, 10] // print(a.index(10)) => 2
insert :  a번째 위치에 b를 넣음 a.insert(a,b) 뒤에 리스트 값은 밀림
remove : a.remove(6) // (그냥 '6')
del : a[6] -->비효율적 // [6번째]
pop : 기존의 리스트에서 마지막 index에 해당하는 원소를 꺼내옴 a.pop() *(자료구조)stack -> last-in first-out
count : a.count(내가 찾는 값) => 내가 찾는 값이 리스트에 몇 개 있을까
extend : 리스트 추가 (요소만!)
"""

a = [5, 1, 2, 3, 4]

print(a)

a.append(10)
print(a)
a.sort()
print(a)
a.reverse()
print(a)
a.reverse()
print(a)
print(a[2])
print(a.index(10))
a.insert(2, 9)
print(a)
a.sort()
print(a)
a.remove(9)
print(a)
del a[2]
print(a)
print(a.pop())
print(a)
a.append(6)
print(a)
print(a.count(6))
ex = [8,9]
a.extend(ex)
print(a)

while a:
    l = a.pop()
    print(l)


# 팩킹 & 언팩킹

#packing

t = ('foo', 'bar', 'baz', 'qux')

print(t)
print(t[0])
print(t[-1])
print(t[0:2])


#unpacking

# x1, x2, x3, x4 = t --> 상관없음,,, 다만 관습상
(x1, x2, x3, x4) = t

print(type(x1), type(x2), type(x3), type(x4))
print(x1, x2, x3, x4)

#packing & unpacking(parentheses, bracket omitted)
t2 = 1, 2, 3
t3 = 4,
x1, x2, x3 = t2
x4, x5, x6 = 4, 5, 6

print(t2)
print(t3, type(t3))
print(x1, x2, x3)
print(x4, x5, x6)


z = [5, 2, 3, 1, 4]

z.append(6)
print('z -', z)
print('z -', z.index(6))
z.insert(2,8)
print('z -', z)
print('z -', z.count(5))
ex = [10,11]
z.extend(ex)
print('z -', z)
z.sort()
print('z -', z)

