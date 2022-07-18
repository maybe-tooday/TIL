# 6066 : [기초-조건/선택실행구조] 정수 3개 입력받아 짝/홀 출력하기(설명)(py)

a, b, c = map(int,input().split())

if a%2==0 :  #논리적으로 한 단위로 처리해야하는 경우 콜론(:)을 찍고, 들여쓰기로 작성 한다.
    print('even')
else:
    print('odd')
    
if b%2==0 :
    print('even')
else:
    print('odd') 

if c%2==0 :
    print('even')
else:
    print('odd') 