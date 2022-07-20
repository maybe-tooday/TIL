# 2071. 평균값 구하기 D1
T = int(input())
avr = 0
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    sum = 0
    a = list(map(int,input().split()))
    for num in a :
        sum += num
    avr = sum /10
    print(f'#{test_case} {avr:.0f}')    