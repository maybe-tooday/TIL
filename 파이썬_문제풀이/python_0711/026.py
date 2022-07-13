# 6026 : [기초-값변환] 실수 2개 입력받아 합 계산하기(설명)(py)

a= input()
b= input()
c = float(a) + float(b)
print(c)

a, b = map(float,input().split())
c = a + b
print(c)