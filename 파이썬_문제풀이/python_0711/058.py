# 6058 : [기초-논리연산] 둘 다 거짓일 경우만 참 출력하기(py)

a, b = map(int,input().split())
c = bool(int(a))
d = bool(int(b))

print((not a) and (not b))