# 1986. 지그재그 숫자 D2

T = int(input())

for t in range(1,T+1):
    num = int(input())
    answer = 0
    for i in range(1,num+1):
        answer += (i*(-1)**(i+1))
    print(f'#{t}',answer)
