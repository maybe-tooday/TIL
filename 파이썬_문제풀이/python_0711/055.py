# 6055 : [기초-논리연산] 하나라도 참이면 참 출력하기(설명)(py)

a, b= map(int,input().split())
c = bool(a) or bool(b)
print(c)