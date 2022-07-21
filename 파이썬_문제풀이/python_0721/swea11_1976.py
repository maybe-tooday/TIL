# 1976. 시각 덧셈 D2
# import sys
# sys.stdin=open('ASDF.txt','r')

#시간,분 따로 더하고 조건쓰기 머리아프다 한가지단위(분)로 변경하여 처리하자
T = int(input())
for t in range(1, T + 1):
    a, b, A, B = map(int,input().split())
    clock = (a + A) * 60 + b + B #모든 시간을 분으로 변환
    C = clock // 60 #60분이 넘으면 1시간
    c = clock % 60 #시간을 넘긴 나머지가 분
    if C > 12:
        C -= 12
    print('#{} {} {}'.format(t,C,c))
    # = print(f'#{t} {C} {c}')

    