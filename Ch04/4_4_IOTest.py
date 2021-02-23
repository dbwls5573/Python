#파일 입출력 함수
file1= open('C:/Users/bigdata/Desktop/test.txt.txt')

line = file1.read()
print('line : ', line)
file1.close()

#여러줄 파일 읽기
file2 = open('C:/Users/bigdata/Desktop/test.txt.txt', 'r')

while True:
    line = file2.read()

    if not line:
        break

        print('line:', line)

file2.close()


#파일 만들기
file3 = open('C:/Users/bigdata/Desktop/test3.txt.txt', 'w')
file3.write("안녕하세요")
file3.write("반갑습니다\n")
file3.write("또만나요\n")

file3.close()


file4 = open('C:/Users/bigdata/Desktop/test4.txt.txt', 'w')

for a in range(2,10):
    file4.wrtie('%d단\n' % a )
    for b in range(1,10):
        file4.write('%d x %d = $d\n' % (a, b, a*b))

file4.close()

# with 문(파일 생성과 close를 한번에 실행하는 구문)
with open('C:/Users/bigdata/Desktop/test5.txt.txt') as file5 :
    for i in range(10):
        file5.write('☆'*i)

        file5.write('\n')