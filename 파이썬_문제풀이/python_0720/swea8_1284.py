# 1284. 수도 요금 경쟁 D2 Attack
# P:A사요금, Q:B사기본요금, R:B사초과량기준기본금, S:B사초과량요금, W사용량 

T = int(input())

for t in range(1,T+1): #테스트케이스 반복문
    p, q, r, s, w = map(int,input().split())
    result = 0 #수도세
    if w <= r:
        if (p * w) >= q:
            result = q
        else:
            result = (p * w)
    if w > r:
        if (p * w) >= q + ((w-r) * s):
            result = q + ((w-r) * s)
        else:
            result = (p * w)
    print(f'#{t}', result)