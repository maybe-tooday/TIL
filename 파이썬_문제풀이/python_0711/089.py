# 6089 : [기초-종합] 수 나열하기2(py)

a, b, n = map(int,input().split())
#a : 시작숫자, b : 등비의 값, n : 몇번쨰인가

print(a * (b ** (n-1)))