# 6093 : [기초-리스트] 이상한 출석 번호 부르기2(py)

n = int(input())      #개수를 입력받아 n에 정수로 저장
a = input().split()  #공백을 기준으로 잘라 a에 순서대로 저장

for i in range(n-1, -1, -1) :
    print(a[i], end=' ') # 입력받은 a값을 반대로 출력