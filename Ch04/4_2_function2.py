# 기본값 매개 변수
def hello(name='황유진', old=24):
    print('-------------')
    print('이름은 %d 입니다.' % name)
    print('나이는 %d 입니다.' % old)

hello()
hello('김연아')
hello('황유진', 25)

# 가변 매개 변수
def total(*param):
    tot = 0
    for k in param:
          tot += k
    return tot

r1 = total(1)
r2 = total(1, 2, 3)
r3 = total(1, 2, 3, 4, 5)

# 여러개의 값을 변환하는 수
def sum_and_mul(x, y):
    z1 = x+y
    z2 = x*y

    return z1, z2
sum_and_mul(1, 2)
rs1, rs2 = sum_and_mul(1, 2)
rs3, rs4 = sum_and_mul(3, 4)

print('rs1:', rs1)
print('rs2:', rs2)
print('rs3:', rs1)


# 함수의 지역변수, 전역변수
var1 = 1
def scope_test():
    # 전역변수 var1을 참조하기위한 global 선언
    global var1
    var1 += 1
    print('var1: ', var1)

scope_test()

# 함수를 변수에 저장해서 호출하기
def message( param ):
    print('param:', param)

val1 = message
val1 = message

val1('황유진')
val1('김연아')

def plus(x, y):
    return x+y

def minus(x, y):
    return x-y

list = [plus, minus]
r1 = list[0](1, 2)
r2 = list[1](1, 2)

print('r1:', r1)
print('r2:', r2)



# 함수를 변수에 저장해서 호출하기 까지


