# 2019. 더블더블 D1 /'0 부터 주어진 숫자까지 2의 i승을 출력하라' 라고 수정해야겠는데요

n = int(input())

for i in range(n+1):
    print(f'{2**i}',end = ' ')