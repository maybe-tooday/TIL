# 2063. 중간값 찾기

T = int(input())
number = list(map(int,input().split()))
number = sorted(number) #number.sort

print(number[int((T-1)/2)])