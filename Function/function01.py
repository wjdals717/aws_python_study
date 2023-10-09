# def(define) -> 함수를 정의한다

# 오버로딩 안 됨!!!
def add(x, y):
    result = x + y
    return result

# 여러 개의 매개 변수, 여러 개의 리턴은 튜플 자료형으로 정의됨
def add(*a):                    #*as는 튜플로 받겠다는 의미
    print(type(a))
    return list(a),10

r = list(add(20, 10, 5, 30, 40))

print(r)

# **이면 딕셔너리 자료형으로 매개변수를 변환해준다.
def sub(**data):
    print(type(data))
    print(data)

sub(a=1, b=2)

def sub(data):
    print(type(data))
    print(data)

sub({"a":1,"b":2})

#초기값이 없는 경우 앞에 배치
def connection(serverName, password, ip="127.0.0.1", port="8080", username="root"):
    print(f"id: {ip}")
    print(f"port: {port}")
    print(f"serverName: {serverName}")
    print(f"username: {username}")
    print(f"password: {password}")

connection(serverName="test_server", password="1q2w3e4r", port="3306")

a = 2
def multi(a):
    return a ** 2

a = multi(a)
print(a)

def div():
    global a
    a = a * 10

div()
print(a)

###################################################################################################
#lamda
def add(a,b):
    return a + b

print(add(10, 20))

#파이썬에서 람다는 하나의 명령만 수행할 수 있다.(여러 줄 불가능)
add = lambda a, b: print(a + b)

add(30, 30)














