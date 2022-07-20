#2072. 홀수만 더하기 D1

T = int(input())
answer = 0

for t in range(1, T + 1):
    answer = 0
    num = list(map(int,input().split()))
    for n in num:
        if n%2 == 1:
            answer += n
    print(f'#{t}',answer)