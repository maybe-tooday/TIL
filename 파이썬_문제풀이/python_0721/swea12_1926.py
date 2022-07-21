# 1926. 간단한 369게임
# import sys
# sys.stdin=open('ASDF.txt','r')

T = int(input())

for t in range(1, T + 1):
    number = str(t) # 숫자를 문자로 변환
    cnt = 0 #369갯수 넣을 통
    for n in number:
        if n == '3' or n == '6' or n == '9':
            cnt += 1
    
    if cnt > 0 :
        number = '-'*cnt
        cnt = 0

    print(number, end=' ')
