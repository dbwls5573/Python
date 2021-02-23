#입력함수
num = input('숫자 입력: ')

#출력함수
print('num:', num)

def grade(score):
    if 90 <= score <= 100:
        print('A')
    elif 80 <= score <= 90:
        print('b')
    elif 70 <= score <= 80:
        print('c')
    elif 60 <= score <= 70:
        print('d')
    else:
        print('f')

while True:
    score = input('점수 입력(종료는 -1) :', )

    #입력받은 문자열을 숫자로 변환
    score = int(score)
    if score == -1:
        break

        grade(score)
        
        print('프로그램종료')