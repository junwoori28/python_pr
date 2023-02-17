# #슬라이싱
# str_s1 = 'Nice Python'

# #슬라이싱 연습
# print(str_s1[0:3])
# print(str_s1[:3])
# print(str_s1[:-8])
# print(str_s1[:len(str_s1)-8])
# print(str_s1[:len(str_s1)])
# print(str_s1[1:4:2])
# print(str_s1[1:-2])
# print(str_s1[::2])

# a = 'z'

# print(ord(a))
# print(chr(122))

# im_str = "Good Boy!"

# print(dir(im_str))

# for i in im_str:
#     print(i)

# str_o1 = "Python"
# str_o2 = "Apple"
# str_o3 = "How are you doing?"
# str_o4 = "Seoul Deajeon Busan Jinju"

# print('Capitalize:', str_o1.capitalize())
# print('endwith?:',str_o2.endswith('e'))
# print('join str:', str_o1.join(['I\'m ', '!']))
# print('replace1:',str_o1.replace('thon','good'))
# print('replace2:',str_o3.replace('are', 'was'))
# print('split:', str_o4.split(' '))
# print('sorted:', sorted(str_o1))
# print('reversed1:', (reversed(str_o2)))
# print('reversed:', list(reversed(str_o2)))

# print(dir(str_o1))
# print(str_o2 + str_o3)

# multi_str2 = \
#     '''
#     문자열 멀티라인 
#     역슬래시(\)
#     테스트
#     '''
# # 멀티라인(역슬래시) 출력
# print(multi_str2)

str1 = 'I am Python.'
str2 = 'Python'
str3 = 'How are you?'
str4 = 'Thank you!'

print(str1)
print(str2)
print(str3)
print(str4)

print()

print(type(str1))
print(type(str2))
print(type(str3))
print(type(str4))

print()

print(len(str1))
print(len(str2))
print(len(str3))
print(len(str4))

print()

str_t1 = ''
str_t2 = str()

print(str_t1, type(str_t1), len(str_t1))
print(str_t2, type(str_t2), len(str_t2))

"""
\n \t \\ \' \" \000
"""

escape_str1 = 'Do you have a\000\"retro games\"?'

print(escape_str1)

raw_s1 = r'D:\Python\python3'
raw_s2 = r"\\x\y\z\q"

print(raw_s1)
print(raw_s2)

multi_str1 = \
'''
Hello
World
My name is
Park junwoo\
dfdfdfdf
'''
print(multi_str1)

str_o1 = 'python'
str_o2 = 'Apple'
str_o3 = 'How are you doing?'
str_o4 = 'Seoul Daejeon Busan Jinju'

print(str_o1*3)
print(str_o1 + str_o2)
print(dir(str_o1))
print('y' in str_o1)
print('y' in str_o2)
print('y' not in str_o3)

print(str(66))
print(str(10.1))
print(str(True))
print(str(complex(12)))

print()

print('Capitalize:', str_o1.capitalize())
print('end with e?:', str_o2.endswith('e'))
print('join str:', str_o1.join(['I\'m ', '!']))
print('replace1:', str_o1.replace('thon', 'Good'))
print('replace2:', str_o4.replace('Daejeon', 'Daegu'))
print('split:', str_o4.split(' '))
print('reversed1:', (reversed(str_o1)))
print('reversed2:', (reversed(str_o2)))

print()

im_str = 'Good Day!'

for i in im_str:
    print(i)

str_sl  = 'Nice Python'

print(str_sl[0:3])
print(str_sl[:len(str_sl)])
print(str_sl[:])
print(str_sl[1:4:2])
print(str_sl[-4:-2])
print(str_sl[1:-2])
print(str_sl[::2])