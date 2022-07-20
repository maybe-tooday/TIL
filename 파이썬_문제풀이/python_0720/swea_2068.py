# 2068. 최대수 구하기 D1

T = int(input())

for t in range(1, T + 1):
    a = list(map(int,input().split()))
    answer = a[0]
    for b in a:
        if answer < b:
            answer = b
    print(f'#{t}',answer)