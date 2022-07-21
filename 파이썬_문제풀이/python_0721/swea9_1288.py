# 1288. 새로운 불면증 치료법 D2
# import sys
# sys.stdin=open('ASDF.txt','r')

T = int(input()) #테스트 케이스 입력
for t in range(1, T + 1): 
    N = int(input())
    sheep = [0,0,0,0,0,0,0,0,0,0] #자릿수 카운터
    #print(sheep,type(sheep))
    k = 1
    while 0 in sheep: #sheep에 0이 없을떄 까지 반복!!
        num = str(k * N) #kN을 문자화시켜서 길이와 위치별값을 이용하기 위해
        for n in range(len(num)):
            sheep[int(num[n])] += 1 #sheep 리스트에 위치에 계속 값을 넣는다. 
        k += 1 
    print(f'#{t} {num}')