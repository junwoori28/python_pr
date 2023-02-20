a = {'name': 'Kim', 'phone': '01045681234', 'birth': '223355'}
b = {0: 'Hello Python'}
c = {'arr': [1,2,3,4]}
d = {
    'Name' : 'Niceman',
    'City' : 'Seoul',
    'Age' : '33',
    'Grade' : 'A',
    'Status' : True
}
e = dict([
    ('Name', 'Niceman'),
    ('City', 'Seoul'),
    ('Age', '33'),
    ('Grade', 'A'),
    ('Status', True)
])

f = dict(
    Name = 'Niceman',
    City = 'Seoul',
    Age = 33,
    Grade = 'A',
    Status = True
)

print(a)
print('a -', type(a), a)
print('b -', b[0])
print('a -', a['name'])
print('a -', a.get('name'))

a['address'] = 'seoul'
print('a -' ,a)

print('a -', len(a))

print('a -', a.keys())
print('a -', list(a.keys()))

print('a -', a.values())
print('a -', list(a.values()))

print('a -', a.items())
print('a -', list(a.items()))

print('a -', a.popitem())
print('a -', a)
print('a -', a.popitem())
print('a -', a)
print('a -', a.popitem())
print('a -', a)
print('a -', a.popitem())
print('a -', a)

print('a -', 'birth' in a)
