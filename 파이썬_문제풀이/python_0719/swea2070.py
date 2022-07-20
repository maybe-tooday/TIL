# 2070. 큰 놈, 작은 놈, 같은 놈

T = int(input())

for case in range(1, T + 1):
    a, b = map(int,input().split())
    if a > b:
        print(f'#{case} >')
    elif a < b:
        print(f'#{case} <')
    else:
        print(f'#{case} =')