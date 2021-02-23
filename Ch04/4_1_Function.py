# 함수 정의
def f(x):
    y = 2 * x + 3
    return y

# 함수 호출
    rs1=f(1)
    rs2=f(2)
    rs3=f(3)

print('rs1:', rs1)
print('rs2:', rs2)
print('rs3:', rs3)


# 함수타입 1 - 매개변수 0, 반환값 0
def f1(x,y):
    z = x+y
    return z

# 함수타입 2 - 매개변수 x, 반환값 0
def f2():
    tot= 0
    for k in range(11):
        tot +=k
        return k

# 함수타입 3 - 매개변수 0, 반환값 x
def f3(items):
    tot=0
    for i in items:
        tot += i
# 함수타입 4 - 매개변수 x, 반환값 x
def f4():
    for i in range(11):
        print('*', *i)


r1 = f1(1, 2)
r2 = f1(2, 3)

print('r1:', r1)
print('r2:', r2)

f3([1, 2, 3, 4, 5])
f3([6, 7, 8, 9, 10])

f4()