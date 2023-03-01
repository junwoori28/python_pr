# 매개변수가 필요한 함수
# 매개변수가 필요하지 않은 함수
# 결과값을 반환하는 함수
# 결과값을 반환하지 않는 함수

# 1. 매개변수가 필요하지 않은 함수

def function1():
    print('예제1 호출')

# 2. 매개변수가 필요한 함수

def function2(a, b):
    print('예제2 호출', a, b)

# 3. 결과값을 반환하지 않는 함수

def function3(x, y):
    print('예제3 호출', x, y)

# 4. 결과값을 반환하는 함수

def function4(x, y):
    return x + y

#실행

function1()
function2(10, 20)
function3(100, 200)
function4(50, 50)

r = function4(50, 50)

print('예제4 호출', r)
