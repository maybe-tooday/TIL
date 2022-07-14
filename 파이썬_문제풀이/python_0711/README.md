017
021
045

**잘라서 변수에 각각 입력**
a, b = input().split(':')

**16진수를 8진수로 변경**
a = input()
a = int(a,16)
print("%o"%a)

**입력받은 문자를 10진수 유니코드 값으로 변환한 후, n에 저장한다.**
n = ord(input())
print(n)

**c에 저장되어 있는 정수 값을 유니코드 문자(chracter)로 바꿔 출력한다.**
c = int(input())
print(chr(c))  

a, b, c = map(int,input().split())