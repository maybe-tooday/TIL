#1933. 간단한 N 의 약수 D1

N = int(input()) #1이상1000이하

for i in range(1,N+1): #0은뺴고 계산
    if N % i == 0:
        print(i, end=' ')
