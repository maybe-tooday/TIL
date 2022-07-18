# 6057 : [기초-논리연산] 참/거짓이 서로 같을 때에만 참 출력하기(설명)(py)

a, b = map(int,input().split())
c = bool(int(a))
d = bool(int(b))
print((c and (not d)) or ((not c) and d))