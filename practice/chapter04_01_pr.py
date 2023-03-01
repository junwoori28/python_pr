print(type(True))
print(type(False))

if True:
    print('Good')

if False:
    print('bad')

if False:
    print('Bad')
else:
    print('Good')

x = 15
y = 10

print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x<=y)
print(x>=y)

city = ''

if city:
    print('you are in:', city)
else:
    print('please enter your city')

city = 'seoul'

if city:
    print('You are in :', city)

else:
    print('please enter your city')

a = 75
b = 40
c = 10

print('and : ', a>b and b>c)
print('or : ', a>b or b>c)
print('not : ', not a>b)
print('not : ', not b>c)
print(not True)
print(not False)

print('e1 : ', 3+12 > 7+3)
print('e2 : ', 5+10*3 > 7+3*20)
print('e3 : ', 5+10>3 and 7+3==10)
print('e4 : ', 5+10>0 and not 7+3==10)

score1 = 90
score2 = 'A'

if score1 >= 90 and score2 == 'A':
    print('Pass.')
else:
    print('Fail.')


id1 = 'vip'
id2 = 'admin'
grade = 'platinum'

if id1 == 'vip' or id2 == 'admin' :
    print('관리자 인증')

else :
    print('일반 회원')

if id2 == 'admin' or grade == 'platinum' :
    print('최상위 관리자')

else :
    print('일반 회원')

num = 65

if num >= 90 :
    print('Grade : A')
elif num >= 80 :
    print('Grade : B')
elif num >= 70 :
    print('Grade : C')
elif num >= 60 :
    print('Grade : D')



















